#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstration des bases de Python :
- Variables et types
- Conditions (if/else)
- Boucles (for/while)
"""

def main():
    print("--- 1. VARIABLES ---")
    
    # Python devine le type tout seul
    score = 100
    nom_joueur = "Baba"
    vitesse = 1.5
    est_vivant = True
    
    # Affichage avec une 'f-string' (très pratique pour mélanger texte et variables)
    print(f"Joueur : {nom_joueur} | Score : {score}")
    print(f"Type de score : {type(score)}") # Affiche <class 'int'>

    print("\n--- 2. CONDITIONS ---")
    
    vie = 50
    
    # L'indentation (4 espaces) est ce qui définit le bloc de code
    if vie > 80:
        print("Santé : Excellente")
    elif vie > 20:
        print("Santé : OK")
    else:
        print("Santé : Critique !")

    print("\n--- 3. BOUCLES ---")

    print("Boucle FOR (compter de 0 à 2) :")
    # range(3) génère 0, 1, 2
    for i in range(3):
        print(f"  Étape {i}")

    print("Boucle WHILE (compte à rebours) :")
    compteur = 3
    while compteur > 0:
        print(f"  {compteur}...")
        compteur -= 1 # Équivaut à compteur = compteur - 1
    print("  Décollage !")

if __name__ == "__main__":
    main()
