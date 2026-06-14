"""
MODULE 01 - Les briques de base
================================
Ce script illustre, dans l'ordre, les notions du README :
variables, types, conditions, boucles, fonctions, listes et dictionnaires.

Lance-le :  python3 python/automatisation/01_les_bases/bases.py
"""

# ─────────────────────────────────────────────
# 1. VARIABLES ET TYPES
# ─────────────────────────────────────────────
# Une variable = une boîte étiquetée. Le '=' RANGE la valeur de droite dans
# la boîte nommée à gauche. Chaque valeur a un TYPE (sa "nature") :
prenom = "Alice"      # str   : du texte (entre guillemets "...")
age = 30              # int   : un nombre entier (sans virgule)
taille = 1.68         # float : un nombre à virgule (on écrit un POINT, pas une virgule)
majeur = True         # bool  : Vrai/Faux. Toujours avec une Majuscule : True ou False

# f"..." = f-string : le 'f' permet d'insérer des variables entre { }.
# Chaque { } est remplacé par la valeur de la variable à l'intérieur.
print(f"{prenom}, {age} ans, {taille} m. Majeur ? {majeur}")

# type(x) révèle la nature de la valeur x. Utile pour comprendre un bug.
print(f"Le type de 'age' est : {type(age)}")

# ATTENTION au type : "5" (texte) et 5 (nombre) ne se comportent pas pareil.
print("5" + "5")   # affiche 55 : avec du texte, '+' COLLE les deux morceaux
print(5 + 5)       # affiche 10 : avec des nombres, '+' ADDITIONNE


# ─────────────────────────────────────────────
# 2. CONDITIONS (if / elif / else)
# ─────────────────────────────────────────────
note = 12
# 'if' = "si". La ligne se termine par ':' et le bloc qui DÉPEND du if est
# décalé de 4 espaces vers la droite (cette indentation est OBLIGATOIRE).
if note >= 16:                 # >= signifie "supérieur ou égal à"
    print("Très bien 🌟")
elif note >= 10:               # 'elif' = "sinon si" (testé seulement si le if était faux)
    print("Reçu ✅")
else:                          # 'else' = "sinon" (dans tous les autres cas)
    print("À retravailler ❌")


# ─────────────────────────────────────────────
# 3. BOUCLES (répéter une action)
# ─────────────────────────────────────────────
# Boucle 'for' : "POUR CHAQUE élément de la liste". Lis-le comme une phrase :
# "pour chaque fruit dans fruits, fais...". Le bloc indenté s'exécute 1 fois par fruit.
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(f"- {fruit}")

# range(3) génère les nombres 0, 1, 2 (il s'ARRÊTE avant 3, et commence à 0).
# Pratique pour répéter un nombre PRÉCIS de fois.
for i in range(3):
    print(f"Répétition {i}")

# Boucle 'while' : "TANT QUE la condition est vraie, répète".
compteur = 0
while compteur < 3:
    print(f"compteur = {compteur}")
    compteur += 1     # '+=' veut dire "compteur = compteur + 1".
    #                   Sans cette ligne, compteur resterait à 0 et la boucle
    #                   tournerait à l'infini !


# ─────────────────────────────────────────────
# 4. FONCTIONS (emballer du code réutilisable)
# ─────────────────────────────────────────────
# 'def' = "définir". On définit la fonction UNE fois, on l'appelle autant qu'on veut.
#   saluer        = le nom qu'on donne à la fonction
#   (prenom)      = le PARAMÈTRE : une information qu'on lui donne en entrée
#   return ...    = la valeur que la fonction RENVOIE à celui qui l'a appelée
def saluer(prenom):
    """Renvoie un message de salutation personnalisé."""
    return f"Bonjour {prenom} !"

# Ici on APPELLE la fonction : on lui donne une valeur, elle nous renvoie le message.
print(saluer("Alice"))
print(saluer("Bob"))


# ─────────────────────────────────────────────
# 5. LISTES ET DICTIONNAIRES (ranger plusieurs valeurs)
# ─────────────────────────────────────────────
# Une LISTE = une suite ordonnée de valeurs, entre crochets [ ].
courses = ["pain", "lait", "œufs"]
courses.append("café")          # .append() ajoute un élément À LA FIN de la liste
# courses[0] = le PREMIER élément. En Python, on compte à partir de 0 (pas de 1) !
print(f"Premier article : {courses[0]}")
print(f"Liste complète : {courses}")

# Un DICTIONNAIRE = des paires "clé": valeur, entre accolades { }.
# Parfait pour décrire un objet avec plusieurs caractéristiques.
personne = {"nom": "Alice", "age": 30, "ville": "Paris"}
# On accède à une valeur par sa CLÉ, entre crochets : personne["nom"].
print(f"{personne['nom']} habite à {personne['ville']}")
