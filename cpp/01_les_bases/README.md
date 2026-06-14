# Module 01 — Les bases du C++

Les mêmes briques fondamentales que dans tout langage (variables, conditions, boucles,
fonctions), mais avec la **rigueur du C++** : on déclare le **type** de chaque variable, et
on termine chaque instruction par un **`;`**. Bonne nouvelle : le C++ rend l'affichage, la
lecture et le texte **plus simples** qu'en C.

> Fichiers du module : `bases.cpp` (les briques) et `mini_calculatrice.cpp` (un mini-projet).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Les variables ont un TYPE déclaré

En Python tu écrivais `age = 30`. En C++, tu dois **annoncer le type** de la variable :

```cpp
int age = 30;            // int    : un nombre entier
double prix = 9.99;      // double : un nombre à virgule (décimal)
char lettre = 'A';       // char   : UN seul caractère, entre apostrophes simples ' '
std::string nom = "Lou"; // string : du TEXTE, entre guillemets doubles " "
bool majeur = true;      // bool   : vrai (true) ou faux (false)
```

Pourquoi ? Parce que le C++ a besoin de savoir **comment** interpréter la valeur. Une fois
le type fixé, il ne change pas.

Les **types de base** à connaître :

| Type | Sert à | Exemple |
|------|--------|---------|
| `int` | nombre entier | `42` |
| `double` | nombre à virgule | `3.14` |
| `char` | un seul caractère | `'A'` |
| `std::string` | du texte | `"Bonjour"` |
| `bool` | vrai ou faux | `true` / `false` |

> 🆚 **Différences avec le C** : le C++ a un vrai type `bool` (`true`/`false`) et, surtout,
> un vrai type texte **`std::string`** (en C il fallait jongler avec des tableaux de `char`).
> Pour utiliser `std::string`, on ajoute `#include <string>`.

---

## 2. Afficher avec `std::cout`

Fini les `%d`, `%f`, `%s` du `printf` du C ! En C++, on **enchaîne** les valeurs avec
l'opérateur `<<`, et le C++ devine tout seul comment les afficher :

```cpp
int age = 30;
double prix = 9.99;
std::cout << "Age : " << age << " ans" << std::endl;     // mélange texte + nombre
std::cout << "Prix : " << prix << " euros" << std::endl; // pas de %f à se rappeler
```

- `std::cout` = la sortie console (l'écran).
- `<<` = « envoie ceci vers l'écran » ; on en enchaîne autant qu'on veut.
- `std::endl` = un retour à la ligne (équivalent du `\n`).

> 🆚 En C : `printf("Age : %d\n", age);`. En C++ : `std::cout << "Age : " << age <<
> std::endl;`. Plus besoin de faire correspondre un `%...` à chaque variable.

---

## 3. Lire une saisie avec `std::cin`

L'équivalent C++ de `input()`. On utilise `std::cin` avec l'opérateur `>>` (les flèches
pointent **vers la variable** : « range ce que tape l'utilisateur dans la variable »).

```cpp
int age;
std::cout << "Quel age as-tu ? ";
std::cin >> age;   // lit un entier tapé au clavier et le range dans 'age'
```

> 🆚 En C : `scanf("%d", &age);` (avec un `%d` et un `&`). En C++ : `std::cin >> age;`
> — **pas de `%d`, pas de `&`**. C'est plus simple et plus sûr.

---

## 4. Conditions : `if` / `else if` / `else`

```cpp
int note = 12;
if (note >= 16) {                              // la condition est entre parenthèses ( )
    std::cout << "Tres bien" << std::endl;     // le bloc est entre accolades { }
} else if (note >= 10) {
    std::cout << "Recu" << std::endl;
} else {
    std::cout << "A retravailler" << std::endl;
}
```

Différences avec Python : la condition est entre **`( )`**, le bloc entre **`{ }`**, et on
écrit **`else if`** (pas `elif`). Les comparaisons sont les mêmes : `==`, `!=`, `<`, `>`,
`<=`, `>=`, et les opérateurs logiques `&&` (ET), `||` (OU), `!` (NON). (Identique au C.)

---

## 5. Boucles : `for` et `while`

```cpp
// Répéter un nombre précis de fois.
// for (initialisation ; condition ; incrément)
for (int i = 0; i < 3; i++) {                       // i++ veut dire "i = i + 1"
    std::cout << "Tour " << i << std::endl;         // affiche 0, 1, 2
}

// Répéter tant qu'une condition est vraie.
int compteur = 0;
while (compteur < 3) {
    std::cout << "compteur = " << compteur << std::endl;
    compteur++;                                      // sans ça, boucle infinie !
}
```

Le `for` du C++ est très explicite : entre les `( )`, on déclare **3 choses** séparées par
`;` — par où on commence, jusqu'à quand on continue, et comment on avance à chaque tour.
(Mêmes boucles qu'en C.)

---

## 6. Fonctions : on déclare le type de retour et des paramètres

```cpp
// 'int' (à gauche) = type de la valeur RENVOYÉE.
// (int a, int b)   = les paramètres, chacun avec SON type.
int additionner(int a, int b) {
    return a + b;   // 'return' renvoie le résultat
}

// Une fonction qui ne renvoie rien utilise 'void' :
void saluer() {
    std::cout << "Bonjour !" << std::endl;
}
```

⚠️ Comme en C, une fonction doit être **connue avant d'être appelée**. On la définit donc
*au-dessus* de `main` (ou on en met le « prototype » en haut — on verra ça plus tard).

---

## ▶️ À toi de jouer

```bash
# Le fichier des briques de base
g++ cpp/01_les_bases/bases.cpp -o bases && ./bases

# Le mini-projet calculatrice (tape l'opération puis deux nombres quand il le demande)
g++ cpp/01_les_bases/mini_calculatrice.cpp -o calc && ./calc
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : ajoute une opération,
change les conditions, crée ta propre fonction.

➡️ La suite du parcours (objets & classes, `std::vector`, fichiers…) arrivera dans le même style.
