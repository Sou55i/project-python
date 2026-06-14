# Module 03 — Pointeurs & mémoire

Voici LE chapitre qui fait peur aux débutants… et qui n'a pas besoin de faire peur. Un
**pointeur**, c'est juste une variable un peu spéciale. Une fois l'idée comprise avec une
bonne analogie, tout devient logique. On y va doucement.

> Fichiers du module : `pointeurs.c` (l'adresse `&` et le déréférencement `*`) et
> `memoire.c` (réserver/libérer de la mémoire avec `malloc`/`free`).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Une variable vit quelque part : elle a une ADRESSE

Quand tu écris `int age = 30;`, l'ordinateur range ce `30` **quelque part** dans sa mémoire.
Cet « endroit » a un **numéro** : c'est son **adresse**.

🏠 **Analogie : une rue de maisons.** Chaque maison (case mémoire) a un **numéro** (l'adresse).
La variable `age`, c'est la maison ; `30`, c'est ce qu'il y a **dedans** ; et l'adresse, c'est
le **numéro** écrit sur la façade.

Pour obtenir l'adresse d'une variable, on utilise l'opérateur **`&`** (« adresse de ») —
celui-là même que tu as déjà croisé avec `scanf` au module 01 !

```c
int age = 30;
printf("La valeur : %d\n", age);    // 30
printf("L'adresse : %p\n", &age);   // ex: 0x7ffd... (un numéro de case mémoire)
```

> `%p` est le spécificateur `printf` pour afficher une **adresse** (un « pointeur »).

---

## 2. Un POINTEUR : une variable qui contient une adresse

📝 **Analogie : un papier où est noté le numéro d'une maison.** Le papier n'est pas la
maison ; il **indique** où elle se trouve. Un **pointeur**, c'est exactement ça : une
variable qui ne contient pas une valeur « normale », mais **l'adresse d'une autre variable**.

On le déclare en mettant une **étoile `*`** dans le type :

```c
int age = 30;
int *p = &age;   // 'p' est un pointeur vers un int ; il contient l'ADRESSE de 'age'
```

À lire ainsi : `int *p` veut dire « `p` est un pointeur vers un `int` ». Et `p = &age`
range **l'adresse** de `age` dans `p`. Maintenant `p` « pointe sur » `age`.

```
   age                          p
 ┌──────┐                    ┌──────────┐
 │  30  │  ◄──── pointe ──── │ adresse  │
 └──────┘                    │ de age   │
 maison                      papier (note le numéro)
```

---

## 3. L'étoile `*` pour ALLER VOIR la valeur (déréférencer)

L'opérateur `*` placé **devant un pointeur** veut dire « va à l'adresse notée, et donne-moi
ce qu'il y a là ». On appelle ça **déréférencer**.

🚶 **Analogie :** tu lis le numéro sur le papier (`p`), tu te rends à la maison, et tu
regardes ce qu'il y a dedans (`*p`).

```c
int age = 30;
int *p = &age;

printf("%d\n", *p);   // 30  -> "va à l'adresse dans p, lis la valeur"

*p = 42;              // "va à l'adresse dans p, et ÉCRIS 42 là-bas"
printf("%d\n", age);  // 42  -> on a modifié 'age' À TRAVERS le pointeur !
```

> ⚠️ Ne confonds pas les deux rôles de l'étoile :
> - **à la déclaration** (`int *p`) → ça veut dire « `p` est un pointeur » ;
> - **à l'utilisation** (`*p`) → ça veut dire « la valeur pointée ».

| Écriture | Se lit | Donne |
|----------|--------|-------|
| `age` | la valeur | `42` |
| `&age` | l'adresse de age | une adresse (ex: `0x7ffd…`) |
| `p` | l'adresse rangée dans p | la même adresse |
| `*p` | la valeur à cette adresse | `42` |

---

## 4. À quoi ça sert ? Modifier une variable DEPUIS une fonction

Voici le cas concret qui rend les pointeurs indispensables. En C, quand tu passes une
variable à une fonction, la fonction reçoit une **copie**. Modifier la copie ne change
**pas** l'original :

```c
void doubler_rate(int n) {   // n est une COPIE
    n = n * 2;               // on modifie la copie... pour rien
}
// après l'appel, la variable d'origine n'a pas bougé.
```

Pour modifier **vraiment** l'original, on passe son **adresse** (un pointeur). La fonction
peut alors aller écrire directement à la bonne case :

```c
void doubler(int *n) {   // n est un pointeur : l'adresse de l'original
    *n = *n * 2;         // on écrit le double À L'ADRESSE pointée
}

int x = 5;
doubler(&x);             // on donne l'ADRESSE de x
printf("%d\n", x);       // 10  -> x a bien été modifié !
```

C'est précisément le mécanisme du `&` de `scanf("%d", &age)` : on donne l'adresse de `age`
pour que `scanf` puisse **y écrire** ce que tu tapes.

---

## 5. Tableaux et pointeurs : une famille proche

Souviens-toi du module 02 : un tableau, c'est une suite de cases côte à côte. En C, le **nom
d'un tableau** représente en réalité **l'adresse de sa première case**. Tableaux et pointeurs
sont donc très liés :

```c
int notes[3] = {10, 20, 30};
int *p = notes;        // 'notes' vaut déjà l'adresse de la 1ʳᵉ case (pas besoin de &)

printf("%d\n", *p);    // 10  -> la première case
printf("%d\n", p[1]);  // 20  -> on peut indexer un pointeur comme un tableau !
```

> 💡 C'est pour ça que `%s` (les chaînes) marche avec un simple tableau de `char` : on lui
> passe l'**adresse** du début, et il lit jusqu'au `'\0'`.

---

## 6. `NULL` : le pointeur qui ne pointe sur rien

Parfois un pointeur ne désigne **aucune** variable. On lui donne alors la valeur spéciale
**`NULL`** (le « papier vierge », sans numéro noté dessus).

```c
int *p = NULL;   // p ne pointe sur rien pour l'instant
```

C'est utile pour dire « pas encore prêt » et pour **tester** avant d'utiliser :

```c
if (p != NULL) {
    printf("%d\n", *p);   // sûr : on ne déréférence que si p pointe sur quelque chose
}
```

---

## 7. ⚠️ Le danger : le pointeur invalide → plantage (`segfault`)

Déréférencer un pointeur qui ne pointe sur rien de valable (un `NULL`, ou une adresse au
hasard) fait **planter** le programme : c'est la fameuse **`Segmentation fault`** (« segfault »).

🏚️ **Analogie :** ton papier indique un numéro de maison **qui n'existe pas**. Tu y vas… et
il n'y a rien. Le système d'exploitation coupe net le programme pour te protéger.

```c
int *p = NULL;
*p = 5;   // 💥 BOUM : segfault (on écrit "nulle part")
```

> 🛡️ **Règles d'or :** un pointeur doit pointer sur quelque chose de **valide** avant d'être
> déréférencé. Dans le doute, initialise à `NULL` et **teste** `!= NULL` avant de faire `*p`.

---

## 8. La mémoire DYNAMIQUE : `malloc` pour réserver

Jusqu'ici, la taille de nos tableaux était **fixée à l'écriture du code** (`int notes[5]`).
Mais comment faire si on ne connaît le nombre d'éléments qu'**au moment de l'exécution**
(par exemple, l'utilisateur tape combien il en veut) ?

Réponse : on **demande de la mémoire à la volée** avec **`malloc`** (« memory allocation »).
Il faut inclure `<stdlib.h>`.

🏗️ **Analogie : louer une place de parking.** Tu demandes au gardien (`malloc`) un espace
d'une certaine **taille**. Il te répond en te donnant **l'adresse** de la place réservée
(un pointeur). Tu peux t'en servir tant que tu veux…

```c
#include <stdlib.h>

int n = 5;
int *tab = malloc(n * sizeof(int));   // réserve la place pour n entiers
```

- `sizeof(int)` = la taille (en octets) d'**un** `int` ;
- `n * sizeof(int)` = la place pour **n** entiers ;
- `malloc` renvoie l'**adresse** du début de la zone réservée (un pointeur).

⚠️ `malloc` peut **échouer** (mémoire pleine) : il renvoie alors `NULL`. On vérifie
**toujours** :

```c
if (tab == NULL) {
    printf("Plus de memoire !\n");
    return 1;   // on arrête proprement
}
```

Ensuite, on utilise `tab` exactement comme un tableau normal : `tab[0]`, `tab[1]`, etc.

---

## 9. `free` : TOUJOURS rendre la mémoire empruntée

La mémoire réservée par `malloc` n'est **pas** rendue automatiquement. C'est à **toi** de la
libérer avec **`free`** quand tu n'en as plus besoin.

🅿️ **Suite de l'analogie :** quand tu as fini, tu **rends la place de parking** au gardien
(`free`). Si tout le monde garde sa place « au cas où » sans jamais la rendre, le parking se
**remplit** et plus personne ne peut se garer. En programmation, ça s'appelle une **fuite de
mémoire** (*memory leak*).

```c
free(tab);     // on rend la mémoire réservée plus haut
tab = NULL;    // bonne habitude : on évite de réutiliser un pointeur "rendu"
```

> 🛡️ **Règle d'or :** à **chaque** `malloc` doit correspondre **un** `free`. Réserve →
> utilise → libère. Et ne te sers **plus** d'un pointeur après l'avoir `free` (sinon, danger).

---

## ▶️ À toi de jouer

```bash
# Les pointeurs : adresse &, déréférencement *, modifier via une fonction
gcc -Wall c/03_pointeurs_memoire/pointeurs.c -o pointeurs && ./pointeurs

# La mémoire dynamique : malloc, remplir, afficher, free
gcc -Wall c/03_pointeurs_memoire/memoire.c -o memoire && ./memoire
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : écris une fonction qui
échange deux variables via leurs pointeurs, change la taille du tableau dynamique, ajoute le
test `== NULL`, oublie volontairement le `free` pour voir l'idée de la fuite.

➡️ La suite du parcours (fichiers, projets…) arrivera dans le même style.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
