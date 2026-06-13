"""
MODULE 05 - Mini-projet : un rapport de ventes automatique
==========================================================
On part de données de ventes brutes (un CSV) et on génère un rapport :
chiffre d'affaires total, CA par produit, meilleur commercial, etc.
Puis on exporte le tout en CSV et en Excel.

Nécessite : pandas + openpyxl  (pip install -r requirements.txt)

Lance-le :  python3 automatisation/05_donnees_rapports/rapport_ventes.py
"""

from pathlib import Path

import pandas as pd

dossier = Path(__file__).parent / "exemples"
dossier.mkdir(exist_ok=True)
fichier_ventes = dossier / "ventes.csv"


def creer_donnees_demo():
    """Crée un faux fichier de ventes pour la démo (à remplacer par tes vraies données)."""
    ventes = [
        {"date": "2026-01-05", "produit": "Clavier", "commercial": "Alice", "quantite": 3, "prix_unitaire": 45},
        {"date": "2026-01-06", "produit": "Souris", "commercial": "Bob", "quantite": 5, "prix_unitaire": 20},
        {"date": "2026-01-07", "produit": "Écran", "commercial": "Alice", "quantite": 2, "prix_unitaire": 150},
        {"date": "2026-01-08", "produit": "Clavier", "commercial": "Chloé", "quantite": 1, "prix_unitaire": 45},
        {"date": "2026-01-09", "produit": "Souris", "commercial": "Alice", "quantite": 4, "prix_unitaire": 20},
        {"date": "2026-01-10", "produit": "Écran", "commercial": "Bob", "quantite": 1, "prix_unitaire": 150},
    ]
    pd.DataFrame(ventes).to_csv(fichier_ventes, index=False)


def generer_rapport():
    # 1. CHARGER les données. df = DataFrame = "feuille Excel" en mémoire.
    df = pd.read_csv(fichier_ventes)

    # 2. CRÉER une nouvelle colonne calculée : le montant de chaque vente.
    #    pandas applique le calcul à TOUTES les lignes d'un coup.
    df["montant"] = df["quantite"] * df["prix_unitaire"]

    print("--- Aperçu des données ---")
    print(df.head())          # affiche les premières lignes

    # 3. CALCULER des indicateurs globaux.
    ca_total = df["montant"].sum()
    panier_moyen = df["montant"].mean()
    print(f"\n💰 Chiffre d'affaires total : {ca_total} €")
    print(f"🛒 Panier moyen            : {panier_moyen:.2f} €")

    # 4. REGROUPER : CA par produit (l'opération clé d'un rapport).
    ca_par_produit = df.groupby("produit")["montant"].sum().sort_values(ascending=False)
    print("\n📦 Chiffre d'affaires par produit :")
    print(ca_par_produit)

    # 5. REGROUPER : meilleur commercial.
    ca_par_commercial = df.groupby("commercial")["montant"].sum().sort_values(ascending=False)
    meilleur = ca_par_commercial.index[0]   # le premier du classement trié
    print(f"\n🏆 Meilleur commercial : {meilleur} ({ca_par_commercial.iloc[0]} €)")

    # 6. EXPORTER le rapport, prêt à être partagé.
    ca_par_produit.to_csv(dossier / "rapport_produits.csv")
    ca_par_produit.to_excel(dossier / "rapport_produits.xlsx")
    print(f"\n✅ Rapports exportés dans : {dossier}")


if __name__ == "__main__":
    creer_donnees_demo()
    generer_rapport()
