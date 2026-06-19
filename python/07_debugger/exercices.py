#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 07 : débugger (TROUVE ET CORRIGE LES BUGS)

Ici, c'est différent : les fonctions ci-dessous CONTIENNENT DES BUGS.
  1. Lance :   python3 exercices.py   → tu verras des ❌.
  2. Pour chaque ❌, trouve POURQUOI le résultat est faux.
     Outils : ajoute des print(...), ou pose un breakpoint() et inspecte.
  3. Corrige le code jusqu'à obtenir 100 % de ✅.
  4. Corrigé expliqué dans solutions.py.
"""


def moyenne(notes):
    """Devrait renvoyer la moyenne d'une liste de notes.
    moyenne([10, 20, 30]) devrait valoir 20.0
    """
    total = 0
    for note in notes:
        total = note          # 🐞 BUG : à chaque tour, on ÉCRASE total au lieu de l'additionner
    return total / len(notes)


def maximum(liste):
    """Devrait renvoyer le plus grand élément.
    maximum([-5, -2, -9]) devrait valoir -2
    """
    plus_grand = 0            # 🐞 BUG : partir de 0 casse tout si tous les nombres sont négatifs
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand


def compter_voyelles(mot):
    """Devrait compter les voyelles (a, e, i, o, u).
    compter_voyelles("bonjour") devrait valoir 3   (o, o, u)
    """
    voyelles = "aeiou"
    total = 0
    for lettre in mot:
        if lettre not in voyelles:   # 🐞 BUG : la condition est INVERSÉE (compte les consonnes)
            total += 1
    return total


# ════════════════════════════════════════════════════════════════════
#  Auto-vérification — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Vérification — module 07 (corrige les bugs !) ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("moyenne([10,20,30])", lambda: moyenne([10, 20, 30]), 20.0)
    essai("maximum([-5,-2,-9])", lambda: maximum([-5, -2, -9]), -2)
    essai("maximum([3,9,4])", lambda: maximum([3, 9, 4]), 9)
    essai("compter_voyelles('bonjour')", lambda: compter_voyelles("bonjour"), 3)

    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
