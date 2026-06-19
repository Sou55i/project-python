"""
FIL ROUGE — Étape 5/5 : la VRAIE appli en ligne de commande
===========================================================
On rassemble tout : les fonctions (étape 3) + la sauvegarde (étape 4) + des
COMMANDES pour piloter l'outil depuis le terminal. C'est désormais un véritable
gestionnaire de dépenses, utilisable au quotidien.

Notions réunies : dictionnaires, listes, fonctions, fichiers/JSON, argparse,
rapport par catégorie (modules 02, 03, 04, 12, 13).

Exemples :
   python3 python/projets/fil_rouge/etape_5_cli.py ajouter --montant 12.5 --categorie courses
   python3 python/projets/fil_rouge/etape_5_cli.py ajouter --montant 40 --categorie transport
   python3 python/projets/fil_rouge/etape_5_cli.py lister
   python3 python/projets/fil_rouge/etape_5_cli.py rapport
   python3 python/projets/fil_rouge/etape_5_cli.py --help

🗺️ CHEMINEMENT : IMPORTS → CHEMIN → fonctions de données (charger/sauvegarder)
   → fonctions métier (ajouter/lister/rapport) → parseur de commandes → main.
"""

import argparse
import json
from datetime import date as date_du_jour
from pathlib import Path

FICHIER = Path(__file__).parent / "exemples" / "depenses.json"


# ── Données : lire / écrire le fichier ─────────────────────────────
def charger():
    if not FICHIER.exists():
        return []
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)


def sauvegarder(depenses):
    FICHIER.parent.mkdir(parents=True, exist_ok=True)
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(depenses, f, indent=2, ensure_ascii=False)


# ── Métier : les actions de l'utilisateur ──────────────────────────
def ajouter(montant, categorie):
    """Ajoute une dépense datée d'aujourd'hui, puis sauvegarde."""
    depenses = charger()
    # date_du_jour.today().isoformat() → "2026-06-19" (la date du jour, en texte).
    depenses.append({
        "montant": montant,
        "categorie": categorie,
        "date": date_du_jour.today().isoformat(),
    })
    sauvegarder(depenses)
    print(f"[+] Dépense ajoutée : {montant:.2f} € ({categorie})")


def lister():
    """Affiche toutes les dépenses, numérotées."""
    depenses = charger()
    if not depenses:
        print("Aucune dépense. Ajoute-en une avec la commande 'ajouter'.")
        return
    print(f"--- {len(depenses)} dépense(s) ---")
    for numero, d in enumerate(depenses, start=1):
        print(f"{numero}. {d['date']} : {d['montant']:.2f} € ({d['categorie']})")
    print(f"Total : {sum(d['montant'] for d in depenses):.2f} €")


def rapport():
    """Affiche le total dépensé PAR catégorie, du plus gros au plus petit."""
    depenses = charger()
    if not depenses:
        print("Aucune dépense à analyser.")
        return

    # Regroupement par catégorie (le 'groupby' manuel vu à l'étape 3 / module 13).
    par_categorie = {}
    for d in depenses:
        cat = d["categorie"]
        par_categorie[cat] = par_categorie.get(cat, 0) + d["montant"]

    print("--- Rapport par catégorie ---")
    # sorted(..., key=..., reverse=True) trie les catégories par montant décroissant.
    #   key=lambda paire: paire[1]  →  on trie sur la VALEUR (le montant), pas la clé.
    for categorie, somme in sorted(par_categorie.items(), key=lambda paire: paire[1], reverse=True):
        print(f"  {categorie:<12} : {somme:.2f} €")
    print(f"  {'TOTAL':<12} : {sum(par_categorie.values()):.2f} €")


# ── Interface : déclarer les commandes ─────────────────────────────
def creer_parseur():
    parseur = argparse.ArgumentParser(description="Gestionnaire de dépenses (fil rouge).")
    sous = parseur.add_subparsers(dest="commande", required=True)

    p_ajouter = sous.add_parser("ajouter", help="Ajouter une dépense")
    p_ajouter.add_argument("--montant", type=float, required=True, help="Montant en euros")
    p_ajouter.add_argument("--categorie", required=True, help="Catégorie (courses, transport...)")

    sous.add_parser("lister", help="Lister toutes les dépenses")
    sous.add_parser("rapport", help="Total par catégorie")

    return parseur


def main():
    args = creer_parseur().parse_args()
    if args.commande == "ajouter":
        ajouter(args.montant, args.categorie)
    elif args.commande == "lister":
        lister()
    elif args.commande == "rapport":
        rapport()


if __name__ == "__main__":
    main()

# 🎉 Tu as suivi un programme de sa forme la plus simple (3 variables) jusqu'à
#    une appli complète. C'est EXACTEMENT comme ça que grandit un vrai logiciel :
#    une petite chose qui marche, puis on l'améliore étape par étape.
