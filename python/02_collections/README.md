# 📦 Module 02 : Les Collections

En Python, on manipule rarement des variables isolées. On utilise des **collections** pour regrouper des données.

---

## 1. Les Listes (`list`)
C'est la collection la plus utilisée. Elle est ordonnée et on peut ajouter/supprimer des éléments.
```python
fruits = ["pomme", "banane", "cerise"]
fruits.append("orange")
print(fruits[0]) # "pomme"
```

## 2. Les Dictionnaires (`dict`)
Idéal pour stocker des données sous forme de paires **Clé: Valeur**.
```python
pilote = {"nom": "Hamilton", "ecurie": "Mercedes"}
print(pilote["nom"]) # "Hamilton"
```

## 3. Les Tuples (`tuple`)
Comme une liste, mais **non modifiable** après création. Très rapide.
```python
coordonnees = (48.8566, 2.3522)
```

## 4. Les Sets (`set`)
Une collection de valeurs **uniques**, non ordonnée. Très utile pour supprimer les doublons.
```python
nombres = {1, 2, 2, 3} # deviendra {1, 2, 3}
```

---

## 🏁 Exercice
1. Explore [collections.py](./collections_demo.py) pour voir ces collections en action.
2. Essaie d'ajouter des éléments et de parcourir les dictionnaires avec une boucle.
