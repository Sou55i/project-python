"""
MODULE 01 - Mini-projet : une calculatrice
===========================================
On combine TOUT ce qu'on a vu (variables, types, conditions, fonctions,
boucle while, input) dans un petit programme utile.

Lance-le :  python3 python/automatisation/01_les_bases/mini_calculatrice.py
Pour quitter : tape 'q' quand on te demande l'opération.
"""


# Une fonction par opération : du code clair, nommé et réutilisable.
#   def        -> "je définis une fonction"
#   additionner-> son nom
#   (a, b)     -> ses deux PARAMÈTRES (les deux nombres à traiter)
#   return     -> renvoie le résultat à celui qui a appelé la fonction
def additionner(a, b):
    return a + b


def soustraire(a, b):
    return a - b


def multiplier(a, b):
    return a * b      # '*' = multiplication


def diviser(a, b):
    # '==' compare deux valeurs (≠ du '=' qui RANGE dans une variable).
    # On se protège de la division par zéro, qui ferait planter le programme.
    if b == 0:
        return "Erreur : on ne peut pas diviser par zéro."
    return a / b      # '/' = division


# ─────────────────────────────────────────────
# Boucle principale : on répète tant que l'utilisateur ne quitte pas.
# ─────────────────────────────────────────────
print("🧮 Mini-calculatrice (tape 'q' pour quitter)")

# 'while True:' = boucle qui tourne INDÉFINIMENT... jusqu'à un 'break' (voir plus bas).
while True:
    # \n (en début de texte) ajoute une ligne vide avant la question, pour aérer.
    operation = input("\nOpération (+, -, *, / ou q) : ")

    # Si l'utilisateur tape 'q', on sort de la boucle.
    if operation == "q":
        print("Au revoir ! 👋")
        break                 # 'break' = "casse" la boucle while et en sort

    # input() renvoie TOUJOURS du texte. float(...) le convertit en nombre à virgule,
    # sinon on ne pourrait pas calculer ("3" + "4" donnerait "34", pas 7).
    nombre1 = float(input("Premier nombre  : "))
    nombre2 = float(input("Deuxième nombre : "))

    # Selon l'opération choisie, on appelle la bonne fonction.
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
