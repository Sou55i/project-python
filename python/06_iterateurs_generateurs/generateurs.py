#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstration des générateurs et de l'efficacité mémoire.
"""

import sys

def main():
    print("--- 1. COMPREHENSION DE LISTE ---")
    nombres = [1, 2, 3, 4, 5]
    # On crée une nouvelle liste avec les carrés
    carres = [x**2 for x in nombres]
    print(f"Carrés : {carres}")

    print("\n--- 2. GÉNÉRATEURS (yield) ---")
    
    # Une liste de 10 000 nombres
    liste_geante = [i for i in range(10000)]
    
    # Un générateur de 10 000 nombres
    generateur_geant = (i for i in range(10000))
    
    print(f"Taille en mémoire de la LISTE : {sys.getsizeof(liste_geante)} octets")
    print(f"Taille en mémoire du GÉNÉRATEUR : {sys.getsizeof(generateur_geant)} octets")
    
    print("\nLe générateur ne contient pas les données, il SAIT comment les produire !")

    # Utilisation d'un générateur personnalisé
    def mon_generateur():
        print("  (Générateur) Je produis 1")
        yield 1
        print("  (Générateur) Je produis 2")
        yield 2

    gen = mon_generateur()
    print("Appel de next() :")
    print(f"Valeur reçue : {next(gen)}")
    print(f"Valeur reçue : {next(gen)}")

if __name__ == "__main__":
    main()
