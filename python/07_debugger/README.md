# 🐞 Module 07 : Le Debugger

Faire des erreurs est normal. Savoir les trouver rapidement est ce qui différencie un débutant d'un expert.

---

## 1. La méthode "Print" (Le début)
C'est la méthode la plus simple : on affiche les variables pour voir ce qu'elles contiennent à un instant T.
```python
print(f"DEBUG: x vaut {x}")
```

## 2. Le debugger de VSCode (Recommandé)
Si tu utilises VSCode, tu peux mettre des **points d'arrêt** (le petit point rouge à gauche du numéro de ligne). Le programme s'arrêtera là et tu pourras :
- Voir la valeur de toutes les variables.
- Avancer ligne par ligne.
- Entrer dans les fonctions.

## 3. `pdb` : Le debugger intégré
Si tu es dans un terminal sans interface graphique, tu peux utiliser `pdb`.
```python
import pdb; pdb.set_trace()
```
Depuis Python 3.7, il y a un raccourci plus simple :
```python
breakpoint()
```

---

## 🏁 Exercice
1. Lance [demo_debug.py](./demo_debug.py). Il contient un bug subtil.
2. Utilise `breakpoint()` pour arrêter le programme et inspecter la variable `total`.
