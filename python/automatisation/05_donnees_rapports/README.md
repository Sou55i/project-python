# Module 05 — Données et rapports automatiques

Le module final, et le plus gratifiant : transformer des **données brutes** (un export CSV
en vrac) en un **rapport propre** (totaux, moyennes, classements, fichier Excel), le tout
automatiquement. C'est ce que font des milliers de gens **à la main** dans Excel chaque jour.

> Fichier du module : `rapport_ventes.py`. Il crée lui-même un jeu de données de démo.
> Nécessite `pandas` et `openpyxl` (`pip install -r python/requirements.txt`).

---

## 1. Pourquoi `pandas` ?

On pourrait tout faire avec le module `csv` du module 02… mais dès qu'il s'agit de
**calculer, regrouper, filtrer, trier** des milliers de lignes, ça devient vite pénible.

**`pandas`** est la bibliothèque reine de la manipulation de données en Python. Elle
introduit un objet central : le **DataFrame**, qui est **un tableau intelligent**, exactement
comme une feuille Excel — mais pilotable par du code.

> 🧠 Image mentale : un **DataFrame = une feuille Excel dans une variable**. Lignes,
> colonnes, en-têtes… mais sur laquelle tu peux faire des calculs en une ligne de code,
> de façon **reproductible** (même résultat à chaque exécution, sans clic manuel).

---

## 2. Charger des données

`pandas` lit la plupart des formats en **une ligne** :

```python
import pandas as pd          # 'pd' est l'abréviation universelle, par convention

df = pd.read_csv("ventes.csv")     # df = "DataFrame", le nom habituel
# pd.read_excel("ventes.xlsx")     # marche aussi pour Excel
```

Premiers réflexes pour explorer un tableau qu'on découvre :

| Commande | Ce qu'elle montre |
|----------|-------------------|
| `df.head()` | les 5 premières lignes |
| `df.shape` | (nombre de lignes, nombre de colonnes) |
| `df.columns` | les noms des colonnes |
| `df.info()` | type de chaque colonne et valeurs manquantes |
| `df.describe()` | statistiques (moyenne, min, max…) des colonnes numériques |

---

## 3. Sélectionner et filtrer

On accède à une **colonne** par son nom :

```python
df["produit"]            # toute la colonne "produit"
df["prix"].sum()         # la somme de la colonne "prix"
df["prix"].mean()        # la moyenne
```

On **filtre** les lignes avec une condition (comme un « filtre » Excel) :

```python
# Garde seulement les ventes supérieures à 100 €
grosses_ventes = df[df["montant"] > 100]
```

Lis `df[df["montant"] > 100]` comme : *« dans `df`, garde les lignes où la colonne montant
dépasse 100 »*.

---

## 4. Regrouper : le cœur des rapports (`groupby`)

C'est **l'opération clé** d'un rapport : regrouper des lignes par catégorie et calculer un
total/une moyenne par groupe. C'est l'équivalent du **tableau croisé dynamique** d'Excel.

```python
# Chiffre d'affaires total par produit :
ca_par_produit = df.groupby("produit")["montant"].sum()
```

`groupby("produit")` rassemble toutes les lignes d'un même produit, puis `["montant"].sum()`
additionne leurs montants. En une ligne, tu obtiens ce qui prendrait plusieurs manipulations
manuelles dans un tableur.

---

## 5. Exporter le résultat

Une fois le rapport calculé, on l'enregistre pour le partager :

```python
ca_par_produit.to_csv("rapport.csv")               # en CSV
ca_par_produit.to_excel("rapport.xlsx")            # en Excel (nécessite openpyxl)
```

> 🔁 **La grande idée du module** : tu écris ce code **une fois**. Ensuite, chaque semaine,
> tu remplaces le fichier de données et tu relances le script → ton rapport est régénéré en
> une seconde, sans erreur. C'est ça, l'automatisation des données.

---

## ▶️ À toi de jouer

```bash
python3 python/automatisation/05_donnees_rapports/rapport_ventes.py
```

Le script génère un faux fichier de ventes, calcule plusieurs indicateurs (chiffre
d'affaires total, CA par produit, meilleur vendeur…) et exporte un rapport `.csv` et `.xlsx`.
Ouvre les fichiers produits dans `exemples/` pour voir le résultat.

🎉 **Bravo, tu as terminé le parcours Automatisation !** Tu as maintenant les bases pour
écrire tes propres scripts utiles au quotidien. La suite ? Choisis une corvée répétitive de
ta vraie vie et essaie de l'automatiser.
