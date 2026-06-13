"""
MODULE 00 - Premier script
===========================
Ton tout premier programme Python. Objectif : voir le cycle
« écrire -> lancer -> observer » en action.

Pour le lancer, ouvre un terminal et tape :
    python3 automatisation/00_demarrer/premier_script.py

Rappel : tout ce qui suit un '#' est un COMMENTAIRE. L'ordinateur l'ignore,
c'est écrit pour TOI. Lis-les, ce sont des explications.
"""

# ─────────────────────────────────────────────
# 1. AFFICHER DU TEXTE avec print()
# ─────────────────────────────────────────────
# Décodage de la ligne ci-dessous, morceau par morceau :
#   print   = le nom de l'instruction qui "affiche à l'écran"
#   ( )     = les parenthèses contiennent ce qu'on veut afficher
#   "..."   = les guillemets délimitent du TEXTE (une "chaîne de caractères")
print("Bonjour le monde ! 👋")
print("Je viens de lancer mon premier programme Python.")

# Python lit les lignes de HAUT en BAS, une par une, dans l'ordre.
print("Cette ligne s'affiche après les précédentes.")


# ─────────────────────────────────────────────
# 2. POSER UNE QUESTION avec input()
# ─────────────────────────────────────────────
# input("...") fait 3 choses :
#   1. affiche le texte entre guillemets (la question),
#   2. met le programme EN PAUSE et attend que tu tapes quelque chose + Entrée,
#   3. renvoie ce que tu as tapé.
#
# Le signe '=' RANGE ce résultat dans une "variable" nommée prenom.
#   Une variable = une boîte étiquetée qui retient une valeur pour la réutiliser.
prenom = input("Comment t'appelles-tu ? ")

# Décodage du f"..." (on l'appelle une "f-string") :
#   le 'f' juste avant les guillemets active un mode spécial,
#   où tout ce qui est entre accolades { } est REMPLACÉ par la valeur de la variable.
#   Ici {prenom} sera remplacé par ce que la personne a tapé.
print(f"Enchanté, {prenom} ! Bienvenue dans le monde de Python. 🐍")


# ─────────────────────────────────────────────
# 3. À TOI DE MODIFIER
# ─────────────────────────────────────────────
# Essaie de :
#   - changer le texte des print() ci-dessus,
#   - ajouter un nouveau print() avec ton message,
#   - poser une 2e question (ex : "Quel âge as-tu ?").
# Puis relance le script pour voir tes changements. C'est comme ça qu'on apprend !
print("Fin du programme. Relance-le après l'avoir modifié. 🚀")
