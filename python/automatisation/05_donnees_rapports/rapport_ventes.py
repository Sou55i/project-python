"""
MODULE 05 - Mini-projet : un rapport de ventes automatique
==========================================================
On part de données de ventes brutes (un CSV) et on génère un rapport :
chiffre d'affaires total, CA par produit, meilleur commercial, etc.
Puis on exporte le tout en CSV et en Excel.

Nécessite : pandas + openpyxl  (pip install -r python/requirements.txt)

Lance-le :  python3 python/automatisation/05_donnees_rapports/rapport_ventes.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : pandas (manipulation de tableaux) + Path.
   2. FONCTIONS  : - creer_donnees_demo() fabrique un faux fichier de ventes,
                   - generer_rapport() fait tout le travail d'analyse :
                       a) CHARGER le CSV,         b) CALCULER la colonne montant,
                       c) CALCULER les totaux,    d) REGROUPER (groupby) par produit
                                                     et par commercial,
                       e) EXPORTER en CSV et Excel.
   3. PROGRAMME  : le bloc __main__ crée les données PUIS génère le rapport.
"""

from pathlib import Path

# 'import pandas as pd' : on importe pandas et on lui donne le SURNOM 'pd'.
# C'est une convention universelle : tout le monde écrit 'pd' pour pandas,
# ça rend le code plus court (pd.read_csv au lieu de pandas.read_csv).
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
    # pd.DataFrame(liste) transforme la liste de dictionnaires en TABLEAU pandas,
    # puis .to_csv(...) l'enregistre en fichier CSV.
    #   index=False -> n'écrit PAS la colonne de numéros de ligne ajoutée par pandas.
    pd.DataFrame(ventes).to_csv(fichier_ventes, index=False)


def generer_rapport():
    # 1. CHARGER les données. 'df' (pour DataFrame) est le nom habituel d'un
    #    tableau pandas. Pense à une feuille Excel rangée dans une variable.
    df = pd.read_csv(fichier_ventes)

    # 2. CRÉER une nouvelle colonne calculée : le montant de chaque vente.
    #    df["montant"] = ...  crée (ou remplace) la colonne "montant".
    #    pandas multiplie quantite par prix_unitaire LIGNE PAR LIGNE, automatiquement.
    df["montant"] = df["quantite"] * df["prix_unitaire"]

    print("--- Aperçu des données ---")
    print(df.head())          # .head() affiche les 5 premières lignes du tableau

    # 3. CALCULER des indicateurs globaux sur la colonne "montant".
    ca_total = df["montant"].sum()        # .sum() = somme de toute la colonne
    panier_moyen = df["montant"].mean()   # .mean() = moyenne
    print(f"\n💰 Chiffre d'affaires total : {ca_total} €")
    # {panier_moyen:.2f} -> affiche le nombre avec 2 chiffres après la virgule.
    print(f"🛒 Panier moyen            : {panier_moyen:.2f} €")

    # 4. REGROUPER : le chiffre d'affaires PAR produit (cœur d'un rapport).
    #    .groupby("produit")      -> rassemble les lignes ayant le même produit
    #    ["montant"].sum()        -> additionne leur montant
    #    .sort_values(ascending=False) -> trie du plus grand au plus petit
    ca_par_produit = df.groupby("produit")["montant"].sum().sort_values(ascending=False)
    print("\n📦 Chiffre d'affaires par produit :")
    print(ca_par_produit)

    # 5. REGROUPER : le chiffre d'affaires par commercial.
    ca_par_commercial = df.groupby("commercial")["montant"].sum().sort_values(ascending=False)
    #   .index    = les étiquettes (ici les noms des commerciaux), déjà triées
    #   .index[0] = la première étiquette = le meilleur commercial
    meilleur = ca_par_commercial.index[0]
    #   .iloc[0]  = la première VALEUR (le montant correspondant)
    print(f"\n🏆 Meilleur commercial : {meilleur} ({ca_par_commercial.iloc[0]} €)")

    # 6. EXPORTER le rapport, prêt à être partagé.
    ca_par_produit.to_csv(dossier / "rapport_produits.csv")
    ca_par_produit.to_excel(dossier / "rapport_produits.xlsx")   # nécessite openpyxl
    print(f"\n✅ Rapports exportés dans : {dossier}")


if __name__ == "__main__":
    creer_donnees_demo()
    generer_rapport()
