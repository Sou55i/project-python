"""
FIL ROUGE — Étape 3/5 : ranger le code dans des FONCTIONS
========================================================
Aux étapes 1-2, le code était "à plat" : difficile à réutiliser. On le découpe
maintenant en FONCTIONS, chacune avec UN rôle clair. Le programme devient
lisible et chaque morceau est testable séparément.

Notions : fonctions, paramètres, return, dictionnaire de regroupement
(modules 03 et 13).

Lance-le :  python3 python/projets/fil_rouge/etape_3_fonctions.py
"""


def creer_depense(montant, categorie, date):
    """Construit (et renvoie) une dépense sous forme de dictionnaire."""
    return {"montant": montant, "categorie": categorie, "date": date}


def total(depenses):
    """Renvoie la somme de tous les montants."""
    return sum(d["montant"] for d in depenses)


def total_par_categorie(depenses):
    """Renvoie un dict {catégorie: somme dépensée} — un 'groupby' à la main."""
    resultat = {}
    for d in depenses:
        cat = d["categorie"]
        # .get(cat, 0) renvoie le total déjà accumulé pour cette catégorie,
        # ou 0 si on la voit pour la première fois.
        resultat[cat] = resultat.get(cat, 0) + d["montant"]
    return resultat


def afficher(depenses):
    """Affiche la liste et les totaux de façon lisible."""
    print(f"{len(depenses)} dépense(s) :")
    for d in depenses:
        print(f"  - {d['date']} : {d['montant']:.2f} € ({d['categorie']})")

    print(f"\nTotal : {total(depenses):.2f} €")
    print("Par catégorie :")
    for categorie, somme in total_par_categorie(depenses).items():
        print(f"  {categorie:<12} : {somme:.2f} €")


# ── Programme principal ────────────────────────────────────────────
if __name__ == "__main__":
    # On construit nos dépenses via la fonction creer_depense (plus lisible).
    depenses = [
        creer_depense(12.5, "courses", "2026-06-19"),
        creer_depense(40.0, "transport", "2026-06-19"),
        creer_depense(8.9, "courses", "2026-06-20"),
    ]
    afficher(depenses)

# ➡️ Problème restant : à chaque lancement, les dépenses repartent de zéro.
#    On va les SAUVEGARDER dans un fichier. Voir etape_4_sauvegarde.py
