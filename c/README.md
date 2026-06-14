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

> 🚧 D'autres modules (tableaux & chaînes, pointeurs & mémoire, fichiers, projets…)
> viendront ensuite, dans le même style.

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
