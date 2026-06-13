"""
MODULE 04 - Une tâche qui se répète toute seule
================================================
Démo de planification EN PUR PYTHON avec la bibliothèque 'schedule'.
Ici, on exécute une petite tâche toutes les 2 secondes, et on s'arrête
automatiquement après 3 répétitions (pour ne pas tourner à l'infini en démo).

Nécessite : pip install -r requirements.txt  (pour 'schedule')

Lance-le :  python3 automatisation/04_taches_scripts/tache_repetee.py

Dans la vraie vie, on remplacerait 'every(2).seconds' par 'every().day.at("08:00")'
et on laisserait le programme tourner (ou on utiliserait cron / Planificateur Windows).
"""

import time
from datetime import datetime

import schedule

# Compteur global pour arrêter la démo après quelques tours.
compteur = 0


def ma_tache():
    """La tâche à répéter. Ici, elle affiche simplement l'heure."""
    global compteur
    compteur += 1
    maintenant = datetime.now().strftime("%H:%M:%S")
    print(f"[{maintenant}] Tâche exécutée (fois n°{compteur}) ✅")


if __name__ == "__main__":
    print("⏱️  Planification : la tâche s'exécute toutes les 2 secondes.")
    print("    (la démo s'arrête après 3 répétitions)\n")

    # On programme la répétition. Autres exemples possibles :
    #   schedule.every().hour.do(ma_tache)
    #   schedule.every().day.at("08:00").do(ma_tache)
    #   schedule.every().monday.do(ma_tache)
    schedule.every(2).seconds.do(ma_tache)

    # La boucle qui fait vivre le planificateur : il vérifie en continu
    # s'il est l'heure de lancer une tâche en attente.
    while compteur < 3:
        schedule.run_pending()   # lance les tâches dont l'heure est venue
        time.sleep(1)            # petite pause pour ne pas surcharger le processeur

    print("\n✅ Démo terminée.")
