"""
MODULE 03 - Web scraping
========================
Quand un site n'a pas d'API, on lit directement son HTML pour en extraire
des infos. On utilise ici 'example.com', un site public prévu pour les tests.

Nécessite : connexion Internet + 'requests' et 'beautifulsoup4'
            (pip install -r requirements.txt)

Lance-le :  python3 automatisation/03_web_apis/scraping.py
"""

import requests
from bs4 import BeautifulSoup

URL = "https://example.com"


def scraper(url):
    """Télécharge la page et extrait son titre et ses paragraphes."""
    # 1. On télécharge le code HTML de la page.
    reponse = requests.get(url, timeout=10)
    reponse.raise_for_status()

    # 2. On donne ce HTML à BeautifulSoup, qui le rend "fouillable".
    soup = BeautifulSoup(reponse.text, "html.parser")

    # 3. find() récupère le PREMIER élément correspondant à une balise.
    titre = soup.find("h1")

    # find_all() récupère TOUS les éléments correspondants (ici tous les <p>).
    paragraphes = soup.find_all("p")

    return titre, paragraphes


# ─────────────────────────────────────────────
# Programme principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        titre, paragraphes = scraper(URL)

        # .text récupère le texte visible, sans les balises HTML.
        print("📄 Titre de la page :")
        print(f"   {titre.text.strip()}")

        print(f"\n📝 {len(paragraphes)} paragraphe(s) trouvé(s) :")
        for i, p in enumerate(paragraphes, start=1):
            print(f"   {i}. {p.text.strip()[:80]}...")   # 80 premiers caractères
    except requests.RequestException as erreur:
        print(f"❌ Impossible de télécharger la page : {erreur}")
