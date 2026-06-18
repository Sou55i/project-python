#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script avec un bug volontaire pour s'entraîner au debug.
Le but est de calculer la moyenne, mais quelque chose ne va pas.
"""

def calculer_moyenne(nombres):
    total = 0
    for n in nombres:
        # Imaginons qu'on fasse une erreur ici
        total += n
    
    # Bug : on divise par une valeur fixe au lieu de len(nombres)
    # AJOUTE UN breakpoint() ICI pour inspecter 'total' et 'nombres'
    # breakpoint()
    
    return total / 5 

def main():
    mes_notes = [10, 15, 20] # Moyenne devrait être 15
    resultat = calculer_moyenne(mes_notes)
    
    print(f"Ma moyenne est : {resultat}")
    print("Est-ce correct ? (Spoiler: Non, car on a 3 notes, pas 5)")

if __name__ == "__main__":
    main()
