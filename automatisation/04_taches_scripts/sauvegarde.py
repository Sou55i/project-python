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
"""

import argparse
import logging
import shutil
from datetime import datetime
from pathlib import Path

# On configure les logs : chaque message sera horodaté.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def preparer_demo(source: Path) -> None:
    """Crée un petit dossier source avec quelques fichiers, pour la démo."""
    source.mkdir(parents=True, exist_ok=True)
    (source / "rapport.txt").write_text("Contenu du rapport", encoding="utf-8")
    (source / "notes.txt").write_text("Mes notes", encoding="utf-8")


def sauvegarder(source: Path, destination: Path) -> None:
    """Copie 'source' dans un sous-dossier horodaté de 'destination'."""
    if not source.exists():
        logging.error("Le dossier source n'existe pas : %s", source)
        return

    # Nom de sauvegarde avec date + heure, ex : sauvegarde_2026-06-13_14-30-00
    horodatage = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    cible = destination / f"sauvegarde_{horodatage}"

    # shutil.copytree copie tout un dossier (et son contenu) d'un coup.
    shutil.copytree(source, cible)
    logging.info("Sauvegarde réussie : %s -> %s", source, cible)


def lire_options():
    """Définit et lit les arguments de la ligne de commande."""
    parseur = argparse.ArgumentParser(description="Sauvegarde horodatée d'un dossier.")
    parseur.add_argument("--source", default="exemples/source",
                         help="Dossier à sauvegarder (défaut : exemples/source)")
    parseur.add_argument("--destination", default="exemples/sauvegardes",
                         help="Dossier où ranger les sauvegardes")
    return parseur.parse_args()


# ─────────────────────────────────────────────
# Ce bloc ne s'exécute que si on LANCE ce fichier directement.
# ─────────────────────────────────────────────
if __name__ == "__main__":
    args = lire_options()

    # Les chemins sont relatifs à l'emplacement de ce script (pratique pour la démo).
    base = Path(__file__).parent
    source = base / args.source
    destination = base / args.destination

    preparer_demo(source)           # (pour la démo seulement)
    sauvegarder(source, destination)
