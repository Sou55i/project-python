# 🐍 Apprendre Python — de zéro à l'automatisation

Bienvenue ! Ce dépôt est une **référence d'apprentissage de Python en français**, pensée
pour les **grands débutants**. L'objectif : comprendre le langage, puis l'utiliser pour
**automatiser des tâches du quotidien** (ranger des fichiers, télécharger des données,
remplir des tableaux, envoyer des rapports…).

> 💡 La philosophie du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module commence par un fichier `README.md` qui pose la théorie avec des mots
> simples et des analogies. Le code Python qui suit n'est là que pour *illustrer* ce que
> tu viens de lire. Lis la théorie, puis lance le code, puis modifie-le.

---

## 🗺️ Les deux parcours

| Parcours | Dossier | Pour qui ? |
|----------|---------|------------|
| 🤖 **Automatisation** (débutant) | [`automatisation/`](./automatisation/) | Tu débutes en programmation et tu veux automatiser des tâches concrètes. **Commence ici.** |
| 🔐 **Pentest / Sécurité** (avancé) | [`pentest/`](./pentest/) | Tu connais déjà les bases et tu t'intéresses à la sécurité informatique. |

---

## 🚀 Démarrer en 3 étapes

### 1. Installer Python

- **Windows** : télécharge Python sur [python.org/downloads](https://www.python.org/downloads/).
  ⚠️ Pendant l'installation, **coche la case « Add Python to PATH »**.
- **macOS** : Python est souvent déjà là, mais installe la dernière version depuis
  [python.org](https://www.python.org/downloads/) ou via `brew install python`.
- **Linux** : Python est généralement préinstallé (`python3 --version` pour vérifier).

Vérifie que tout marche en ouvrant un **terminal** et en tapant :

```bash
python3 --version
```

Tu devrais voir quelque chose comme `Python 3.12.1`. Si oui, bravo, tu es prêt !

### 2. Récupérer ce dépôt et installer les dépendances

```bash
git clone <url-de-ce-depot>
cd project-python
pip install -r requirements.txt
```

> Les **dépendances** sont des « boîtes à outils » écrites par d'autres que l'on réutilise
> (par exemple `pandas` pour les tableaux). Le fichier `requirements.txt` en contient la liste.

### 3. Lancer ton premier programme

```bash
python3 automatisation/00_demarrer/premier_script.py
```

---

> 🧭 Tu te demandes **dans quel ordre** écrire ton code (imports, fonctions, etc.) ?
> Lis le guide [automatisation/ANATOMIE_D_UN_SCRIPT.md](./automatisation/ANATOMIE_D_UN_SCRIPT.md).

## 📚 Le parcours Automatisation en un coup d'œil

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | `00_demarrer` | C'est quoi un programme, un terminal, comment lancer un script |
| 1 | `01_les_bases` | Variables, types, conditions, boucles, fonctions |
| 2 | `02_fichiers_dossiers` | Lire/écrire des fichiers, ranger des dossiers, CSV, JSON, Excel |
| 3 | `03_web_apis` | Télécharger une page, appeler une API, extraire des infos (scraping) |
| 4 | `04_taches_scripts` | Créer des scripts réutilisables et les planifier (cron / Windows) |
| 5 | `05_donnees_rapports` | Nettoyer des données et générer des rapports automatiques (pandas) |
| 6 | `06_bibliotheques` | Savoir quelle bibliothèque ajouter, quand, et comment (`pip`) |

👉 **Suis les modules dans l'ordre.** Chaque module suppose que tu as compris le précédent.

---

## ❓ Comment étudier un module

1. Ouvre le `README.md` du module et **lis la théorie** tranquillement.
2. Ouvre le fichier `.py`, **lis les commentaires** (les lignes qui commencent par `#`).
3. **Lance le script** et observe ce qu'il affiche.
4. **Modifie une valeur** et relance : c'est en cassant les choses qu'on apprend. 🛠️

---

## 📄 Licence

Voir le fichier [LICENSE](./LICENSE). Contenu à but **éducatif**.
