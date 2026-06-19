#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SOLUTIONS — Module 08 : asyncio

Corrigé commenté. Lance :   python3 solutions.py   (doit être tout vert).
"""

import asyncio


async def addition_async(a, b):
    """Somme, version asynchrone."""
    await asyncio.sleep(0)      # point d'attente : rend la main à la boucle d'événements
    return a + b


async def executer_tout(coroutines):
    """Lance toutes les coroutines ensemble et renvoie leurs résultats."""
    return await asyncio.gather(*coroutines)   # * "déballe" la liste en arguments séparés


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


async def _scenario():
    r1 = await addition_async(2, 3)
    r2 = await executer_tout([addition_async(1, 1), addition_async(10, 5)])
    return r1, r2


def _verifier():
    print("--- Vérification — module 08 (solutions) ---")
    r1, r2 = asyncio.run(_scenario())
    res = [
        _check("addition_async(2, 3)", r1, 5),
        _check("executer_tout([...])", r2, [2, 15]),
    ]
    print(f"\n{sum(res)}/{len(res)} réussis")


if __name__ == "__main__":
    _verifier()
