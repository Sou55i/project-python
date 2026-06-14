"""
MINI-PROJET - Suivi météo de plusieurs villes -> rapport CSV
============================================================
Ce script combine ce que tu as vu dans plusieurs modules :
  - module 03 : appeler une API web avec 'requests' (Open-Meteo, gratuite et
                SANS clé d'inscription) ;
  - modules 02 / 05 : écrire un fichier CSV avec le module 'csv'.

L'idée : pour CHAQUE ville d'une petite liste, on demande la météo actuelle,
puis on range tout dans un seul tableau et on l'enregistre en CSV.

Nécessite : une connexion Internet + la bibliothèque 'requests'
            (installe tout d'un coup avec :  pip install -r requirements.txt)

Lance-le :  python3 automatisation/projets/suivi_meteo.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : requests (parler au web), csv (écrire un tableau), Path (chemins).
   2. CONSTANTES : l'URL de l'API + la LISTE des villes (nom, latitude, longitude)
                   + le chemin du fichier CSV à produire.
   3. FONCTION meteo_d_une_ville() : demande la météo d'UNE ville à l'API.
   4. FONCTION ecrire_csv()        : enregistre la liste de résultats en CSV.
   5. PROGRAMME (__main__)         : parcourt les villes, collecte ce qui marche,
                                     puis écrit le rapport CSV.
"""

# ─────────────────────────────────────────────
# 1. IMPORTS
# ─────────────────────────────────────────────
# 'requests' est une bibliothèque TIERCE (installée via pip), pas de la stdlib.
import requests
# 'csv' fait partie de Python : pas besoin de l'installer.
import csv
# Path aide à construire des chemins de fichiers proprement.
from pathlib import Path


# ─────────────────────────────────────────────
# 2. CONSTANTES (des valeurs fixes, en MAJUSCULES par convention)
# ─────────────────────────────────────────────
# L'adresse (URL) de l'API météo.
URL = "https://api.open-meteo.com/v1/forecast"

# Notre liste de villes. C'est une LISTE [ ] de DICTIONNAIRES { }.
# Chaque dictionnaire décrit une ville : son nom + ses coordonnées GPS.
VILLES = [
    {"nom": "Paris", "latitude": 48.85, "longitude": 2.35},
    {"nom": "Lyon", "latitude": 45.76, "longitude": 4.83},
    {"nom": "Marseille", "latitude": 43.30, "longitude": 5.37},
]

# Où enregistrer le rapport ? Dans un sous-dossier "exemples" À CÔTÉ de ce script.
#   Path(__file__).parent = le dossier qui contient ce fichier .py
#   ... / "exemples" / "meteo.csv" = on descend dans "exemples", fichier "meteo.csv".
# Le dossier "exemples/" est ignoré par git (il est recréé à chaque exécution).
FICHIER_CSV = Path(__file__).parent / "exemples" / "meteo.csv"


# ─────────────────────────────────────────────
# 3. FONCTION : obtenir la météo d'UNE ville
# ─────────────────────────────────────────────
def meteo_d_une_ville(ville):
    """Demande à l'API la météo de 'ville' et renvoie un dictionnaire
    {ville, temperature, vent}."""
    # Les "paramètres" de la demande : requests va les coller à l'URL sous la forme
    #   ?latitude=48.85&longitude=2.35&current_weather=True
    parametres = {
        "latitude": ville["latitude"],
        "longitude": ville["longitude"],
        "current_weather": True,   # on veut la météo ACTUELLE
    }

    # requests.get(...) envoie une requête GET ("donne-moi des données").
    #   params=parametres -> ajoute nos paramètres à l'URL
    #   timeout=10        -> abandonne si le serveur ne répond pas en 10 secondes
    #                        (sinon le programme pourrait attendre pour toujours)
    reponse = requests.get(URL, params=parametres, timeout=10)

    # Le serveur renvoie un "code de statut" (200 = OK, 404 = introuvable, etc.).
    # .raise_for_status() déclenche une erreur claire si le code n'est PAS un succès.
    reponse.raise_for_status()

    # La réponse arrive en JSON (texte) ; .json() la convertit en dictionnaire Python.
    donnees = reponse.json()

    # On creuse dans le dictionnaire avec les crochets [ ] pour récupérer la météo.
    meteo = donnees["current_weather"]

    # On renvoie UNIQUEMENT ce qui nous intéresse, déjà rangé pour le CSV.
    return {
        "ville": ville["nom"],
        "temperature": meteo["temperature"],
        "vent": meteo["windspeed"],
    }


# ─────────────────────────────────────────────
# 4. FONCTION : écrire le rapport CSV
# ─────────────────────────────────────────────
def ecrire_csv(resultats):
    """Enregistre la liste 'resultats' (des dictionnaires) dans le fichier CSV."""
    # On s'assure que le dossier "exemples" existe (on le crée au besoin).
    #   parents=True   -> crée aussi les dossiers parents manquants
    #   exist_ok=True  -> pas d'erreur s'il existe déjà
    FICHIER_CSV.parent.mkdir(parents=True, exist_ok=True)

    # On ouvre le fichier en écriture.
    #   "w"        = mode write (écrase l'existant)
    #   newline="" = réglage recommandé pour le module csv (évite des lignes vides)
    with open(FICHIER_CSV, "w", newline="", encoding="utf-8") as f:
        colonnes = ["ville", "temperature", "vent"]
        # DictWriter sait écrire des dictionnaires en lignes de tableau.
        #   fieldnames=colonnes -> l'ordre et le nom des colonnes
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()          # écrit la 1re ligne d'en-tête : ville,temperature,vent
        writer.writerows(resultats)   # écrit toutes les lignes de données d'un coup

    print(f"[+] Rapport CSV écrit : {FICHIER_CSV}")


# ─────────────────────────────────────────────
# 5. PROGRAMME PRINCIPAL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # On prépare une liste vide : on y ajoutera la météo des villes qui réussissent.
    resultats = []

    # On parcourt CHAQUE ville de la liste, une par une.
    for ville in VILLES:
        # try / except : on "ESSAIE" le code risqué (le réseau peut échouer).
        #   - si tout va bien, on ajoute le résultat à notre liste,
        #   - si une erreur réseau survient, Python saute dans le bloc 'except',
        #     on affiche un message clair, et on CONTINUE avec la ville suivante
        #     (le script ne plante donc jamais, même sans Internet).
        try:
            meteo = meteo_d_une_ville(ville)
            resultats.append(meteo)   # .append() ajoute un élément à la fin de la liste
            print(f"☁️  {meteo['ville']} : {meteo['temperature']} °C, "
                  f"vent {meteo['vent']} km/h")
        except requests.RequestException as erreur:
            # 'as erreur' range les détails du problème dans la variable 'erreur'.
            print(f"❌ {ville['nom']} ignorée (problème de connexion) : {erreur}")

    # Après la boucle : on n'écrit le CSV que s'il y a au moins un résultat.
    if resultats:
        ecrire_csv(resultats)
    else:
        # Cas typique sans Internet : aucune ville n'a répondu.
        print("Aucune donnée récupérée : pas de rapport à écrire "
              "(as-tu une connexion Internet ?).")
