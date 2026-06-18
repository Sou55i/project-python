# 🏗️ Module 01 : Les bases (Variables & Contrôle)

Maintenant que tu sais lancer un script, voyons comment stocker des informations et prendre des décisions.

---

## 1. Les Variables (Typage dynamique)

En Python, tu ne déclares pas le type d'une variable. C'est Python qui devine.
```python
age = 25          # C'est un entier (int)
nom = "Marc"      # C'est du texte (str)
taille = 1.75     # C'est un nombre à virgule (float)
est_content = True # C'est un booléen (bool)
```

**⚠️ Attention :** Python est sensible à la casse (`Age` est différent de `age`).

## 2. Prendre des décisions (`if`, `elif`, `else`)

C'est ici que l'**indentation** (les 4 espaces) devient obligatoire.

```python
if age >= 18:
    print("Majeur")
elif age > 13:
    print("Adolescent")
else:
    print("Enfant")
```

## 3. Répéter des actions (`for`, `while`)

-   **`for`** : Pour parcourir une liste de choses ou répéter un nombre de fois précis.
-   **`while`** : Pour répéter tant qu'une condition est vraie.

```python
# Répéter 5 fois
for i in range(5):
    print(f"Tour numéro {i}")
```

---

## 🏁 Exercice
1. Explore [bases.py](./bases.py) pour voir comment manipuler les variables et les boucles.
2. Essaie de modifier les valeurs pour voir comment le programme réagit.
