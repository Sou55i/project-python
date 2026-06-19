# ✅ Module 09 : Tests & qualité

> 🎯 **Objectif** : passer de « ça **a l'air** de marcher » à « je suis **sûr** que ça marche, et
> que ça ne cassera pas demain ». Tu vas apprendre à écrire des **tests automatiques** (`pytest`)
> et à garder un code **propre** (formatage, style).

---

## 1. Pourquoi tester ?

À la main, tu vérifies ton programme une fois… puis tu ajoutes une fonctionnalité, et sans le
savoir tu **casses** ce qui marchait avant (une *régression*). Plus le projet grandit, plus le
risque explose. Les **tests automatiques** rejouent toutes les vérifications **en une seconde**,
à chaque modification.

> 🧠 **L'image** : un test est un **filet de sécurité**. Tu peux refactorer, optimiser, oser des
> changements — si un test passe au rouge, tu sais **immédiatement** ce que tu as cassé, et où.

---

## 2. `assert` : la brique de base

Avant les outils, le mot-clé `assert` : il **vérifie qu'une condition est vraie**, et fait
planter le programme avec un message si elle est fausse.

```python
assert 2 + 2 == 4          # OK, rien ne se passe
assert 2 + 2 == 5          # AssertionError : le programme s'arrête ici
```

Un test, c'est essentiellement : « j'appelle ma fonction, j'**assert** que le résultat est celui
attendu ».

---

## 3. `pytest` : l'outil standard

`pytest` trouve et exécute automatiquement tous tes tests. On l'installe une fois :

```bash
pip install pytest
```

### Écrire un test

Les conventions que `pytest` reconnaît **automatiquement** :

- le **fichier** commence par `test_` (ex. `test_calcul.py`) ;
- la **fonction** de test commence par `test_` ;
- à l'intérieur, on utilise `assert`.

```python
# fichier : test_calcul.py
def addition(a, b):           # la fonction qu'on veut tester (souvent importée d'un autre fichier)
    return a + b

def test_addition_simple():
    assert addition(2, 2) == 4

def test_addition_negatifs():
    assert addition(-1, 1) == 0
    assert addition(-5, -5) == -10
```

### Lancer les tests

Dans le dossier, tape simplement :

```bash
pytest
```

`pytest` découvre tout seul les `test_*.py`, exécute chaque `test_*`, et affiche un point vert
par succès, un `F` rouge par échec — avec **exactement** quelle assertion a échoué et les valeurs
en cause.

> 🔑 **Le bon réflexe : tester aussi les cas limites.** Ne teste pas que le cas « qui marche » :
> teste le **zéro**, le **vide**, le **négatif**, l'**inattendu**. C'est là que vivent les bugs.

### Tester qu'une erreur est bien levée

```python
import pytest

def diviser(a, b):
    return a / b

def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):   # "je m'attends à CETTE erreur"
        diviser(10, 0)
```

---

## 4. Garder un code propre : formatage & style

Du code lisible se relit et se corrige plus vite. Deux familles d'outils :

| Outil | Rôle | Commande |
|-------|------|----------|
| **Black** | **reformate** automatiquement (indentation, espaces, guillemets) | `black .` |
| **Ruff** / **Flake8** | **signale** les problèmes de style et erreurs probables | `ruff check .` |

- **Black** met fin aux débats sur la mise en forme : il impose **un** style cohérent, point.
- Les *linters* (**Ruff**, **Flake8**) vérifient le respect de la **PEP 8** (le guide de style
  officiel de Python) et repèrent les imports inutilisés, variables jamais utilisées, etc.

> 🧠 **PEP 8** est la convention de style de référence en Python (noms en `snake_case`, 4 espaces
> d'indentation, lignes pas trop longues…). Tu n'as pas à la mémoriser : laisse Black et Ruff la
> faire respecter pour toi.

---

## 5. Le cycle de travail d'un dev outillé

```
   écris du code
        │
        ▼
   écris un test qui décrit le comportement attendu
        │
        ▼
   pytest  ──► ROUGE ? corrige et recommence
        │
        ▼ VERT
   black .  (reformate)   +   ruff check .  (vérifie le style)
        │
        ▼
   commit en confiance
```

> 🔑 **Va plus loin** : écrire le **test d'abord**, puis le code qui le fait passer, s'appelle
> le **TDD** (*Test-Driven Development*). C'est une discipline puissante quand le comportement
> attendu est clair.

---

## 🏁 Exercices

> 🎯 **Entraînement TDD** : dans [`exercices.py`](./exercices.py), les **tests sont déjà écrits** —
> implémente les fonctions pour les faire passer au vert (rouge → vert). Corrigé dans
> [`solutions.py`](./solutions.py).

1. **Installe** pytest (`pip install pytest`) et lance `pytest` dans ce dossier.
2. **Lis** [`test_demo.py`](./test_demo.py) pour voir la structure d'un fichier de tests.
3. **Écris tes tests** : crée une fonction `est_pair(n)` et un fichier `test_pair.py` qui vérifie
   qu'elle renvoie `True` pour 4, `False` pour 3, et `True` pour 0.

<details>
<summary>💡 Solution — exercice 3 (est_pair)</summary>

```python
# fichier : test_pair.py
def est_pair(n):
    return n % 2 == 0

def test_est_pair():
    assert est_pair(4) is True
    assert est_pair(3) is False
    assert est_pair(0) is True
```
Lance ensuite `pytest` : tu dois voir un point vert.
</details>

➡️ **Tu as terminé le cœur du langage !** Direction le **Python appliqué** :
[module 10 — fichiers & dossiers](../10_fichiers_dossiers/).
