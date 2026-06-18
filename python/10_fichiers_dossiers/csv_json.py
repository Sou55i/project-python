"""
MODULE 02 - Les formats CSV et JSON
===================================
Comment lire et écrire les deux formats de données les plus courants
en automatisation, avec les modules 'csv' et 'json' (inclus dans Python).

Lance-le :  python3 python/10_fichiers_dossiers/csv_json.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS   : csv et json (outils inclus dans Python) + Path.
   2. PRÉPARER  : on crée un dossier "exemples" pour y ranger les fichiers produits.
   3. PARTIE 1  : CSV  -> on ÉCRIT une liste de données en CSV, puis on la RELIT.
   4. PARTIE 2  : JSON -> on ÉCRIT un dictionnaire en JSON, puis on le RELIT.
   (Schéma répété : on écrit d'abord, on relit ensuite pour vérifier.)
"""

# 'import csv' = on ouvre la caisse à outils 'csv' de la bibliothèque standard.
# Ensuite on appellera ses fonctions en écrivant 'csv.quelquechose'.
import csv
import json
from pathlib import Path

# On prépare un dossier "exemples" à côté de ce script (voir lire_ecrire.py pour le détail).
dossier = Path(__file__).parent / "exemples"
dossier.mkdir(exist_ok=True)


# ═════════════════════════════════════════════
#  PARTIE 1 : CSV (un tableau stocké en texte)
# ═════════════════════════════════════════════
# Une LISTE [ ] de DICTIONNAIRES { }. Chaque dictionnaire = une ligne du tableau,
# où la clé est le nom de la colonne et la valeur, la donnée de la cellule.
employes = [
    {"nom": "Alice", "age": 30, "ville": "Paris"},
    {"nom": "Bob", "age": 25, "ville": "Lyon"},
    {"nom": "Chloé", "age": 35, "ville": "Marseille"},
]

fichier_csv = dossier / "employes.csv"

# --- Écrire un CSV à partir de cette liste de dictionnaires ---
#   "w"        = mode write (écriture, écrase l'existant)
#   newline="" = réglage recommandé pour le module csv (évite des lignes vides
#                en trop sous Windows). Mets-le toujours pour du CSV.
with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
    colonnes = ["nom", "age", "ville"]
    # DictWriter sait écrire des dictionnaires en lignes de tableau.
    #   fieldnames=colonnes -> l'ordre et le nom des colonnes
    writer = csv.DictWriter(f, fieldnames=colonnes)
    writer.writeheader()          # écrit la 1re ligne d'en-tête : nom,age,ville
    writer.writerows(employes)    # écrit toutes les lignes de données d'un coup
print(f"[+] CSV écrit : {fichier_csv}")

# --- Relire ce CSV ---
print("\n--- Lecture du CSV ---")   # le \n ajoute une ligne vide pour aérer
with open(fichier_csv, "r", encoding="utf-8") as f:   # "r" = read (lecture)
    # DictReader lit chaque ligne du tableau et la transforme en dictionnaire,
    # en utilisant la 1re ligne (l'en-tête) comme noms de clés.
    reader = csv.DictReader(f)
    for ligne in reader:          # on parcourt chaque ligne (chaque dictionnaire)
        # ATTENTION : les valeurs lues depuis un CSV sont du TEXTE (même "30").
        # Pour calculer dessus, il faudrait faire int(ligne['age']).
        print(f"{ligne['nom']} a {ligne['age']} ans et vit à {ligne['ville']}")


# ═════════════════════════════════════════════
#  PARTIE 2 : JSON (données structurées)
# ═════════════════════════════════════════════
# Un dictionnaire Python qui contient aussi une LISTE (loisirs) : structure imbriquée.
profil = {
    "nom": "Alice",
    "age": 30,
    "actif": True,
    "loisirs": ["lecture", "vélo", "code"],
}

fichier_json = dossier / "profil.json"

# --- Écrire (= "sérialiser") un dictionnaire Python en texte JSON ---
# json.dump(objet, fichier, ...) écrit l'objet dans le fichier.
#   indent=2          -> présente joliment, avec 2 espaces de décalage (lisible)
#   ensure_ascii=False-> garde les accents é/à/ç tels quels (sinon ils seraient
#                        remplacés par des codes du style é)
with open(fichier_json, "w", encoding="utf-8") as f:
    json.dump(profil, f, indent=2, ensure_ascii=False)
print(f"\n[+] JSON écrit : {fichier_json}")

# --- Relire le JSON : json.load() renvoie un VRAI dictionnaire Python ---
with open(fichier_json, "r", encoding="utf-8") as f:
    donnees = json.load(f)
print("--- Lecture du JSON ---")
print(f"Nom    : {donnees['nom']}")
# "  ".join(liste) colle les éléments d'une liste en un seul texte,
# en intercalant le séparateur (ici ", "). Ex : ['a','b'] -> "a, b".
print(f"Loisirs: {', '.join(donnees['loisirs'])}")
