"""
FIL ROUGE — Étape 2/5 : PLUSIEURS dépenses dans une liste
=========================================================
Une dépense seule ne sert à rien : on veut suivre TOUTES nos dépenses. On range
donc nos dictionnaires (étape 1) dans une LISTE, puis on apprend à la parcourir
pour calculer un total.

Notions : listes, boucle for, accumulation d'un total (modules 01 et 02).

Lance-le :  python3 python/projets/fil_rouge/etape_2_liste.py
"""

# Une LISTE [ ] de DICTIONNAIRES { } : chaque élément est une dépense.
depenses = [
    {"montant": 12.5, "categorie": "courses", "date": "2026-06-19"},
    {"montant": 40.0, "categorie": "transport", "date": "2026-06-19"},
    {"montant": 8.9, "categorie": "courses", "date": "2026-06-20"},
]

# Combien de dépenses ? len() compte les éléments d'une liste.
print(f"{len(depenses)} dépenses enregistrées.\n")

# On les affiche une par une avec une boucle for.
for depense in depenses:
    print(f"- {depense['date']} : {depense['montant']:.2f} € ({depense['categorie']})")

# ── Calculer le TOTAL : le motif "accumulateur" ────────────────────
# On part de 0, et on AJOUTE le montant de chaque dépense au fur et à mesure.
total = 0
for depense in depenses:
    total += depense["montant"]      # total = total + le montant courant

print(f"\nTotal dépensé : {total:.2f} €")

# 🔎 La même idée, en plus court (pour plus tard) :
#    total = sum(d["montant"] for d in depenses)

# ➡️ Étape suivante : ce code commence à se répéter (deux boucles for...).
#    On va le RANGER dans des fonctions réutilisables. Voir etape_3_fonctions.py
