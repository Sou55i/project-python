# 🧭 Écrire un script de zéro — la méthode pour RAISONNER

> Savoir écrire `if` ou `for` ne suffit pas à écrire un script : devant une page blanche, le
> débutant bute souvent sur *« par où commencer ? quelle fonction utiliser ? quels
> arguments ? »*.
>
> C'est **le** vrai blocage : pas la syntaxe, mais **le raisonnement**. Personne ne « connaît »
> par cœur la bonne fonction — on la **trouve** avec une méthode. La voici.

---

## 1. Pourquoi tu bloques (et pourquoi ce n'est pas ta faute)

Quand tu lis un script fini, tout semble « évident » et tu crois que l'auteur a tout su
d'avance. **Faux.** Il a suivi un cheminement : il a découpé le problème, **cherché** les
fonctions, testé, corrigé. Le code propre est le **résultat**, pas le point de départ.

> 🧠 L'erreur classique : vouloir écrire la bonne ligne **du premier coup**. À la place :
> écris une version **bête mais qui marche**, puis améliore.

---

## 2. La méthode en 5 étapes

Avant de taper du code, réponds à ces questions **en français** :

1. **OBJECTIF** — En une phrase, que doit faire le script ? *(« compter les fichiers d'un dossier »)*
2. **ENTRÉES → SORTIES** — Qu'est-ce qui ENTRE ? Qu'est-ce qui SORT ?
   *(entrée : un chemin de dossier ; sortie : un nombre affiché)*
3. **ÉTAPES** — Décris la recette **à voix haute**, comme à un humain :
   *« ouvrir le dossier → regarder chaque élément → garder ceux qui sont des fichiers →
   les compter → afficher le total »*.
4. **OUTILS** — Pour chaque étape, **quelle fonction/quel module** ? (c'est l'étape §3 : la
   *recherche*.)
5. **CODE** — Traduis chaque étape en une ou deux lignes. Teste. Corrige.

> ✍️ Astuce : écris d'abord les étapes en **commentaires**, puis remplis le code **sous**
> chaque commentaire. Le plan devient le squelette du script.

```python
# 1. récupérer le dossier à examiner
# 2. lister son contenu
# 3. ne garder que les fichiers (pas les sous-dossiers)
# 4. compter
# 5. afficher
```

---

## 3. « Comment trouver la BONNE fonction ? » (la compétence-clé)

Tu ne devines pas `pathlib.Path.iterdir()` par magie. Tu le **trouves**. Quatre techniques :

### a) La carte mentale de la bibliothèque standard
Associe un **domaine** à un **module**. Mémorise cette petite table, elle couvre 90 % des cas :

| Ton besoin | Module à regarder |
|------------|-------------------|
| fichiers & dossiers, chemins | `pathlib` (moderne) ou `os` |
| lire/écrire du JSON | `json` |
| CSV | `csv` |
| base de données SQL simple | `sqlite3` |
| dates & heures | `datetime` |
| hasard | `random` |
| arguments en ligne de commande | `argparse` |
| requêtes web | `requests` (externe) ou `urllib` |
| exécuter une commande système | `subprocess` |

### b) Chercher sur le web — **la bonne formulation**
Tape ton besoin **en anglais, par l'intention** :
> `python count files in directory` · `python parse json file` · `python insert into sqlite`

Vise la **doc officielle** (`docs.python.org`) et les réponses très votées.

### c) Explorer dans le terminal interactif (`python3` puis Entrée)
C'est ton **labo**. Tu testes une idée en 5 secondes :

```python
>>> from pathlib import Path
>>> dir(Path)            # liste TOUT ce qu'un Path sait faire (cherche "iter", "is_", "glob")
>>> help(Path.iterdir)   # explique iterdir, avec un exemple
>>> list(Path(".").iterdir())   # ESSAIE pour de vrai et regarde ce que ça renvoie
```

> 🔑 `dir(objet)` = « **qu'est-ce que tu sais faire ?** » · `help(truc)` = « **explique-moi** ».
> Ce sont tes deux meilleurs amis pour découvrir une bibliothèque **sans quitter Python**.

### d) Lire le **type** de ce que tu obtiens
Si tu ne sais pas quoi faire d'une valeur, demande son type et regarde ses méthodes :

```python
>>> x = Path(".").iterdir()
>>> type(x)        # <class 'generator'>  → ça se parcourt avec une boucle for / list()
```

---

## 4. Exemple complet n°1 — compter les fichiers d'un dossier

Suivons la méthode, **en montrant les hésitations** (c'est ça, programmer).

**1. Objectif** : compter les fichiers d'un dossier.
**2. Entrées → sorties** : entrée = un chemin (texte) ; sortie = un entier affiché.
**3. Étapes** : lister le contenu → garder les fichiers → compter → afficher.
**4. Outils** : « fichiers & dossiers » → table §3a → **`pathlib`**. Je cherche comment lister :
   `dir(Path)` me montre `iterdir` (« iter-dir » = parcourir le dossier) et `glob`. Je teste
   `list(Path('.').iterdir())` : ça renvoie des `Path`, dossiers **et** fichiers mélangés. Il
   me faut distinguer → `dir(Path)` montre `is_file()`. 👍

**5. Code (version 1, naïve mais qui marche) :**

```python
from pathlib import Path

dossier = Path(".")            # "." = le dossier courant
total = 0
for element in dossier.iterdir():   # chaque fichier OU sous-dossier
    if element.is_file():           # on ne garde que les fichiers
        total += 1
print(f"{total} fichiers")
```

**Et les « arguments » ?** Pour l'instant le dossier est codé en dur (`"."`). Pour le rendre
**réutilisable**, on le reçoit en **argument de ligne de commande** — c'est exactement ta
question. Le module dédié est **`argparse`** (table §3a) :

```python
import argparse
from pathlib import Path

# On DÉCLARE l'argument attendu (ici un chemin de dossier).
parseur = argparse.ArgumentParser(description="Compter les fichiers d'un dossier")
parseur.add_argument("dossier", help="le dossier à examiner")
args = parseur.parse_args()         # lit ce que l'utilisateur a tapé

total = sum(1 for e in Path(args.dossier).iterdir() if e.is_file())
print(f"{total} fichiers dans {args.dossier}")
```

> 💡 **Comment j'ai « su » qu'il fallait `argparse` et `add_argument` ?** Je suis parti du
> **besoin** (« je veux passer le dossier au lancement, ex. `python compter.py /tmp` »), j'ai
> cherché *« python command line argument »*, et la doc d'`argparse` montre exactement
> `add_argument`. **On part toujours du besoin, jamais de la fonction.**

➡️ Version **finale, commentée pas à pas et exécutable** :
[`15_construire_un_script/compter_fichiers.py`](./15_construire_un_script/compter_fichiers.py).

---

## 5. Exemple complet n°2 — convertir du JSON en SQL

**1. Objectif** : lire un fichier JSON (une liste d'objets) et produire des instructions
`INSERT INTO` SQL.
**2. Entrées → sorties** : entrée = un fichier `.json` ; sortie = du texte SQL (ou une vraie
base SQLite).
**3. Étapes** : lire le JSON → obtenir une liste de dictionnaires → pour chaque dict,
fabriquer un `INSERT INTO table (colonnes) VALUES (valeurs)` → écrire le résultat.
**4. Outils** : « lire du JSON » → `json` ; « base SQL simple » → `sqlite3` (inclus, aucune
install). Je cherche *« python read json file »* → `json.load(fichier)`. Et *« python sqlite
insert »* → `cursor.execute("INSERT ...", valeurs)`.

**5. Le raisonnement sur les données** (le vrai cœur) :

```python
import json

# json.load transforme le fichier en STRUCTURE Python.
# Une liste d'objets JSON  →  une liste de dictionnaires.
with open("gens.json", encoding="utf-8") as f:
    lignes = json.load(f)     # ex: [{"nom": "Alice", "age": 30}, {"nom": "Bob", "age": 25}]

# Pour UN dictionnaire, les colonnes = ses clés, les valeurs = ses valeurs.
premier = lignes[0]
colonnes = list(premier.keys())     # ["nom", "age"]
```

Maintenant, **comment construire le `INSERT` sans me tromper sur les virgules ?** C'est là
que `', '.join(...)` (vu dans [COMPRENDRE_LE_CODE.md](./COMPRENDRE_LE_CODE.md)) devient utile :

```python
noms_colonnes = ", ".join(colonnes)          # "nom, age"
placeholders  = ", ".join("?" for _ in colonnes)  # "?, ?"  (un ? par colonne)
sql = f"INSERT INTO gens ({noms_colonnes}) VALUES ({placeholders});"
# → "INSERT INTO gens (nom, age) VALUES (?, ?);"
```

> 🔐 **Pourquoi des `?` et pas les valeurs directement ?** Ce sont des *placeholders* : on
> laisse `sqlite3` insérer les valeurs **à notre place**. Ça évite l'**injection SQL** (voir
> `pentest/`) et les soucis de guillemets. On lui passe les valeurs séparément :
> `cursor.execute(sql, tuple(dico.values()))`.

➡️ Version **finale, commentée pas à pas et exécutable** (génère le SQL **et** remplit une
vraie base SQLite) : [`15_construire_un_script/json_vers_sql.py`](./15_construire_un_script/json_vers_sql.py).

---

## 6. Récap : la boucle de l'écriture

```
   IDÉE
    │  (1) une phrase d'objectif
    ▼
   ENTRÉES → SORTIES        (2) ce qui entre, ce qui sort
    │
    ▼
   ÉTAPES en français       (3) la recette, en commentaires
    │
    ▼
   CHERCHER les outils      (4) table mentale · web · dir()/help() · REPL
    │
    ▼
   CODE bête qui MARCHE  ───►  AMÉLIORER (arguments, robustesse, fonctions)
            ▲                         │
            └─────────  tester, corriger  ◄──┘
```

> 🧠 **À retenir** : on part **toujours** du *besoin* exprimé en français, on le découpe, puis
> on **cherche** l'outil pour chaque étape. La maîtrise des fonctions vient en **cherchant
> souvent**, pas en mémorisant. Plus tu écris de petits scripts, plus ta « carte mentale »
> grandit.

➡️ Entraîne-toi avec les deux scripts commentés du module
[`15_construire_un_script`](./15_construire_un_script/), puis invente tes propres mini-outils.
