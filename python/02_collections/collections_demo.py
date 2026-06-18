#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstration des 4 grandes collections Python :
Listes, Dictionnaires, Tuples et Sets.
"""

def main():
    # --- 1. LES LISTES ---
    print("--- 1. LISTES (Modifiables et ordonnées) ---")
    inventaire = ["Épée", "Bouclier", "Potion"]
    inventaire.append("Arc") # Ajouter à la fin
    inventaire[0] = "Épée laser" # Modifier un élément
    print(f"Inventaire complet : {inventaire}")
    print(f"Deuxième objet : {inventaire[1]}")

    # --- 2. LES DICTIONNAIRES ---
    print("\n--- 2. DICTIONNAIRES (Clé: Valeur) ---")
    stats = {
        "force": 15,
        "agilité": 10,
        "intelligence": 12
    }
    print(f"Force du personnage : {stats['force']}")
    stats["chance"] = 5 # Ajouter une nouvelle paire
    
    # Parcourir un dictionnaire
    for cle, valeur in stats.items():
        print(f"  - {cle} : {valeur}")

    # --- 3. LES TUPLES ---
    print("\n--- 3. TUPLES (Fixes / Immuables) ---")
    # On les utilise souvent pour des données qui ne doivent pas changer
    position_depart = (0, 0)
    # position_depart[0] = 10 # ❌ Erreur ! Un tuple ne peut pas être modifié.
    print(f"Position de départ : {position_depart}")

    # --- 4. LES SETS ---
    print("\n--- 4. SETS (Valeurs uniques) ---")
    emails = {"a@test.com", "b@test.com", "a@test.com"}
    print(f"Emails uniques : {emails}") # "a@test.com" n'apparaîtra qu'une fois.

if __name__ == "__main__":
    main()
