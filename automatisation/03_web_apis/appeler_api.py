"""
MODULE 03 - Appeler une API
===========================
On interroge une vraie API météo gratuite et SANS clé d'inscription :
Open-Meteo (https://open-meteo.com). On lui demande la météo de Paris.

Nécessite : une connexion Internet + la bibliothèque 'requests'
            (pip install -r requirements.txt)

Lance-le :  python3 automatisation/03_web_apis/appeler_api.py
"""

import requests

# ─────────────────────────────────────────────
# 1. L'URL de l'API + les "paramètres" de notre demande.
#    requests ajoute proprement ces paramètres à l'URL (?latitude=...&longitude=...).
# ─────────────────────────────────────────────
URL = "https://api.open-meteo.com/v1/forecast"
parametres = {
    "latitude": 48.85,        # Paris
    "longitude": 2.35,
    "current_weather": True,  # on veut la météo actuelle
}


def obtenir_meteo():
    """Appelle l'API et renvoie les données météo actuelles (un dictionnaire)."""
    # timeout=10 : on abandonne si le serveur n'a pas répondu en 10 secondes.
    reponse = requests.get(URL, params=parametres, timeout=10)

    # raise_for_status() déclenche une erreur claire si le code n'est pas 2xx.
    reponse.raise_for_status()

    # .json() transforme la réponse JSON en dictionnaire Python.
    return reponse.json()


# ─────────────────────────────────────────────
# Programme principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # try / except : on "essaie" le code, et si une erreur réseau survient,
    # on l'attrape pour afficher un message propre au lieu de planter.
    try:
        donnees = obtenir_meteo()
        meteo = donnees["current_weather"]   # on creuse dans le dictionnaire

        print("☁️  Météo actuelle à Paris")
        print(f"  Température : {meteo['temperature']} °C")
        print(f"  Vent        : {meteo['windspeed']} km/h")
    except requests.RequestException as erreur:
        print(f"❌ Problème de connexion à l'API : {erreur}")
