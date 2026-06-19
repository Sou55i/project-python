# 🧵 Fil rouge — un gestionnaire de dépenses, construit pas à pas

> 🎯 **Pourquoi ce dossier ?** Les autres projets te montrent un programme **déjà fini**. Ici,
> on fait l'inverse : on regarde **UN même programme grandir**, étape par étape, exactement comme
> dans la vraie vie. Tu pars de 3 variables et tu finis avec une appli en ligne de commande —
> en ajoutant **une seule notion à la fois**.

> 🧠 **La grande leçon** : un vrai logiciel ne s'écrit jamais parfait du premier coup. On écrit
> une **petite chose qui marche**, puis on l'améliore. Ce fil rouge te montre ce mouvement.

---

## Les 5 étapes

| Étape | Fichier | Ce qu'on ajoute | Notions (modules) |
|------:|---------|-----------------|-------------------|
| 1 | [`etape_1_une_depense.py`](./etape_1_une_depense.py) | représenter **une** dépense (variables → dict) | 01, 02 |
| 2 | [`etape_2_liste.py`](./etape_2_liste.py) | **plusieurs** dépenses + total (liste, boucle) | 01, 02 |
| 3 | [`etape_3_fonctions.py`](./etape_3_fonctions.py) | ranger le code en **fonctions** réutilisables | 03, 13 |
| 4 | [`etape_4_sauvegarde.py`](./etape_4_sauvegarde.py) | **sauvegarder** dans un fichier JSON (persistance) | 04, 10 |
| 5 | [`etape_5_cli.py`](./etape_5_cli.py) | une vraie **appli** avec des commandes (`argparse`) | 12, 13 |

Lance-les dans l'ordre et **compare** : à chaque étape, demande-toi *« qu'est-ce qui a changé,
et quel problème ça résout ? »* (la réponse est en commentaire à la fin de chaque fichier).

```bash
python3 python/projets/fil_rouge/etape_1_une_depense.py
python3 python/projets/fil_rouge/etape_2_liste.py
python3 python/projets/fil_rouge/etape_3_fonctions.py
python3 python/projets/fil_rouge/etape_4_sauvegarde.py     # relance-le plusieurs fois !

# L'appli finale :
python3 python/projets/fil_rouge/etape_5_cli.py ajouter --montant 12.5 --categorie courses
python3 python/projets/fil_rouge/etape_5_cli.py ajouter --montant 40 --categorie transport
python3 python/projets/fil_rouge/etape_5_cli.py lister
python3 python/projets/fil_rouge/etape_5_cli.py rapport
```

---

## Le « pourquoi » de chaque saut

- **1 → 2** : une dépense seule ne sert à rien ; on veut les **suivre toutes** → une **liste**.
- **2 → 3** : le code se **répète** (plusieurs boucles) → on le range en **fonctions** nommées.
- **3 → 4** : tout **disparaît** à la fin du programme → on **sauvegarde** sur le disque (JSON).
- **4 → 5** : la dépense est **codée en dur** → on laisse l'utilisateur **piloter** via des
  commandes (`ajouter`, `lister`, `rapport`).

> 🛠️ **À toi de continuer le fil rouge** (mêmes étapes que les pros) :
> - ajoute une commande `supprimer --numero N` (inspire-toi de [`../todo.py`](../todo.py)) ;
> - filtre le `rapport` par mois ;
> - refactore le tout en une **classe** `Budget` (révise le [module 05](../../05_poo/)) ;
> - écris des **tests** pour `total_par_categorie` (révise le [module 09](../../09_tests_qualite/)).

➡️ Besoin de la méthode pour transformer une idée en code ? Relis
[`../../ECRIRE_UN_SCRIPT.md`](../../ECRIRE_UN_SCRIPT.md).
