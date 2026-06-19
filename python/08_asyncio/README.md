# ⚡ Module 08 : la programmation asynchrone (`asyncio`)

> 🎯 **Objectif** : comprendre comment faire **plusieurs choses « en même temps »** quand le
> programme passe son temps à **attendre** (réseau, fichiers, API). C'est un sujet avancé : ne
> l'aborde qu'une fois les modules 00→05 bien digérés.

---

## 1. Le problème : l'attente qui bloque tout

Par défaut, Python exécute **une ligne à la fois**, dans l'ordre. Si une ligne **attend**
(télécharger un fichier, interroger un site, dormir 2 s), **tout le programme est figé** pendant
ce temps, même s'il n'a rien d'autre à faire qu'attendre.

> 🧠 **L'image** : un cuisinier qui lance des pâtes (10 min), reste planté devant la casserole
> sans rien faire, **puis** seulement commence la sauce. Absurde : pendant que l'eau chauffe, il
> pourrait préparer la sauce. L'asynchrone, c'est **utiliser les temps d'attente** pour avancer
> ailleurs.

> ⚠️ **Important** : l'asynchrone n'accélère **pas** les calculs (additionner des millions de
> nombres). Il aide quand le programme **attend** une ressource extérieure (I/O : réseau,
> disque). Pour paralléliser du **calcul** pur, c'est un autre outil (`multiprocessing`).

---

## 2. `async`, `await`, et la boucle d'événements

Trois mots-clés à connaître :

```python
import asyncio

async def saluer_plus_tard():        # async devant def → c'est une "coroutine"
    print("Je vais saluer dans 1 seconde...")
    await asyncio.sleep(1)           # await = "attends ICI, mais LIBÈRE le programme entre-temps"
    print("Bonjour !")

asyncio.run(saluer_plus_tard())      # asyncio.run lance la machinerie asynchrone
```

| Mot-clé | Rôle |
|---------|------|
| `async def` | définit une **coroutine** : une fonction « pausable » |
| `await` | marque un point d'attente ; rend la main pour que d'autres tâches avancent |
| `asyncio.run(...)` | démarre la **boucle d'événements** et exécute la coroutine |

> 🔑 **Règle absolue** : `await` ne peut s'utiliser **que** dans une fonction `async`. Et
> appeler une coroutine sans `await` (ni `asyncio.run`) ne l'exécute **pas** — ça crée juste un
> objet coroutine inerte. C'est l'erreur n°1 du débutant en asyncio.

> 🧠 La **boucle d'événements** (*event loop*) est le « chef d'orchestre » : pendant qu'une
> tâche est en attente (`await`), elle donne la main à une autre tâche prête. C'est ce qui crée
> l'illusion du « en même temps » — avec **un seul** fil d'exécution.

---

## 3. Le vrai gain : lancer plusieurs tâches ensemble

Une coroutine seule ne sert à rien. Le bénéfice apparaît quand on en lance **plusieurs en
parallèle** avec `asyncio.gather` :

```python
import asyncio

async def telecharger(nom, duree):
    print(f"Début {nom}")
    await asyncio.sleep(duree)        # simule une attente réseau
    print(f"Fini {nom}")
    return f"{nom} OK"

async def main():
    # gather lance les 3 EN MÊME TEMPS et attend qu'elles soient toutes finies
    resultats = await asyncio.gather(
        telecharger("A", 2),
        telecharger("B", 1),
        telecharger("C", 3),
    )
    print(resultats)

asyncio.run(main())
```

- **Sans** asynchrone : 2 + 1 + 3 = **6 secondes** (l'une après l'autre).
- **Avec** `gather` : ~**3 secondes** (la plus longue), car les attentes se chevauchent.

> 🔎 **`await asyncio.gather(...)`** : on *await* l'ensemble. La boucle démarre les trois,
> bascule de l'une à l'autre à chaque `await asyncio.sleep`, et rend les résultats **dans
> l'ordre des arguments** une fois tout terminé.

---

## 4. Quand utiliser asyncio (et quand l'éviter)

| Situation | Asynchrone utile ? |
|-----------|--------------------|
| appeler 100 URLs / API | ✅ oui : énorme gain (attentes réseau) |
| lire/écrire beaucoup de fichiers, requêtes BD | ✅ souvent |
| gros calcul mathématique (CPU) | ❌ non → vois `multiprocessing` |
| petit script séquentiel simple | ❌ non : ça complique pour rien |

> 🧠 **Règle de sagesse** : n'introduis `asyncio` que si tu as un **vrai** problème d'attentes
> nombreuses. Pour la plupart des scripts d'apprentissage, le code synchrone est plus simple et
> suffisant. La complexité doit être **justifiée**.

---

## 🏁 Exercices

1. **Lis et lance** [`demo_async.py`](./demo_async.py) : compare la durée synchrone vs asynchrone.
2. **Ajoute une 3ᵉ tâche** dans le `gather` et observe que le total reste ≈ la tâche la plus
   longue.
3. **Expérience** : remplace `await asyncio.sleep(1)` par un vrai `time.sleep(1)` (bloquant) et
   constate que le gain **disparaît** — c'est `await` qui permet le chevauchement.

➡️ **Prochaine étape** : [module 09 — tests & qualité](../09_tests_qualite/).
