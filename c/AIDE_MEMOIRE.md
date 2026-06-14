# 🃏 Aide-mémoire C (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle du C. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases`, `02_tableaux_chaines`…

> 🧠 Rappels de fond : chaque instruction se termine par **`;`**, les blocs sont entre
> **accolades `{ }`**, et il faut **compiler** avant de pouvoir exécuter.

---

## Compiler et lancer (gcc)

```bash
gcc programme.c -o programme   # compile programme.c -> exécutable "programme"
./programme                    # lance l'exécutable

gcc -Wall programme.c -o prog  # -Wall : ACTIVE TOUS les avertissements (recommandé)
```

## Structure type d'un programme

```c
#include <stdio.h>     // 1. inclure les boîtes à outils (ici : printf)

int additionner(int a, int b) {   // 2. fonctions (AVANT main)
    return a + b;
}

int main(void) {       // 3. main : le point de départ obligatoire
    // ... ton code ...
    return 0;          // 0 = tout s'est bien passé
}
```

## Types de base

```c
int    age   = 30;     // entier
double prix  = 9.99;   // nombre à virgule (décimal)
float  x     = 1.5f;   // décimal moins précis
char   lettre = 'A';   // UN caractère, entre apostrophes ' '
```

> Pas de vrai booléen d'origine : `0 = faux`, tout le reste `= vrai`.
> (`#include <stdbool.h>` ajoute `bool`, `true`, `false`.)

## Afficher / lire : printf & scanf + spécificateurs

```c
printf("Age : %d\n", age);       // \n = retour à la ligne
printf("Prix : %.2f\n", prix);   // .2 = 2 chiffres après la virgule
scanf("%d", &age);               // lire un entier (NE PAS oublier le &)
```

| Spécificateur | Type | Usage printf / scanf |
|---------------|------|----------------------|
| `%d` | `int` | entier |
| `%f` | `float`/`double` | décimal (`%.2f` = 2 décimales) |
| `%c` | `char` | un caractère |
| `%s` | chaîne | du texte (tableau de char) |
| `%lu` | `size_t` | ce que renvoie `strlen` |

## Opérateurs

```c
+  -  *  /        // arithmétique
%                 // reste (modulo) : 7 % 2 == 1
==  !=            // égal / différent
<  >  <=  >=      // comparaisons
&&  ||  !         // ET / OU / NON logiques
i++   i--         // i = i + 1   /   i = i - 1
```

## Conditions

```c
if (note >= 16) {
    printf("Tres bien\n");
} else if (note >= 10) {     // 'else if', pas 'elif'
    printf("Recu\n");
} else {
    printf("A retravailler\n");
}
```

## Boucles

```c
// for : (début ; condition ; pas)
for (int i = 0; i < 5; i++) {   // i va de 0 à 4
    printf("%d\n", i);
}

// while : tant que la condition est vraie
int n = 0;
while (n < 5) {
    n++;                         // sinon : boucle infinie !
}
```

## Fonctions

```c
int additionner(int a, int b) {  // type de retour + paramètres typés
    return a + b;
}
void saluer(void) {              // void = ne renvoie rien
    printf("Bonjour !\n");
}
```

> À définir **avant** `main`, ou à annoncer par un **prototype** en haut du fichier :
> `int additionner(int a, int b);`

## Tableaux (taille fixe, indices à partir de 0)

```c
int notes[5];                       // 5 cases (vides)
int notes[5] = {12, 8, 15, 10, 18}; // 5 cases remplies
notes[0]                            // 1re case ; notes[4] = dernière
notes[1] = 9;                       // modifier une case

for (int i = 0; i < 5; i++) {       // parcourir SANS dépasser (i < 5)
    somme += notes[i];
}
```

> ⚠️ Indices valides : `0` à `taille - 1`. Dépasser = bug ou plantage (aucun garde-fou).

## Chaînes de caractères (`#include <string.h>`)

```c
char nom[] = "Alice";   // tableau de char terminé par '\0'

strlen(nom)             // longueur (5) — sans compter le '\0'
strcpy(copie, nom)      // copier nom dans copie (copie doit être assez grand)
strcmp(a, b) == 0       // a et b identiques ? (PAS de == sur les chaînes !)

for (int i = 0; nom[i] != '\0'; i++) {  // parcourir lettre par lettre
    printf("%c", nom[i]);
}
```

> ⚠️ `"Alice"` (5 lettres) occupe **6 cases** : les lettres + le `'\0'` final.

---

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) pour le sens des mots du C.
