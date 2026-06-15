# Module 00 — Démarrer : comprendre ce qu'on fait

Avant d'écrire une seule ligne de code, prenons 5 minutes pour comprendre **de quoi on parle**.
Ce module est 100 % théorique (plus un tout petit script à la fin).

---

## 1. C'est quoi JavaScript ?

**JavaScript** (souvent abrégé **JS**) est un langage de programmation né pour **le web** :
au départ, il servait à rendre les pages internet *vivantes* (boutons qui réagissent,
animations, formulaires…). Il tourne dans **tous les navigateurs** (Chrome, Firefox, Safari…).

Mais JavaScript ne se limite plus au navigateur. Grâce à **Node.js** (un programme qui sait
exécuter du JavaScript *en dehors* du navigateur), on peut aussi écrire :

- des **scripts** qui automatisent des tâches (comme on le ferait en Python),
- des **serveurs** et des **outils** en ligne de commande.

C'est exactement ce qu'on va faire dans ce parcours : du JavaScript **avec Node.js**, dans
le terminal.

> 💬 Comme Python, JavaScript est un langage **interprété** : tu écris du texte, et Node.js
> le lit et l'exécute **directement**, sans étape de « compilation » manuelle à gérer. Si tu
> te trompes, tu le sauras au lancement (et c'est normal de se tromper !).

---

## 2. Et TypeScript, alors ?

Tu verras souvent le mot **TypeScript** (abrégé **TS**) à côté de JavaScript.

TypeScript, c'est **JavaScript + les types**. Les « types » sont des étiquettes qui précisent
la *nature* d'une valeur (un nombre ? du texte ? un booléen ?). Elles permettent d'attraper
des erreurs **avant** même de lancer le programme.

> 📌 Pour l'instant, **on apprend JavaScript**. TypeScript arrivera **plus tard** dans le
> parcours, une fois les bases solides. Pas besoin de t'en occuper maintenant : tout ce que
> tu apprends en JavaScript reste vrai en TypeScript.

---

## 3. C'est quoi le « terminal » ?

Le **terminal** (aussi appelé « console » ou « invite de commandes ») est une fenêtre où
tu **tapes des commandes au clavier** au lieu de cliquer sur des boutons.

C'est là qu'on va **lancer** nos programmes JavaScript avec Node.js. Une commande typique
ressemble à ça :

```bash
node mon_programme.js
```

Décortiquons :
- `node` → « Hé, Node.js, réveille-toi, j'ai du JavaScript à exécuter. »
- `mon_programme.js` → « Voici le fichier à exécuter. »

> 📌 Les fichiers JavaScript se terminent toujours par **`.js`**. C'est juste une convention
> qui dit « ceci est du code JavaScript ». (Les fichiers TypeScript, eux, finissent par `.ts`.)

---

## 4. Le cycle : écrire → lancer → observer → corriger

Programmer, c'est une **boucle** :

```
   ┌──────────────┐
   │  J'écris du   │
   │     code      │
   └──────┬───────┘
          ▼
   ┌──────────────┐
   │  Je le lance  │
   └──────┬───────┘
          ▼
   ┌──────────────┐      ça marche ? ──► 🎉 suivant
   │  J'observe    │
   │  le résultat  │      erreur ? ──► je lis le message et je corrige
   └──────────────┘
```

Personne n'écrit du code parfait du premier coup. **Même les pros passent leur temps à
corriger des erreurs.** C'est normal et attendu.

> 💡 Astuce : `node --check mon_programme.js` vérifie la **syntaxe** d'un fichier **sans
> l'exécuter**. Pratique pour repérer une faute de frappe avant de lancer pour de vrai.

---

## 5. Les commentaires : des notes pour les humains

Dans un fichier JavaScript, on peut écrire des **commentaires** : du texte que Node.js
**ignore** complètement. Ils servent à **expliquer le code aux humains** (toi, dans 6 mois,
ou un collègue). Il y a **deux** façons :

```javascript
// Ceci est un commentaire sur UNE ligne : tout ce qui suit // est ignoré.

/*
  Ceci est un commentaire sur PLUSIEURS lignes.
  Tout ce qui est entre /* et la fermeture est ignoré.
*/

console.log("Bonjour"); // On peut aussi commenter en fin de ligne.
```

Dans ce dépôt, les fichiers `.js` sont **remplis de commentaires** : lis-les, ils font
partie du cours.

---

## 6. La première instruction : `console.log()`

`console.log()` est l'instruction la plus simple : elle **affiche** du texte à l'écran
(le `.log` veut dire « écris dans le journal »).

```javascript
console.log("Bonjour le monde !");
```

Le texte entre **guillemets** `"..."` s'appelle une **chaîne de caractères** (en anglais
*string*). On en reparlera au module 01.

> 💬 En JavaScript, on termine souvent une instruction par un **point-virgule** `;`. Ce
> n'est pas toujours obligatoire, mais c'est une bonne habitude : on le mettra partout.

---

## 📚 Les modules de ce parcours

| Module | Contenu |
|--------|---------|
| [`00_demarrer`](./) | Comprendre JavaScript, Node.js, le terminal (tu es ici) |
| [`01_les_bases`](../01_les_bases/) | Variables, types, conditions, boucles, fonctions |

---

## ▶️ À toi de jouer

Lance le petit script de ce module :

```bash
node js-ts/00_demarrer/premier_script.js
```

Lis ensuite le fichier [`premier_script.js`](./premier_script.js) en entier : chaque ligne
est commentée. Puis **modifie le texte affiché** et relance le script pour voir le changement.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/) — les briques du langage.
