"""
MODULE 03 - Web scraping
========================
Quand un site n'a pas d'API, on lit directement son HTML pour en extraire
des infos. On utilise ici 'example.com', un site public prévu pour les tests.

Nécessite : connexion Internet + 'requests' et 'beautifulsoup4'
            (pip install -r requirements.txt)

Lance-le :  python3 automatisation/03_web_apis/scraping.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : requests (télécharger) + BeautifulSoup (analyser le HTML).
   2. CONSTANTE  : l'URL de la page à analyser.
   3. FONCTION   : scraper() télécharge la page, l'analyse, et extrait
                   le titre et les paragraphes.
   4. PROGRAMME  : le bloc __main__ appelle la fonction (dans un try/except)
                   PUIS affiche ce qui a été extrait.
"""

import requests
# Décodage : 'from bs4 import BeautifulSoup' veut dire :
#   dans la bibliothèque 'bs4' (le nom de code de beautifulsoup4),
#   prends l'outil 'BeautifulSoup' pour pouvoir l'utiliser directement par son nom.
from bs4 import BeautifulSoup

URL = "https://example.com"


def scraper(url):
    """Télécharge la page et extrait son titre et ses paragraphes."""
    # 1. On télécharge le code HTML de la page (requête GET).
    reponse = requests.get(url, timeout=10)
    reponse.raise_for_status()

    # 2. On donne le texte HTML (reponse.text) à BeautifulSoup, qui l'analyse
    #    et le rend "fouillable". "html.parser" est l'analyseur intégré à Python.
    soup = BeautifulSoup(reponse.text, "html.parser")

    # 3. .find("h1") récupère le PREMIER élément <h1> (le grand titre).
    #    En HTML, <h1>...</h1> entoure un titre de niveau 1.
    titre = soup.find("h1")

    # .find_all("p") récupère TOUS les éléments <p> (les paragraphes) dans une liste.
    paragraphes = soup.find_all("p")

    return titre, paragraphes      # on renvoie DEUX valeurs d'un coup (un tuple)


# ─────────────────────────────────────────────
# Programme principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        # La fonction renvoie deux valeurs : on les récupère dans deux variables
        # d'un coup (c'est le "dépaquetage"/déstructuration).
        titre, paragraphes = scraper(URL)

        # .text récupère le texte VISIBLE, sans les balises HTML autour.
        # .strip() enlève les espaces/retours à la ligne inutiles aux extrémités.
        print("📄 Titre de la page :")
        print(f"   {titre.text.strip()}")

        # len(liste) = le NOMBRE d'éléments dans la liste.
        print(f"\n📝 {len(paragraphes)} paragraphe(s) trouvé(s) :")
        # enumerate(..., start=1) numérote les tours en commençant à 1.
        for i, p in enumerate(paragraphes, start=1):
            # [:80] = "tranche" qui garde seulement les 80 premiers caractères,
            # pour ne pas inonder l'écran si le paragraphe est très long.
            print(f"   {i}. {p.text.strip()[:80]}...")
    except requests.RequestException as erreur:
        print(f"❌ Impossible de télécharger la page : {erreur}")
