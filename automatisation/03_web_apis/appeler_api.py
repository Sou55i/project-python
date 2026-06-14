"""
MODULE 03 - Appeler une API
===========================
On interroge une vraie API météo gratuite et SANS clé d'inscription :
Open-Meteo (https://open-meteo.com). On lui demande la météo de Paris.

Nécessite : une connexion Internet + la bibliothèque 'requests'
            (pip install -r requirements.txt)

Lance-le :  python3 automatisation/03_web_apis/appeler_api.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : la bibliothèque requests (pour parler au web).
   2. CONSTANTES : l'URL de l'API + les paramètres de la demande (latitude...).
   3. FONCTION   : obtenir_meteo() envoie la requête, vérifie la réponse,
                   et renvoie les données (converties en dictionnaire).
   4. PROGRAMME  : le bloc __main__ appelle la fonction (dans un try/except
                   au cas où le réseau échoue) PUIS affiche le résultat.
"""

# 'requests' est une bibliothèque TIERCE (installée via pip), pas de la stdlib.
import requests

# ─────────────────────────────────────────────
# 1. L'URL (l'adresse) de l'API + les "paramètres" de notre demande.
# ─────────────────────────────────────────────
URL = "https://api.open-meteo.com/v1/forecast"

# Un dictionnaire de paramètres. requests va les coller proprement à la fin de
# l'URL, sous la forme  ?latitude=48.85&longitude=2.35&current_weather=True
parametres = {
    "latitude": 48.85,        # coordonnées de Paris
    "longitude": 2.35,
    "current_weather": True,  # on demande la météo ACTUELLE
}


def obtenir_meteo():
    """Appelle l'API et renvoie les données météo actuelles (un dictionnaire)."""
    # requests.get(...) envoie une requête de type GET ("donne-moi des données").
    #   params=parametres -> ajoute nos paramètres à l'URL
    #   timeout=10        -> abandonne si le serveur ne répond pas en 10 secondes
    #                        (sinon le programme pourrait attendre pour toujours)
    reponse = requests.get(URL, params=parametres, timeout=10)

    # Le serveur renvoie un "code de statut" (200 = OK, 404 = introuvable, etc.).
    # .raise_for_status() déclenche une erreur claire si le code n'est PAS un succès.
    reponse.raise_for_status()

    # La réponse arrive au format JSON (texte). .json() le convertit
    # automatiquement en dictionnaire Python, qu'on peut fouiller.
    return reponse.json()


# ─────────────────────────────────────────────
# Programme principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # try / except : on "ESSAIE" le code risqué (le réseau peut échouer).
    #   - si tout va bien, le bloc 'try' s'exécute normalement,
    #   - si une erreur réseau survient, Python saute dans le bloc 'except'
    #     au lieu de planter avec un message effrayant.
    try:
        donnees = obtenir_meteo()
        # donnees est un dictionnaire ; on creuse dedans avec les crochets [ ].
        meteo = donnees["current_weather"]

        print("☁️  Météo actuelle à Paris")
        print(f"  Température : {meteo['temperature']} °C")
        print(f"  Vent        : {meteo['windspeed']} km/h")
    except requests.RequestException as erreur:
        # 'as erreur' range les détails du problème dans la variable 'erreur'.
        print(f"❌ Problème de connexion à l'API : {erreur}")
