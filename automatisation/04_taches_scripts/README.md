# Module 04 — Scripts réutilisables et tâches planifiées

Jusqu'ici, nos scripts faisaient une chose figée. Ici, on apprend à en faire de **vrais
outils** : configurables au lancement, et capables de tourner **tout seuls** à heure fixe
(sauvegarde nocturne, rapport hebdomadaire…).

> Fichiers du module : `sauvegarde.py` (un outil avec options) et `tache_repetee.py`
> (une tâche qui se répète toute seule).

---

## 1. `if __name__ == "__main__"` : la ligne mystérieuse

Tu l'as déjà croisée. Voici enfin son explication.

Un fichier Python peut servir à **deux choses** :
1. être **lancé directement** (`python3 sauvegarde.py`),
2. être **importé** par un autre fichier pour réutiliser ses fonctions.

La ligne `if __name__ == "__main__":` veut dire :
**« exécute ce bloc UNIQUEMENT si le fichier est lancé directement, pas s'il est importé. »**

C'est la **bonne pratique** : on range nos fonctions au-dessus (réutilisables), et le code
qui « démarre » le programme va dans ce bloc, à la fin. Ainsi, importer le fichier ne
déclenche pas tout par surprise.

---

## 2. Donner des options à un script : `argparse`

Un bon outil ne code pas ses valeurs « en dur ». On veut pouvoir écrire :

```bash
python3 sauvegarde.py --source mes_docs --destination sauvegardes
```

Ces `--source` et `--destination` sont des **arguments en ligne de commande**. Le module
**`argparse`** (inclus dans Python) les gère pour toi : il lit les arguments, vérifie qu'ils
sont présents, et génère même une **aide automatique** (`--help`).

```python
import argparse

parseur = argparse.ArgumentParser(description="Sauvegarde un dossier")
parseur.add_argument("--source", required=True, help="Dossier à sauvegarder")
parseur.add_argument("--destination", default="sauvegardes", help="Où copier")
args = parseur.parse_args()

print(args.source, args.destination)
```

> 💡 Avantage énorme : ton script devient **réutilisable** pour n'importe quel dossier,
> sans toucher au code. Et `python3 sauvegarde.py --help` documente tout seul son usage.

---

## 3. Planifier une tâche : la faire tourner toute seule

Automatiser, c'est aussi **ne plus avoir à lancer le script soi-même**. Trois approches,
de la plus simple à la plus « système » :

### a) En pur Python avec `schedule` (le plus simple pour débuter)

La bibliothèque `schedule` fait répéter une fonction à intervalle régulier, **tant que le
programme tourne** :

```python
import schedule, time

schedule.every(10).seconds.do(ma_fonction)
schedule.every().day.at("08:00").do(ma_fonction)

while True:               # le programme doit rester ouvert
    schedule.run_pending()
    time.sleep(1)
```

Pratique pour apprendre, mais il faut que le terminal reste ouvert.

### b) `cron` sur Mac / Linux (planification système)

`cron` est le planificateur intégré de Mac/Linux. Tu édites ta liste de tâches avec
`crontab -e` et tu ajoutes une ligne :

```cron
# ┌ minute  ┌ heure  ┌ jour  ┌ mois  ┌ jour de semaine
  0          8        *       *       *     python3 /chemin/sauvegarde.py
# = tous les jours à 08h00
```

Avantage : ça tourne **même si aucun terminal n'est ouvert**, géré par le système.

### c) Le Planificateur de tâches sur Windows

Sur Windows, l'équivalent graphique s'appelle **« Planificateur de tâches »**
(*Task Scheduler*). Tu crées une tâche, choisis le déclencheur (ex : tous les jours à 8h)
et l'action (« démarrer un programme » → `python` avec ton script en argument).

> 📌 À retenir : `schedule` = simple, dépend du programme ouvert. `cron`/Planificateur =
> géré par le système, plus robuste pour la production.

---

## 4. Les logs : savoir ce qu'a fait un script qui tourne seul

Quand un script tourne sans toi (la nuit, par exemple), tu as besoin de **traces** pour
savoir s'il a réussi ou échoué. Plutôt que `print()`, on utilise le module **`logging`**,
qui horodate chaque message et peut l'écrire dans un fichier :

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logging.info("Sauvegarde démarrée")
logging.error("Le dossier source est introuvable")
```

---

## ▶️ À toi de jouer

```bash
# Affiche l'aide générée automatiquement par argparse :
python3 automatisation/04_taches_scripts/sauvegarde.py --help

# Lance une vraie sauvegarde (crée des dossiers de test) :
python3 automatisation/04_taches_scripts/sauvegarde.py

# Démo de planification (s'arrête tout seul après quelques répétitions) :
python3 automatisation/04_taches_scripts/tache_repetee.py
```

➡️ Module suivant : [`05_donnees_rapports`](../05_donnees_rapports/).
