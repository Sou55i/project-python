# 🚀 Module 00 : Démarrer avec Python

> 🎯 **Objectif de ce module** : comprendre ce qu'est *vraiment* « coder », installer Python,
> lancer ton premier script, et apprendre dès le départ la bonne habitude des **environnements
> virtuels**. À la fin, tu sauras exécuter du code Python sur ta machine et tu comprendras
> chaque mot de ton premier programme.

---

## 0. C'est quoi « coder », au juste ?

Un ordinateur ne sait rien faire seul : il **exécute des instructions**, une par une, très
vite. **Coder**, c'est écrire ces instructions dans un langage qu'il peut comprendre.

Le problème : le processeur ne comprend que des `0` et des `1`. Écrire directement en `0`/`1`
serait infaisable. On utilise donc un **langage de programmation** : un texte lisible par un
humain, qu'un programme se charge de traduire pour la machine.

- Avec **Python**, tu écris du texte dans un fichier qui finit par `.py`.
- Un programme appelé **l'interpréteur Python** (la commande `python3`) lit ce fichier
  **de haut en bas**, ligne après ligne, et fait ce que tu as demandé.

> 🧠 **L'image à retenir** : ton fichier `.py` est une **recette de cuisine**. L'interpréteur
> `python3` est le **cuisinier** qui lit la recette et exécute chaque étape dans l'ordre.

---

## 1. Le terminal : ton poste de pilotage

Avant Python, un mot sur le **terminal** (aussi appelé « console » ou « ligne de commande »).
C'est une fenêtre où tu **tapes des commandes** au lieu de cliquer. Les développeurs l'utilisent
en permanence car c'est plus rapide et plus précis que la souris.

Trois commandes suffisent pour commencer :

| Commande | Ce qu'elle fait | Moyen mnémotechnique |
|----------|-----------------|----------------------|
| `pwd`    | affiche le dossier où tu te trouves | **p**rint **w**orking **d**irectory |
| `ls`     | liste les fichiers du dossier courant | **l**i**s**t |
| `cd nom` | entre dans le dossier `nom` (`cd ..` pour remonter) | **c**hange **d**irectory |

> 💡 Sur Windows, le terminal s'appelle **PowerShell** (ou « Invite de commandes ») ; sur
> macOS/Linux, c'est **Terminal**. Les commandes ci-dessus marchent partout (PowerShell les
> comprend aussi).

---

## 2. Vérifier que Python est installé

Dans le terminal, tape :

```bash
python3 --version
```

- Si tu vois quelque chose comme `Python 3.10.x` (ou un numéro plus récent) : **c'est gagné**,
  Python est déjà là.
- Si tu vois `command not found` (ou « commande introuvable ») : Python n'est pas installé.
  Va sur **[python.org/downloads](https://www.python.org/downloads/)**, télécharge la dernière
  version, et **sur Windows coche la case « Add Python to PATH »** pendant l'installation
  (sinon le terminal ne trouvera pas la commande).

> 🔎 **Pourquoi `python3` et pas `python` ?** Sur beaucoup de systèmes, `python` tout court
> désigne encore l'ancien Python 2 (abandonné). `python3` lève toute ambiguïté. Si chez toi
> `python3` ne marche pas mais `python` oui, utilise `python`.

---

## 3. Ton tout premier script : « Hello World »

Par tradition, le premier programme qu'on écrit dans **tous** les langages affiche un petit
message. En Python, ça tient en **une ligne**.

Crée un fichier nommé `hello.py` contenant :

```python
print("Bonjour le monde !")
```

Puis, dans le terminal, **place-toi dans le bon dossier** (`cd`) et lance :

```bash
python3 hello.py
```

Tu devrais voir s'afficher : `Bonjour le monde !` 🎉

### Décortiquons cette unique ligne

```python
print("Bonjour le monde !")
```

- `print` est une **fonction** : un outil tout prêt, fourni par Python, dont le rôle est
  d'**afficher** quelque chose à l'écran.
- Les **parenthèses** `( )` veulent dire « **exécute** cette fonction **avec** ce qu'il y a
  à l'intérieur ». (Le rôle précis des parenthèses est détaillé dans
  [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md).)
- Les **guillemets** `" "` entourent du **texte**. En programmation, un morceau de texte
  s'appelle une **chaîne de caractères** (en anglais *string*, souvent abrégé `str`).
  Sans les guillemets, Python croirait que `Bonjour` est un nom de variable et planterait.

> 🧠 **À retenir** : `nom_de_fonction(...)` = « **fais** cette action avec ce qu'il y a dans
> les parenthèses ». C'est la forme la plus courante en Python ; tu vas la voir partout.

---

## 4. Le vrai fichier `hello.py`, commenté en entier

Le fichier [`hello.py`](./hello.py) de ce module est un peu plus complet. Voici à quoi
servent les lignes qu'on n'a pas encore expliquées :

```python
#!/usr/bin/env python3       # le "shebang" : indique quel programme lance ce fichier (Linux/macOS)
# -*- coding: utf-8 -*-      # précise l'encodage : autorise les accents (é, à, ç...) sans souci

"""
Ceci est une docstring : un texte de documentation
qui explique à quoi sert le fichier.
"""

# Une ligne qui commence par # est un COMMENTAIRE : Python l'ignore totalement.
# Les commentaires sont là pour les humains qui lisent le code.
print("Bonjour ! Bienvenue dans le monde de Python.")

print("2 + 2 font :", 2 + 2)   # on peut afficher du texte ET un calcul, séparés par une virgule
```

Trois nouveautés à mémoriser :

1. **Le commentaire** (`# ...`) : tout ce qui suit le `#` sur la ligne est **ignoré** par
   Python. Sert à expliquer le code. *Ne change rien à l'exécution.*
2. **La docstring** (`""" ... """`) : un commentaire sur **plusieurs lignes**, placé en haut
   d'un fichier ou d'une fonction pour le décrire.
3. **Le shebang et l'encodage** (les deux premières lignes) : des détails techniques utiles
   mais **pas obligatoires** pour débuter. Tu peux les copier sans tout comprendre pour
   l'instant.

> ⚠️ **Python lit de haut en bas.** Si une erreur se trouve à la ligne 10, les lignes 1 à 9
> se seront déjà exécutées. C'est important pour comprendre dans quel ordre les choses arrivent.

---

## 5. Le secret des pros : l'environnement virtuel (`venv`)

C'est l'étape que beaucoup de débutants sautent… et regrettent. Prends l'habitude **maintenant**.

### Le problème

Imagine deux projets sur ta machine :

- Le projet **A** a besoin de la bibliothèque `requests` en **version 1.0**.
- Le projet **B** a besoin de cette même `requests` mais en **version 2.0**.

Si tu installes tout « globalement » (au niveau du système), les deux versions entrent en
conflit et **un des deux projets casse**. Impossible d'avoir les deux versions en même temps.

### La solution

**Un environnement virtuel par projet** : une « bulle » isolée qui contient sa propre copie de
Python et ses propres bibliothèques. Ce qui est installé dans la bulle du projet A n'affecte
pas le projet B, ni le reste du système.

> 🧠 **L'image** : un environnement virtuel est une **boîte à outils dédiée à un projet**.
> Chaque projet a la sienne ; elles ne se mélangent jamais.

### Comment faire (les 4 commandes à connaître)

```bash
# 1. CRÉER l'environnement (on le nomme .venv par convention) — à faire UNE fois par projet
python3 -m venv .venv

# 2. L'ACTIVER (dire au terminal "utilise cette bulle") — à refaire à chaque session
source .venv/bin/activate          # Linux / macOS
.venv\Scripts\activate             # Windows (PowerShell)

# 3. INSTALLER des outils — ils n'iront QUE dans cette bulle
pip install requests

# 4. SORTIR de la bulle quand tu as fini
deactivate
```

Quand la bulle est active, ton invite de terminal affiche souvent `(.venv)` au début de la
ligne : c'est le signe que tu es bien dedans.

> 🔎 **Que signifie `python3 -m venv .venv` ?** L'option `-m` veut dire « lance le **module**
> nommé `venv` ». `venv` est l'outil de création d'environnements fourni avec Python. Le dernier
> `.venv` est simplement le **nom du dossier** qui va contenir la bulle. Tu pourrais l'appeler
> autrement, mais `.venv` est la convention universelle.

> 🛠️ **`pip`**, c'est quoi ? C'est le **gestionnaire de paquets** de Python : la commande qui
> télécharge et installe des bibliothèques écrites par d'autres. On l'approfondit au
> [module 14](../14_bibliotheques/).

---

## 6. Les erreurs de débutant (et comment les lire)

Tomber sur une erreur n'est **pas** un échec : c'est le quotidien de tout développeur. Le
réflexe pro, c'est de **lire le message** — Python est souvent très clair.

| Message (en gros) | Cause probable | Solution |
|-------------------|----------------|----------|
| `command not found: python3` | Python pas installé / pas dans le PATH | (ré)installe Python, coche « Add to PATH » |
| `No such file or directory: 'hello.py'` | tu n'es pas dans le bon dossier | `ls` pour vérifier, `cd` pour t'y rendre |
| `SyntaxError` | faute de frappe (parenthèse/guillemet oublié) | relis la ligne indiquée par le numéro |
| `NameError: name 'x' is not defined` | tu utilises un nom jamais créé (ou mal orthographié) | vérifie l'orthographe, la casse |

> 💡 **Lis toujours la DERNIÈRE ligne de l'erreur en premier** : elle donne le **type** d'erreur
> et un résumé. Juste au-dessus, Python indique le **numéro de la ligne** fautive.

---

## 🏁 Exercices

1. **Lis et lance** [`hello.py`](./hello.py). Repère le commentaire, la docstring, les `print`.
2. **Modifie-le** : ajoute une ligne qui affiche ton prénom, puis une autre qui calcule et
   affiche `7 * 8`.
3. **Crée un environnement virtuel** dans ce dossier (`python3 -m venv .venv`), active-le,
   vérifie que `(.venv)` apparaît, puis quitte-le avec `deactivate`.

<details>
<summary>💡 Solution de l'exercice 2</summary>

```python
print("Bonjour le monde !")
print("Je m'appelle Alex.")     # remplace par ton prénom
print("7 fois 8 font :", 7 * 8) # affiche : 7 fois 8 font : 56
```
</details>

➡️ **Prochaine étape** : [module 01 — les bases](../01_les_bases/) (variables, conditions, boucles).
