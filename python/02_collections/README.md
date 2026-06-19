# 📦 Module 02 : Les collections (listes, dictionnaires, tuples, sets)

> 🎯 **Objectif** : jusqu'ici une variable contenait **une seule** valeur. Une **collection**
> en regroupe **plusieurs**. C'est ce qui rend les programmes vraiment utiles : gérer une liste
> de clients, un panier, des résultats… À la fin, tu sauras **choisir** la bonne collection et
> la manipuler avec aisance.

---

## 0. Pourquoi quatre collections différentes ?

Parce qu'elles répondent à des besoins différents. Voici la table de décision — garde-la sous
le coude, c'est elle qui te dira **laquelle utiliser** :

| Collection | Forme | Ordonnée ? | Modifiable ? | Doublons ? | Quand l'utiliser |
|------------|-------|:----------:|:------------:|:----------:|------------------|
| **liste** `list` | `[ ]` | ✅ | ✅ | ✅ | une suite d'éléments qui peut changer |
| **dictionnaire** `dict` | `{clé: valeur}` | ✅* | ✅ | clés uniques | associer une **étiquette** à une valeur |
| **tuple** `tuple` | `( )` | ✅ | ❌ | ✅ | un groupe **figé** (coordonnées, date…) |
| **set** `set` | `{ }` | ❌ | ✅ | ❌ | garder des valeurs **uniques**, dédoublonner |

> \* Depuis Python 3.7, le dictionnaire conserve l'ordre d'insertion.
>
> 🔎 **Le piège des symboles** : `[ ]` = liste, `( )` = tuple, `{ }` = dict **ou** set selon le
> contenu. Le détail de ces symboles est dans [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md).

---

## 1. Les listes (`list`) — la collection à tout faire

Une suite **ordonnée** d'éléments, entre **crochets** `[ ]`. C'est la plus courante.

```python
fruits = ["pomme", "banane", "cerise"]
```

### Accéder à un élément : l'indexation

Chaque élément a une **position** (un *index*) qui **commence à 0** :

```python
#          index :  0        1         2
fruits = ["pomme", "banane", "cerise"]
print(fruits[0])    # "pomme"   ← le PREMIER est à l'index 0, pas 1 !
print(fruits[2])    # "cerise"
print(fruits[-1])   # "cerise"  ← index négatif = on compte depuis la FIN
print(fruits[-2])   # "banane"
```

> 🧠 **« Pourquoi ça commence à 0 ? »** Question légitime. C'est une convention de presque
> tous les langages : l'index est une *distance depuis le début*. Le premier élément est à une
> distance de 0. Retiens : **dernier index = longueur − 1**.

### Le découpage (*slicing*) : prendre une tranche

```python
nombres = [10, 20, 30, 40, 50]
print(nombres[1:3])   # [20, 30]   ← du index 1 JUSQU'À 3 exclu
print(nombres[:2])    # [10, 20]   ← du début jusqu'à 2 exclu
print(nombres[2:])    # [30, 40, 50] ← de l'index 2 jusqu'à la fin
print(nombres[::-1])  # [50, 40, 30, 20, 10] ← inverse la liste
```

> 🔎 La règle des tranches : `[début:fin]` inclut `début`, **exclut** `fin`. Le nombre
> d'éléments obtenus est `fin - début`.

### Modifier une liste : les méthodes courantes

```python
fruits.append("orange")      # AJOUTE à la fin           → [..., "orange"]
fruits.insert(0, "kiwi")     # insère à une position     → ["kiwi", ...]
fruits.remove("banane")      # SUPPRIME par valeur
dernier = fruits.pop()       # retire ET RENVOIE le dernier élément
fruits.sort()                # trie sur place (ordre alphabétique/numérique)
print(len(fruits))           # nombre d'éléments
print("pomme" in fruits)     # True/False : l'élément est-il présent ?
```

> 🧠 **Méthode vs fonction** : `fruits.append(...)` (avec un point) est une **méthode** : une
> action que la liste **sait faire sur elle-même**. `len(fruits)` est une **fonction** qui
> *reçoit* la liste. Les deux formes coexistent — voir [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md).

### Parcourir une liste

```python
for fruit in fruits:                 # le plus courant : juste les valeurs
    print(fruit)

for i, fruit in enumerate(fruits):   # quand tu veux AUSSI l'index
    print(f"{i} : {fruit}")          # enumerate() donne (index, valeur)
```

---

## 2. Les dictionnaires (`dict`) — associer une clé à une valeur

Quand l'index numérique ne suffit pas, on veut nommer ses données. Le dictionnaire associe une
**clé** (une étiquette) à une **valeur**.

```python
pilote = {"nom": "Hamilton", "ecurie": "Mercedes", "titres": 7}
```

> 🧠 **L'image** : un vrai dictionnaire de langue. Tu cherches un **mot** (la clé) pour obtenir
> sa **définition** (la valeur). Ici la clé `"nom"` donne `"Hamilton"`.

### Lire, ajouter, modifier

```python
print(pilote["nom"])              # "Hamilton"  ← accès par la clé, entre crochets
pilote["points"] = 25            # AJOUTE une nouvelle paire clé:valeur
pilote["titres"] = 8             # MODIFIE une valeur existante (la clé existe déjà)
```

### Lire sans planter : `.get()`

```python
print(pilote["sponsor"])           # ❌ KeyError : la clé n'existe pas → plantage
print(pilote.get("sponsor"))       # ✅ None (pas de plantage)
print(pilote.get("sponsor", "—"))  # ✅ "—"  : valeur par défaut si absente
```

> 🔑 **Règle pratique** : `dico[clé]` quand tu es **sûr** que la clé existe ; `dico.get(clé, défaut)`
> quand elle pourrait manquer. C'est un motif que tu reverras partout.

### Parcourir un dictionnaire

```python
for cle in pilote:                       # par défaut, on parcourt les CLÉS
    print(cle, "→", pilote[cle])

for cle, valeur in pilote.items():       # le plus pratique : clé ET valeur d'un coup
    print(f"{cle} = {valeur}")

print(pilote.keys())     # toutes les clés
print(pilote.values())   # toutes les valeurs
```

---

## 3. Les tuples (`tuple`) — un groupe figé

Comme une liste, mais **non modifiable** (*immuable*) une fois créé. Entre **parenthèses** `( )`.

```python
coordonnees = (48.8566, 2.3522)   # latitude, longitude : ça ne doit pas changer
print(coordonnees[0])             # 48.8566  (on lit comme une liste)
# coordonnees[0] = 0.0            # ❌ TypeError : un tuple ne se modifie pas
```

### Quand préférer un tuple à une liste ?

- les données forment un **tout cohérent et figé** : une date `(2026, 6, 19)`, un point `(x, y)` ;
- tu veux **protéger** les données contre une modification accidentelle ;
- besoin d'une **clé de dictionnaire** composite (une liste ne peut pas être une clé, un tuple oui).

> 🔎 **L'affectation multiple**, que tu verras souvent, repose sur les tuples :
> ```python
> x, y = (10, 20)     # x reçoit 10, y reçoit 20  (les parenthèses sont même facultatives)
> a, b = b, a         # échange deux variables en une ligne (astuce classique)
> ```

---

## 4. Les sets (`set`) — des valeurs uniques

Une collection **non ordonnée** de valeurs **uniques** : les doublons disparaissent
automatiquement. Entre **accolades** `{ }`.

```python
nombres = {1, 2, 2, 3, 3, 3}      # devient {1, 2, 3}  : doublons éliminés
```

### L'usage n°1 : dédoublonner une liste

```python
emails = ["a@x.fr", "b@x.fr", "a@x.fr"]
uniques = set(emails)              # {"a@x.fr", "b@x.fr"}
uniques_liste = list(set(emails))  # repasse en liste si besoin
```

### Les opérations ensemblistes (comme en maths)

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)   # {2, 3}      intersection : présents dans les DEUX
print(a | b)   # {1, 2, 3, 4} union : présents dans l'un OU l'autre
print(a - b)   # {1}         différence : dans a mais pas dans b
```

> ⚠️ `{}` **tout seul** crée un **dictionnaire vide**, pas un set ! Pour un set vide, écris
> `set()`. C'est un piège classique.

---

## 5. Récapitulatif visuel

```
liste   [ ]   ordonnée, modifiable, doublons OK      → une suite qui évolue
dict    {k:v} clé → valeur                            → données étiquetées
tuple   ( )   ordonné, FIGÉ                           → un groupe constant
set     { }   unique, non ordonné                     → dédoublonner, ensembles
```

> 🧠 **Le réflexe de choix** : *« Ai-je besoin d'étiquettes ? »* → `dict`. *« Que des valeurs
> uniques ? »* → `set`. *« Ça doit rester figé ? »* → `tuple`. *« Sinon »* → `list`.

---

## 🏁 Exercices

1. **Lis et lance** [`collections_demo.py`](./collections_demo.py), puis modifie les valeurs.
2. **Inventaire** : crée un dictionnaire `stock = {"pommes": 5, "poires": 0}`. Affiche chaque
   produit et sa quantité avec `.items()`, puis affiche uniquement ceux en rupture (quantité 0).
3. **Dédoublonnage** : à partir de `notes = [12, 15, 12, 18, 15]`, obtiens la liste des notes
   distinctes, triées.

<details>
<summary>💡 Solution — exercice 2 (inventaire)</summary>

```python
stock = {"pommes": 5, "poires": 0, "kiwis": 3}
for produit, quantite in stock.items():
    print(f"{produit} : {quantite}")

print("En rupture :")
for produit, quantite in stock.items():
    if quantite == 0:
        print(f"  - {produit}")
```
</details>

<details>
<summary>💡 Solution — exercice 3 (dédoublonnage trié)</summary>

```python
notes = [12, 15, 12, 18, 15]
distinctes = sorted(set(notes))   # set() enlève les doublons, sorted() trie et renvoie une liste
print(distinctes)                 # [12, 15, 18]
```
</details>

➡️ **Prochaine étape** : [module 03 — fonctions & modules](../03_fonctions_modules/).
