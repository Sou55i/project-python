# ⚙️ Module 06 : Itérateurs & Générateurs

Python possède des outils très puissants pour manipuler des séquences de données de manière efficace, surtout quand elles sont très grandes.

---

## 1. Les Itérateurs
Un itérateur est un objet qui permet de parcourir une collection. En Python, la plupart des collections (listes, dicts) sont des **itérables**.

## 2. Les Générateurs (`yield`)
C'est la partie "magique". Un générateur permet de produire des valeurs **une par une**, au lieu de tout stocker en mémoire d'un coup.
```python
def compter_jusqua_un_milliard():
    n = 0
    while n < 1000000000:
        yield n  # On "renvoie" la valeur sans arrêter la fonction
        n += 1
```
Si tu essayais de mettre un milliard de nombres dans une liste, ton ordinateur planterait (plus de RAM). Avec un générateur, ça ne prend quasiment aucune place !

## 3. List Comprehensions
Une syntaxe compacte pour transformer une liste.
```python
nombres = [1, 2, 3, 4]
carres = [n**2 for n in nombres if n > 2] # [9, 16]
```

---

## 🏁 Exercice
1. Explore [generateurs.py](./generateurs.py) pour voir la différence de consommation mémoire.
2. Essaie d'écrire une comprehension de liste qui extrait les noms commençant par "A".
