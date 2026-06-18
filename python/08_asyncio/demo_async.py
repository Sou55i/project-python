#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstration de la puissance de l'asynchrone.
"""

import asyncio
import time

# Une tâche qui simule une attente (ex: appel réseau)
async def tache_longue(n):
    print(f"  [Tâche {n}] Démarrage...")
    await asyncio.sleep(1) # Attente asynchrone
    print(f"  [Tâche {n}] Terminé !")
    return f"Résultat {n}"

async def main():
    print("Lancement de 3 tâches en PARALLÈLE...")
    debut = time.perf_counter()

    # On lance les tâches et on attend qu'elles finissent toutes
    resultats = await asyncio.gather(
        tache_longue(1),
        tache_longue(2),
        tache_longue(3)
    )

    fin = time.perf_counter()
    print(f"\nRésultats : {resultats}")
    print(f"Temps total : {fin - debut:.2f} secondes")
    print("(En synchrone, cela aurait pris 3 secondes !)")

if __name__ == "__main__":
    asyncio.run(main())
