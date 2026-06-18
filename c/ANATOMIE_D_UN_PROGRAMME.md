# 🧭 Anatomie d'un programme C : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire des lignes de C, mais ne savent pas **dans quel
ordre les ranger** pour former un programme complet et propre. Ce guide explique le
**cheminement logique** d'un programme C, du début à la fin.

> 📌 À lire après les modules [`00_demarrer`](./00_demarrer/) et
> [`01_les_bases`](./01_les_bases/), puis à garder sous la main comme aide-mémoire.
> C'est le cousin, côté C, du guide Python `python/ANATOMIE_D_UN_SCRIPT.md`.

---

## 1. LA règle d'or : le C se lit de HAUT en BAS

C'est le point le plus important, et la cause n°1 des bugs de débutant.

> Le compilateur lit ton fichier **de haut en bas**, comme tu lis une page.
> **Une chose doit exister AVANT qu'on l'utilise.**

Tu ne peux pas verser le café dans une tasse que tu n'as pas encore sortie du placard.
En code, c'est pareil : tu ne peux pas utiliser une variable, une fonction ou un outil
**avant** de l'avoir déclaré/inclus plus haut.

En C, cette règle a une conséquence très concrète :

> ⚠️ **Une fonction doit être connue du compilateur AVANT le premier endroit où on
> l'appelle.** Quand on appelle une fonction qui est *définie plus bas* dans le fichier,
> on prévient le compilateur à l'avance avec un **prototype** (sa « carte de visite »).

Un prototype, c'est juste l'en-tête de la fonction (type renvoyé, nom, types des
paramètres) suivi d'un point-virgule :

```c
int additionner(int a, int b);   // ← prototype : « cette fonction existe, voici sa forme »
```

Grâce à ce prototype écrit en haut, tu peux **appeler** `additionner(...)` dans `main()`
même si son **vrai code** est écrit plus bas. C'est la différence majeure avec Python,
où l'on doit définir la fonction entière avant de l'appeler.

---

## 2. Le SQUELETTE STANDARD d'un programme C

Presque tous les programmes C bien écrits suivent **ce même ordre**, de haut en bas :

```c
/*                                                         ┐
   Description du programme : à quoi il sert,              │  (0) COMMENTAIRE D'EN-TÊTE
   comment le compiler et le lancer.                       │      (facultatif mais conseillé)
*/                                                         ┘

#include <stdio.h>                                         ┐  (1) LES #include
#include <math.h>                                          ┘     (les boîtes à outils)

#define PI 3.14159                                         ┐  (2) #define / CONSTANTES
#define TAILLE_MAX 100                                     ┘     (valeurs fixes, EN MAJUSCULES)

int additionner(int a, int b);                            ┐  (3) PROTOTYPES de fonctions
double aire_disque(double rayon);                         ┘     (les « cartes de visite »)

int main(void)                                            ┐  (4) LA FONCTION main()
{                                                          │     (le POINT D'ENTRÉE :
    int somme = additionner(2, 3);                         │      le programme DÉMARRE ici
    printf("2 + 3 = %d\n", somme);                         │      et appelle les fonctions)
    printf("Aire d'un disque de rayon 1 : %.2f\n",         │
           aire_disque(1.0));                              │
    return 0;                                              │  ← 0 = « tout s'est bien passé »
}                                                          ┘

int additionner(int a, int b)                             ┐  (5) DÉFINITIONS des fonctions
{                                                          │     (le VRAI code des fonctions
    return a + b;                                          │      annoncées par les prototypes)
}                                                          │
                                                           │
double aire_disque(double rayon)                          │
{                                                          │
    return PI * rayon * rayon;                             │
}                                                          ┘
```

### Pourquoi cet ordre, partie par partie

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 0 | **Commentaire d'en-tête** | La 1re chose qu'on lit : « ce programme sert à… ». Facultatif, mais bien utile. |
| 1 | **`#include`** | On **ouvre les boîtes à outils** avant de s'en servir. `<stdio.h>` apporte `printf`/`scanf`, `<math.h>` les fonctions mathématiques, etc. (cours détaillé : module [`06_preprocesseur_modules`](./06_preprocesseur_modules/)) |
| 2 | **`#define` / constantes** | Les réglages fixes, regroupés en haut pour les changer facilement. Par convention, on les écrit `EN_MAJUSCULES`. |
| 3 | **Prototypes** | On **annonce** les fonctions au compilateur **avant** `main()`. Comme ça, `main()` (et les autres fonctions) peuvent les appeler même si leur code est écrit plus bas. C'est ça qui respecte la règle d'or « connu avant d'être utilisé ». |
| 4 | **`main()`** | Le **chef d'orchestre** : c'est le **point d'entrée**, l'endroit où le programme commence vraiment. Il appelle les fonctions dans le bon ordre. |
| 5 | **Définitions des fonctions** | Le **vrai code** des fonctions. Souvent placé **après** `main()` pour qu'on lise d'abord le déroulé général, puis les détails. Grâce aux prototypes, l'ordre du code ne pose plus de problème. |

> 💡 **Prototype vs définition.** Le *prototype* (en haut) est la **carte de visite** :
> il dit « cette fonction existe et voilà sa forme ». La *définition* (en bas) est
> l'**atelier** : c'est le vrai code. On annonce en haut, on détaille en bas.

> 🧠 **Variante fréquente.** Certains préfèrent écrire les fonctions **complètes au-dessus**
> de `main()`. Dans ce cas, les prototypes deviennent inutiles (la fonction est déjà connue).
> Mais dès qu'un programme grandit, **prototypes en haut + définitions en bas** reste la
> disposition la plus lisible — c'est celle à apprendre.

---

## 3. Le cycle en C : écrire → COMPILER → corriger → lancer

C'est LA grande différence avec Python. En Python, tu écris `script.py` et tu le lances
directement. En C, il y a une étape de plus : la **compilation**.

```
   programme.c   ──[ gcc ]──►   programme (exécutable)   ──►   ./programme
   (ton code)     COMPILATION    (langage machine)             EXÉCUTION
```

Le cycle complet ressemble à ceci :

```
   1. ÉCRIRE        2. COMPILER         3. CORRIGER          4. LANCER
   le .c            avec gcc            les erreurs          l'exécutable
   ──────           ─────────           ───────────          ──────────
   ton éditeur      gcc prog.c -o prog  gcc se plaint ?      ./prog
                                        tu corriges et
                                        tu re-compiles
```

```bash
# 1. Compiler le fichier source en un exécutable nommé "programme"
gcc -Wall c/00_demarrer/premier_programme.c -o programme

# 2. Lancer l'exécutable créé
./programme
```

> 💡 Ajoute toujours **`-Wall`** (« all warnings ») : le compilateur te signale les
> erreurs probables. C'est ton meilleur allié de débutant.

> ⚠️ **Important :** si tu modifies ton `.c`, tu dois **re-compiler** avant de relancer.
> Sinon tu exécutes l'ancienne version ! (En Python, pas besoin : il relit le fichier
> à chaque lancement.)

---

## 4. Le rôle spécial de `main()`

Dans tout programme C, **l'exécution commence par la fonction `main()`** — jamais ailleurs.
C'est le **point d'entrée** imposé par le langage : peu importe où `main()` est écrit dans
le fichier, c'est toujours par là que ça démarre.

```c
int main(void)
{
    /* ... tout le déroulé du programme ... */
    return 0;   // ← on rend 0 au système : « tout s'est bien passé »
}
```

Deux choses à retenir :

- **`int` devant `main`** : `main()` renvoie un entier au système d'exploitation.
- **`return 0;` à la fin** : par convention, **0 = succès**. Un nombre différent de zéro
  signale une **erreur** (utile pour les scripts qui enchaînent des programmes).

> 🧠 `int main(void)` : le `void` entre parenthèses veut dire « cette fonction ne reçoit
> aucune information ». (Plus tard, tu verras `int main(int argc, char *argv[])` pour lire
> les arguments de la ligne de commande — mais pas besoin pour débuter.)

---

## 5. La logique INTERNE : entrée → traitement → sortie

À l'intérieur de `main()` (ou d'une fonction), le code suit presque toujours **3 phases**,
dans cet ordre :

```
   1. ENTRÉE              2. TRAITEMENT              3. SORTIE
   (je récupère           (je calcule, je décide,    (j'affiche ou
    les données)           je transforme)             j'enregistre)
   ──────────             ───────────────            ──────────
   scanf(...)             if / else if / else         printf(...)
   fgets(...)             for / while                 fprintf(...) (fichier)
   fopen(...) + fread     calculs, appels de          fputs(...)
                          fonctions
```

Exemple complet et correct des 3 phases :

```c
#include <stdio.h>

int main(void)
{
    int age;

    /* 1. ENTRÉE : je récupère une donnée saisie au clavier */
    printf("Quel est ton age ? ");
    scanf("%d", &age);              // le & est obligatoire avec scanf

    /* 2. TRAITEMENT : je décide en fonction de la donnée */
    int annees_restantes = 18 - age;

    /* 3. SORTIE : j'affiche le résultat */
    if (age >= 18)
        printf("Tu es majeur.\n");
    else
        printf("Encore %d an(s) avant la majorite.\n", annees_restantes);

    return 0;
}
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

---

## 6. Comment lire un programme C complexe qu'on découvre

Quand un programme te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va directement à `main()`.** C'est le **point de départ** réel : il montre
   l'enchaînement principal des grandes étapes. (Inutile de t'attarder d'abord sur les
   `#include` ou les prototypes : ce ne sont que des préparatifs.)
2. **Suis les appels de fonctions** depuis `main()`. Quand tu vois `aire_disque(1.0)`,
   descends lire la fonction `double aire_disque(...)` pour comprendre ce qu'elle fait.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : `main()` te donne les titres de chapitres, puis tu
> ouvres les chapitres qui t'intéressent (les fonctions définies plus bas).

---

## 7. Récapitulatif visuel

```
┌─────────────────────────────────────────────────┐
│ 0. /* Commentaire */ : à quoi sert le programme  │
│ 1. #include <...>    : les boites a outils       │  ← on prépare
│ 2. #define / CONST   : les réglages fixes        │
├─────────────────────────────────────────────────┤
│ 3. prototypes ;      : on ANNONCE les fonctions  │  ← on outille
├─────────────────────────────────────────────────┤
│ 4. int main(void) {                              │
│        entrée  ->  traitement  ->  sortie        │  ← on EXÉCUTE
│        return 0;                                  │    (ça démarre ICI)
│    }                                              │
├─────────────────────────────────────────────────┤
│ 5. définitions des fonctions : le VRAI code      │  ← les détails
└─────────────────────────────────────────────────┘
   (le compilateur lit de haut en bas ; on COMPILE
    avec gcc, PUIS on lance l'exécutable)
```

➡️ Garde ce modèle en tête pour démarrer tes propres programmes du bon pied, et reviens-y
dès qu'un programme te semble en désordre. Sous la main aussi :
l'[`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md) et le [`GLOSSAIRE.md`](./GLOSSAIRE.md).
