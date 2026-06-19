# 🐍 Apprendre le Python — pour grands débutants

Le **Python** est l'un des langages les plus populaires au monde. Pourquoi ? Parce qu'il est
**incroyablement lisible**, **polyvalent** et possède une **communauté immense**. Que tu
veuilles faire de l'automatisation, de l'intelligence artificielle, du développement web ou
de la cybersécurité (pentest), Python est l'outil de prédilection.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, lance, modifie.

---

## 🆚 Pourquoi Python ?

Si tu as déjà jeté un œil au C, au Go ou à l'Assembleur, Python va te sembler être du
**pseudo-code anglais** (du code qui ressemble à du langage naturel).

- **Interprété** : Pas besoin de compiler ton code. Tu tapes `python script.py` et ça se lance.
- **Typage dynamique** : Tu n'as pas besoin de dire que `x` est un entier. Python le comprend tout seul.
- **Indentation obligatoire** : C'est ce qui rend Python propre. Pas d'accolades `{}` partout, c'est l'alignement du texte qui définit les blocs de code.
- **Piles incluses** : Python vient avec énormément d'outils déjà prêts (gestion de fichiers, réseau, mathématiques...).

| | C / Go | Python |
|--|--------|--------|
| Complexité | Élevée (beaucoup de détails techniques) | **Faible** (proche de l'anglais) |
| Vitesse | Très rapide (proche du processeur) | **Modérée** (plus lent, mais plus rapide à écrire) |
| Gestion mémoire | Souvent manuelle ou semi-auto | **Automatique** (Garbage Collector) |
| Blocs de code | Accolades `{ }` | **Indentation** (espaces/tabulations) |

---

## 🗺️ Ta feuille de route

Un **seul** parcours, en deux temps : d'abord le **cœur du langage**, puis le **Python
appliqué** (automatisation) pour mettre les concepts en pratique.

### Le cœur du langage
1.  **[00_demarrer](./00_demarrer/)** : Installer Python et comprendre les environnements virtuels.
2.  **[01_les_bases](./01_les_bases/)** : Variables, types et structures de contrôle (`if`, `for`).
3.  **[02_collections](./02_collections/)** : Listes, Dictionnaires, Tuples et Sets.
4.  **[03_fonctions_modules](./03_fonctions_modules/)** : Découper son code et importer des outils.
5.  **[04_exceptions_fichiers](./04_exceptions_fichiers/)** : Lire, écrire et gérer les erreurs.
6.  **[05_poo](./05_poo/)** : La Programmation Orientée Objet (Classes).
7.  **[06_iterateurs_generateurs](./06_iterateurs_generateurs/)** : Concepts avancés et efficacité.
8.  **[07_debugger](./07_debugger/)** : Apprendre à trouver et corriger ses bugs.
9.  **[08_asyncio](./08_asyncio/)** : Faire plusieurs choses « en même temps ».
10. **[09_tests_qualite](./09_tests_qualite/)** : Écrire du code propre et vérifié.

### Python appliqué (automatisation) — mettre en pratique
11. **[10_fichiers_dossiers](./10_fichiers_dossiers/)** : Ranger des fichiers, CSV / JSON / Excel.
12. **[11_web_apis](./11_web_apis/)** : Télécharger, appeler des APIs, scraping.
13. **[12_taches_scripts](./12_taches_scripts/)** : Scripts réutilisables (`argparse`) & planification.
14. **[13_donnees_rapports](./13_donnees_rapports/)** : Manipuler des données et générer des rapports (`pandas`).
15. **[14_bibliotheques](./14_bibliotheques/)** : `pip`, environnements virtuels, `requirements.txt`.

---

## 🛠️ Pratiquer & sécurité

- **[15_construire_un_script/](./15_construire_un_script/)** : écrire un script de zéro en
  **raisonnant** (compter des fichiers, convertir JSON → SQL) — commenté pas à pas.
- **[projets/](./projets/)** : mini-projets concrets (ranger des fichiers, carnet de contacts, suivi météo).
- **[pentest/](./pentest/)** : sécurité (éducatif) — scanners réseau et démos offensives.
- **[modele_script.py](./modele_script.py)** : un squelette de script prêt à copier.

---

## 🧠 Comprendre VRAIMENT le code (à lire si tu bloques en lisant des scripts)

- **[LES_SYMBOLES.md](./LES_SYMBOLES.md)** : à quoi servent `( )`, `[ ]`, `{ }`, `.`, `=`, `%`,
  `:` — **quand** les mettre et **pourquoi** — et surtout **comment savoir quels arguments**
  accepte une fonction (le `exist_ok=`, le `2` entre parenthèses…).
- **[COMPRENDRE_LE_CODE.md](./COMPRENDRE_LE_CODE.md)** : lire et **décoder** n'importe quelle
  ligne (les `__main__`, `__init__.py`, `', '.join(...)`, `if not x`, le `_prive`…).
- **[ECRIRE_UN_SCRIPT.md](./ECRIRE_UN_SCRIPT.md)** : la **méthode pour raisonner** et trouver
  les bonnes fonctions/arguments quand on part d'une idée.

---

## 📚 Ressources indispensables

- **[ANATOMIE_D_UN_SCRIPT.md](./ANATOMIE_D_UN_SCRIPT.md)** : Comment structurer un fichier `.py`.
- **[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md)** : La syntaxe résumée sur une page.
- **[GLOSSAIRE.md](./GLOSSAIRE.md)** : Le dictionnaire des termes techniques.
