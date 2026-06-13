"""
MODULE 06 - Explorer les bibliothèques disponibles
===================================================
Ce script montre, depuis Python, comment savoir :
  - ce qui est DÉJÀ installé (stdlib ou tierce),
  - quelle VERSION est installée,
  - quoi faire quand une bibliothèque manque.

Lance-le :  python3 automatisation/06_bibliotheques/explorer_modules.py
"""

# 'importlib.util' fait partie de la bibliothèque STANDARD.
# On s'en sert ici pour vérifier si un module existe SANS le lancer.
import importlib.util


def est_installe(nom_module: str) -> bool:
    """Renvoie True si le module 'nom_module' est disponible, False sinon.

    find_spec() cherche le module et renvoie ses 'coordonnées' s'il le trouve,
    ou None s'il n'existe pas. On compare donc le résultat à None.
    """
    return importlib.util.find_spec(nom_module) is not None


# ─────────────────────────────────────────────
# 1. Vérifier une liste de modules (stdlib + tierces)
# ─────────────────────────────────────────────
# Les premiers sont dans la bibliothèque standard (toujours présents).
# Les derniers sont tiers (présents seulement si tu as fait 'pip install').
modules_a_tester = ["json", "csv", "pathlib", "requests", "pandas", "openpyxl"]

print("État des modules sur ta machine :\n")
for nom in modules_a_tester:
    # On choisit un symbole selon que le module est présent ou non.
    symbole = "✅" if est_installe(nom) else "❌ (à installer avec pip)"
    print(f"  {nom:<12} {symbole}")   # :<12 aligne le nom sur 12 caractères


# ─────────────────────────────────────────────
# 2. Connaître la VERSION d'une bibliothèque tierce installée
# ─────────────────────────────────────────────
# 'importlib.metadata' (stdlib) lit les infos d'un paquet installé via pip.
from importlib.metadata import version, PackageNotFoundError

print("\nVersions installées :\n")
for nom in ["requests", "pandas"]:
    try:
        # version("requests") renvoie par ex. "2.31.0"
        print(f"  {nom} : {version(nom)}")
    except PackageNotFoundError:
        # Ce 'except' se déclenche si le paquet n'est pas installé.
        print(f"  {nom} : non installé (fais 'pip install {nom}')")


# ─────────────────────────────────────────────
# 3. La bonne réaction face à un module manquant
# ─────────────────────────────────────────────
print(
    "\n💡 Rappel : si tu vois 'ModuleNotFoundError: No module named X',\n"
    "   c'est qu'il faut l'installer :  pip install X\n"
    "   (et l'ajouter à requirements.txt pour ne pas l'oublier)."
)
