"""
MODULE 15 - Construire un script : COMPTER LES FICHIERS D'UN DOSSIER
===================================================================
Ce script est l'aboutissement du raisonnement détaillé dans
../ECRIRE_UN_SCRIPT.md (exemple n°1). Il est commenté pas à pas pour que tu
voies POURQUOI chaque morceau est là, pas seulement COMMENT.

Lance-le :
    python3 python/15_construire_un_script/compter_fichiers.py
    python3 python/15_construire_un_script/compter_fichiers.py /tmp
    python3 python/15_construire_un_script/compter_fichiers.py . --recursif

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : argparse (lire les arguments) + pathlib (les fichiers).
   2. FONCTION   : compter(dossier, recursif) renvoie le nombre de fichiers.
   3. ARGUMENTS  : on déclare un argument 'dossier' (optionnel, défaut ".")
                   et une option '--recursif'.
   4. PROGRAMME  : (a) lire les arguments, (b) appeler compter(), (c) afficher.
"""

# (1) On part du BESOIN, et le besoin dicte les outils :
#   - "lire un argument au lancement"  -> module argparse
#   - "parcourir des fichiers/dossiers" -> module pathlib (Path)
import argparse
from pathlib import Path


# (2) Une fonction = une idée nommée et réutilisable.
#     Décodage de la signature :
#       dossier: Path   -> on lui donne un chemin (annotation de type = aide à la lecture)
#       recursif: bool = False -> option ; par défaut on NE descend PAS dans les sous-dossiers
#       -> int          -> la fonction RENVOIE un entier (le compte)
def compter(dossier: Path, recursif: bool = False) -> int:
    """Compte les fichiers (pas les dossiers) contenus dans 'dossier'."""

    # Comment choisir entre "juste ce dossier" et "tout en profondeur" ?
    #   - .iterdir()    -> seulement le 1er niveau du dossier
    #   - .rglob("*")   -> récursif : TOUT, à toutes les profondeurs
    # On a découvert ces deux méthodes avec dir(Path) / help(Path.iterdir).
    elements = dossier.rglob("*") if recursif else dossier.iterdir()

    # Pour chaque élément, on ne garde que les VRAIS fichiers (.is_file()),
    # pas les sous-dossiers. sum(1 for ...) compte les éléments qui passent le filtre.
    return sum(1 for element in elements if element.is_file())


# (3) On déclare ce que le script accepte en ligne de commande.
#     C'est CETTE étape qui répond à ta question "comment trouver les arguments".
def lire_arguments():
    parseur = argparse.ArgumentParser(description="Compter les fichiers d'un dossier.")
    # Argument POSITIONNEL avec une valeur par défaut : si l'utilisateur ne donne rien,
    # on examine le dossier courant ".".
    parseur.add_argument("dossier", nargs="?", default=".",
                         help="dossier à examiner (défaut : le dossier courant)")
    # Option (drapeau) : présente -> True, absente -> False.
    parseur.add_argument("--recursif", action="store_true",
                         help="compter aussi dans les sous-dossiers")
    return parseur.parse_args()


# (4) Le "chef d'orchestre" : il ne s'exécute QUE si on lance CE fichier
#     directement (et pas si on l'importe). Voir ../COMPRENDRE_LE_CODE.md §3.1.
if __name__ == "__main__":
    args = lire_arguments()               # (a) lire les arguments
    chemin = Path(args.dossier)           # transformer le texte en objet Path

    # On vérifie que le dossier existe VRAIMENT (sinon message clair, pas de plantage).
    if not chemin.is_dir():
        print(f"❌ '{args.dossier}' n'est pas un dossier valide.")
    else:
        total = compter(chemin, args.recursif)   # (b) calculer
        portee = "récursif" if args.recursif else "1er niveau"
        print(f"📁 {total} fichier(s) dans '{args.dossier}' ({portee})")   # (c) afficher
