# Module 05 — Lire et écrire des fichiers

Jusqu'ici, tout ce que nos programmes affichaient disparaissait dès qu'ils s'arrêtaient :
le `printf` écrit à l'écran, mais rien n'est **gardé**. Pour **mémoriser** des informations
d'une fois sur l'autre (une liste de notes, un score, un journal…), on les écrit dans un
**fichier** sur le disque. C'est exactement ce qu'on apprend ici : **écrire** dans un
fichier, puis le **relire**. On y va doucement.

> Fichiers du module : `ecrire.c` (créer un fichier et y écrire quelques lignes) et
> `lire.c` (rouvrir ce fichier et l'afficher ligne par ligne).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Le cahier : ouvrir, écrire/lire, refermer

📒 **Analogie : un cahier.** Travailler avec un fichier, c'est comme se servir d'un cahier :

1. tu **l'ouvres** (tu sais à quelle page tu vas travailler),
2. tu **écris** dedans, ou tu **lis** ce qui y est déjà,
3. tu le **refermes** quand tu as fini.

En C, ces trois gestes ont chacun leur fonction, dans `<stdio.h>` (le même en-tête que
`printf`) :

| Geste | Fonction C | Analogie cahier |
|-------|-----------|-----------------|
| Ouvrir | `fopen` | prendre le cahier et l'ouvrir |
| Écrire | `fprintf` / `fputs` | écrire une ligne dedans |
| Lire | `fgets` | lire une ligne |
| Refermer | `fclose` | refermer le cahier |

> ⚠️ **Refermer est important.** Tant que le cahier n'est pas refermé (`fclose`), ce que tu
> viens d'écrire peut ne pas être **réellement** enregistré sur le disque. On referme
> **toujours** ce qu'on a ouvert.

---

## 2. Ouvrir un fichier : `fopen` et son MODE

Pour ouvrir un fichier, on appelle `fopen` avec deux choses : **le nom du fichier** et le
**mode** (ce qu'on veut en faire).

```c
FILE *f = fopen("exemples/notes.txt", "w");
```

`FILE *` est un nouveau type : c'est une **poignée** vers le fichier ouvert (le « marque-page »
qui dit où on en est). On la garde dans une variable pour s'en servir ensuite.

Les trois modes à connaître :

| Mode | Sens | Effet sur le contenu existant |
|------|------|-------------------------------|
| `"w"` | **w**rite — écrire | ⚠️ **écrase** tout : on repart d'un cahier vide |
| `"a"` | **a**ppend — ajouter | garde le contenu, écrit **à la suite** |
| `"r"` | **r**ead — lire | ne modifie rien, on lit seulement |

> 🧠 **À retenir :** `"w"` repart de zéro (efface l'ancien contenu), `"a"` complète sans
> effacer, `"r"` lit sans toucher.

---

## 3. TOUJOURS vérifier que `fopen` n'a pas échoué (`NULL`)

L'ouverture peut **rater** : fichier introuvable (en lecture), dossier qui n'existe pas,
droits insuffisants… Quand ça rate, `fopen` renvoie **`NULL`** (le « rien » des pointeurs,
vu au module 03). Si on s'en sert quand même, le programme **plante**.

La règle est donc **systématique** : juste après `fopen`, on vérifie.

```c
FILE *f = fopen("exemples/notes.txt", "r");
if (f == NULL) {                 // l'ouverture a échoué ?
    printf("Impossible d'ouvrir le fichier.\n");
    return 1;                    // on arrête proprement (1 = erreur)
}
```

> 🔑 **Réflexe à graver :** un `fopen`, puis **tout de suite** un `if (... == NULL)`. Toujours.

---

## 4. Écrire dans le fichier : `fprintf` et `fputs`

Une fois le fichier ouvert en `"w"` (ou `"a"`), on écrit dedans presque comme avec `printf` :

```c
fprintf(f, "Note : %d/20\n", 15);   // comme printf, mais ça va dans le fichier f
fputs("Bravo !\n", f);              // écrit une chaîne telle quelle dans f
```

- `fprintf` = `printf` **vers un fichier** : même `"%d"`, `"%s"`… le 1er argument est `f`.
- `fputs` = écrit une chaîne simple (pas de format). Pratique pour une ligne toute prête.

> 💡 N'oublie pas le `\n` (retour à la ligne) si tu veux **une ligne par information** —
> sinon tout se colle sur la même ligne.

---

## 5. Lire le fichier ligne par ligne : `fgets`

Pour relire, on ouvre en `"r"` et on lit **une ligne à la fois** avec `fgets`. On lui donne :
une **boîte** (un tableau de `char` qui recevra la ligne), sa **taille**, et le fichier.

```c
char ligne[256];                       // une boîte assez grande pour une ligne
while (fgets(ligne, sizeof(ligne), f) != NULL) {
    printf("%s", ligne);               // ligne contient déjà le \n, pas besoin d'en remettre
}
```

🪣 **Analogie :** `fgets` puise **une louche** (une ligne) à chaque tour. La boucle `while`
continue tant qu'il **reste** quelque chose à puiser. Quand le fichier est terminé, `fgets`
renvoie `NULL` et la boucle s'arrête toute seule.

> 💡 `sizeof(ligne)` donne la taille de la boîte : `fgets` ne dépassera pas, donc pas de
> débordement. C'est une lecture **sûre**.

---

## 6. Refermer : `fclose`

Quand on a fini (écriture **ou** lecture), on referme :

```c
fclose(f);   // on referme le cahier ; ce qui était écrit est bien enregistré
```

---

## 🧹 Où sont créés les fichiers ? (rangement et lancement)

Pour **ne pas polluer** le dépôt avec des fichiers de test partout, nos deux programmes
écrivent dans un **sous-dossier `exemples/`** (chemin `exemples/notes.txt`). Ils **créent**
ce dossier au démarrage s'il n'existe pas, grâce à `mkdir` de `<sys/stat.h>` :

```c
#include <sys/stat.h>
mkdir("exemples", 0777);   // crée le dossier "exemples" ; si déjà là, on ignore l'erreur
```

> ⚠️ **Lance les commandes DEPUIS LA RACINE du dépôt.** Le chemin `"exemples/notes.txt"` est
> **relatif** : il dépend de l'endroit d'où tu lances le programme. Le dossier `exemples/`
> est déjà ignoré par git (il ne sera pas ajouté au dépôt).

---

## ▶️ À toi de jouer

```bash
# 1. Écrire : crée exemples/notes.txt et y écrit quelques lignes
gcc -Wall c/05_fichiers/ecrire.c -o ecrire && ./ecrire

# 2. Lire : rouvre exemples/notes.txt et l'affiche ligne par ligne
gcc -Wall c/05_fichiers/lire.c -o lire && ./lire
```

Lance **d'abord** `ecrire`, **puis** `lire` : tu dois voir s'afficher exactement ce que le
premier a écrit. Ensuite **modifie** : ajoute des lignes dans `ecrire.c`, ou passe le mode de
`fopen` de `"w"` à `"a"` et relance plusieurs fois (les lignes s'**ajoutent** au lieu de
s'écraser). Essaie aussi de lire un fichier qui n'existe pas pour voir le message d'erreur
`NULL` s'afficher.

➡️ La suite du parcours (projets plus complets…) arrivera dans le même style.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
