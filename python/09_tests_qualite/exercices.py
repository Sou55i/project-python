#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 09 : tests & qualité (approche TDD)

Ici on inverse la logique : LES TESTS SONT DÉJÀ ÉCRITS (tout en bas).
Ton travail : implémenter les fonctions pour faire passer les tests au VERT.
C'est exactement la démarche TDD (Test-Driven Development) : rouge → vert.

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Bonus : ce sont des asserts, comme pytest. Tu peux aussi écrire un
     fichier test_xxx.py et lancer `pytest`.
"""


def est_palindrome(mot):
    """Renvoie True si `mot` se lit pareil à l'endroit et à l'envers.
    Ex : est_palindrome("kayak") -> True ; est_palindrome("python") -> False
    Indice : on peut inverser une chaîne avec mot[::-1].
    """
    # TODO
    ...


def inverser(texte):
    """Renvoie `texte` à l'envers.
    Ex : inverser("abc") -> "cba"
    """
    # TODO
    ...


def factorielle(n):
    """Renvoie n! = 1 × 2 × ... × n.   factorielle(0) vaut 1.
    Ex : factorielle(5) -> 120
    """
    # TODO : une boucle, ou la récursivité
    ...


# ════════════════════════════════════════════════════════════════════
#  Les TESTS (comme pytest) — NE PAS MODIFIER
# ════════════════════════════════════════════════════════════════════
def _check(nom, obtenu, attendu):
    ok = obtenu == attendu
    print(f"{'✅' if ok else '❌'} {nom}")
    if not ok:
        print(f"     attendu : {attendu!r}")
        print(f"     obtenu  : {obtenu!r}")
    return ok


def _verifier():
    print("--- Tests — module 09 ---")
    res = []

    def essai(nom, fn, attendu):
        try:
            obtenu = fn()
        except Exception as e:
            obtenu = f"ERREUR: {e}"
        res.append(_check(nom, obtenu, attendu))

    essai("est_palindrome('kayak')", lambda: est_palindrome("kayak"), True)
    essai("est_palindrome('python')", lambda: est_palindrome("python"), False)
    essai("inverser('abc')", lambda: inverser("abc"), "cba")
    essai("factorielle(5)", lambda: factorielle(5), 120)
    essai("factorielle(0)", lambda: factorielle(0), 1)

    print(f"\n{sum(res)}/{len(res)} tests réussis")


if __name__ == "__main__":
    _verifier()
