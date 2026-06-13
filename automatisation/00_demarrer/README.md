# Module 00 — Démarrer : comprendre ce qu'on fait

Avant d'écrire une seule ligne de code, prenons 5 minutes pour comprendre **de quoi on parle**.
Ce module est 100 % théorique (plus un tout petit script à la fin).

---

## 1. C'est quoi un « programme » ?

Un ordinateur ne sait rien faire seul. Il faut lui donner une **suite d'instructions
précises**, dans l'ordre, comme une recette de cuisine :

> 1. Prends 200 g de farine
> 2. Ajoute 2 œufs
> 3. Mélange
> 4. Mets au four 20 minutes

Un **programme**, c'est exactement ça : une recette écrite dans un langage que l'ordinateur
comprend. Ici, ce langage est **Python**. Chaque ligne est une instruction, et l'ordinateur
les exécute **de haut en bas, une par une**.

La grosse différence avec une recette de cuisine : l'ordinateur est **bête mais obéissant**.
Il fait *exactement* ce que tu écris, même si c'est une erreur. Si tu te trompes d'une
virgule, il s'arrête. Ce n'est pas grave : apprendre à lire les messages d'erreur fait
partie du métier.

---

## 2. C'est quoi le « terminal » ?

Le **terminal** (aussi appelé « console » ou « invite de commandes ») est une fenêtre où
tu **tapes des commandes au clavier** au lieu de cliquer sur des boutons.

C'est là qu'on va **lancer** nos programmes Python. Une commande typique ressemble à ça :

```bash
python3 mon_programme.py
```

Décortiquons :
- `python3` → « Hé, Python, réveille-toi, j'ai du travail. »
- `mon_programme.py` → « Voici le fichier-recette à exécuter. »

> 📌 Les fichiers Python se terminent toujours par **`.py`**. C'est juste une convention
> qui dit « ceci est du code Python ».

---

## 3. Le cycle : écrire → lancer → observer → corriger

Programmer, c'est une **boucle** :

```
   ┌──────────────┐
   │  J'écris du   │
   │     code      │
   └──────┬───────┘
          ▼
   ┌──────────────┐
   │  Je le lance  │
   └──────┬───────┘
          ▼
   ┌──────────────┐      ça marche ? ──► 🎉 suivant
   │  J'observe    │
   │  le résultat  │      erreur ? ──► je lis le message et je corrige
   └──────────────┘
```

Personne n'écrit du code parfait du premier coup. **Même les pros passent leur temps à
corriger des erreurs.** C'est normal et attendu.

---

## 4. Les commentaires : des notes pour les humains

Dans un fichier Python, tout ce qui suit le symbole `#` est un **commentaire**. L'ordinateur
l'**ignore** complètement. Les commentaires servent à **expliquer le code aux humains**
(toi, dans 6 mois, ou un collègue).

```python
# Ceci est un commentaire : Python ne le lit pas.
print("Bonjour")   # On peut aussi commenter en fin de ligne.
```

Dans ce dépôt, les fichiers `.py` sont **remplis de commentaires** : lis-les, ils font
partie du cours.

---

## 5. La première instruction : `print()`

`print()` est l'instruction la plus simple : elle **affiche** du texte à l'écran.

```python
print("Bonjour le monde !")
```

Le texte entre **guillemets** `"..."` s'appelle une **chaîne de caractères** (en anglais
*string*). On en reparlera au module 01.

---

## ▶️ À toi de jouer

Lance le petit script de ce module :

```bash
python3 automatisation/00_demarrer/premier_script.py
```

Lis ensuite le fichier [`premier_script.py`](./premier_script.py) en entier : chaque ligne
est commentée. Puis **modifie le texte affiché** et relance le script pour voir le changement.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/) — les briques du langage.
