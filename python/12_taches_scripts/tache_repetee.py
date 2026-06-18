"""
MODULE 04 - Une tâche qui se répète toute seule
================================================
Démo de planification EN PUR PYTHON avec la bibliothèque 'schedule'.
Ici, on exécute une petite tâche toutes les 2 secondes, et on s'arrête
automatiquement après 3 répétitions (pour ne pas tourner à l'infini en démo).

Nécessite : pip install -r python/requirements.txt  (pour 'schedule')

Lance-le :  python3 python/12_taches_scripts/tache_repetee.py

Dans la vraie vie, on remplacerait 'every(2).seconds' par 'every().day.at("08:00")'
et on laisserait le programme tourner (ou on utiliserait cron / Planificateur Windows).

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS   : time, datetime, et la bibliothèque schedule.
   2. FONCTION  : ma_tache() = l'action qu'on veut répéter.
   3. PROGRAMME : le bloc __main__ (a) programme la répétition,
                  (b) lance une boucle qui "fait vivre" le planificateur.
"""

import time                        # 'time.sleep()' fait une PAUSE
from datetime import datetime      # pour afficher l'heure courante

import schedule                    # bibliothèque tierce de planification

# Une variable GLOBALE (déclarée ici, en dehors de toute fonction).
# Elle nous sert de compteur pour arrêter la démo après quelques tours.
compteur = 0


def ma_tache():
    """La tâche à répéter. Ici, elle affiche simplement l'heure."""
    # 'global compteur' = "je veux MODIFIER la variable compteur du dessus,
    # pas en créer une nouvelle locale à la fonction". Sans ça, le += planterait.
    global compteur
    compteur += 1                  # +1 à chaque exécution
    # %H:%M:%S = heure:minute:seconde
    maintenant = datetime.now().strftime("%H:%M:%S")
    print(f"[{maintenant}] Tâche exécutée (fois n°{compteur}) ✅")


if __name__ == "__main__":
    print("⏱️  Planification : la tâche s'exécute toutes les 2 secondes.")
    print("    (la démo s'arrête après 3 répétitions)\n")

    # On programme la répétition. Lecture quasi naturelle : "toutes les 2 secondes,
    # FAIS ma_tache". Note : on écrit 'ma_tache' SANS les parenthèses, car on donne
    # la fonction elle-même à schedule (il l'appellera lui-même au bon moment).
    # Autres exemples possibles :
    #   schedule.every().hour.do(ma_tache)
    #   schedule.every().day.at("08:00").do(ma_tache)
    #   schedule.every().monday.do(ma_tache)
    schedule.every(2).seconds.do(ma_tache)

    # Le planificateur ne "vit" que tant que ce programme tourne. Cette boucle
    # le maintient en vie et lui demande régulièrement s'il a du travail.
    while compteur < 3:            # on s'arrête une fois 3 exécutions atteintes
        schedule.run_pending()     # lance les tâches dont l'heure est venue
        time.sleep(1)              # pause d'1 seconde, pour ne pas saturer le processeur

    print("\n✅ Démo terminée.")
