#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 09 : tests & qualité

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""


def est_palindrome(mot):
    """Pareil à l'endroit et à l'envers."""
    return mot == mot[::-1]      # [::-1] renvoie la chaîne inversée


def inverser(texte):
    """Texte à l'envers."""
    return texte[::-1]


def factorielle(n):
    """n! par une boucle."""
    resultat = 1
    for i in range(2, n + 1):    # 2, 3, ..., n  (commencer à 2 suffit ; ×1 est inutile)
        resultat *= i
    return resultat              # pour n = 0, la boucle ne tourne pas → resultat reste 1


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
    print("--- Tests — module 09 (solutions) ---")
    res = [
        _check("est_palindrome('kayak')", est_palindrome("kayak"), True),
        _check("est_palindrome('python')", est_palindrome("python"), False),
        _check("inverser('abc')", inverser("abc"), "cba"),
        _check("factorielle(5)", factorielle(5), 120),
        _check("factorielle(0)", factorielle(0), 1),
    ]
    print(f"\n{sum(res)}/{len(res)} tests réussis")


if __name__ == "__main__":
    _verifier()
