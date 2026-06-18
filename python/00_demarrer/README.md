# 🚀 Module 00 : Démarrer avec Python

Dans ce premier module, nous allons voir comment installer Python, comment lancer un script et, plus important encore, comment garder ton ordinateur propre grâce aux **environnements virtuels**.

---

## 1. Vérifier l'installation

Ouvre un terminal et tape :
```bash
python3 --version
```
Si tu vois quelque chose comme `Python 3.10.x` (ou plus récent), c'est gagné !

## 2. Ton premier script : Hello World

En Python, pas besoin de configurer des tonnes de choses. Un fichier `.py` et une ligne de code suffisent.

**Fichier `hello.py` :**
```python
print("Bonjour le monde !")
```

**Pour le lancer :**
```bash
python3 hello.py
```

## 3. Le secret des pros : L'environnement virtuel (`venv`)

C'est l'étape que beaucoup de débutants sautent et qu'ils regrettent ensuite.
Imagine que tu travailles sur deux projets :
- Projet A a besoin de `requests` version 1.0.
- Projet B a besoin de `requests` version 2.0.

Si tu installes tout sur ton système global, ça va planter. La solution ? **Un environnement virtuel par projet.**

### Comment faire ?

1.  **Créer l'environnement** (on le nomme souvent `.venv`) :
    ```bash
    python3 -m venv .venv
    ```
2.  **L'activer** (pour dire à ton terminal d'utiliser cet environnement) :
    - Sur Linux/macOS : `source .venv/bin/activate`
    - Sur Windows : `.venv\Scripts\activate`
3.  **Installer des outils** (ils ne seront installés QUE dans ce dossier) :
    ```bash
    pip install requests
    ```
4.  **Le quitter** quand tu as fini :
    ```bash
    deactivate
    ```

---

## 🏁 Exercice
1. Lis le fichier [hello.py](./hello.py) pour voir la structure minimale.
2. Crée un environnement virtuel dans ce dossier pour t'entraîner.
