"""
MODULE 15 - Construire un script : CONVERTIR DU JSON EN SQL
===========================================================
Aboutissement du raisonnement de ../ECRIRE_UN_SCRIPT.md (exemple n°2).
Le script lit une liste d'objets JSON et :
  1. AFFICHE les instructions SQL "INSERT INTO ..." correspondantes,
  2. les INSÈRE réellement dans une base SQLite, puis relit pour vérifier.

Tout est AUTO-CONTENU : il fabrique son propre fichier JSON de démo. Aucune
bibliothèque externe (json et sqlite3 sont inclus dans Python).

Lance-le :  python3 python/15_construire_un_script/json_vers_sql.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. Fabriquer un JSON de démo (pour que le script tourne tout seul).
   2. LIRE le JSON -> une liste de dictionnaires Python.
   3. DÉDUIRE les colonnes (les clés du 1er dictionnaire).
   4. CONSTRUIRE la requête "INSERT INTO ... VALUES (?, ?)" avec des placeholders.
   5. CRÉER une base SQLite et INSÉRER chaque ligne en toute sécurité.
   6. RELIRE la table pour prouver que ça a marché.
"""

import json
import sqlite3
from pathlib import Path

# Tout se passe dans un sous-dossier "exemples" (ignoré par git).
DOSSIER = Path(__file__).parent / "exemples"
FICHIER_JSON = DOSSIER / "gens.json"
FICHIER_DB = DOSSIER / "gens.db"
TABLE = "gens"


def fabriquer_json_demo() -> None:
    """Crée un petit fichier JSON d'exemple (liste d'objets)."""
    DOSSIER.mkdir(exist_ok=True)
    donnees = [
        {"nom": "Alice", "age": 30, "ville": "Paris"},
        {"nom": "Bob", "age": 25, "ville": "Lyon"},
        {"nom": "Chloe", "age": 35, "ville": "Marseille"},
    ]
    # json.dump écrit la structure Python dans le fichier, au format JSON.
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2, ensure_ascii=False)


def construire_requete_insert(colonnes: list[str]) -> str:
    """Fabrique la requête 'INSERT INTO table (col1, col2) VALUES (?, ?)'."""
    # ", ".join(colonnes) colle les noms de colonnes : ["nom","age"] -> "nom, age"
    noms = ", ".join(colonnes)
    # Un point d'interrogation (placeholder) PAR colonne : -> "?, ?"
    # On NE met PAS les valeurs ici : sqlite les insérera à notre place (anti-injection).
    placeholders = ", ".join("?" for _ in colonnes)
    return f"INSERT INTO {TABLE} ({noms}) VALUES ({placeholders});"


def main() -> None:
    # (1) Données de démo + (2) lecture du JSON
    fabriquer_json_demo()
    with open(FICHIER_JSON, encoding="utf-8") as f:
        lignes = json.load(f)        # -> liste de dictionnaires

    # (3) Les colonnes = les clés du premier objet.
    colonnes = list(lignes[0].keys())     # ["nom", "age", "ville"]
    requete = construire_requete_insert(colonnes)   # (4)

    # (1 du sujet) AFFICHER le SQL généré, pour bien voir ce qu'on produit.
    print("--- SQL généré ---")
    print(f"CREATE TABLE {TABLE} (" + ", ".join(f"{c} TEXT" for c in colonnes) + ");")
    for ligne in lignes:
        # tuple(ligne.values()) = les valeurs dans l'ordre des colonnes.
        # On montre ici à quoi ressemblerait la ligne, valeurs comprises.
        valeurs = ", ".join(repr(v) for v in ligne.values())
        print(f"INSERT INTO {TABLE} ({', '.join(colonnes)}) VALUES ({valeurs});")

    # (5) Créer une VRAIE base SQLite et insérer proprement.
    if FICHIER_DB.exists():
        FICHIER_DB.unlink()           # on repart d'une base propre
    conn = sqlite3.connect(FICHIER_DB)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {TABLE} (" + ", ".join(f"{c} TEXT" for c in colonnes) + ");")
    for ligne in lignes:
        # On passe la requête à trous + les valeurs SÉPARÉMENT (sûr et propre).
        cur.execute(requete, tuple(ligne.values()))
    conn.commit()

    # (6) Relire pour prouver que l'insertion a marché.
    print("\n--- Contenu réel de la base SQLite ---")
    for ligne_db in cur.execute(f"SELECT * FROM {TABLE};"):
        print("  ", ligne_db)
    conn.close()

    print(f"\n✅ Base créée : {FICHIER_DB}")


if __name__ == "__main__":
    main()
