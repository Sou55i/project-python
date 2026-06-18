# Module 15 — Construire un script de zéro (le raisonnement en pratique)

Ce module est le **passage à l'acte** des deux guides transverses :
- 🔍 **[../COMPRENDRE_LE_CODE.md](../COMPRENDRE_LE_CODE.md)** — lire/décoder n'importe quel code.
- 🧭 **[../ECRIRE_UN_SCRIPT.md](../ECRIRE_UN_SCRIPT.md)** — la méthode pour raisonner et écrire.

Ici, **deux scripts réels**, écrits en suivant la méthode (objectif → entrées/sorties →
étapes → recherche des outils → code), et **commentés pas à pas** pour que tu voies *pourquoi*
chaque morceau est là.

## Les scripts

| Script | Ce qu'il fait | Notions / outils |
|--------|---------------|------------------|
| [`compter_fichiers.py`](./compter_fichiers.py) | Compte les fichiers d'un dossier (option `--recursif`) | `argparse` (arguments), `pathlib` (`iterdir`/`rglob`/`is_file`), `if __name__` |
| [`json_vers_sql.py`](./json_vers_sql.py) | Lit un JSON et génère/insère des `INSERT` SQL | `json`, `sqlite3`, `', '.join(...)`, placeholders `?` |

## Lancer

```bash
# Compter les fichiers du dossier courant, puis d'un autre dossier, puis en récursif :
python3 python/15_construire_un_script/compter_fichiers.py
python3 python/15_construire_un_script/compter_fichiers.py /tmp
python3 python/15_construire_un_script/compter_fichiers.py . --recursif

# JSON -> SQL (fabrique ses données de démo, affiche le SQL, remplit une base SQLite) :
python3 python/15_construire_un_script/json_vers_sql.py
```

> 💡 Lis le code **en même temps** que `ECRIRE_UN_SCRIPT.md` : tu y retrouveras, étape par
> étape, *comment on a su* qu'il fallait `argparse`, `iterdir`, `join`, les placeholders `?`…
>
> 🎯 **Ton entraînement** : reprends un de ces scripts et **modifie-le** (compter seulement
> les `.txt` ; exporter le SQL dans un fichier `.sql` ; ajouter une colonne). C'est en
> bricolant qu'on apprend à « trouver les arguments ».

Les fichiers générés vont dans un sous-dossier `exemples/` (ignoré par git).
