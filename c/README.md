# 🇨 Apprendre le C — pour grands débutants

Le **C** est l'un des langages les plus importants de l'histoire : Linux, Windows, les
bases de données, et même l'interpréteur Python… sont en grande partie écrits en C. C'est
un langage **« bas niveau »**, c'est-à-dire **proche de la machine** : il te donne beaucoup
de contrôle (et donc beaucoup de responsabilités).

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, compile, lance, modifie.

---

## 🆚 Différence clé avec Python : il faut COMPILER

C'est LA grande nouveauté si tu viens de Python.

- **Python** est *interprété* : tu écris `script.py` et tu le lances directement.
- **C** est *compilé* : tu écris un fichier `.c`, puis un programme appelé **compilateur**
  (`gcc`) le **traduit en langage machine** dans un fichier **exécutable**. C'est seulement
  cet exécutable que l'ordinateur lance.

```
   programme.c   ──[ gcc ]──►   programme (exécutable)   ──►   ça tourne
   (ton code)     compilation    (langage machine)            exécution
```

> Le module `00_demarrer` détaille ce cycle et comment installer le compilateur.

Autres différences notables avec Python :
| | Python | C |
|--|--------|---|
| Types | dynamiques (`x = 5`) | **statiques** : on déclare le type (`int x = 5;`) |
| Fin d'instruction | retour à la ligne | un **point-virgule `;`** |
| Blocs | indentation | des **accolades `{ }`** |
| Mémoire | gérée automatiquement | **souvent manuelle** (pointeurs — plus tard) |

---

## 📚 Le parcours (fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Compiler/exécuter, structure d'un programme C, `printf` |
| 1 | [`01_les_bases`](./01_les_bases/) | Types, variables, `printf`/`scanf`, conditions, boucles, fonctions |
| 2 | [`02_tableaux_chaines`](./02_tableaux_chaines/) | Tableaux (indices, parcours, somme/moyenne), chaînes (`'\0'`, `<string.h>`) |
| 3 | [`03_pointeurs_memoire`](./03_pointeurs_memoire/) | Pointeurs (`&`, `*`, `NULL`), modifier via une fonction, mémoire dynamique (`malloc`/`free`) |
| 4 | [`04_structures`](./04_structures/) | Structures (`struct`, `typedef`), champ `.` et flèche `->`, tableaux de structures |
| 5 | [`05_fichiers`](./05_fichiers/) | Fichiers : `fopen` (modes `"w"`/`"a"`/`"r"`), vérifier `NULL`, écrire (`fprintf`/`fputs`), lire (`fgets`), `fclose` |
| 6 | [`06_preprocesseur_modules`](./06_preprocesseur_modules/) | Préprocesseur (`#define`, `#include` `<>` vs `""`), séparer en `.h`/`.c`, garde d'inclusion, compiler plusieurs fichiers ensemble |
| 7 | [`07_debugger`](./07_debugger/) | Trouver/corriger les bugs : compiler avec `-g`/`-Wall`, erreurs fréquentes (segfault, tableau hors limites, fuite mémoire…), l'essentiel de `gdb` (`run`, `bt`, `break`, `print`…) et `valgrind` |

> 🎯 **Et après les fondations ?** Le dossier [`projets/`](./projets/) rassemble des
> **mini-projets « capstone »** qui combinent plusieurs modules (tableaux + structures +
> fichiers) pour construire de vrais petits outils. À faire une fois les bases acquises.

> 📎 **Ressources** (à garder sous la main) : l'[`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md)
> (cheat-sheet d'une page) et le [`GLOSSAIRE.md`](./GLOSSAIRE.md) (les mots du C expliqués).

---

## ⚙️ Pré-requis : un compilateur

Tu as besoin de **`gcc`** (ou `clang`). Vérifie s'il est déjà là :

```bash
gcc --version
```

Sinon, voir les instructions d'installation dans [`00_demarrer`](./00_demarrer/).

## ▶️ Compiler et lancer un programme

```bash
# 1. Compiler le fichier source en un exécutable nommé "programme"
gcc c/00_demarrer/premier_programme.c -o programme

# 2. Lancer l'exécutable créé
./programme
```

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).
