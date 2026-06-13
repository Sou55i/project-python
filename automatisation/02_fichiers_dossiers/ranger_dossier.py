"""
MODULE 02 - Mini-projet : ranger automatiquement un dossier
===========================================================
Le scénario classique : un dossier "Téléchargements" en bazar, plein de
fichiers de toutes sortes. Ce script les TRIE dans des sous-dossiers selon
leur extension (.pdf -> PDF/, .jpg -> Images/, etc.).

Pour ne RIEN casser chez toi, le script crée d'abord un faux dossier de test
rempli de fichiers vides, puis le range. Adapte ensuite 'dossier_a_ranger'
vers ton vrai dossier quand tu te sens prêt.

Lance-le :  python3 automatisation/02_fichiers_dossiers/ranger_dossier.py
"""

from pathlib import Path

# ─────────────────────────────────────────────
# 1. On associe chaque extension à un dossier de destination.
#    (Un dictionnaire : la clé = l'extension, la valeur = le nom du dossier.)
# ─────────────────────────────────────────────
RANGEMENT = {
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".csv": "Tableaux",
    ".xlsx": "Tableaux",
    ".mp3": "Audio",
    ".zip": "Archives",
}


def preparer_dossier_de_test(base: Path) -> None:
    """Crée un dossier 'bazar' rempli de fichiers vides pour la démo."""
    base.mkdir(parents=True, exist_ok=True)
    faux_fichiers = [
        "facture.pdf", "photo_vacances.jpg", "notes.txt",
        "budget.csv", "musique.mp3", "logo.png", "archive.zip",
        "fichier_inconnu.xyz",          # extension non prévue : on le laissera tranquille
    ]
    for nom in faux_fichiers:
        (base / nom).touch()            # .touch() crée un fichier vide
    print(f"[+] Dossier de test prêt : {base}")


def ranger(dossier: Path) -> None:
    """Déplace chaque fichier du dossier dans le sous-dossier qui lui correspond."""
    for element in dossier.iterdir():
        # On ignore les sous-dossiers : on ne range que les FICHIERS.
        if element.is_dir():
            continue

        extension = element.suffix.lower()        # ".JPG" -> ".jpg"
        destination_nom = RANGEMENT.get(extension)  # None si extension inconnue

        if destination_nom is None:
            print(f"[ ] Ignoré (extension inconnue) : {element.name}")
            continue

        # On crée le sous-dossier de destination s'il n'existe pas encore.
        destination = dossier / destination_nom
        destination.mkdir(exist_ok=True)

        # On déplace le fichier. .rename() = couper/coller.
        element.rename(destination / element.name)
        print(f"[+] {element.name}  ->  {destination_nom}/")


# ─────────────────────────────────────────────
# Programme principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Ce dossier de test est créé à côté du script.
    dossier_a_ranger = Path(__file__).parent / "exemples" / "bazar"

    preparer_dossier_de_test(dossier_a_ranger)
    print("\n--- Rangement en cours ---")
    ranger(dossier_a_ranger)
    print("\n✅ Terminé ! Ouvre le dossier 'exemples/bazar' pour voir le résultat.")
