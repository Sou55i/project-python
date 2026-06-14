# 🐚 Apprendre le Bash — pour grands débutants

Le **Bash** est le langage du **terminal**. C'est lui qui interprète les commandes que tu
tapes dans une console Linux ou macOS. Mais c'est aussi un vrai **langage de script** :
on peut enchaîner des commandes dans un fichier pour **automatiser** des tâches (sauvegardes,
installation, traitement de fichiers en masse…).

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par ligne**.

---

## 🆚 En quoi c'est différent des autres langages ?

- Comme **Python**, Bash est **interprété** : pas de compilation, on lance le script
  directement.
- Sa **grande force** : il **pilote les autres programmes**. Une ligne de Bash peut lancer
  `git`, `ls`, `grep`, `python3`… et combiner leurs résultats. C'est le **chef d'orchestre**
  de ta machine.
- Sa syntaxe a des **pièges** propres (les espaces comptent énormément, les guillemets sont
  cruciaux). On va les démonter un par un.

| | Python | Bash |
|--|--------|------|
| Exécution | interprété | interprété |
| Variable | `x = 5` | `x=5` (⚠️ **pas d'espaces** autour du `=`) |
| Utiliser une variable | `x` | `"$x"` (avec le `$`, et entre guillemets) |
| Afficher | `print("salut")` | `echo "salut"` |
| Point fort | calcul, données, web | **automatiser le terminal** et enchaîner des outils |

---

## 📚 Le parcours

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Le shell, le shebang, lancer un script, `echo`, les commentaires |
| 1 | [`01_les_bases`](./01_les_bases/) | Variables & guillemets, `read`, conditions `[[ ]]`, boucles, fonctions, calcul |
| 2 | [`02_fichiers`](./02_fichiers/) | Redirections (`>`, `>>`, `<`), pipes `|`, lire un fichier (`while read`), tests `-f`/`-d` |
| 3 | [`03_texte`](./03_texte/) | Le super-pouvoir du shell : `grep`, `cut`, `sort`, `uniq`, `wc`, `sed`, `awk` |
| 4 | [`04_arguments`](./04_arguments/) | Arguments & options : `$0`/`$1`/`$@`/`$#`, `shift`, `getopts` |
| 5 | [`05_tableaux`](./05_tableaux/) | Tableaux indexés et associatifs (dictionnaires) |
| 6 | [`06_robustesse`](./06_robustesse/) | `set -euo pipefail`, code de retour `$?`, `&&`/`||`, `trap` (nettoyage) |
| 7 | [`07_debugger`](./07_debugger/) | Déboguer : `set -x` / `bash -x`, `shellcheck`, erreurs fréquentes |

### 🚀 Modules avancés

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 8 | [`08_fonctions_avancees`](./08_fonctions_avancees/) | Variables `local`, `return`/`$?`, bibliothèques réutilisables avec `source` |
| 9 | [`09_parallelisme`](./09_parallelisme/) | Lancer des tâches en parallèle : `&`, `wait`, `xargs -P` |

Puis, pour mettre tout en pratique : le **[projet capstone](./projets/)** (ranger
automatiquement des fichiers par extension), qui combine plusieurs modules.

> 📎 **Ressources** (à garder sous la main) : l'[`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md)
> (cheat-sheet d'une page), le [`GLOSSAIRE.md`](./GLOSSAIRE.md) (les mots du Bash) et le guide
> [`ANATOMIE_D_UN_SCRIPT.md`](./ANATOMIE_D_UN_SCRIPT.md) (dans quel ordre écrire un script).

---

## ▶️ Lancer un script Bash

Il y a **deux façons** de lancer un script `mon_script.sh` :

```bash
# 1. En le passant à bash (le plus simple) :
bash bash/00_demarrer/premier_script.sh

# 2. En le rendant "exécutable" une fois, puis en l'appelant directement :
chmod +x bash/00_demarrer/premier_script.sh   # donne le droit d'exécution
./bash/00_demarrer/premier_script.sh
```

> 💡 Les scripts Bash se terminent par convention par **`.sh`**, et commencent par une ligne
> spéciale appelée **shebang** (`#!/usr/bin/env bash`) qui dit « exécute-moi avec bash ».
> Tout cela est expliqué dans le module [`00_demarrer`](./00_demarrer/).

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).
