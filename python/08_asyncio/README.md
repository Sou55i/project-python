# ⚡ Module 08 : Programmation Asynchrone (`asyncio`)

Traditionnellement, Python exécute une ligne après l'autre. Si une ligne prend 10 secondes (ex: télécharger un gros fichier), tout le programme s'arrête en attendant.

L'asynchrone permet de faire autre chose en attendant que l'opération longue se termine.

---

## 1. `async` et `await`
Pour rendre une fonction asynchrone, on ajoute `async` devant `def`. Pour attendre le résultat sans bloquer, on utilise `await`.

```python
import asyncio

async def saluer_plus_tard():
    print("Je vais saluer dans 1 seconde...")
    await asyncio.sleep(1) # On attend sans bloquer le reste
    print("Bonjour !")

asyncio.run(saluer_plus_tard())
```

## 2. Pourquoi c'est utile ?
Imagine que tu doives scanner 100 ports réseau.
- **Synchrone** : Scan 1, attend. Scan 2, attend. (Total: 100 secondes).
- **Asynchrone** : Lance les 100 scans presque en même temps, et traite les résultats dès qu'ils arrivent. (Total: ~1 seconde).

---

## 🏁 Exercice
1. Explore [demo_async.py](./demo_async.py) pour voir la différence de vitesse flagrante entre synchrone et asynchrone.
2. Essaie d'ajouter une troisième tâche asynchrone.
