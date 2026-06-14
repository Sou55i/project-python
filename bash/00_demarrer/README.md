# Module 00 — Démarrer en Bash

Avant d'écrire un script, comprenons **ce qu'est le shell** et comment Bash exécute nos
commandes. Module surtout théorique, avec un premier script à la fin.

---

## 1. C'est quoi le « shell » ?

Quand tu ouvres un **terminal**, le programme qui lit ce que tu tapes et l'exécute s'appelle
le **shell**. **Bash** (*Bourne Again SHell*) est le shell le plus répandu sous Linux.

Chaque ligne que tu tapes est une **commande** : `ls` (lister les fichiers), `cd` (changer
de dossier), `echo` (afficher du texte)… Un **script Bash**, c'est simplement **un fichier
qui contient une suite de ces commandes**, exécutées de haut en bas.

🎯 L'intérêt : au lieu de retaper 20 commandes à la main chaque jour, tu les écris **une
fois** dans un script, et tu le relances quand tu veux. C'est ça, l'automatisation.

---

## 2. Le « shebang » : la première ligne magique

Un script Bash commence par une ligne spéciale appelée **shebang** :

```bash
#!/usr/bin/env bash
```

Elle dit au système : « ce fichier doit être exécuté **avec bash** ». Le `#!` est le signal,
et `/usr/bin/env bash` trouve bash où qu'il soit installé. **Mets toujours cette ligne en
tout premier**, avant tout le reste.

> ℹ️ Bizarrement, cette ligne commence par `#`, qui sert normalement aux commentaires. C'est
> une exception : le `#!` tout en haut d'un fichier a un sens spécial pour le système.

---

## 3. Les commentaires

Tout ce qui suit un `#` (sauf le shebang) est un **commentaire** : ignoré par Bash, écrit
pour les humains.

```bash
# Ceci est un commentaire.
echo "Bonjour"   # On peut aussi commenter en fin de ligne.
```

---

## 4. Afficher du texte avec `echo`

`echo` est la commande la plus simple : elle **affiche** ce qu'on lui donne.

```bash
echo "Bonjour le monde !"
```

> 💡 Mets ton texte entre **guillemets doubles** `"..."`. On verra au module 01 pourquoi
> c'est important (surtout dès qu'il y a des variables).

---

## 5. Rendre un script exécutable

Par défaut, un fichier `.sh` n'a pas le **droit** d'être lancé directement. Deux options :

```bash
# Option A : on passe le script à bash (aucune permission nécessaire)
bash mon_script.sh

# Option B : on donne le droit d'exécution UNE fois, puis on l'appelle avec ./
chmod +x mon_script.sh    # chmod +x = "rends ce fichier exécutable"
./mon_script.sh           # le ./ veut dire "dans le dossier courant"
```

Le cycle de travail est donc : **écrire → lancer → observer → corriger**, comme en Python
(et sans étape de compilation).

---

## ▶️ À toi de jouer

```bash
bash bash/00_demarrer/premier_script.sh
```

Lis ensuite [`premier_script.sh`](./premier_script.sh) (tout est commenté), modifie le texte,
et relance-le.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
