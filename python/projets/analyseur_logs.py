"""
MINI-PROJET - Analyseur de fichiers de logs -> rapport d'activité
=================================================================
Le scénario : un programme qui tourne (un serveur, un script de nuit...) écrit
au fur et à mesure un "journal" (en anglais *log*) : une ligne par événement.
Au bout d'un moment, ce fichier fait des milliers de lignes et devient illisible.
Ce script le LIT à ta place et en sort un RÉSUMÉ clair : combien d'INFO, de
WARNING, d'ERROR, quelles sont les erreurs les plus fréquentes, sur quelle
période, etc.

C'est l'un des scripts les plus utiles du monde réel : tout le monde a, un jour,
besoin de "fouiller des logs".

Il réutilise plein de notions du cours :
   - module 01 : les boucles et les conditions ;
   - module 02 : les dictionnaires et la classe Counter (compter des choses) ;
   - module 04 : lire un fichier ligne par ligne, gérer les erreurs ;
   - module 12 : le format de log "date - NIVEAU - message" (logging).

Pour ne RIEN exiger de toi (pas de fichier à fournir, pas d'Internet), le script
fabrique d'abord un faux fichier de logs de DÉMO, PUIS il l'analyse. Tu peux
donc le lancer tel quel.

Lance-le :  python3 python/projets/analyseur_logs.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : Counter (compter), Path (chemins), datetime (les dates), random.
   2. CONSTANTES : où ranger le fichier de logs de démo.
   3. preparer_logs_de_demo() : crée un faux journal réaliste.
   4. analyser()  : LE CŒUR — lit le fichier, décode chaque ligne, accumule les stats.
   5. afficher_rapport() : met en forme les stats en un rapport lisible.
   6. PROGRAMME (__main__) : prépare la démo, analyse, affiche.
   (Pour comprendre : commence par lire le bloc __main__ tout en bas.)
"""

# ─────────────────────────────────────────────
# 1. LES IMPORTS (tout vient de la bibliothèque standard : RIEN à installer)
# ─────────────────────────────────────────────

# Counter = un dictionnaire spécialisé dans le COMPTAGE. On lui donne une liste
# d'éléments, il compte combien de fois chacun apparaît. Parfait pour les niveaux.
from collections import Counter

# Path = pour manipuler les chemins de fichiers proprement.
from pathlib import Path

# datetime = pour transformer le texte d'une date ("2026-06-19 08:23:01") en
# vraie date manipulable, et calculer une durée.
from datetime import datetime

# random = uniquement pour fabriquer un faux journal varié (la démo).
import random


# ─────────────────────────────────────────────
# 2. CONSTANTES
# ─────────────────────────────────────────────
# Le fichier de logs de démo, rangé dans "exemples/" À CÔTÉ de ce script.
# (Le dossier exemples/ est ignoré par git : il est recréé à chaque exécution.)
FICHIER_LOG = Path(__file__).parent / "exemples" / "app.log"

# Le format des dates utilisé dans nos logs. Ces codes %... sont expliqués plus
# bas (voir analyser). C'est le MÊME modèle pour écrire et pour relire la date.
FORMAT_DATE = "%Y-%m-%d %H:%M:%S"


# ─────────────────────────────────────────────
# 3. PRÉPARER UN FAUX JOURNAL (pour pouvoir lancer le script sans rien fournir)
# ─────────────────────────────────────────────
def preparer_logs_de_demo(chemin: Path) -> None:
    """Écrit un faux fichier de logs réaliste, avec des niveaux variés."""
    # On crée le dossier "exemples" s'il n'existe pas (voir module 12 pour mkdir).
    chemin.parent.mkdir(parents=True, exist_ok=True)

    # Des messages possibles, rangés par niveau. C'est un dictionnaire dont les
    # valeurs sont des LISTES de messages.
    messages = {
        "INFO": [
            "Démarrage de l'application",
            "Utilisateur connecté",
            "Requête traitée avec succès",
            "Sauvegarde terminée",
        ],
        "WARNING": [
            "Mémoire disponible faible",
            "Réponse lente de la base de données",
            "Certificat bientôt expiré",
        ],
        "ERROR": [
            "Connexion à la base de données échouée",
            "Fichier de configuration introuvable",
            "Connexion à la base de données échouée",  # volontairement en double
            "Délai dépassé sur l'API externe",
        ],
    }

    # On va écrire 40 lignes. random.choices permet de tirer un niveau au hasard,
    # mais avec des POIDS : beaucoup d'INFO, un peu de WARNING, quelques ERROR
    # (comme dans un vrai log en bonne santé).
    niveaux = list(messages.keys())                 # ["INFO", "WARNING", "ERROR"]
    poids = [70, 20, 10]                             # 70% INFO, 20% WARNING, 10% ERROR

    # heure de départ fictive ; chaque ligne avancera de quelques secondes.
    instant = datetime(2026, 6, 19, 8, 0, 0)

    with open(chemin, "w", encoding="utf-8") as f:
        for _ in range(40):                          # "_" = variable dont on se fiche
            # random.choices(..., weights=..., k=1) renvoie une LISTE d'1 élément ;
            # le [0] récupère cet unique élément.
            niveau = random.choices(niveaux, weights=poids, k=1)[0]
            message = random.choice(messages[niveau])

            # On avance l'horloge de 1 à 90 secondes au hasard.
            secondes = random.randint(1, 90)
            instant = instant.fromtimestamp(instant.timestamp() + secondes)

            # .strftime(FORMAT_DATE) transforme la date en texte "2026-06-19 08:00:42".
            date_texte = instant.strftime(FORMAT_DATE)

            # On écrit la ligne au format "date - NIVEAU - message".
            f.write(f"{date_texte} - {niveau} - {message}\n")

    print(f"[+] Journal de démo créé : {chemin} (40 lignes)")


# ─────────────────────────────────────────────
# 4. LE CŒUR : analyser le fichier de logs
# ─────────────────────────────────────────────
def analyser(chemin: Path) -> dict:
    """Lit le fichier ligne par ligne et renvoie un dictionnaire de statistiques :
    {
      "total":        nombre de lignes valides,
      "par_niveau":   Counter {"INFO": .., "WARNING": .., "ERROR": ..},
      "erreurs":      Counter {message d'erreur: nombre d'occurrences},
      "premiere":     datetime de la 1re ligne,
      "derniere":     datetime de la dernière ligne,
      "ignorees":     nombre de lignes mal formées qu'on a sautées,
    }
    """
    # Counter() part à zéro et compte au fur et à mesure qu'on lui ajoute des clés.
    par_niveau = Counter()
    erreurs = Counter()

    dates = []          # on collectera ici toutes les dates, pour trouver min et max
    total = 0
    ignorees = 0

    # On entoure la lecture d'un try/except : si le fichier n'existe pas, on
    # renvoie des stats vides au lieu de planter (patron vu au module 04).
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:                  # parcours ligne par ligne (économe en mémoire)
                ligne = ligne.strip()        # enlève les espaces et le \n des deux bouts
                if not ligne:                # "si la ligne est vide" → on saute
                    continue

                # Chaque ligne vaut "date - NIVEAU - message".
                # .split(" - ", 2) DÉCOUPE sur " - ", au MAXIMUM 2 fois : on obtient
                # donc exactement 3 morceaux, même si le message contient lui-même
                # un " - ". Le "2" est la limite de découpages.
                morceaux = ligne.split(" - ", 2)

                # Si on n'a pas 3 morceaux, la ligne est mal formée : on l'ignore.
                if len(morceaux) != 3:
                    ignorees += 1
                    continue

                date_texte, niveau, message = morceaux   # affectation multiple (module 02)

                total += 1
                par_niveau[niveau] += 1      # ajoute 1 au compteur de ce niveau

                # On accumule les messages d'ERROR pour repérer les plus fréquents.
                if niveau == "ERROR":
                    erreurs[message] += 1

                # On tente de relire la date. datetime.strptime = "string parse time" :
                # l'INVERSE de strftime — il LIT un texte selon le modèle FORMAT_DATE
                # et renvoie une vraie date. Si le texte ne colle pas, ça lève une
                # ValueError, qu'on attrape pour ne pas planter sur une ligne bizarre.
                try:
                    dates.append(datetime.strptime(date_texte, FORMAT_DATE))
                except ValueError:
                    pass
    except FileNotFoundError:
        # Le fichier n'existe pas : on renvoie un rapport "vide" cohérent.
        return {"total": 0, "par_niveau": Counter(), "erreurs": Counter(),
                "premiere": None, "derniere": None, "ignorees": 0}

    return {
        "total": total,
        "par_niveau": par_niveau,
        "erreurs": erreurs,
        # min(dates)/max(dates) donnent la 1re et la dernière date — mais seulement
        # si la liste n'est pas vide (sinon min() planterait). D'où le "if dates".
        "premiere": min(dates) if dates else None,
        "derniere": max(dates) if dates else None,
        "ignorees": ignorees,
    }


# ─────────────────────────────────────────────
# 5. METTRE EN FORME LE RAPPORT
# ─────────────────────────────────────────────
def afficher_rapport(stats: dict) -> None:
    """Affiche joliment les statistiques calculées par analyser()."""
    if stats["total"] == 0:
        print("Aucune ligne de log valide à analyser.")
        return

    print("\n" + "=" * 50)
    print("  RAPPORT D'ANALYSE DES LOGS")
    print("=" * 50)

    print(f"Lignes analysées : {stats['total']}")
    if stats["ignorees"]:
        print(f"Lignes ignorées (mal formées) : {stats['ignorees']}")

    # Période couverte par le journal.
    if stats["premiere"] and stats["derniere"]:
        duree = stats["derniere"] - stats["premiere"]   # soustraire 2 dates → une durée
        print(f"Période : du {stats['premiere']} au {stats['derniere']}")
        print(f"Durée couverte : {duree}")

    # Répartition par niveau, du plus fréquent au moins fréquent.
    print("\nRépartition par niveau :")
    # .most_common() d'un Counter renvoie les paires (clé, nombre) triées du plus
    # grand au plus petit. Très pratique pour un classement.
    for niveau, nombre in stats["par_niveau"].most_common():
        # On calcule le pourcentage. :>3 aligne le nombre sur 3 caractères,
        # :5.1f affiche le pourcentage avec 1 décimale.
        pourcent = nombre / stats["total"] * 100
        print(f"  {niveau:<8} : {nombre:>3}  ({pourcent:5.1f} %)")

    # Top des erreurs (le plus utile au quotidien).
    if stats["erreurs"]:
        print("\nErreurs les plus fréquentes :")
        for message, nombre in stats["erreurs"].most_common(3):   # les 3 premières
            print(f"  {nombre}× {message}")
    else:
        print("\nAucune erreur 🎉")

    print("=" * 50)


# ─────────────────────────────────────────────
# 6. PROGRAMME PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ⚠️ POUR L'UTILISER SUR UN VRAI FICHIER :
    #    Remplace la ligne FICHIER_LOG en haut par le chemin de ton vrai .log,
    #    et SUPPRIME l'appel à preparer_logs_de_demo() juste en dessous.
    preparer_logs_de_demo(FICHIER_LOG)

    stats = analyser(FICHIER_LOG)
    afficher_rapport(stats)
