# Module AVANCÉ 08 — La RÉCURSION (et le rôle de la pile)

Bravo, tu as digéré les **fondations** ! Ce module est **avancé** : il combine ce que tu
sais déjà sur la **pile** et les **fonctions** (module 02) pour comprendre une idée
puissante : une fonction qui **s'appelle elle-même**, la **récursion**.

> Fichier du module : [`factorielle.s`](./factorielle.s) — calcule `factorielle(5) = 120`
> de façon récursive. Comme d'habitude, tout est commenté presque ligne par ligne.

---

## 1. C'est quoi une fonction RÉCURSIVE ? (les poupées russes)

Une fonction **récursive** est une fonction qui **s'appelle elle-même**.

Imagine des **poupées russes** : tu ouvres une poupée, et à l'intérieur il y en a une
**plus petite**. Tu l'ouvres, encore une plus petite… jusqu'à la **toute petite** qu'on ne
peut **plus** ouvrir. Là, tu t'arrêtes, et tu **remontes** en refermant chaque poupée.

En récursion :

- Ouvrir une poupée = **se rappeler soi-même** avec un problème **plus petit**.
- La toute petite poupée = le **CAS DE BASE** : le cas le plus simple, qui **arrête** la
  descente. **Sans cas de base, ça ne s'arrêterait jamais** (boucle infinie qui plante).

---

## 2. La factorielle, un exemple parfait

La **factorielle** d'un nombre `n` (notée `n!`) est le produit de tous les entiers de 1 à n :

```
5! = 5 x 4 x 3 x 2 x 1 = 120
```

On peut la définir de façon **récursive** :

```
factorielle(n) = 1                       si n == 0   <- CAS DE BASE
factorielle(n) = n x factorielle(n - 1)  sinon       <- APPEL RÉCURSIF
```

Déroulé pour `5` (descente, puis remontée) :

```
factorielle(5) = 5 x factorielle(4)
factorielle(4) = 4 x factorielle(3)
factorielle(3) = 3 x factorielle(2)
factorielle(2) = 2 x factorielle(1)
factorielle(1) = 1 x factorielle(0)
factorielle(0) = 1                  <- CAS DE BASE atteint, on remonte
              -> 1 x 1 = 1
              -> 2 x 1 = 2
              -> 3 x 2 = 6
              -> 4 x 6 = 24
              -> 5 x 24 = 120       <- résultat final
```

---

## 3. Pourquoi la PILE est INDISPENSABLE ici

Rappel du module 02 :

- `push valeur` / `pop registre` : **poser** / **reprendre** une valeur sur la pile (LIFO).
- `call etiquette` / `ret` : **appeler** une fonction / **revenir** après l'appel. En
  coulisses, `call` **pose l'adresse de retour sur la pile**, et `ret` la **reprend**.

Le problème : chaque appel de `factorielle` se sert du **même registre** `rdi` pour
stocker **son** `n`. Mais avant de se rappeler avec `n - 1`, il doit **modifier** `rdi`…
et donc **écraser** sa propre valeur ! S'il ne faisait rien, au moment de remonter il aurait
**perdu** son `n` et ne pourrait plus faire la multiplication `n x factorielle(n-1)`.

La solution, c'est la **pile** :

1. **AVANT** l'appel récursif : `push rdi` — chaque appel **sauvegarde son n** sur la pile.
2. **APRÈS** l'appel récursif : `pop rdi` — il **récupère son n intact** pour multiplier.

Comme la pile est **LIFO**, chaque appel reprend **exactement** la valeur qu'il avait posée,
dans le bon ordre. C'est elle qui « se souvient » de tous les `n` empilés pendant la descente.

```asm
    push rdi          # sauvegarde MON n avant de tout chambouler
    sub  rdi, 1       # prépare n - 1
    call factorielle  # rax = factorielle(n - 1)
    pop  rdi          # je RÉCUPÈRE mon n intact
    imul rax, rdi     # rax = factorielle(n - 1) x n
    ret
```

> 💡 `imul rax, rdi` veut dire **multiplie** : `rax = rax x rdi`. C'est la version
> « multiplication » du `add` que tu connais déjà.

---

## 4. Pourquoi `5` et pas `6` ?

On « voit » le résultat en le renvoyant comme **CODE DE SORTIE** du programme (`echo $?`),
comme dans le module 01. Mais un code de sortie ne peut aller que de **0 à 255**.

| Calcul | Résultat | Tient dans 0–255 ? |
|--------|----------|--------------------|
| `5!`   | **120**  | ✅ oui (120 < 256) |
| `6!`   | **720**  | ❌ non (720 > 255) — on lirait `720 % 256 = 208`, faux et trompeur |

On choisit donc **`5`** pour que `120` rentre **pile** dans le code de sortie et reste
**lisible directement**. (Pour de plus grands nombres, il faudrait **afficher** le résultat
avec `write` + conversion en chiffres, comme au module 04.)

---

## ▶️ À toi de jouer

```bash
# factorielle.s : calcule factorielle(5) de façon récursive -> exit=120
as asm/08_recursion/factorielle.s -o /tmp/f.o && ld /tmp/f.o -o /tmp/f && /tmp/f ; echo "exit=$?"
```

Tu dois lire **`exit=120`**. Ensuite, expérimente :

- Change `mov rdi, 5` en `mov rdi, 4` : tu devrais lire `exit=24` (car `4! = 24`).
- Essaie `mov rdi, 0` : `exit=1` (le **cas de base** seul). Puis `mov rdi, 1` : `exit=1`.
- ⚠️ Essaie `mov rdi, 6` pour **voir** le piège : tu liras `exit=208` (720 ne tient pas).
- Pour aller plus loin : lance le programme **pas à pas dans gdb** (module 07) et regarde la
  pile grandir à chaque appel, puis se vider à chaque `ret`. C'est la récursion en direct !

📎 Besoin d'un rappel ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md), le
[GLOSSAIRE.md](../GLOSSAIRE.md) et surtout le module
[`02_pile_fonctions`](../02_pile_fonctions/) (pile, `push`/`pop`, `call`/`ret`).
