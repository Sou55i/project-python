"""
MODULE 02 - Lire et écrire des fichiers texte
==============================================
Les 3 opérations de base : écrire, ajouter, lire.

Lance-le :  python3 automatisation/02_fichiers_dossiers/lire_ecrire.py
"""

from pathlib import Path

# On travaille dans un sous-dossier "exemples" À CÔTÉ de ce script,
# peu importe d'où tu lances la commande. __file__ = ce fichier .py.
dossier = Path(__file__).parent / "exemples"
dossier.mkdir(exist_ok=True)            # crée le dossier s'il n'existe pas encore
fichier = dossier / "notes.txt"


# ─────────────────────────────────────────────
# 1. ÉCRIRE ("w" écrase tout le contenu existant)
# ─────────────────────────────────────────────
with open(fichier, "w", encoding="utf-8") as f:
    f.write("Liste de courses\n")       # \n = passer à la ligne suivante
    f.write("- Pain\n")
    f.write("- Café\n")
print(f"[+] Fichier écrit : {fichier}")


# ─────────────────────────────────────────────
# 2. AJOUTER ("a" écrit à la fin sans effacer)
# ─────────────────────────────────────────────
with open(fichier, "a", encoding="utf-8") as f:
    f.write("- Chocolat\n")
print("[+] Une ligne ajoutée à la fin.")


# ─────────────────────────────────────────────
# 3. LIRE ("r")
# ─────────────────────────────────────────────
# 3a. Tout le contenu d'un coup :
with open(fichier, "r", encoding="utf-8") as f:
    contenu = f.read()
print("\n--- Contenu complet ---")
print(contenu)

# 3b. Ligne par ligne (idéal pour les gros fichiers) :
print("--- Lecture ligne par ligne ---")
with open(fichier, "r", encoding="utf-8") as f:
    for numero, ligne in enumerate(f, start=1):
        # .strip() retire le retour à la ligne et les espaces en trop
        print(f"Ligne {numero} : {ligne.strip()}")
