"""
MODULE 01 - Les briques de base
================================
Ce script illustre, dans l'ordre, les notions du README :
variables, types, conditions, boucles, fonctions, listes et dictionnaires.

Lance-le :  python3 automatisation/01_les_bases/bases.py
"""

# ─────────────────────────────────────────────
# 1. VARIABLES ET TYPES
# ─────────────────────────────────────────────
prenom = "Alice"      # str  : du texte (entre guillemets)
age = 30              # int  : un nombre entier
taille = 1.68         # float: un nombre à virgule (point !)
majeur = True         # bool : vrai ou faux (majuscule)

# f-string : le 'f' permet d'insérer des variables entre { }
print(f"{prenom}, {age} ans, {taille} m. Majeur ? {majeur}")

# type() révèle la nature d'une valeur
print(f"Le type de 'age' est : {type(age)}")

# Attention au type : texte vs nombre
print("5" + "5")   # "55" (collage de texte)
print(5 + 5)       # 10  (addition de nombres)


# ─────────────────────────────────────────────
# 2. CONDITIONS (if / elif / else)
# ─────────────────────────────────────────────
note = 12
if note >= 16:
    print("Très bien 🌟")
elif note >= 10:          # "sinon si"
    print("Reçu ✅")
else:
    print("À retravailler ❌")


# ─────────────────────────────────────────────
# 3. BOUCLES
# ─────────────────────────────────────────────
# for : pour chaque élément d'une liste
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(f"- {fruit}")

# range : répéter un nombre précis de fois
for i in range(3):        # 0, 1, 2
    print(f"Répétition {i}")

# while : tant qu'une condition est vraie
compteur = 0
while compteur < 3:
    print(f"compteur = {compteur}")
    compteur += 1         # += veut dire "compteur = compteur + 1"


# ─────────────────────────────────────────────
# 4. FONCTIONS
# ─────────────────────────────────────────────
def saluer(prenom):
    """Renvoie un message de salutation personnalisé."""
    return f"Bonjour {prenom} !"

# On appelle la fonction plusieurs fois, sans réécrire son code
print(saluer("Alice"))
print(saluer("Bob"))


# ─────────────────────────────────────────────
# 5. LISTES ET DICTIONNAIRES
# ─────────────────────────────────────────────
courses = ["pain", "lait", "œufs"]
courses.append("café")          # ajoute à la fin
print(f"Premier article : {courses[0]}")   # on compte à partir de 0
print(f"Liste complète : {courses}")

personne = {"nom": "Alice", "age": 30, "ville": "Paris"}
print(f"{personne['nom']} habite à {personne['ville']}")
