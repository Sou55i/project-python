# 🐍 Apprendre Python — le cours de référence (pour grands débutants)

[![CI](https://github.com/Sou55i/apprendre-programmation/actions/workflows/ci.yml/badge.svg)](https://github.com/Sou55i/apprendre-programmation/actions/workflows/ci.yml)

Bienvenue ! Ce dépôt est une **référence d'apprentissage de Python en français**, pensée pour
les **grands débutants**. On part de zéro et on va jusqu'aux sujets avancés (POO, asyncio,
tests) puis au **Python appliqué** (automatisation, données, web) et même à un volet
**sécurité** éducatif.

> 💡 **On explique d'abord, on code ensuite.**
> Chaque module commence par un `README.md` qui pose la théorie avec des mots simples et des
> analogies. Le code qui suit ne fait qu'*illustrer* la théorie. Lis, lance, modifie.
> Les scripts sont **commentés presque ligne par ligne** et les plus complexes commencent par
> un bloc **« 🗺️ CHEMINEMENT DU SCRIPT »** qui résume leurs étapes.

> 📁 **Tout le cours est dans le dossier [`python/`](./python/).** Cette page en est le sommaire.

---

## 🆚 Pourquoi Python ?

Python ressemble à du **pseudo-code anglais** : c'est le langage idéal pour apprendre à
programmer **sans se battre avec la syntaxe**.

- **Interprété** : pas de compilation, tu tapes `python3 script.py` et ça tourne.
- **Typage dynamique** : pas besoin de déclarer le type des variables.
- **Indentation** : ce sont les espaces qui structurent le code (pas les accolades).
- **« Piles incluses »** : une énorme bibliothèque standard + un écosystème immense.

---

## 🗺️ Le parcours

Un **seul** parcours progressif, en deux temps : le **cœur du langage**, puis le **Python
appliqué** pour mettre les concepts en pratique.

### Le cœur du langage
| # | Module | Ce que tu apprends |
|---|--------|--------------------|
| 0 | [`00_demarrer`](./python/00_demarrer/) | Installer Python, environnements virtuels, premier script |
| 1 | [`01_les_bases`](./python/01_les_bases/) | Variables, types, `if`/`for`/`while` |
| 2 | [`02_collections`](./python/02_collections/) | Listes, dictionnaires, tuples, sets |
| 3 | [`03_fonctions_modules`](./python/03_fonctions_modules/) | Fonctions, découper et importer son code |
| 4 | [`04_exceptions_fichiers`](./python/04_exceptions_fichiers/) | Lire/écrire des fichiers, gérer les erreurs |
| 5 | [`05_poo`](./python/05_poo/) | Programmation orientée objet (classes) |
| 6 | [`06_iterateurs_generateurs`](./python/06_iterateurs_generateurs/) | Itérateurs, générateurs, efficacité |
| 7 | [`07_debugger`](./python/07_debugger/) | Trouver et corriger ses bugs |
| 8 | [`08_asyncio`](./python/08_asyncio/) | Faire plusieurs choses « en même temps » |
| 9 | [`09_tests_qualite`](./python/09_tests_qualite/) | Tests, code propre et vérifié |

### Python appliqué (automatisation)
| # | Module | Ce que tu apprends |
|---|--------|--------------------|
| 10 | [`10_fichiers_dossiers`](./python/10_fichiers_dossiers/) | Ranger des fichiers, CSV / JSON / Excel |
| 11 | [`11_web_apis`](./python/11_web_apis/) | Télécharger, appeler des APIs, scraping |
| 12 | [`12_taches_scripts`](./python/12_taches_scripts/) | Scripts réutilisables (`argparse`) & planification |
| 13 | [`13_donnees_rapports`](./python/13_donnees_rapports/) | Manipuler des données et générer des rapports (`pandas`) |
| 14 | [`14_bibliotheques`](./python/14_bibliotheques/) | `pip`, environnements virtuels, `requirements.txt` |

### Pratiquer & aller plus loin
- 🛠️ **[projets/](./python/projets/)** — mini-projets concrets (ranger des fichiers, carnet de contacts, suivi météo).
- 🔐 **[pentest/](./python/pentest/)** — sécurité **éducative** (scanners réseau + démos offensives, usage lab uniquement).
- 🧩 **[modele_script.py](./python/modele_script.py)** — un squelette de script prêt à copier.

---

## 🚀 Démarrer

```bash
git clone <url-de-ce-depot>
cd apprendre-programmation
pip install -r python/requirements.txt        # pour les modules web/données
python3 python/00_demarrer/hello.py
```

➡️ Puis suis les modules dans l'ordre, en commençant par [`python/00_demarrer`](./python/00_demarrer/).

---

## 📎 Ressources

- **[python/AIDE_MEMOIRE.md](./python/AIDE_MEMOIRE.md)** — la syntaxe Python résumée sur une page.
- **[python/GLOSSAIRE.md](./python/GLOSSAIRE.md)** — les termes techniques expliqués simplement.
- **[python/ANATOMIE_D_UN_SCRIPT.md](./python/ANATOMIE_D_UN_SCRIPT.md)** — dans quel ordre écrire un script.
- **[SECURITE.md](./SECURITE.md)** — index des démos sécurité (éducatives). ⚠️ Usage autorisé uniquement.

---

## 🌍 Autres langages (plus tard)

Ce dépôt contient aussi des parcours pour **9 autres langages** (Bash, PowerShell, C, C++, Go,
Assembleur, Rust, JS/TS, Java), construits sur la même pédagogie. Ils sont **en retrait** pour
l'instant — la priorité est faite à Python.

👉 Si ça t'intéresse : **[SOMMAIRE.md](./SOMMAIRE.md)** (tous les langages) et
**[COMPARATIF.md](./COMPARATIF.md)** (le même code d'un langage à l'autre).

---

## 📄 Licence

Voir le fichier [LICENSE](./LICENSE). Contenu à but **éducatif**.
