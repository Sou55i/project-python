# 📝 Aide-mémoire Python (Cheat Sheet)

L'essentiel de la syntaxe Python sur une seule page.

---

## 🚀 Bases & Variables
```python
x = 5                # Entier (int)
y = 3.14             # Flottant (float)
nom = "Alice"        # Chaîne de caractères (str)
est_vrai = True      # Booléen (bool)

# Affichage & Saisie
print(f"Salut {nom}")      # f-string (recommandé)
age = input("Ton âge ? ")  # Toujours du texte, à convertir : int(age)
```

## 📦 Collections
```python
# Liste (ordonnée, modifiable)
L = [1, 2, 3]
L.append(4)
print(L[0])          # Premier élément : 1

# Dictionnaire (Clé: Valeur)
D = {"nom": "Alice", "age": 25}
print(D["nom"])

# Tuple (ordonné, NON modifiable)
T = (10, 20)

# Set (valeurs uniques, non ordonné)
S = {1, 2, 2, 3}     # Deviendra {1, 2, 3}
```

## ⚙️ Contrôle de flux
```python
# Conditions
if age >= 18:
    print("Majeur")
elif age > 0:
    print("Mineur")
else:
    print("Erreur")

# Boucle For (Parcourir)
for i in range(5):   # 0 à 4
    print(i)

for item in ["a", "b"]:
    print(item)

# Boucle While (Tant que)
while x > 0:
    x -= 1
```

## 🛠️ Fonctions & Classes
```python
# Fonction
def addition(a, b=10):  # b a une valeur par défaut
    return a + b

# Classe (POO)
class Humain:
    def __init__(self, nom):
        self.nom = nom  # Attribut
    
    def parler(self):
        print(f"Je suis {self.nom}")
```

## 📂 Fichiers & Exceptions
```python
# Gestion d'erreurs
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Oups !")

# Lecture/Écriture (Le 'with' ferme le fichier tout seul)
with open("test.txt", "w") as f:
    f.write("Hello")

with open("test.txt", "r") as f:
    contenu = f.read()
```

## 🔍 Astuces Pythoniques
```python
# List Comprehension (Créer une liste rapidement)
carres = [x**2 for x in range(10)]

# Unpacking
a, b = 1, 2

# Enumerate (Index + Valeur)
for i, val in enumerate(["a", "b"]):
    print(f"Index {i} : {val}")
```
