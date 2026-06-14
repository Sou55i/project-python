"""
MODÈLE DE SCRIPT — à copier pour démarrer tes propres scripts
=============================================================
Ce fichier montre l'ORDRE standard d'un script Python complet.
Lis le guide associé : automatisation/ANATOMIE_D_UN_SCRIPT.md

Exemple concret ici : on demande l'âge de l'utilisateur et on lui dit
dans combien d'années il aura 100 ans. Simple, mais il illustre la structure.

Lance-le :  python3 automatisation/modele_script.py
"""

# ═══════════════════════════════════════════════════════════════
# (2) LES IMPORTS  ->  on ouvre les caisses à outils, tout en haut.
#     (Ici on n'a besoin d'aucun outil externe, donc rien à importer.
#      On laisse la section pour montrer où elle se place.
#      Cours sur les imports : automatisation/06_bibliotheques/)
# ═══════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# (3) LES CONSTANTES  ->  les valeurs fixes, en MAJUSCULES par convention.
#     On les regroupe ici pour les modifier facilement à un seul endroit.
# ═══════════════════════════════════════════════════════════════
AGE_CIBLE = 100


# ═══════════════════════════════════════════════════════════════
# (4) LES FONCTIONS  ->  on DÉFINIT les actions réutilisables.
#     Attention : écrire 'def' ne LANCE pas le code ; ça le prépare.
#     Le code d'une fonction ne s'exécute que lorsqu'on l'APPELLE (voir plus bas).
# ═══════════════════════════════════════════════════════════════
def annees_restantes(age):
    """Calcule combien d'années il reste avant d'atteindre AGE_CIBLE."""
    # TRAITEMENT : un simple calcul, renvoyé à celui qui appelle la fonction.
    return AGE_CIBLE - age


# ═══════════════════════════════════════════════════════════════
# (5) LE PROGRAMME PRINCIPAL  ->  le "chef d'orchestre" qui démarre tout.
#     Il suit les 3 phases : ENTRÉE -> TRAITEMENT -> SORTIE.
#     'if __name__ == "__main__":' = "n'exécute ce bloc que si on lance
#     CE fichier directement" (voir module 04 pour le détail).
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # 1. ENTRÉE : on récupère l'info AVANT de s'en servir.
    #    int(input(...)) : input() renvoie du TEXTE, int() le convertit en nombre.
    age = int(input("Quel âge as-tu ? "))

    # 2. TRAITEMENT : on appelle la fonction définie plus haut.
    reste = annees_restantes(age)

    # 3. SORTIE : on affiche le résultat.
    print(f"Il te reste {reste} ans avant d'avoir {AGE_CIBLE} ans. 🎂")
