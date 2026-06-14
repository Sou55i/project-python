"""
MODULE 01 - Bonus : demander une note avec input() (les 2 pièges classiques)
===========================================================================
Beaucoup de débutants essaient d'ajouter un input() à l'exemple des conditions
et obtiennent une erreur. Ce fichier explique POURQUOI et montre la version
qui marche. Voir aussi le guide : automatisation/ANATOMIE_D_UN_SCRIPT.md

Lance-le :  python3 automatisation/01_les_bases/note_avec_input.py


🗺️ CE QUE BEAUCOUP ESSAIENT (et qui NE MARCHE PAS) :

    if note >= 16:
        print("Très bien")
    elif note >= 10:
        print("Passable")
    else:
        print("c'est nul")

    note = input("donne ta note: ")   # ← problème !

    Deux bugs :
      1) ORDRE : Python lit de haut en bas. La 'note' est créée APRÈS le if,
         donc au moment du if elle n'existe pas encore -> NameError.
      2) TYPE : input() renvoie TOUJOURS du texte. Comparer du texte "15" à un
         nombre 16 plante -> TypeError.

    Règle : on DEMANDE d'abord (entrée), on CONVERTIT en nombre, PUIS on teste.
"""

# ─────────────────────────────────────────────
# ✅ LA VERSION QUI MARCHE
# ─────────────────────────────────────────────

# 1. ENTRÉE — on demande la note AVANT de l'utiliser.
#    Décodage de int(input("...")) en partant de l'intérieur :
#      input("donne ta note: ") -> affiche la question, attend, et renvoie du TEXTE
#      int( ... )               -> convertit ce texte en nombre entier
#    Sans le int(...), 'note' resterait du texte et la comparaison planterait.
note = int(input("Donne ta note (0-20) : "))

# 2. TRAITEMENT — maintenant 'note' existe ET c'est un nombre : on peut comparer.
if note >= 16:
    print("Très bien 🌟")
elif note >= 10:                 # 'elif' = "sinon si"
    print("Passable ✅")
else:                            # 'else' = "sinon" (tous les autres cas)
    print("C'est nul ❌")

# 💡 Pour des notes à virgule (ex : 12.5), remplace int(...) par float(...) :
#       note = float(input("Donne ta note : "))
