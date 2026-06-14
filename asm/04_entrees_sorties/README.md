# Module 04 — Entrées / Sorties (afficher des nombres, lire le clavier)

Jusqu'ici, ton programme « parlait » au monde extérieur de façon très limitée : il rendait
un **code de sortie** (un seul petit nombre via `exit`), ou il affichait un **texte déjà
écrit** dans `.data`. Dans ce module, on franchit deux étapes très importantes :

1. **Afficher** un **nombre calculé** (pas un texte figé) — ce qui est plus subtil qu'il n'y
   paraît !
2. **Lire** ce que l'utilisateur **tape au clavier**, puis le réutiliser.

> Fichiers du module : [`afficher_nombre.s`](./afficher_nombre.s) (convertir un entier en
> texte et l'afficher) et [`echo.s`](./echo.s) (lire une ligne au clavier et la réafficher).
> Tout est commenté presque ligne par ligne.

---

## 1. Les deux appels système d'entrée/sortie : `write` et `read`

Souviens-toi : l'assembleur seul ne sait **ni** afficher **ni** lire. Il doit **demander au
système** (Linux). On a déjà vu `write` (afficher) ; voici son frère `read` (lire) :

| Service | Numéro (dans `rax`) | Rôle |
|---------|---------------------|------|
| `read`  | **0**  | **lire** des octets (par ex. depuis le clavier) |
| `write` | **1**  | **écrire** (afficher) des octets |
| `exit`  | **60** | quitter le programme |

Les deux fonctionnent **de la même manière** : on prépare **quatre** registres, puis on
déclenche avec `syscall`.

| Registre | Pour `write` / `read` | Détail |
|----------|------------------------|--------|
| `rax` | le **numéro** du service | `1` pour write, `0` pour read |
| `rdi` | le **descripteur** | **0** = entrée (clavier), **1** = sortie (écran) |
| `rsi` | l'**adresse du tampon** | où prendre les octets (write) / où les ranger (read) |
| `rdx` | la **taille** | combien d'octets au maximum |

> 🗂️ Un **descripteur** est juste un **numéro de canal** : `0` = l'**entrée standard**
> (souvent le clavier), `1` = la **sortie standard** (souvent l'écran). Ils existent déjà au
> démarrage, tu n'as rien à ouvrir.
>
> 📦 Un **tampon** (en anglais *buffer*) est simplement une **zone mémoire** que tu réserves
> pour y mettre ou y récupérer des octets. On le déclare dans `.bss` (mémoire réservée vide).

### Le schéma à retenir

```asm
mov rax, 1          # service = write (afficher)
mov rdi, 1          # descripteur = 1 (écran)
lea rsi, [message]  # adresse d'où lire les octets à afficher
mov rdx, 6          # nombre d'octets à afficher
syscall             # on demande à Linux d'afficher
```

Pour `read`, c'est le même schéma, mais `rax = 0`, `rdi = 0` (clavier) et `rsi` pointe vers le
tampon **où ranger** ce que l'utilisateur tape. Après le `syscall`, **`rax` contient le nombre
d'octets réellement lus** (utile : c'est la longueur de ce qui a été tapé !).

---

## 2. Le vrai défi : afficher un NOMBRE, ce n'est PAS afficher un texte

Voici le point le plus important — et le plus surprenant — de tout le module.

### Nombres binaires vs caractères affichés

Dans un registre comme `rax`, un entier est rangé en **binaire** (une suite de bits). Mais
l'écran, lui, n'affiche pas des nombres : il affiche des **caractères** (des dessins de
lettres et de chiffres). Et chaque caractère a son propre **code** dans la table **ASCII** :

| Caractère affiché | Son code ASCII (en décimal) |
|-------------------|------------------------------|
| `'0'` | 48 |
| `'1'` | 49 |
| `'2'` | 50 |
| …     | …  |
| `'9'` | 57 |

> 🔑 Conséquence cruciale : le **nombre** `5` (la valeur cinq dans un registre) et le
> **caractère** `'5'` (qu'on dessine à l'écran, code ASCII **53**) sont **deux choses
> différentes** ! Pour passer du chiffre `5` au caractère `'5'`, il faut **ajouter 48**
> (`5 + 48 = 53`).

Donc si tu mets `12345` dans `rax` et que tu demandes à `write` d'afficher l'octet à cette
adresse, **tu n'obtiendras pas « 12345 » à l'écran**. Il faut d'abord **convertir** le nombre
en une suite de **caractères**.

### La méthode : les divisions successives par 10

Comment extraire les chiffres d'un nombre ? En le **divisant par 10** plusieurs fois. À chaque
division, le **reste** te donne le **dernier chiffre**, et le **quotient** est le nombre
« sans son dernier chiffre ». On répète jusqu'à tomber sur 0.

Exemple avec **12345** :

```
12345 ÷ 10  ->  quotient 1234 ,  reste 5   (dernier chiffre : 5)
 1234 ÷ 10  ->  quotient  123 ,  reste 4   (chiffre suivant  : 4)
  123 ÷ 10  ->  quotient   12 ,  reste 3   (chiffre suivant  : 3)
   12 ÷ 10  ->  quotient    1 ,  reste 2   (chiffre suivant  : 2)
    1 ÷ 10  ->  quotient    0 ,  reste 1   (chiffre suivant  : 1)
                quotient = 0  ->  STOP
```

⚠️ Remarque : les chiffres sortent **À L'ENVERS** (5, 4, 3, 2, 1) alors qu'on veut les
afficher dans l'ordre (1, 2, 3, 4, 5). L'astuce classique : on **remplit un tampon en partant
de la FIN** vers le début. Ainsi, le premier chiffre trouvé (5) se range tout à droite, et le
dernier (1) se range juste avant — et l'ensemble se lit alors dans le bon ordre.

> 🔢 N'oublie pas, à chaque reste : on **ajoute 48** pour transformer le **chiffre** (0-9) en
> **caractère ASCII** (`'0'`-`'9'`) avant de le ranger dans le tampon.

### La division en assembleur : `div` (et le piège `rdx`)

L'instruction de division `div` est un peu spéciale :

- Elle divise le nombre formé par la paire `rdx:rax` (un très grand nombre sur 128 bits) par
  ce que tu lui donnes (par ex. un registre contenant `10`).
- Le **quotient** atterrit dans `rax`, et le **reste** dans `rdx`.

> 🩹 Piège à connaître : **avant chaque `div`**, il faut **mettre `rdx` à 0** (`xor rdx, rdx`),
> sinon Linux croit qu'on divise un nombre énorme et le programme plante. On le fait à chaque
> tour de boucle.

Tout ceci est mis en pratique, pas à pas, dans [`afficher_nombre.s`](./afficher_nombre.s).

---

## 3. Lire le clavier avec `read`

[`echo.s`](./echo.s) montre le cas symétrique : on **réserve un tampon** dans `.bss`, on
appelle `read` (depuis le descripteur `0`, le clavier) pour y ranger la ligne tapée, puis on
appelle `write` (vers le descripteur `1`, l'écran) pour la **réafficher**. C'est le principe de
l'« **echo** » : la machine te renvoie ce que tu lui as dit.

> 💡 Astuce déjà mentionnée : `read` renvoie dans `rax` le **nombre d'octets lus**. On le
> réutilise tel quel comme **taille** (`rdx`) pour `write` — ainsi on réaffiche **exactement**
> ce qui a été tapé, ni plus ni moins.

---

## ▶️ À toi de jouer

```bash
# afficher_nombre.s : convertit 12345 en texte et l'affiche -> "12345"
as asm/04_entrees_sorties/afficher_nombre.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x

# echo.s : lit une ligne au clavier et la réaffiche.
#   On lui « envoie » du texte avec printf, via le tube | :
printf "coucou\n" | { as asm/04_entrees_sorties/echo.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x ; } ; printf "coucou\n" | /tmp/x
```

Ensuite, **modifie** les fichiers : dans `afficher_nombre.s`, change le nombre déclaré (par ex.
`7`, `100`, `999999`) et vérifie qu'il s'affiche correctement. Dans `echo.s`, lance-le **sans
tube** et tape toi-même une phrase au clavier : il devrait te la répéter.

➡️ La suite du parcours (manipulation de chaînes, plus de calculs…) arrivera dans le même
style.

📎 Besoin d'un rappel rapide ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
