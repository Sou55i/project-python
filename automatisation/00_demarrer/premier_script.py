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
# print() affiche à l'écran ce qu'on met entre parenthèses.
# Le texte entre guillemets "..." s'appelle une "chaîne de caractères".
print("Bonjour le monde ! 👋")
print("Je viens de lancer mon premier programme Python.")

# On peut afficher plusieurs lignes : Python lit de haut en bas, une par une.
print("Cette ligne s'affiche après les précédentes.")


# ─────────────────────────────────────────────
# 2. POSER UNE QUESTION avec input()
# ─────────────────────────────────────────────
# input() met le programme en PAUSE et attend que tu tapes quelque chose,
# puis valide avec Entrée. Ce que tu tapes est "récupéré" dans une variable.
# (Une variable = une boîte étiquetée qui retient une valeur. Voir module 01.)
prenom = input("Comment t'appelles-tu ? ")

# On réutilise ce que la personne a tapé.
# Le 'f' devant les guillemets permet d'insérer une variable entre accolades {}.
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
