# Module 04 — L'asynchrone : le point fort de Node.js

Voici une notion qui déroute souvent les débutants… et qui est **le cœur** de
Node.js. Prenons vraiment notre temps, avec une image du quotidien.

---

## 1. Le problème : certaines choses prennent du temps

Imagine que tu commandes une pizza. Deux façons d'attendre :

- **Synchrone (bloquant)** : tu restes **planté devant le four**, sans rien faire
  d'autre, jusqu'à ce que la pizza soit prête. Pendant ce temps, **tout est bloqué**.
- **Asynchrone (non bloquant)** : tu **lances** la commande, puis tu fais **autre
  chose** ; quand la pizza est prête, on **te prévient** et tu reviens la chercher.

En programmation, certaines opérations sont **longues** : lire un fichier,
interroger un serveur sur internet, attendre un délai… Si on bloquait à chaque
fois, le programme serait figé. Node.js est conçu pour faire de l'asynchrone :
il **lance** une tâche longue et continue à travailler, puis revient au résultat
**quand il est prêt**.

> 💬 `setTimeout(fonction, ms)` est notre « four » pour s'entraîner : il exécute
> `fonction` **après** un délai en millisecondes (ms). Pendant l'attente, Node.js
> n'est **pas** bloqué.

---

## 2. Étape 1 — les callbacks (l'ancienne façon)

La première façon de gérer l'asynchrone : donner une fonction (un **callback**)
qui sera appelée **quand c'est prêt**.

```javascript
console.log("Je commande la pizza");
setTimeout(() => {
  console.log("Pizza prête !"); // s'affiche APRÈS le délai
}, 1000);
console.log("En attendant, je mets la table");
```

L'ordre affiché est : *commande* → *table* → (1 s plus tard) *pizza*. Surprenant
au début ! Le souci : si on enchaîne plusieurs étapes, on imbrique les callbacks
les uns dans les autres et ça devient illisible (on appelle ça le « callback hell »,
l'enfer des callbacks).

---

## 3. Étape 2 — les Promesses (*Promises*)

Une **Promesse** est un **objet** qui représente un résultat **à venir** : « je te
**promets** une valeur, plus tard ». Elle a deux issues possibles :

- **résolue** (*resolve*) → tout s'est bien passé, voici la valeur ;
- **rejetée** (*reject*) → il y a eu une erreur.

On réagit avec `.then(...)` (si ça réussit) et `.catch(...)` (si ça échoue) :

```javascript
maPromesse
  .then((valeur) => console.log("Reçu :", valeur))
  .catch((erreur) => console.log("Raté :", erreur));
```

C'est déjà plus propre que les callbacks imbriqués : on **enchaîne** les `.then`.

---

## 4. Étape 3 — `async` / `await` (la façon moderne)

`async`/`await` est du **sucre** par-dessus les Promesses : ça permet d'écrire du
code asynchrone qui **se lit** comme du code normal, ligne après ligne.

- On marque une fonction avec **`async`** → elle peut utiliser `await`.
- **`await`** met la fonction **en pause** jusqu'à ce que la Promesse soit prête,
  **sans bloquer** le reste du programme, puis récupère la valeur.

```javascript
async function commander() {
  console.log("Je commande");
  const pizza = await preparerPizza(); // on ATTEND le résultat, sans bloquer
  console.log("Reçu :", pizza);
}
```

> 💡 Pour gérer les erreurs avec `await`, on utilise `try { ... } catch (e) { ... }` :
> `try` = « essaie », `catch` = « attrape l'erreur si ça casse ».

---

## 5. Résumé de la progression

```
   callbacks   ──►   Promesses (.then/.catch)   ──►   async / await
  (historique)        (objet "résultat futur")        (lisible, moderne)
```

Les trois existent encore et reposent sur la même idée : **ne pas bloquer**. En
pratique aujourd'hui, on écrit surtout du **`async`/`await`**.

---

## ▶️ À toi de jouer

```bash
node js-ts/04_async/async_demo.js
```

Le script affiche les étapes **dans l'ordre où elles se terminent**, attend
volontairement de courts délais, puis **se termine proprement** tout seul. Lis-le
en entier : chaque ligne est commentée.

➡️ Module suivant : [`05_typescript`](../05_typescript/) — ajouter les types.
