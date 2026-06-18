# 🏗️ Module 05 : Programmation Orientée Objet (POO)

En Python, **tout est objet**. Apprendre à créer tes propres objets te permettra d'organiser ton code comme un pro.

---

## 1. La Classe : le moule
Une classe est un plan de fabrication.
```python
class Voiture:
    def __init__(self, marque, couleur):
        # Attributs (données)
        self.marque = marque
        self.couleur = couleur

    # Méthode (action)
    def klaxonner(self):
        print(f"La {self.marque} fait : POUT POUT !")
```

## 2. L'Objet : le produit fini
On crée une "instance" de la classe.
```python
ma_caisse = Voiture("Tesla", "Rouge")
ma_caisse.klaxonner()
```

## 3. L'Héritage
Tu peux créer une classe qui hérite des capacités d'une autre.
```python
class VoitureElectrique(Voiture):
    def klaxonner(self):
        print("Bip bip (je suis silencieuse) !")
```

---

## 🏁 Exercice
1. Analyse [poo.py](./poo.py) pour comprendre `self`, `__init__` et l'héritage.
2. Crée une nouvelle classe `Moto` qui hérite aussi de `Vehicule` (si tu l'as définie).
