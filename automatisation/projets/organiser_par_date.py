"""
MINI-PROJET - Ranger des fichiers par MOIS de dernière modification
===================================================================
Le scénario : tu as un dossier rempli de fichiers créés à des moments
différents, et tu aimerais les classer proprement par période. Ce script
range chaque fichier dans un sous-dossier nommé d'après le mois de sa
dernière modification, au format AAAA-MM (par exemple "2026-06").

À la fin tu obtiens quelque chose comme :
    a_ranger/
        2026-04/   <- les fichiers modifiés en avril 2026
        2026-05/   <- ceux de mai 2026
        2026-06/   <- ceux de juin 2026

Il réutilise les notions du module 02 : pathlib (les chemins de fichiers),
les dossiers, et les dates.

Pour ne RIEN casser chez toi, le script crée d'abord un faux dossier de
DÉMO rempli de fichiers vides avec des dates de modification variées, PUIS
il les range. Tu peux donc le lancer sans aucun risque.

Lance-le :  python3 automatisation/projets/organiser_par_date.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS   : on charge Path (chemins de fichiers), datetime (les dates)
                  et time (pour fabriquer de fausses dates de modification).
   2. FONCTIONS : - preparer_dossier_de_demo() crée un faux dossier de démo
                    rempli de fichiers vides avec des dates variées,
                  - mois_de_modification() lit la date d'un fichier et renvoie
                    "AAAA-MM",
                  - organiser_par_date() range chaque fichier dans le
                    sous-dossier correspondant à son mois.
   3. PROGRAMME : le bloc __main__ prépare la démo PUIS appelle organiser().
   (Pour comprendre : commence par lire le bloc __main__ tout en bas.)
"""

# ─────────────────────────────────────────────
# 1. LES IMPORTS : on emprunte des outils à la "bibliothèque standard" de
#    Python (livrée d'office avec Python, donc RIEN à installer).
# ─────────────────────────────────────────────

# Path = l'outil moderne pour manipuler des chemins de fichiers/dossiers.
# Un "chemin", c'est l'adresse d'un fichier sur ton disque
# (ex : /home/toi/Documents/facture.pdf).
from pathlib import Path

# datetime = l'outil pour travailler avec les dates et les heures.
from datetime import datetime

# time = l'outil pour les mesures de temps. On ne s'en sert ICI que pour la
# démo : fabriquer artificiellement des fichiers "modifiés il y a X jours".
import time


# Décodage de la signature de la fonction :
#   base: Path  -> on indique que 'base' est censé être un chemin (Path).
#                  C'est une "annotation de type" : une aide à la lecture.
#   -> None     -> indique que la fonction ne RENVOIE rien (elle agit, c'est tout).
def preparer_dossier_de_demo(base: Path) -> None:
    """Crée un dossier de démo rempli de fichiers vides aux dates variées."""
    # parents=True   -> crée aussi les dossiers parents manquants si besoin.
    # exist_ok=True  -> ne plante PAS si le dossier existe déjà
    #                   (sans ça, relancer le script provoquerait une erreur).
    base.mkdir(parents=True, exist_ok=True)

    # Une liste de couples (nom_du_fichier, nombre_de_jours_dans_le_passé).
    # Exemple : ("photo.jpg", 70) = un fichier modifié il y a 70 jours.
    # Comme les dates s'étalent sur plusieurs mois, on verra apparaître
    # plusieurs sous-dossiers AAAA-MM différents à la fin.
    faux_fichiers = [
        ("rapport.txt", 5),       # modifié il y a 5 jours
        ("photo.jpg", 40),        # il y a ~1 mois et demi
        ("facture.pdf", 70),      # il y a ~2 mois
        ("notes.md", 100),        # il y a ~3 mois
        ("budget.csv", 5),        # tout récent, comme rapport.txt
        ("musique.mp3", 200),     # il y a ~6 mois
    ]

    # Le nombre de secondes dans une journée : 24h x 60min x 60s = 86400.
    # On s'en servira pour reculer les dates de N jours.
    secondes_par_jour = 24 * 60 * 60

    # time.time() = l'instant présent, exprimé en secondes (un grand nombre,
    # le "timestamp" : le nombre de secondes écoulées depuis le 1er janvier 1970).
    maintenant = time.time()

    for nom, jours_dans_le_passe in faux_fichiers:
        # (base / nom) construit le chemin complet du fichier dans le dossier.
        chemin = base / nom

        # .touch() crée un fichier VIDE (s'il n'existe pas déjà).
        chemin.touch()

        # On calcule l'instant "il y a N jours" : on part de maintenant et on
        # SOUSTRAIT N jours convertis en secondes.
        date_voulue = maintenant - (jours_dans_le_passe * secondes_par_jour)

        # os.utime via Path ? Non : on utilise directement le module os pour
        # changer la date du fichier. Mais pour rester simple ET sans import
        # supplémentaire visible, pathlib propose .touch() qui, hélas, met la
        # date à "maintenant". On force donc la date avec un petit outil :
        import os  # importé ici, juste pour la démo (changer la date d'un fichier)
        # os.utime(chemin, (date_acces, date_modification)) écrit deux dates
        # sur le fichier : la date du dernier accès et la date de dernière
        # modification. On met la même valeur pour les deux.
        os.utime(chemin, (date_voulue, date_voulue))

    print(f"[+] Dossier de démo prêt : {base}")


def mois_de_modification(fichier: Path) -> str:
    """Renvoie le mois de dernière modification du fichier, au format 'AAAA-MM'."""
    # .stat() = "statistiques" du fichier (taille, dates, etc.).
    # .st_mtime = "modification time" = la date de dernière modification,
    #             exprimée en secondes depuis 1970 (un nombre, le timestamp).
    timestamp = fichier.stat().st_mtime

    # datetime.fromtimestamp(...) TRADUIT ce nombre de secondes en une vraie
    # date lisible (année, mois, jour, heure...).
    date = datetime.fromtimestamp(timestamp)

    # .strftime("...") = "string format time" = transforme la date en TEXTE
    # selon un modèle. Ici :
    #   %Y = l'année sur 4 chiffres (ex : 2026)
    #   %m = le mois sur 2 chiffres (ex : 06)
    # Résultat : un texte comme "2026-06".
    return date.strftime("%Y-%m")


def organiser_par_date(dossier: Path) -> None:
    """Range chaque fichier dans un sous-dossier nommé d'après son mois (AAAA-MM)."""
    # .iterdir() = "itère sur le dossier" = parcourt chacun de ses éléments.
    for element in dossier.iterdir():
        # .is_dir() = "est-ce un dossier ?". On ne range que les FICHIERS.
        # Si c'est un dossier (par ex. un dossier "2026-06" déjà créé lors
        # d'un précédent passage), 'continue' saute au tour suivant.
        if element.is_dir():
            continue

        # On demande à notre fonction le mois du fichier, ex : "2026-06".
        nom_du_mois = mois_de_modification(element)

        # On construit le chemin du sous-dossier de destination.
        destination = dossier / nom_du_mois

        # On crée ce sous-dossier s'il n'existe pas encore.
        # exist_ok=True -> ne plante pas s'il existe déjà.
        destination.mkdir(exist_ok=True)

        # .rename(nouveau_chemin) = renommer/DÉPLACER le fichier (couper-coller).
        #   element.name = juste le nom du fichier (sans le chemin).
        element.rename(destination / element.name)
        print(f"[+] {element.name}  ->  {nom_du_mois}/")


# ─────────────────────────────────────────────
# 2. PROGRAMME PRINCIPAL.
# 'if __name__ == "__main__":' = "n'exécute ce bloc que si on LANCE ce fichier
# directement" (et pas si un autre fichier l'importe). Détaillé au module 04.
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Path(__file__) = le chemin de CE script.
    # .parent = le dossier qui le contient.
    # On place le dossier de démo dans "exemples/a_ranger", JUSTE À CÔTÉ du
    # script. Le dossier "exemples/" est ignoré par git : aucun risque de le
    # committer par accident.
    dossier_a_ranger = Path(__file__).parent / "exemples" / "a_ranger"

    # ⚠️ POUR L'UTILISER SUR UN VRAI DOSSIER :
    #    Remplace la ligne ci-dessus par le chemin de ton vrai dossier, ex :
    #        dossier_a_ranger = Path.home() / "Downloads"
    #    ET commente/supprime l'appel à preparer_dossier_de_demo() juste en
    #    dessous (sinon il ajouterait des fichiers de démo dans ton dossier).
    #    PRUDENCE : ce script DÉPLACE des fichiers. Teste-le d'abord sur une
    #    copie d'un petit dossier, jamais directement sur des fichiers
    #    importants tant que tu n'es pas à l'aise.

    preparer_dossier_de_demo(dossier_a_ranger)
    print("\n--- Rangement par mois en cours ---")
    organiser_par_date(dossier_a_ranger)
    print("\n✅ Terminé ! Ouvre 'exemples/a_ranger' pour voir les sous-dossiers AAAA-MM.")
