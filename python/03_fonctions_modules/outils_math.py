#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Un petit MODULE d'exemple : un simple fichier .py qui regroupe des fonctions.

Un module n'a rien de spécial : c'est un fichier que d'AUTRES fichiers peuvent
importer pour réutiliser ses fonctions (voir usage_module.py).
"""

import math


def aire_cercle(rayon):
    """Renvoie l'aire d'un cercle de rayon donné (π × r²)."""
    return math.pi * rayon ** 2


def perimetre_cercle(rayon):
    """Renvoie le périmètre (la circonférence) d'un cercle (2 × π × r)."""
    return 2 * math.pi * rayon


# Ce bloc ne s'exécute QUE si on lance ce fichier directement
# (python3 outils_math.py). Il ne s'exécute PAS quand le fichier est importé.
# C'est ce qui permet à usage_module.py d'importer les fonctions ci-dessus
# SANS déclencher ce petit test.
if __name__ == "__main__":
    print("Test interne du module outils_math :")
    print(f"  aire d'un cercle de rayon 2 = {aire_cercle(2):.2f}")
    print(f"  périmètre d'un cercle de rayon 2 = {perimetre_cercle(2):.2f}")
