"""
FIL ROUGE — Étape 4/5 : SAUVEGARDER les dépenses (persistance JSON)
==================================================================
Jusqu'ici, tout disparaissait à la fin du programme. On rend les données
PERSISTANTES : on les écrit dans un fichier JSON et on les relit au lancement
suivant. C'est ce qui transforme un script de démo en vrai outil.

Notions : fichiers, JSON, gestion du "fichier qui n'existe pas encore"
(modules 04 et 10).

Lance-le PLUSIEURS fois de suite :
    python3 python/projets/fil_rouge/etape_4_sauvegarde.py
À chaque exécution, une dépense de plus est mémorisée d'un lancement à l'autre.
"""

import json
from pathlib import Path

# Le fichier de données, rangé dans "exemples/" à côté du fil rouge
# (dossier ignoré par git).
FICHIER = Path(__file__).parent / "exemples" / "depenses.json"


def charger():
    """Lit les dépenses depuis le fichier JSON, ou renvoie une liste vide."""
    if not FICHIER.exists():        # 1er lancement : pas encore de fichier
        return []
    with open(FICHIER, "r", encoding="utf-8") as f:
        return json.load(f)         # texte JSON → liste de dicts


def sauvegarder(depenses):
    """Écrit la liste des dépenses dans le fichier JSON (crée le dossier au besoin)."""
    FICHIER.parent.mkdir(parents=True, exist_ok=True)
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(depenses, f, indent=2, ensure_ascii=False)


def total(depenses):
    """Somme des montants."""
    return sum(d["montant"] for d in depenses)


# ── Programme principal ────────────────────────────────────────────
if __name__ == "__main__":
    # 1. On RÉCUPÈRE ce qui était déjà enregistré (au lieu de repartir de zéro).
    depenses = charger()

    # 2. On ajoute une nouvelle dépense (ici une valeur fixe, pour la démo).
    depenses.append({"montant": 9.99, "categorie": "loisirs", "date": "2026-06-21"})

    # 3. On RÉ-ENREGISTRE la liste complète sur le disque.
    sauvegarder(depenses)

    # 4. On affiche l'état courant : le nombre grandit à chaque lancement.
    print(f"{len(depenses)} dépense(s) mémorisée(s) — total {total(depenses):.2f} €")
    print(f"(fichier : {FICHIER})")

# ➡️ Dernière étape : en faire un VRAI outil avec des commandes
#    (ajouter / lister / rapport) au lieu d'une valeur codée en dur.
#    Voir etape_5_cli.py
