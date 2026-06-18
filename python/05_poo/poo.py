#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstration de la POO (Programmation Orientée Objet) en Python.
"""

# Classe parente (générique)
class Vehicule:
    def __init__(self, nom, vitesse_max):
        self.nom = nom
        self.vitesse_max = vitesse_max
    
    def se_deplacer(self):
        print(f"Le véhicule {self.nom} avance.")

# Classe enfant (spécifique) qui hérite de Vehicule
class Voiture(Vehicule):
    def __init__(self, nom, vitesse_max, nb_portes):
        # On appelle le constructeur de la classe parente
        super().__init__(nom, vitesse_max)
        self.nb_portes = nb_portes
    
    # On remplace (override) une méthode du parent
    def se_deplacer(self):
        print(f"La voiture {self.nom} roule sur ses 4 roues à {self.vitesse_max} km/h.")

def main():
    # Création d'un objet
    ma_voiture = Voiture("Peugeot 208", 180, 5)
    
    # Accès aux attributs
    print(f"Marque : {ma_voiture.nom}")
    
    # Appel des méthodes
    ma_voiture.se_deplacer()

if __name__ == "__main__":
    main()
