# 🇨➕➕ Apprendre le C++ — pour grands débutants

Le **C++** part du langage **C** et lui ajoute deux super-pouvoirs : la **programmation
objet** (organiser le code en « objets ») et une grande **bibliothèque standard** (la
**STL**) remplie d'outils tout prêts. On l'utilise pour les jeux vidéo, les navigateurs
web, les logiciels exigeants en performance… Comme le C, c'est un langage **compilé**.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, compile, lance, modifie.

---

## 🆚 Différence clé avec Python : il faut COMPILER

Comme le C, le C++ n'est **pas interprété** : il faut le **compiler**.

- **Python** est *interprété* : tu écris `script.py` et tu le lances directement.
- **C++** est *compilé* : tu écris un fichier `.cpp`, puis un programme appelé
  **compilateur** (`g++`) le **traduit en langage machine** dans un fichier **exécutable**.
  C'est seulement cet exécutable que l'ordinateur lance.

```
   programme.cpp   ──[ g++ ]──►   programme (exécutable)   ──►   ça tourne
   (ton code)       compilation    (langage machine)            exécution
```

> Le module `00_demarrer` détaille ce cycle et comment installer le compilateur.

---

## 🆚 Et avec le C ? Le C++ est plus simple à utiliser

Si tu connais déjà le C, voici les nouveautés que tu verras dès les premiers programmes :

| | C | C++ |
|--|---|-----|
| Afficher | `printf("Age : %d\n", age);` | `std::cout << "Age : " << age << std::endl;` |
| Lire au clavier | `scanf("%d", &age);` | `std::cin >> age;` (pas de `&` ni de `%d`) |
| Texte | tableau de `char` (compliqué) | `std::string` (un vrai type de texte) |
| Boîte à outils | `#include <stdio.h>` | `#include <iostream>` |
| Booléen | `int` (0 = faux) | `bool` (`true` / `false`) natif |
| Espaces de noms | aucun | **namespaces** : `std::` = « dans la bibliothèque standard » |

Le C++ comprend **presque tout** le C, mais on préfère ses outils plus pratiques :
`std::cout` au lieu de `printf`, `std::cin` au lieu de `scanf`, `std::string` pour le texte.

> 💬 Le `std::` devant `cout`, `cin`, `string`… veut dire « cet outil vient de l'**espace de
> noms** (*namespace*) `std`, la bibliothèque standard ». On le garde **explicite** dans ce
> parcours : c'est plus clair pour un débutant que de cacher le `std::`.

Autres différences avec Python (héritées du C) :
| | Python | C++ |
|--|--------|-----|
| Types | dynamiques (`x = 5`) | **statiques** : on déclare le type (`int x = 5;`) |
| Fin d'instruction | retour à la ligne | un **point-virgule `;`** |
| Blocs | indentation | des **accolades `{ }`** |

---

## 📚 Le parcours (🚧 Fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Compiler/exécuter, structure d'un programme C++, `std::cout` |
| 1 | [`01_les_bases`](./01_les_bases/) | Types, variables, `std::cout`/`std::cin`, conditions, boucles, fonctions |
| 2 | [`02_conteneurs_chaines`](./02_conteneurs_chaines/) | `std::string` (texte), `std::vector` (liste qui grandit), boucle range-for |
| 3 | [`03_classes_objets`](./03_classes_objets/) | Programmation objet : classes & objets, attributs/méthodes, constructeur, `public`/`private` (encapsulation) |

> 🚧 **Fondations** : ce parcours débute. D'autres modules (fichiers, projets…) viendront
> ensuite, dans le même style.

---

## 📎 Ressources

- [`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md) — la syntaxe C++ essentielle en une page.
- [`GLOSSAIRE.md`](./GLOSSAIRE.md) — les mots du C++ expliqués simplement.

---

## ⚙️ Pré-requis : un compilateur

Tu as besoin de **`g++`** (ou `clang++`). Vérifie s'il est déjà là :

```bash
g++ --version
```

Sinon, voir les instructions d'installation dans [`00_demarrer`](./00_demarrer/).

## ▶️ Compiler et lancer un programme

```bash
# 1. Compiler le fichier source en un exécutable, puis le lancer
g++ cpp/00_demarrer/premier_programme.cpp -o premier_programme && ./premier_programme
```

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).
