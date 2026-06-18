# 🛠️ Module 03 : Fonctions & Modules

Pour éviter de répéter le même code et pour mieux l'organiser, on utilise des **fonctions** et des **modules**.

---

## 1. Définir une fonction
On utilise le mot-clé `def`.
```python
def saluer(nom, message="Bonjour"):
    return f"{message} {nom} !"

print(saluer("Alice")) # "Bonjour Alice !"
```

## 2. Les arguments nommés (`*args`, `**kwargs`)
Python est très flexible sur la manière de passer des arguments :
- `*args` : Pour passer un nombre variable d'arguments (sous forme de liste).
- `**kwargs` : Pour passer un nombre variable d'arguments nommés (sous forme de dictionnaire).

## 3. Importer des modules
Tu peux importer des fichiers `.py` ou des bibliothèques standards.
```python
import math
print(math.sqrt(16)) # 4.0

from os import path
```

---

## 🏁 Exercice
1. Explore [fonctions.py](./fonctions.py) pour comprendre les arguments et les retours.
2. Regarde [usage_module.py](./usage_module.py) pour voir comment importer tes propres fichiers.
