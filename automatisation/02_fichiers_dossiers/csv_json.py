"""
MODULE 02 - Les formats CSV et JSON
===================================
Comment lire et écrire les deux formats de données les plus courants
en automatisation, avec les modules 'csv' et 'json' (inclus dans Python).

Lance-le :  python3 automatisation/02_fichiers_dossiers/csv_json.py
"""

import csv
import json
from pathlib import Path

dossier = Path(__file__).parent / "exemples"
dossier.mkdir(exist_ok=True)


# ═════════════════════════════════════════════
#  PARTIE 1 : CSV (un tableau en texte)
# ═════════════════════════════════════════════
employes = [
    {"nom": "Alice", "age": 30, "ville": "Paris"},
    {"nom": "Bob", "age": 25, "ville": "Lyon"},
    {"nom": "Chloé", "age": 35, "ville": "Marseille"},
]

fichier_csv = dossier / "employes.csv"

# --- Écrire un CSV à partir d'une liste de dictionnaires ---
# DictWriter écrit chaque dictionnaire comme une ligne du tableau.
with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
    colonnes = ["nom", "age", "ville"]
    writer = csv.DictWriter(f, fieldnames=colonnes)
    writer.writeheader()          # écrit la 1re ligne : nom,age,ville
    writer.writerows(employes)    # écrit toutes les lignes de données
print(f"[+] CSV écrit : {fichier_csv}")

# --- Relire ce CSV ---
print("\n--- Lecture du CSV ---")
with open(fichier_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)     # chaque ligne devient un dictionnaire
    for ligne in reader:
        # Note : les valeurs lues sont du TEXTE (même "30"), d'où int() si calcul.
        print(f"{ligne['nom']} a {ligne['age']} ans et vit à {ligne['ville']}")


# ═════════════════════════════════════════════
#  PARTIE 2 : JSON (données structurées)
# ═════════════════════════════════════════════
profil = {
    "nom": "Alice",
    "age": 30,
    "actif": True,
    "loisirs": ["lecture", "vélo", "code"],
}

fichier_json = dossier / "profil.json"

# --- Écrire un dictionnaire Python en JSON ---
# indent=2 rend le fichier joliment présenté ; ensure_ascii=False garde les accents.
with open(fichier_json, "w", encoding="utf-8") as f:
    json.dump(profil, f, indent=2, ensure_ascii=False)
print(f"\n[+] JSON écrit : {fichier_json}")

# --- Relire le JSON : on récupère un vrai dictionnaire Python ---
with open(fichier_json, "r", encoding="utf-8") as f:
    donnees = json.load(f)
print("--- Lecture du JSON ---")
print(f"Nom    : {donnees['nom']}")
print(f"Loisirs: {', '.join(donnees['loisirs'])}")   # join = colle la liste avec des virgules
