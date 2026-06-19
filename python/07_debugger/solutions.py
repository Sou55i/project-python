#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 07 : débugger (les bugs corrigés et EXPLIQUÉS)

Lance :   python3 solutions.py   (doit être tout vert).
"""


def moyenne(notes):
    """Moyenne d'une liste de notes."""
    total = 0
    for note in notes:
        total += note         # ✔ CORRECTION : += additionne (au lieu de = qui écrasait)
    return total / len(notes)


def maximum(liste):
    """Plus grand élément (marche aussi avec des négatifs)."""
    plus_grand = liste[0]     # ✔ CORRECTION : partir du PREMIER élément, pas de 0
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand


def compter_voyelles(mot):
    """Compte les voyelles."""
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre in voyelles:   # ✔ CORRECTION : "in" (et non "not in")
            total += 1
    return total


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 07 (solutions) ---")
    res = [
        _check("moyenne([10,20,30])", moyenne([10, 20, 30]), 20.0),
        _check("maximum([-5,-2,-9])", maximum([-5, -2, -9]), -2),
        _check("maximum([3,9,4])", maximum([3, 9, 4]), 9),
        _check("compter_voyelles('bonjour')", compter_voyelles("bonjour"), 3),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
