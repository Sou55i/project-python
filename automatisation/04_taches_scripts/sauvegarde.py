"""
MODULE 04 - Un outil de sauvegarde configurable
================================================
Cet outil copie le contenu d'un dossier "source" dans un dossier "destination",
en ajoutant la date au nom (sauvegarde horodatée). Il accepte des OPTIONS en
ligne de commande grâce à argparse.

Exemples :
    python3 automatisation/04_taches_scripts/sauvegarde.py --help
    python3 automatisation/04_taches_scripts/sauvegarde.py
    python3 automatisation/04_taches_scripts/sauvegarde.py --source mes_docs

Concepts : argparse, logging, pathlib, shutil, et le bloc __main__.

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : argparse, logging, shutil, datetime, pathlib.
   2. CONFIG     : on règle l'affichage des logs (messages horodatés).
   3. FONCTIONS  : - preparer_demo()  crée un dossier source de démo,
                   - sauvegarder()    copie la source dans un dossier daté,
                   - lire_options()   lit les options --source / --destination.
   4. PROGRAMME  : le bloc __main__ lit les options PUIS lance la sauvegarde.
"""

import argparse                    # gérer les options de la ligne de commande
import logging                     # afficher des messages horodatés (journaux)
import shutil                      # copier des dossiers entiers
from datetime import datetime      # connaître la date et l'heure actuelles
from pathlib import Path

# On configure le système de logs UNE fois pour tout le script.
#   level=logging.INFO -> on affiche les messages d'info et plus graves
#   format="..."       -> la forme de chaque ligne :
#       %(asctime)s  = la date et l'heure
#       %(levelname)s= le niveau (INFO, ERROR...)
#       %(message)s  = ton message
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def preparer_demo(source: Path) -> None:
    """Crée un petit dossier source avec quelques fichiers, pour la démo."""
    source.mkdir(parents=True, exist_ok=True)
    # .write_text("...") crée le fichier et y écrit directement le texte donné.
    (source / "rapport.txt").write_text("Contenu du rapport", encoding="utf-8")
    (source / "notes.txt").write_text("Mes notes", encoding="utf-8")


def sauvegarder(source: Path, destination: Path) -> None:
    """Copie 'source' dans un sous-dossier horodaté de 'destination'."""
    # 'not source.exists()' = "si la source N'existe PAS". Le 'not' inverse le test.
    if not source.exists():
        # logging.error(...) signale un problème. Le %s sera remplacé par 'source'.
        logging.error("Le dossier source n'existe pas : %s", source)
        return                     # 'return' sans valeur : on arrête la fonction ici

    # datetime.now() = l'instant présent. .strftime(...) le met en TEXTE selon un format :
    #   %Y = année (4 chiffres), %m = mois, %d = jour, %H = heure, %M = minute, %S = seconde
    # Résultat : "2026-06-13_14-30-00"
    horodatage = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # On construit le nom du dossier de sauvegarde avec une f-string.
    cible = destination / f"sauvegarde_{horodatage}"

    # shutil.copytree(source, cible) COPIE tout un dossier (et son contenu) d'un coup.
    shutil.copytree(source, cible)
    logging.info("Sauvegarde réussie : %s -> %s", source, cible)


def lire_options():
    """Définit et lit les arguments (options) tapés sur la ligne de commande."""
    # On crée un "analyseur d'arguments". Le description s'affiche avec --help.
    parseur = argparse.ArgumentParser(description="Sauvegarde horodatée d'un dossier.")
    # .add_argument("--source", ...) déclare une option nommée --source.
    #   default=...  -> la valeur utilisée si l'utilisateur ne précise rien
    #   help=...     -> le texte d'aide affiché par --help
    parseur.add_argument("--source", default="exemples/source",
                         help="Dossier à sauvegarder (défaut : exemples/source)")
    parseur.add_argument("--destination", default="exemples/sauvegardes",
                         help="Dossier où ranger les sauvegardes")
    # .parse_args() lit réellement ce que l'utilisateur a tapé et le renvoie.
    return parseur.parse_args()


# ─────────────────────────────────────────────
# Le bloc ci-dessous ne s'exécute QUE si on lance ce fichier directement
# (python3 sauvegarde.py), et PAS si un autre fichier fait 'import sauvegarde'.
#   __name__ est une variable spéciale de Python. Elle vaut "__main__"
#   uniquement quand le fichier est le programme lancé directement.
# ─────────────────────────────────────────────
if __name__ == "__main__":
    args = lire_options()          # on récupère les options ; args.source, args.destination

    # Les chemins sont calculés à partir de l'emplacement de ce script.
    base = Path(__file__).parent
    source = base / args.source
    destination = base / args.destination

    preparer_demo(source)          # (pour la démo seulement)
    sauvegarder(source, destination)
