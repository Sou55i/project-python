# 🧭 Anatomie d'un script : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire des lignes de Python, mais ne savent pas **dans quel
ordre les ranger** pour former un script complet et propre. Ce guide explique le
**cheminement logique** d'un script, du début à la fin.

> 📌 À lire après les modules `00_demarrer` et `01_les_bases`, et à garder sous la main
> comme aide-mémoire. Un modèle prêt à copier t'attend dans
> [`modele_script.py`](./modele_script.py).

---

## 1. LA règle d'or : Python lit de HAUT en BAS

C'est le point le plus important, et la cause n°1 des bugs de débutant.

> Python exécute ton fichier **ligne par ligne, du haut vers le bas**, comme tu lis une
> page. **Une chose doit exister AVANT qu'on l'utilise.**

Tu ne peux pas verser le café dans une tasse que tu n'as pas encore sortie du placard.
En code, c'est pareil : tu ne peux pas utiliser une variable, une fonction ou un outil
**avant** de l'avoir créé/importé plus haut.

---

## 2. Le squelette standard d'un script complet

Presque tous les scripts Python bien écrits suivent **ce même ordre**, de haut en bas :

```python
"""                                                      ┐
Description du script : à quoi il sert, comment le lancer. │  (1) DOCSTRING
"""                                                      ┘

import os                                                ┐  (2) IMPORTS
import requests                                          ┘     (les outils)

DOSSIER_SORTIE = "resultats"                             ┐  (3) CONSTANTES
TIMEOUT = 10                                             ┘     (valeurs fixes, EN MAJUSCULES)

def telecharger(url):                                    ┐
    """Fait une seule chose, bien."""                    │  (4) FONCTIONS
    ...                                                   │     (on les DÉFINIT ici, elles
                                                          │      ne s'exécutent PAS encore)
def sauvegarder(donnees):                                 │
    ...                                                   ┘

if __name__ == "__main__":                               ┐  (5) PROGRAMME PRINCIPAL
    page = telecharger("https://exemple.com")             │     (le code qui DÉMARRE tout
    sauvegarder(page)                                     ┘      et appelle les fonctions)
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 1 | **Docstring** | La 1re chose qu'on lit : « ce script sert à… ». |
| 2 | **Imports** | On **ouvre les caisses à outils** avant de s'en servir. (cours détaillé : module [`06_bibliotheques`](./06_bibliotheques/)) |
| 3 | **Constantes** | Les réglages fixes, regroupés en haut pour les changer facilement. Par convention, on les écrit `EN_MAJUSCULES`. |
| 4 | **Fonctions (`def`)** | On **définit** les actions réutilisables. ⚠️ Définir ≠ exécuter : le code d'une fonction ne tourne que lorsqu'on l'**appelle**. Elles doivent être écrites **avant** d'être appelées. |
| 5 | **Programme principal** | Le **chef d'orchestre** : il appelle les fonctions dans le bon ordre. On le met tout en bas, dans `if __name__ == "__main__":` (voir module 04). |

> 💡 « Définir une fonction » = écrire la recette. « Appeler la fonction » = cuisiner le
> plat. On écrit toutes les recettes en haut, puis on cuisine en bas.

---

## 3. La logique INTERNE : entrée → traitement → sortie

À l'intérieur du programme principal (ou d'une fonction), le code suit presque toujours
**3 phases**, dans cet ordre :

```
   1. ENTRÉE          2. TRAITEMENT             3. SORTIE
   (je récupère       (je calcule, je décide,   (j'affiche ou
    les données)       je transforme)            j'enregistre)
   ──────────         ───────────────          ──────────
   input()            if / elif / else          print()
   open(...).read()   for / while               écrire un fichier
   requests.get()     calculs, fonctions        envoyer un résultat
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

---

## 4. Comment lire un script complexe qu'on découvre

Quand un script te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va tout en bas**, au bloc `if __name__ == "__main__":`. C'est le **point de départ**
   réel du programme : il montre l'enchaînement principal.
2. **Suis les appels de fonctions** depuis ce bloc. Quand tu vois `telecharger(url)`,
   remonte lire la fonction `def telecharger` pour comprendre ce qu'elle fait.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le bloc
> principal), puis tu ouvres les chapitres qui t'intéressent (les fonctions).

---

## 5. Récapitulatif visuel

```
┌─────────────────────────────────────────────┐
│ 1. """Docstring""" : à quoi sert le script    │
│ 2. import ...       : les outils              │  ← on prépare
│ 3. CONSTANTES       : les réglages fixes      │
├─────────────────────────────────────────────┤
│ 4. def fonction():  : on DÉFINIT les actions  │  ← on outille
├─────────────────────────────────────────────┤
│ 5. if __name__ == "__main__":                 │
│        entrée  -> traitement -> sortie        │  ← on EXÉCUTE
└─────────────────────────────────────────────┘
              (Python lit de haut en bas)
```

➡️ Garde ce modèle en copiant [`modele_script.py`](./modele_script.py) pour démarrer tes
propres scripts du bon pied.
