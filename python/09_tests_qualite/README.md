# ✅ Module 09 : Tests & Qualité

Écrire du code qui marche est une chose. Écrire du code dont on est **sûr** qu'il marche (et qu'il ne cassera pas plus tard) en est une autre.

---

## 1. Pourquoi tester ?
Plus ton projet grandit, plus tu as de chances de casser quelque chose en ajoutant une fonctionnalité. Les tests automatiques vérifient tout en 1 seconde.

## 2. Utiliser `pytest` (Le standard)
Python a un outil génial nommé `pytest`.
```bash
pip install pytest
```

### Un test simple
```python
def addition(a, b):
    return a + b

def test_addition():
    assert addition(2, 2) == 4
    assert addition(-1, 1) == 0
```

## 3. Linters et Formatage
Pour garder un code propre et lisible par tout le monde :
- **Black** : Formate ton code automatiquement (fini les débats sur les espaces).
- **Flake8** : Vérifie que tu respectes les règles de style (PEP8).

---

## 🏁 Exercice
1. Installe pytest : `pip install pytest`.
2. Lance les tests dans ce dossier avec la commande : `pytest`.
3. Regarde [test_demo.py](./test_demo.py) pour voir comment écrire tes propres tests.
