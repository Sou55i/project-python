"""
FIL ROUGE — Étape 1/5 : représenter UNE dépense
================================================
But du fil rouge : construire, petit à petit, un "gestionnaire de dépenses".
À chaque étape, on ajoute UNE notion du cours et le programme grandit.

Ici, étape 1 : juste représenter UNE dépense en mémoire. On part de la version
la plus naïve (des variables séparées) et on découvre POURQUOI un dictionnaire
est mieux adapté.

Notions : variables, types, dictionnaire (modules 01 et 02).

Lance-le :  python3 python/projets/fil_rouge/etape_1_une_depense.py
"""

# ── Version naïve : trois variables séparées ───────────────────────
# Ça marche pour UNE dépense... mais comment en gérer 100 comme ça ?
# Il faudrait montant1, montant2, ... categorie1, categorie2 : ingérable.
montant = 12.5
categorie = "courses"
date = "2026-06-19"

print("Version variables séparées :")
print(montant, categorie, date)


# ── Meilleure idée : REGROUPER ces 3 infos dans un dictionnaire ────
# Un dictionnaire associe une étiquette (clé) à une valeur. Les 3 infos d'une
# dépense vivent maintenant dans UN seul objet, facile à transporter.
depense = {
    "montant": 12.5,
    "categorie": "courses",
    "date": "2026-06-19",
}

print("\nVersion dictionnaire :")
print(depense)

# On accède à une info précise par sa clé, entre crochets.
print(f"\nJ'ai dépensé {depense['montant']} € en {depense['categorie']}.")

# ➡️ Étape suivante : et si on en avait PLUSIEURS ? → une LISTE de dépenses.
#    Voir etape_2_liste.py
