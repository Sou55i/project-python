#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EXERCICES — Module 08 : asyncio

  1. Complète chaque fonction (remplace la ligne `...`).
  2. Lance :   python3 exercices.py
  3. Vise 100 % de ✅. Corrigé dans solutions.py.
"""

import asyncio


async def addition_async(a, b):
    """Fonction ASYNCHRONE qui renvoie a + b.
    Doit contenir un `await asyncio.sleep(0)` (simule un point d'attente),
    puis renvoyer la somme.
    """
    # TODO : await asyncio.sleep(0) puis return a + b
    ...


async def executer_tout(coroutines):
    """Reçoit une LISTE de coroutines, les lance toutes ENSEMBLE et renvoie
    la liste de leurs résultats (dans l'ordre).
    Indice : asyncio.gather(*coroutines) — n'oublie pas le `await` et l'étoile `*`.
    """
    # TODO
    ...


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


async def _scenario():
    r1 = await addition_async(2, 3)
    r2 = await executer_tout([addition_async(1, 1), addition_async(10, 5)])
    return r1, r2


def _verifier():
    print("--- Vérification — module 08 ---")
    try:
        r1, r2 = asyncio.run(_scenario())
    except Exception as e:
        r1, r2 = f"ERREUR: {e}", f"ERREUR: {e}"
    res = [
        _check("addition_async(2, 3)", r1, 5),
        _check("executer_tout([...])", r2, [2, 15]),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
