# Module 00 — Démarrer en C++ : compiler et exécuter

Avant d'écrire du code, comprenons **ce qui se passe** quand on programme en C++. Ce module
est surtout théorique, avec un premier programme à compiler à la fin.

---

## 1. C'est quoi « compiler » ?

L'ordinateur ne comprend pas directement le texte que tu écris (`std::cout << ...`). Il ne
comprend que le **langage machine** (des 0 et des 1). En C++, il faut donc une étape de
**traduction** appelée **compilation** :

```
   premier_programme.cpp   ──[ g++ ]──►   premier_programme   ──►   exécution
   (TON code, lisible)      compilateur    (langage machine)         (ça tourne)
```

Analogie : tu écris une recette en français (`.cpp`), un **traducteur** (`g++`) la traduit
en une langue que le cuisinier (le processeur) comprend, et tu obtiens un **plat prêt à
servir** (l'exécutable).

> 📌 Conséquence importante : si ton code contient une faute, **le compilateur refuse de
> traduire** et t'affiche des erreurs. Rien ne s'exécute tant que ça ne compile pas. C'est
> normal et utile : il attrape beaucoup d'erreurs *avant* l'exécution.

---

## 2. Installer un compilateur

Il te faut **`g++`** (le compilateur C++ le plus répandu) ou `clang++`.

- **Linux (Debian/Ubuntu)** : `sudo apt install build-essential`
- **macOS** : installe les outils de développement avec `xcode-select --install`
  (fournit `clang++`, utilisable comme `g++`).
- **Windows** : installe **MinGW-w64** (fournit `g++`), ou utilise **WSL** (un Linux intégré
  à Windows) puis la commande Linux ci-dessus.

Vérifie l'installation :

```bash
g++ --version
```

---

## 3. La structure minimale d'un programme C++

Voici le plus petit programme C++ utile, décortiqué :

```cpp
#include <iostream>   // (1) on inclut la "boîte à outils" d'entrée/sortie (pour std::cout)

int main() {          // (2) la fonction main : le POINT DE DÉPART de tout programme C++
    std::cout << "Bonjour" << std::endl; // (3) afficher du texte + un retour à la ligne
    return 0;         // (4) on renvoie 0 = "tout s'est bien passé"
}
```

1. **`#include <iostream>`** : charge les outils d'affichage et de lecture (`iostream` =
   *input/output stream*, le flux d'entrée/sortie). Sans ça, `std::cout` est inconnu. C'est
   l'équivalent d'un `import`. (En C on incluait `<stdio.h>` pour `printf`.)
2. **`int main()`** : **tout programme C++ démarre par la fonction `main`**. Le `int`
   indique qu'elle renvoie un nombre entier au système. Les accolades `{ }` délimitent son
   contenu.
3. **`std::cout << ... << std::endl;`** : affiche du texte.
   - `std::cout` = la *sortie console* (l'écran). `std` = la **bibliothèque standard**.
   - `<<` = l'opérateur d'**envoi** : « envoie ceci vers l'écran ». On peut en enchaîner
     plusieurs.
   - `std::endl` = un **retour à la ligne** (l'équivalent du `\n` du C).
   - Chaque instruction se termine par un **`;`**.
4. **`return 0;`** : signale au système que le programme s'est terminé **sans erreur**
   (par convention, `0` = succès).

> 💬 Les commentaires en C++ s'écrivent `// sur une ligne` ou `/* sur plusieurs lignes */`.
> Le compilateur les ignore : ils sont là pour les humains.

> 🆚 En C on écrivait `printf("Bonjour\n");`. En C++ on préfère
> `std::cout << "Bonjour" << std::endl;` : plus sûr (pas de `%d`/`%s` à gérer soi-même).

---

## 4. Compiler et lancer

Une fois le fichier `premier_programme.cpp` écrit :

```bash
# Compiler (-o donne le NOM de l'exécutable) PUIS lancer (le && enchaîne les deux)
g++ cpp/00_demarrer/premier_programme.cpp -o premier_programme && ./premier_programme
```

Le cycle de travail en C++ est donc : **écrire → compiler → (corriger les erreurs) → lancer**.

---

## ▶️ À toi de jouer

Compile et lance le programme de ce module :

```bash
g++ cpp/00_demarrer/premier_programme.cpp -o premier_programme && ./premier_programme
```

Lis ensuite [`premier_programme.cpp`](./premier_programme.cpp) (tout est commenté), puis
**modifie le texte** et **recompile** pour voir le changement.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
