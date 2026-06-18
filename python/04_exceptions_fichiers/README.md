# 📂 Module 04 : Exceptions & Fichiers

Un bon programme doit savoir lire des données et, surtout, ne pas planter au moindre problème.

---

## 1. Gérer les erreurs (`try`, `except`)
Au lieu de laisser le programme s'arrêter avec un message rouge effrayant, on "attrape" l'erreur.
```python
try:
    nombre = int(input("Donne un nombre : "))
    resultat = 10 / nombre
except ZeroDivisionError:
    print("Impossible de diviser par zéro !")
except ValueError:
    print("Ce n'est pas un nombre valide.")
```

## 2. Manipuler des fichiers
On utilise le mot-clé **`with`**. C'est un *Context Manager* : il s'occupe de fermer le fichier proprement pour toi, même s'il y a une erreur.

### Écrire
```python
with open("test.txt", "w") as f:
    f.write("Salut Python !")
```

### Lire
```python
with open("test.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

---

## 🏁 Exercice
1. Explore [fichiers.py](./fichiers.py) pour voir comment créer et lire un fichier de log.
2. Essaie de forcer une erreur dans le code pour voir comment `try/except` la capture.
