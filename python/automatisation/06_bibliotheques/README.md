# Module 06 — Les bibliothèques : laquelle ajouter, et quand ?

Tu as déjà écrit `import requests` ou `import pandas`. Mais d'où viennent ces outils ?
Comment savoir **si** tu as besoin d'une bibliothèque, **laquelle** choisir, et **comment**
l'installer proprement ? C'est tout l'objet de ce module (100 % théorique).

> Fichier du module : `explorer_modules.py` (un petit script qui montre comment vérifier
> ce qui est déjà installé).

---

## 1. Vocabulaire : module, bibliothèque, paquet

Ces mots sont souvent mélangés. Voici l'idée simple :

- **Module** : un **fichier** `.py` contenant des fonctions réutilisables. Exemple : le
  module `json`.
- **Bibliothèque** (en anglais *library*) : un **ensemble de modules** qui rendent un service.
  Exemple : `requests` pour le web. On dit aussi « **paquet** » (*package*).

> 🧰 Image mentale : une bibliothèque est une **caisse à outils** écrite par d'autres
> personnes. Plutôt que de réinventer la roue, tu ouvres la caisse et tu prends l'outil.
> `import` = « ouvrir la caisse à outils ».

---

## 2. Les deux grandes familles de bibliothèques

C'est **la distinction la plus importante** du module.

### a) La bibliothèque standard (*standard library*, ou « stdlib »)

Ce sont les outils **livrés AVEC Python** : déjà sur ta machine, **rien à installer**.
Tu fais juste `import`. Exemples très courants :

| Module stdlib | Sert à |
|---------------|--------|
| `os` / `pathlib` | fichiers et dossiers |
| `json` | lire/écrire du JSON |
| `csv` | lire/écrire des CSV |
| `datetime` | dates et heures |
| `random` | tirages aléatoires |
| `math` | calculs mathématiques |
| `argparse` | options en ligne de commande |
| `logging` | journaux (logs) |
| `re` | recherche de motifs dans du texte (regex) |
| `urllib` | requêtes web basiques |

> ✅ **Réflexe n°1 : avant d'installer quoi que ce soit, demande-toi si la stdlib le fait
> déjà.** Très souvent, oui. La liste complète est sur
> [docs.python.org/fr/3/library](https://docs.python.org/fr/3/library/).

### b) Les bibliothèques tierces (*third-party*)

Écrites par la communauté, **pas livrées avec Python** : il faut les **installer** avec
`pip` (voir §4). On les héberge sur **PyPI** (*Python Package Index*),
le « magasin » officiel : [pypi.org](https://pypi.org).

| Bibliothèque tierce | Remplace / améliore | Pourquoi |
|---------------------|---------------------|----------|
| `requests` | `urllib` (stdlib) | bien plus simple pour le web |
| `pandas` | `csv` (stdlib) | calculs sur de gros tableaux |
| `beautifulsoup4` | (rien en stdlib) | extraire des infos d'une page HTML |
| `openpyxl` | (rien en stdlib) | lire/écrire des fichiers Excel `.xlsx` |
| `schedule` | (rien en stdlib) | planifier des tâches facilement |

---

## 3. Comment décider si tu as besoin d'une bibliothèque

Pose-toi ces questions **dans l'ordre** :

```
1. Est-ce que je peux le faire avec ce que je connais déjà (boucles, fonctions) ?
        │ oui → fais-le toi-même, pas de dépendance inutile.
        │ non ↓
2. Est-ce que la bibliothèque STANDARD le fait déjà ? (cherche dans la doc)
        │ oui → import, rien à installer. 🎉
        │ non ↓
3. Existe-t-il une bibliothèque TIERCE reconnue pour ça ?
        │ oui → installe-la avec pip (voir §4 et §5 pour bien la choisir).
        │ non → c'est peut-être à toi de l'écrire.
```

> ⚠️ **Chaque bibliothèque ajoutée est une dépendance** : du code que tu ne contrôles pas,
> qui peut avoir des bugs, devenir obsolète, ou alourdir ton projet. La règle d'or :
> **« le moins de dépendances possible, mais pas moins que nécessaire. »**

---

## 4. Installer une bibliothèque avec `pip`

`pip` est le **gestionnaire de paquets** de Python : c'est lui qui télécharge les
bibliothèques depuis PyPI et les installe.

```bash
pip install requests              # installe la dernière version
pip install "pandas>=2.0"         # installe une version minimale
pip show requests                 # montre les infos d'un paquet installé
pip list                          # liste tout ce qui est installé
pip uninstall requests            # désinstalle
```

> 💡 Sur certains systèmes, la commande est `pip3` au lieu de `pip`.

### L'environnement virtuel (à connaître)

Pour éviter de mélanger les bibliothèques de tous tes projets, on crée un
**environnement virtuel** : une bulle isolée par projet.

```bash
python3 -m venv .venv          # crée la bulle dans le dossier .venv
source .venv/bin/activate      # l'active (Mac/Linux)
.venv\Scripts\activate         # l'active (Windows)
pip install requests           # s'installe SEULEMENT dans cette bulle
```

C'est la **bonne pratique** dès qu'un projet grandit.

---

## 5. Bien choisir une bibliothèque tierce

Sur PyPI, il y a parfois 10 bibliothèques pour le même besoin. Comment trier ? Regarde :

- **La popularité** : nombre d'étoiles sur GitHub, nombre de téléchargements. Une lib très
  utilisée est mieux testée et plus facile à dépanner (réponses sur Internet).
- **La maintenance** : la dernière mise à jour date-t-elle de cette année ? Un projet
  abandonné est risqué.
- **La documentation** : existe-t-elle, est-elle claire, avec des exemples ?
- **La réputation** : est-ce la bibliothèque « standard de fait » que tout le monde
  recommande (ex : `requests` pour le web) ?

> 🔎 En pratique : tape ton besoin sur un moteur de recherche (« python lire excel ») et
> regarde quelle bibliothèque revient systématiquement. C'est presque toujours la bonne.

---

## 6. Noter ses dépendances : `requirements.txt`

Quand ton script a besoin de bibliothèques tierces, **tu dois le dire** à quiconque
réutilisera ton projet (un collègue, ou toi sur un autre PC). On liste les dépendances
dans un fichier `requirements.txt` :

```
requests>=2.31.0
pandas>=2.0.0
```

L'autre personne tape alors une seule commande pour tout installer :

```bash
pip install -r python/requirements.txt
```

> 🧊 **« Figer » les versions** : `requests==2.31.0` (avec `==`) installe EXACTEMENT cette
> version. Utile pour garantir que ton script marchera pareil dans 2 ans. `>=` autorise les
> versions plus récentes. Pour générer la liste de ce qui est installé :
> `pip freeze > requirements.txt`.

---

## 7. Le piège classique : `ModuleNotFoundError`

Le message d'erreur que **tout débutant rencontre** :

```
ModuleNotFoundError: No module named 'requests'
```

Traduction : *« tu as fait `import requests`, mais cette bibliothèque n'est pas installée. »*
La solution est presque toujours :

```bash
pip install requests
```

Si tu utilises un environnement virtuel, vérifie qu'il est **activé** avant d'installer.

---

## ▶️ À toi de jouer

```bash
python3 python/automatisation/06_bibliotheques/explorer_modules.py
```

Ce script montre comment vérifier, depuis Python, ce qui est déjà disponible et quelle
version est installée.

🎉 **Tu sais maintenant raisonner sur les dépendances** — une compétence que beaucoup de
développeurs mettent du temps à acquérir.
