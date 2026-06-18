#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemple de tests unitaires avec pytest.
Pour lancer ce fichier : 'pytest test_demo.py'
"""

# La fonction que nous voulons tester
def nettoyer_nom(nom):
    """Supprime les espaces inutiles et met en majuscule."""
    return nom.strip().upper()

# --- LES TESTS ---

def test_nettoyer_nom_simple():
    assert nettoyer_nom("alice") == "ALICE"

def test_nettoyer_nom_avec_espaces():
    assert nettoyer_nom("  bob  ") == "BOB"

def test_nettoyer_nom_vide():
    assert nettoyer_nom("") == ""

# Astuce : pytest cherchera toutes les fonctions qui commencent par 'test_'
