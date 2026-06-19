#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comment IMPORTER et utiliser ton propre module (ici : outils_math.py).

Ce fichier montre les deux formes d'import les plus courantes.
Lance-le avec :  python3 usage_module.py
(Il faut être dans le même dossier que outils_math.py.)
"""

# --- Forme 1 : importer tout le module, puis préfixer par son nom ---
# On écrit le nom du FICHIER, sans le ".py".
import outils_math

# --- Forme 2 : importer seulement la fonction voulue (plus de préfixe) ---
from outils_math import perimetre_cercle


def main():
    rayon = 5

    # Forme 1 : on doit préfixer par "outils_math."
    aire = outils_math.aire_cercle(rayon)
    print(f"Aire d'un cercle de rayon {rayon} : {aire:.2f}")

    # Forme 2 : importée directement, on l'appelle sans préfixe
    perimetre = perimetre_cercle(rayon)
    print(f"Périmètre d'un cercle de rayon {rayon} : {perimetre:.2f}")


if __name__ == "__main__":
    main()
