"""
MODULE 02 - Mini-projet : ranger automatiquement un dossier
===========================================================
Le scénario classique : un dossier "Téléchargements" en bazar, plein de
fichiers de toutes sortes. Ce script les TRIE dans des sous-dossiers selon
leur extension (.pdf -> Documents/, .jpg -> Images/, etc.).

Pour ne RIEN casser chez toi, le script crée d'abord un faux dossier de test
rempli de fichiers vides, puis le range. Adapte ensuite 'dossier_a_ranger'
vers ton vrai dossier quand tu te sens prêt.

Lance-le :  python3 python/automatisation/02_fichiers_dossiers/ranger_dossier.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS      : on charge l'outil Path (gestion des chemins de fichiers).
   2. CONSTANTE    : RANGEMENT, le tableau qui associe une extension -> un dossier.
   3. FONCTIONS    : - preparer_dossier_de_test() crée un faux dossier de démo,
                     - ranger() parcourt les fichiers et les déplace au bon endroit.
   4. PROGRAMME    : le bloc __main__ prépare la démo PUIS appelle ranger().
   (Pour comprendre : commence par lire le bloc __main__ tout en bas.)
"""

from pathlib import Path

# ─────────────────────────────────────────────
# 1. Un dictionnaire qui associe chaque extension à un dossier de destination.
#    Clé = l'extension du fichier (avec le point) ; valeur = le nom du dossier cible.
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


# Décodage de la signature de la fonction :
#   base: Path   -> on indique que 'base' est censé être un chemin (Path).
#                   C'est une "annotation de type" : une aide à la lecture, optionnelle.
#   -> None      -> indique que la fonction ne RENVOIE rien (elle agit, c'est tout).
def preparer_dossier_de_test(base: Path) -> None:
    """Crée un dossier 'bazar' rempli de fichiers vides pour la démo."""
    # parents=True -> crée aussi les dossiers parents manquants si besoin.
    base.mkdir(parents=True, exist_ok=True)
    faux_fichiers = [
        "facture.pdf", "photo_vacances.jpg", "notes.txt",
        "budget.csv", "musique.mp3", "logo.png", "archive.zip",
        "fichier_inconnu.xyz",          # extension non prévue : on le laissera tranquille
    ]
    for nom in faux_fichiers:
        # (base / nom) construit le chemin complet ; .touch() crée un fichier VIDE.
        (base / nom).touch()
    print(f"[+] Dossier de test prêt : {base}")


def ranger(dossier: Path) -> None:
    """Déplace chaque fichier du dossier dans le sous-dossier qui lui correspond."""
    # .iterdir() = "itère sur le dossier" = parcourt chacun de ses éléments.
    for element in dossier.iterdir():
        # .is_dir() = "est-ce un dossier ?". On ne range que les FICHIERS,
        # donc si c'est un dossier, 'continue' saute directement au tour suivant.
        if element.is_dir():
            continue

        # .suffix = l'extension du fichier (ex : ".JPG"). .lower() la met en
        # minuscules pour que ".JPG" et ".jpg" soient traités pareil.
        extension = element.suffix.lower()

        # .get(cle) cherche la clé dans le dictionnaire. S'il ne la trouve pas,
        # il renvoie None (au lieu de planter). Ici None = extension non prévue.
        destination_nom = RANGEMENT.get(extension)

        if destination_nom is None:
            print(f"[ ] Ignoré (extension inconnue) : {element.name}")
            continue

        # On crée le sous-dossier de destination s'il n'existe pas encore.
        destination = dossier / destination_nom
        destination.mkdir(exist_ok=True)

        # .rename(nouveau_chemin) = renommer/DÉPLACER le fichier (couper-coller).
        #   element.name = juste le nom du fichier (sans le chemin).
        element.rename(destination / element.name)
        print(f"[+] {element.name}  ->  {destination_nom}/")


# ─────────────────────────────────────────────
# Programme principal.
# 'if __name__ == "__main__":' = "n'exécute ce bloc que si on LANCE ce fichier
# directement" (et pas si un autre fichier l'importe). Détaillé au module 04.
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Ce dossier de test est créé à côté du script.
    dossier_a_ranger = Path(__file__).parent / "exemples" / "bazar"

    preparer_dossier_de_test(dossier_a_ranger)
    print("\n--- Rangement en cours ---")
    ranger(dossier_a_ranger)
    print("\n✅ Terminé ! Ouvre le dossier 'exemples/bazar' pour voir le résultat.")
