# Module 00 — Démarrer en C : compiler et exécuter

Avant d'écrire du code, comprenons **ce qui se passe** quand on programme en C. Ce module est
surtout théorique, avec un premier programme à compiler à la fin.

---

## 1. C'est quoi « compiler » ?

L'ordinateur ne comprend pas directement le texte que tu écris (`printf(...)`). Il ne
comprend que le **langage machine** (des 0 et des 1). En C, il faut donc une étape de
**traduction** appelée **compilation** :

```
   premier_programme.c   ──[ gcc ]──►   premier_programme   ──►   exécution
   (TON code, lisible)    compilateur    (langage machine)         (ça tourne)
```

Analogie : tu écris une recette en français (`.c`), un **traducteur** (`gcc`) la traduit
en une langue que le cuisinier (le processeur) comprend, et tu obtiens un **plat prêt à
servir** (l'exécutable).

> 📌 Conséquence importante : si ton code contient une faute, **le compilateur refuse de
> traduire** et t'affiche des erreurs. Rien ne s'exécute tant que ça ne compile pas. C'est
> normal et utile : il attrape beaucoup d'erreurs *avant* l'exécution.

---

## 2. Installer un compilateur

Il te faut **`gcc`** (le compilateur C le plus répandu) ou `clang`.

- **Linux (Debian/Ubuntu)** : `sudo apt install build-essential`
- **macOS** : installe les outils de développement avec `xcode-select --install`
  (fournit `clang`, utilisable comme `gcc`).
- **Windows** : installe **MinGW-w64** (fournit `gcc`), ou utilise **WSL** (un Linux intégré
  à Windows) puis la commande Linux ci-dessus.

Vérifie l'installation :

```bash
gcc --version
```

---

## 3. La structure minimale d'un programme C

Voici le plus petit programme C utile, décortiqué :

```c
#include <stdio.h>      // (1) on inclut la "boîte à outils" d'entrée/sortie (pour printf)

int main(void) {        // (2) la fonction main : le POINT DE DÉPART de tout programme C
    printf("Bonjour\n"); // (3) afficher du texte. \n = retour à la ligne
    return 0;           // (4) on renvoie 0 = "tout s'est bien passé"
}
```

1. **`#include <stdio.h>`** : charge les outils d'affichage (`stdio` = *standard
   input/output*). Sans ça, `printf` est inconnu. C'est l'équivalent d'un `import`.
2. **`int main(void)`** : **tout programme C démarre par la fonction `main`**. Le `int`
   indique qu'elle renvoie un nombre entier au système. Les accolades `{ }` délimitent son
   contenu.
3. **`printf(...)`** : affiche du texte. Chaque instruction se termine par un **`;`**.
4. **`return 0;`** : signale au système que le programme s'est terminé **sans erreur**
   (par convention, `0` = succès).

> 💬 Les commentaires en C s'écrivent `// sur une ligne` ou `/* sur plusieurs lignes */`.
> Le compilateur les ignore : ils sont là pour les humains.

---

## 4. Compiler et lancer

Une fois le fichier `premier_programme.c` écrit :

```bash
# Compiler : -o donne le NOM de l'exécutable à créer
gcc c/00_demarrer/premier_programme.c -o premier_programme

# Lancer l'exécutable (le ./ signifie "dans le dossier courant")
./premier_programme
```

Le cycle de travail en C est donc : **écrire → compiler → (corriger les erreurs) → lancer**.

---

## ▶️ À toi de jouer

Compile et lance le programme de ce module :

```bash
gcc c/00_demarrer/premier_programme.c -o premier_programme
./premier_programme
```

Lis ensuite [`premier_programme.c`](./premier_programme.c) (tout est commenté), puis
**modifie le texte** et **recompile** pour voir le changement.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
