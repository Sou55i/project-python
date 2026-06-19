# 🏗️ Projets Python — mettre tout en pratique

> 🎯 **À quoi sert ce dossier ?** Les modules t'apprennent les briques une par une. Ici, on
> **assemble** ces briques dans de **vrais petits programmes utiles**. Chaque projet est
> **commenté pas à pas** et conçu pour **tourner sans risque** : ceux qui touchent à des
> fichiers fabriquent eux-mêmes un dossier de démo, ils ne toucheront jamais à tes vrais
> fichiers tant que tu ne le décides pas.

> 💡 **Comment travailler un projet** (la bonne méthode) :
> 1. **Lance-le** d'abord pour voir ce qu'il produit.
> 2. **Lis-le de bas en haut** : commence par le bloc `if __name__ == "__main__":`, qui montre
>    l'enchaînement général, puis remonte vers chaque fonction (méthode du guide
>    [`../COMPRENDRE_LE_CODE.md`](../COMPRENDRE_LE_CODE.md)).
> 3. **Modifie une chose**, relance, observe. C'est en bidouillant qu'on apprend.
> 4. **Tente une extension** (idées en bas de chaque fiche).

---

## 🧵 Le fil rouge (à faire en premier si tu débutes)

Avant les projets « finis » ci-dessous, il y a le **[fil rouge](./fil_rouge/)** : un **même**
gestionnaire de dépenses construit en **5 étapes**, de 3 variables jusqu'à une vraie appli. C'est
la meilleure façon de comprendre **comment un programme grandit** — une notion à la fois.

👉 **[Ouvrir le fil rouge](./fil_rouge/)**

---

## 📂 Les projets disponibles

### 1. 📇 Carnet de contacts — [`carnet_contacts.py`](./carnet_contacts.py)

Un vrai outil en ligne de commande pour **ajouter / lister / chercher / supprimer** des
contacts, avec **sauvegarde** dans un fichier JSON (tes contacts sont toujours là au prochain
lancement).

- **Ce que tu y apprends** : les dictionnaires (un contact = un dict), la persistance en JSON
  (`json.load`/`json.dump`), et surtout `argparse` avec des **sous-commandes** (comme `git commit`
  / `git push`).
- **Modules mobilisés** : 02 (collections), 04 (fichiers), 12 (argparse).
- **Lancer** :
  ```bash
  python3 python/projets/carnet_contacts.py ajouter --nom Alice --tel 0612345678
  python3 python/projets/carnet_contacts.py lister
  python3 python/projets/carnet_contacts.py chercher --nom alice
  python3 python/projets/carnet_contacts.py --help
  ```
- **Idées d'extension** : ajouter un champ « adresse » ; une commande `modifier` ; trier la
  liste par nom dans `lister`.

### 2. 🗂️ Ranger des fichiers par date — [`organiser_par_date.py`](./organiser_par_date.py)

Classe automatiquement les fichiers d'un dossier dans des sous-dossiers `AAAA-MM` selon leur
date de dernière modification. La corvée de tri manuel transformée en une commande.

- **Ce que tu y apprends** : `pathlib` (parcourir un dossier, déplacer un fichier), les dates
  (`datetime`, timestamps), et la prudence (le script travaille sur un dossier de démo qu'il crée).
- **Modules mobilisés** : 02 (collections), 10 (fichiers & dossiers).
- **Lancer** :
  ```bash
  python3 python/projets/organiser_par_date.py
  ```
- **Idées d'extension** : ranger par **extension** plutôt que par date ; afficher un résumé
  « combien de fichiers par dossier » à la fin.

### 3. 📊 Analyseur de logs — [`analyseur_logs.py`](./analyseur_logs.py)

Lit un fichier journal (`.log`) de milliers de lignes et en sort un **rapport** : combien
d'INFO / WARNING / ERROR, les **erreurs les plus fréquentes**, la période couverte. L'un des
scripts les plus utiles du monde réel.

- **Ce que tu y apprends** : lire un fichier ligne par ligne, **découper du texte** (`split`),
  **compter** efficacement avec `collections.Counter` et `.most_common()`, lire/écrire des dates
  (`strptime`/`strftime`). 100 % bibliothèque standard, **aucune dépendance**.
- **Modules mobilisés** : 01, 02, 04, 12 (le format de log).
- **Lancer** :
  ```bash
  python3 python/projets/analyseur_logs.py
  ```
- **Idées d'extension** : n'afficher que les lignes `ERROR` ; compter les erreurs **par heure** ;
  recevoir le chemin du `.log` en argument avec `argparse`.

### 4. 🔐 Générateur de mots de passe — [`generateur_mdp.py`](./generateur_mdp.py)

Fabrique des mots de passe aléatoires solides, configurables (longueur, chiffres, symboles,
nombre à générer).

- **Ce que tu y apprends** : construire un alphabet de caractères (`string`), `argparse` avec des
  **drapeaux** (`action="store_true"`), et **une vraie leçon de sécurité** : pourquoi on utilise
  `secrets` (hasard imprévisible) et **jamais `random`** pour un mot de passe.
- **Modules mobilisés** : 01/02 (texte & listes), 12 (argparse). Aucune dépendance.
- **Lancer** :
  ```bash
  python3 python/projets/generateur_mdp.py --longueur 24 --symboles
  python3 python/projets/generateur_mdp.py --longueur 12 --sans-chiffres --nombre 5
  ```
- **Idées d'extension** : garantir **au moins un** chiffre et un symbole ; estimer la « force »
  du mot de passe ; copier directement dans le presse-papier.

### 5. ✅ Liste de tâches (to-do) — [`todo.py`](./todo.py)

Une to-do list persistante en ligne de commande : ajouter, lister, **marquer comme faite**,
supprimer. Le grand frère du carnet de contacts, avec une notion d'**état**.

- **Ce que tu y apprends** : modéliser une tâche (`{"texte": ..., "fait": ...}`), la persistance
  JSON, les **sous-commandes** `argparse`, et la conversion **numéro humain (1, 2, 3) → index
  (0, 1, 2)** avec vérification des bornes.
- **Modules mobilisés** : 02 (collections), 04 (fichiers), 12 (argparse). Aucune dépendance.
- **Lancer** :
  ```bash
  python3 python/projets/todo.py ajouter --texte "Réviser Python"
  python3 python/projets/todo.py lister
  python3 python/projets/todo.py terminer --numero 1
  ```
- **Idées d'extension** : une commande `nettoyer` qui supprime les tâches faites ; des
  **priorités** ; n'afficher que les tâches non terminées.

### 6. 🌤️ Suivi météo → CSV — [`suivi_meteo.py`](./suivi_meteo.py)

Pour une liste de villes, interroge une **API météo gratuite** (Open-Meteo, sans inscription)
et enregistre un **rapport CSV**.

- **Ce que tu y apprends** : appeler une API web avec `requests`, gérer les erreurs réseau
  proprement (le script ne plante pas sans Internet), écrire un CSV avec `csv.DictWriter`.
- **Modules mobilisés** : 11 (web & APIs), 10 (CSV/JSON).
- **Prérequis** : une connexion Internet + `requests` (`pip install -r python/requirements.txt`).
- **Lancer** :
  ```bash
  python3 python/projets/suivi_meteo.py
  ```
- **Idées d'extension** : ajouter des villes ; ajouter une colonne « humidité » ; enregistrer en
  JSON en plus du CSV.

---

## 🚀 Et après ? Invente les tiens

La meilleure façon de progresser : prends **une corvée répétitive de ta vraie vie** et
automatise-la. Quelques idées de difficulté croissante :

| Projet | Concepts clés | Difficulté |
|--------|---------------|------------|
| Renommer en masse des photos (`IMG_001.jpg`, …) | `pathlib`, boucles, f-strings | ⭐ |
| Minuteur / chronomètre en terminal | `time`, boucles | ⭐ |
| Convertisseur d'unités (°C↔°F, km↔miles) | fonctions, `argparse` | ⭐ |
| Convertisseur de devises (via une API) | `requests`, JSON | ⭐⭐ |
| Quiz à choix multiples avec score | dictionnaires, `input`, boucles | ⭐⭐ |
| Scraper de prix d'une page web | `requests`, `beautifulsoup4` | ⭐⭐⭐ |

> 🧭 Coincé sur « par où commencer / quelle fonction utiliser » ? Relis
> [`../ECRIRE_UN_SCRIPT.md`](../ECRIRE_UN_SCRIPT.md) : la méthode pour passer d'une idée à un
> script qui marche.
