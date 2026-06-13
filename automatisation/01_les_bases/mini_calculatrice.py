"""
MODULE 01 - Mini-projet : une calculatrice
===========================================
On combine TOUT ce qu'on a vu (variables, types, conditions, fonctions,
boucle while, input) dans un petit programme utile.

Lance-le :  python3 automatisation/01_les_bases/mini_calculatrice.py
Pour quitter : tape 'q' quand on te demande l'opération.
"""


# Une fonction par opération : code clair et réutilisable.
def additionner(a, b):
    return a + b


def soustraire(a, b):
    return a - b


def multiplier(a, b):
    return a * b


def diviser(a, b):
    # On se protège de la division par zéro (qui ferait planter le programme).
    if b == 0:
        return "Erreur : on ne peut pas diviser par zéro."
    return a / b


# ─────────────────────────────────────────────
# Boucle principale : on répète tant que l'utilisateur ne quitte pas.
# ─────────────────────────────────────────────
print("🧮 Mini-calculatrice (tape 'q' pour quitter)")

while True:                       # boucle "infinie"... jusqu'au 'break' plus bas
    operation = input("\nOpération (+, -, *, / ou q) : ")

    if operation == "q":
        print("Au revoir ! 👋")
        break                     # 'break' sort de la boucle while

    # input() renvoie du TEXTE : on convertit en float pour pouvoir calculer.
    nombre1 = float(input("Premier nombre  : "))
    nombre2 = float(input("Deuxième nombre : "))

    if operation == "+":
        resultat = additionner(nombre1, nombre2)
    elif operation == "-":
        resultat = soustraire(nombre1, nombre2)
    elif operation == "*":
        resultat = multiplier(nombre1, nombre2)
    elif operation == "/":
        resultat = diviser(nombre1, nombre2)
    else:
        resultat = "Opération inconnue."

    print(f"➡️  Résultat : {resultat}")
