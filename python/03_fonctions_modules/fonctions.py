#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemples sur les fonctions en Python.
"""

# Une fonction simple avec une valeur par défaut
def creer_message(nom, role="Guerrier"):
    """
    Ceci est une Docstring. Elle explique ce que fait la fonction.
    """
    return f"Bienvenue {nom}, le {role} !"

# Fonction avec un nombre variable d'arguments (*args)
def faire_somme(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

def main():
    # Appel simple
    print(creer_message("Baba"))
    
    # Appel avec arguments nommés
    print(creer_message(role="Mage", nom="Gandalf"))

    # Appel avec *args
    resultat = faire_somme(10, 20, 30, 40)
    print(f"Somme variable : {resultat}")

if __name__ == "__main__":
    main()
