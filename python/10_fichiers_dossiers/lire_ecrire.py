"""
MODULE 02 - Lire et écrire des fichiers texte
==============================================
Les 3 opérations de base : écrire, ajouter, lire.

Lance-le :  python3 python/10_fichiers_dossiers/lire_ecrire.py

────────────────────────────────────────────────────────────────────────
MÉMO de symboles qu'on va rencontrer (à lire une fois) :
  "..."   = du texte, appelé "chaîne de caractères".
  \n      = UN caractère spécial : le "retour à la ligne" (comme la touche
            Entrée). À l'écran, il fait passer le texte à la ligne suivante.
  f"..."  = une chaîne "augmentée" : tout ce qui est entre { } sera remplacé
            par la valeur de la variable. Ex : f"Bonjour {prenom}".
  with ... as f:  = on ouvre une ressource (ici un fichier) et on la range
            dans une variable nommée f, le temps du bloc indenté en dessous.
────────────────────────────────────────────────────────────────────────
"""

# On importe l'outil 'Path' depuis la bibliothèque standard 'pathlib'.
# Path représente un CHEMIN de fichier ou de dossier, de façon qui marche
# aussi bien sur Windows que sur Mac/Linux.
from pathlib import Path

# Décodons la ligne suivante, morceau par morceau :
#   __file__              -> le chemin de CE fichier .py (Python le connaît tout seul)
#   Path(__file__)        -> on transforme ce chemin en objet Path manipulable
#   .parent               -> le DOSSIER qui contient ce fichier
#   / "exemples"          -> avec pathlib, le "/" colle un nom au chemin
#                            (ici : le sous-dossier "exemples")
dossier = Path(__file__).parent / "exemples"

# .mkdir() = "make directory" = créer le dossier.
#   exist_ok=True -> "ce n'est PAS une erreur s'il existe déjà" (sinon Python planterait).
dossier.mkdir(exist_ok=True)

# On construit le chemin complet du fichier dans lequel on va écrire.
fichier = dossier / "notes.txt"


# ─────────────────────────────────────────────
# 1. ÉCRIRE  ->  le mode "w" (write) ÉCRASE tout le contenu existant
# ─────────────────────────────────────────────
# Décodage de la ligne 'with open(...) as f:' :
#   open(fichier, "w", ...) -> ouvre le fichier en mode écriture
#       "w"  = write = écrire (efface l'ancien contenu)
#       encoding="utf-8" = jeu de caractères qui gère les accents et emojis
#   as f -> on appelle "f" le fichier ouvert, pour s'en servir dans le bloc
#   with -> garantit que le fichier sera bien REFERMÉ à la fin du bloc,
#           même en cas d'erreur (très pratique, on n'oublie jamais de fermer)
with open(fichier, "w", encoding="utf-8") as f:
    # f.write(...) écrit du texte dans le fichier.
    # Le \n à la fin fait que la ligne suivante ira... à la ligne suivante.
    f.write("Liste de courses\n")
    f.write("- Pain\n")
    f.write("- Café\n")
print(f"[+] Fichier écrit : {fichier}")


# ─────────────────────────────────────────────
# 2. AJOUTER  ->  le mode "a" (append) écrit À LA FIN sans rien effacer
# ─────────────────────────────────────────────
with open(fichier, "a", encoding="utf-8") as f:
    f.write("- Chocolat\n")
print("[+] Une ligne ajoutée à la fin.")


# ─────────────────────────────────────────────
# 3. LIRE  ->  le mode "r" (read = lire). C'est le mode par défaut.
# ─────────────────────────────────────────────
# 3a. Lire TOUT le contenu d'un coup avec .read() :
with open(fichier, "r", encoding="utf-8") as f:
    contenu = f.read()          # range tout le texte du fichier dans 'contenu'

# Le \n au début de "\n--- ..." ajoute une ligne vide AVANT le titre,
# juste pour aérer l'affichage à l'écran.
print("\n--- Contenu complet ---")
print(contenu)

# 3b. Lire LIGNE PAR LIGNE (idéal pour les gros fichiers : on ne charge pas tout).
print("--- Lecture ligne par ligne ---")
with open(fichier, "r", encoding="utf-8") as f:
    # enumerate(f, start=1) parcourt le fichier ligne par ligne ET, en même temps,
    # compte les tours de boucle. À chaque tour on récupère DEUX choses :
    #   - numero : le numéro de la ligne (start=1 dit "commence à compter à 1",
    #              au lieu de 0 par défaut),
    #   - ligne  : le texte de la ligne en cours.
    for numero, ligne in enumerate(f, start=1):
        # ligne.strip() nettoie la chaîne : il retire les espaces inutiles au
        # début/à la fin ET surtout le \n de fin de ligne (sinon on aurait une
        # ligne vide en trop à chaque print).
        print(f"Ligne {numero} : {ligne.strip()}")
