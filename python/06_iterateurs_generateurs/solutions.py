#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 06 : itérateurs & générateurs

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""


def filtrer_positifs(nombres):
    """Garde les nombres > 0."""
    return [n for n in nombres if n > 0]


def noms_en_majuscules(noms):
    """Chaque nom en majuscules."""
    return [nom.upper() for nom in noms]


def somme_carres(n):
    """Somme des carrés de 0 à n-1 (expression génératrice : pas de liste créée)."""
    return sum(i ** 2 for i in range(n))


def pairs_jusqua(limite):
    """Générateur des pairs de 0 à limite (exclu)."""
    n = 0
    while n < limite:
        yield n          # livre n, met en pause, reprend ici au next suivant
        n += 2


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
    print("--- Vérification — module 06 (solutions) ---")
    res = [
        _check("filtrer_positifs", filtrer_positifs([3, -1, 0, 7, -2]), [3, 7]),
        _check("noms_en_majuscules", noms_en_majuscules(["ada", "bob"]), ["ADA", "BOB"]),
        _check("somme_carres(4)", somme_carres(4), 14),
        _check("list(pairs_jusqua(10))", list(pairs_jusqua(10)), [0, 2, 4, 6, 8]),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
