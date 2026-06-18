#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstration de la gestion des erreurs et des fichiers.
"""

def main():
    nom_fichier = "journal.log"

    # --- 1. ÉCRITURE ---
    print(f"Écriture dans {nom_fichier}...")
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write("Début du programme\n")
            f.write("Tout fonctionne bien.\n")
    except Exception as e:
        print(f"Erreur lors de l'écriture : {e}")

    # --- 2. LECTURE ---
    print(f"\nLecture du contenu de {nom_fichier} :")
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            # On lit ligne par ligne
            for i, ligne in enumerate(f, 1):
                print(f"Ligne {i} : {ligne.strip()}")
    except FileNotFoundError:
        print("Erreur : Le fichier n'existe pas.")

    # --- 3. GESTION DES ERREURS ---
    print("\nTest de division par zéro :")
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Capter l'erreur : Division par zéro interdite !")
    finally:
        print("Le bloc 'finally' s'exécute QUOI QU'IL ARRIVE.")

if __name__ == "__main__":
    main()
