# 🛠️ Mini-projets concrets

Une fois les modules `00` à `07` digérés, voici des **projets complets** qui combinent
plusieurs notions. C'est l'étape la plus importante : c'est en construisant de vrais
petits outils qu'on devient autonome.

> Chaque script commence par un bloc **« 🗺️ CHEMINEMENT DU SCRIPT »** qui résume ses
> étapes : lis-le en premier pour comprendre la logique avant de plonger dans le code.

## Les projets

| Projet | Ce qu'il fait | Notions combinées | Dépendances |
|--------|---------------|-------------------|-------------|
| [`organiser_par_date.py`](./organiser_par_date.py) | Range des fichiers dans des sous-dossiers par mois de modification (`AAAA-MM`) | Module 02 (pathlib, dates, dossiers) | Aucune (stdlib) |
| [`carnet_contacts.py`](./carnet_contacts.py) | Un carnet de contacts en ligne de commande, sauvegardé en JSON | Modules 01, 02, 04 (dicts, JSON, argparse) | Aucune (stdlib) |
| [`suivi_meteo.py`](./suivi_meteo.py) | Récupère la météo de plusieurs villes (API) et écrit un rapport CSV | Modules 03, 05 (API `requests`, CSV) | `requests` + Internet |

## Lancer les projets

```bash
# 1. Organiser des fichiers par date (crée un dossier de démo sans risque)
python3 python/automatisation/projets/organiser_par_date.py

# 2. Carnet de contacts (sous-commandes)
python3 python/automatisation/projets/carnet_contacts.py ajouter --nom Alice --tel 0612345678
python3 python/automatisation/projets/carnet_contacts.py lister
python3 python/automatisation/projets/carnet_contacts.py chercher --nom alice
python3 python/automatisation/projets/carnet_contacts.py --help

# 3. Suivi météo (nécessite Internet + pip install -r python/requirements.txt)
python3 python/automatisation/projets/suivi_meteo.py
```

> 💡 Les fichiers produits par les projets (données de démo, contacts, rapports) sont créés
> dans un sous-dossier `exemples/` ignoré par git : tu peux expérimenter sans polluer le dépôt.

## Et ensuite ?

Le meilleur exercice : **prends une corvée répétitive de ta vraie vie** et essaie de
l'automatiser en t'inspirant de ces projets. C'est comme ça qu'on apprend pour de bon. 🚀
