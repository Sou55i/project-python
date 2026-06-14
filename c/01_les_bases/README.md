# Module 01 — Les bases du C

Les mêmes briques fondamentales que dans tout langage (variables, conditions, boucles,
fonctions), mais avec la **rigueur du C** : on déclare le **type** de chaque variable, et
on termine chaque instruction par un **`;`**.

> Fichiers du module : `bases.c` (les briques) et `mini_calculatrice.c` (un mini-projet).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Les variables ont un TYPE déclaré

En Python tu écrivais `age = 30`. En C, tu dois **annoncer le type** de la variable :

```c
int age = 30;        // int    : un nombre entier
double prix = 9.99;  // double : un nombre à virgule (décimal)
char lettre = 'A';   // char   : UN seul caractère, entre apostrophes simples ' '
```

Pourquoi ? Parce que le C a besoin de savoir **combien de place** réserver en mémoire et
**comment** interpréter la valeur. Une fois le type fixé, il ne change pas.

Les **types de base** à connaître :

| Type | Sert à | Exemple |
|------|--------|---------|
| `int` | nombre entier | `42` |
| `double` | nombre à virgule | `3.14` |
| `char` | un seul caractère | `'A'` |
| `float` | décimal (moins précis que `double`) | `1.5f` |

> ⚠️ Le C n'a pas de vrai type « booléen » d'origine : on utilise souvent `int` où **0 = faux**
> et **toute autre valeur = vrai**. (Depuis C99, `#include <stdbool.h>` ajoute `bool`,
> `true`, `false`.)

---

## 2. Afficher avec `printf` et les « spécificateurs de format »

`printf` ne devine pas le type de ce que tu affiches : tu dois le lui dire avec un
**spécificateur** qui commence par `%` :

```c
int age = 30;
double prix = 9.99;
printf("Age : %d\n", age);      // %d = un entier (int)
printf("Prix : %.2f\n", prix);  // %f = un décimal ; .2 = 2 chiffres après la virgule
printf("Lettre : %c\n", 'A');   // %c = un caractère
printf("Texte : %s\n", "salut"); // %s = une chaîne de caractères
```

À chaque `%` dans le texte correspond **une variable** donnée après la virgule, **dans
l'ordre**. C'est l'équivalent (un peu plus manuel) des f-strings de Python.

| Spécificateur | Type affiché |
|---------------|--------------|
| `%d` | entier (`int`) |
| `%f` | décimal (`float`/`double`) |
| `%c` | un caractère (`char`) |
| `%s` | une chaîne de caractères |

---

## 3. Lire une saisie avec `scanf`

L'équivalent C de `input()`. Petite subtilité : il faut mettre un **`&`** devant la variable
(ça signifie « à l'adresse de » — on en reparlera avec les pointeurs).

```c
int age;
printf("Quel age as-tu ? ");
scanf("%d", &age);   // lit un entier tapé au clavier et le range dans 'age'
```

> 💡 Contrairement à Python, pas besoin de convertir : `scanf("%d", ...)` lit **directement**
> un entier (grâce au `%d`).

---

## 4. Conditions : `if` / `else if` / `else`

```c
int note = 12;
if (note >= 16) {          // la condition est entre parenthèses ( )
    printf("Tres bien\n"); // le bloc est entre accolades { }
} else if (note >= 10) {
    printf("Recu\n");
} else {
    printf("A retravailler\n");
}
```

Différences avec Python : la condition est entre **`( )`**, le bloc entre **`{ }`**, et on
écrit **`else if`** (pas `elif`). Les comparaisons sont les mêmes : `==`, `!=`, `<`, `>`,
`<=`, `>=`, et les opérateurs logiques `&&` (ET), `||` (OU), `!` (NON).

---

## 5. Boucles : `for` et `while`

```c
// Répéter un nombre précis de fois.
// for (initialisation ; condition ; incrément)
for (int i = 0; i < 3; i++) {   // i++ veut dire "i = i + 1"
    printf("Tour %d\n", i);     // affiche 0, 1, 2
}

// Répéter tant qu'une condition est vraie.
int compteur = 0;
while (compteur < 3) {
    printf("compteur = %d\n", compteur);
    compteur++;                  // sans ça, boucle infinie !
}
```

Le `for` du C est très explicite : entre les `( )`, on déclare **3 choses** séparées par
`;` — par où on commence, jusqu'à quand on continue, et comment on avance à chaque tour.

---

## 6. Fonctions : on déclare le type de retour et des paramètres

```c
// 'int' (à gauche) = type de la valeur RENVOYÉE.
// (int a, int b)   = les paramètres, chacun avec SON type.
int additionner(int a, int b) {
    return a + b;   // 'return' renvoie le résultat
}

// Une fonction qui ne renvoie rien utilise 'void' :
void saluer(void) {
    printf("Bonjour !\n");
}
```

⚠️ En C, une fonction doit être **connue avant d'être appelée**. On la définit donc *au-dessus*
de `main`, ou on en met le « prototype » en haut du fichier (on verra ça plus tard).

---

## ▶️ À toi de jouer

```bash
# Le fichier des briques de base
gcc c/01_les_bases/bases.c -o bases && ./bases

# Le mini-projet calculatrice (tape deux nombres quand il le demande)
gcc c/01_les_bases/mini_calculatrice.c -o calc && ./calc
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : ajoute une opération,
change les conditions, crée ta propre fonction.

➡️ La suite du parcours (tableaux & chaînes, pointeurs…) arrivera dans le même style.
