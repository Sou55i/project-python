# 🃏 Aide-mémoire Python (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases` et suivants.

---

## Afficher / demander

```python
print("Bonjour")                 # afficher du texte
print(f"Âge : {age}")            # f-string : insère une variable entre { }
nom = input("Ton nom ? ")        # demander (renvoie TOUJOURS du texte)
age = int(input("Ton âge ? "))   # demander un nombre -> convertir avec int()
```

## Variables et types

```python
age = 30          # int   : entier
prix = 9.99       # float : nombre à virgule (point)
nom = "Alice"     # str   : texte
actif = True      # bool  : True / False
rien = None       # absence de valeur

type(age)         # connaître le type
int("42")         # texte -> entier
str(42)           # entier -> texte
float("3.5")      # texte -> décimal
```

## Opérateurs

```python
+  -  *  /        # addition, soustraction, multiplication, division
//                # division entière (7 // 2 == 3)
%                 # reste (modulo) (7 % 2 == 1)
**                # puissance (2 ** 3 == 8)

==  !=            # égal / différent
<  >  <=  >=      # comparaisons
and  or  not      # ET / OU / NON logiques
in                # appartenance ("a" in "chat" -> True)
```

## Conditions

```python
if age >= 18:
    print("Majeur")
elif age >= 13:
    print("Ado")
else:
    print("Enfant")
```

## Boucles

```python
for fruit in ["pomme", "kiwi"]:   # pour chaque élément
    print(fruit)

for i in range(5):                # 0,1,2,3,4
    print(i)

while x < 10:                     # tant que la condition est vraie
    x += 1
```

## Listes (suite ordonnée)

```python
courses = ["pain", "lait"]
courses.append("œufs")    # ajouter à la fin
courses[0]                # premier élément (on compte à partir de 0)
courses[-1]               # dernier élément
len(courses)              # nombre d'éléments
courses[1:3]              # "tranche" (slice) : du 1 au 2
"pain" in courses         # test d'appartenance -> True
```

## Dictionnaires (clé -> valeur)

```python
personne = {"nom": "Alice", "age": 30}
personne["nom"]              # accès par clé -> "Alice"
personne["ville"] = "Paris"  # ajouter / modifier
personne.get("tel", "?")     # accès sûr (valeur par défaut si absent)
for cle, valeur in personne.items():
    print(cle, valeur)
```

## Fonctions

```python
def saluer(nom, poli=True):      # poli a une valeur par défaut
    if poli:
        return f"Bonjour {nom}"
    return f"Salut {nom}"

saluer("Alice")                  # appel
saluer("Bob", poli=False)        # argument nommé
```

## Texte (chaînes)

```python
s = "  Bonjour Monde  "
s.strip()           # enlève les espaces autour
s.lower()           # minuscules ; s.upper() majuscules
s.replace("o", "0") # remplacer
s.split(" ")        # découper -> liste
", ".join(liste)    # recoller une liste en texte
s.startswith("Bon") # commence par ?
```

## Fichiers

```python
# Écrire (w écrase, a ajoute à la fin)
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("ligne\n")          # \n = retour à la ligne

# Lire
with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()          # tout
    # ou ligne par ligne :
    for ligne in f:
        print(ligne.strip())
```

## JSON et CSV

```python
import json
json.dump(data, f, indent=2, ensure_ascii=False)  # écrire
data = json.load(f)                                # lire

import csv
w = csv.DictWriter(f, fieldnames=["nom", "age"]); w.writeheader(); w.writerows(lignes)
for ligne in csv.DictReader(f): ...                # lire
```

## Gérer les erreurs

```python
try:
    risque()                 # code qui peut échouer
except ValueError as e:
    print(f"Erreur : {e}")   # on attrape sans planter
finally:
    nettoyer()               # s'exécute toujours
```

## Importer des outils

```python
import os                    # tout le module : os.getcwd()
from pathlib import Path     # juste un outil : Path("x")
import pandas as pd          # avec un surnom : pd.read_csv(...)
```

## Structure type d'un script

```python
"""Description."""
import ...                   # 1. imports
CONSTANTE = ...              # 2. constantes
def fonction(): ...          # 3. fonctions
if __name__ == "__main__":   # 4. programme principal
    ...                      #    entrée -> traitement -> sortie
```

➡️ Voir aussi : [ANATOMIE_D_UN_SCRIPT.md](./ANATOMIE_D_UN_SCRIPT.md) et [GLOSSAIRE.md](./GLOSSAIRE.md).
