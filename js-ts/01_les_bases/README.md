# Module 01 — Les bases du langage

Ce module présente les **briques fondamentales** de tout programme JavaScript. Une fois ces
briques comprises, tu peux (presque) tout construire.

> 🧠 Lis cette théorie en entier **avant** d'ouvrir les fichiers `.js`. Ensuite, lance-les
> et compare. Les deux scripts du module sont : `bases.js` (les briques) et
> `mini_calculatrice.js` (un mini-projet qui combine tout).

---

## 1. Les variables : des boîtes étiquetées

Une **variable** est une **boîte avec une étiquette** dans laquelle on range une valeur
pour la réutiliser plus tard. En JavaScript, on crée une variable avec `let` ou `const` :

```javascript
let age = 25;        // une boîte "age" qui contient 25
const prenom = "Alice"; // une boîte "prenom" qui contient "Alice"
```

- À gauche du `=` : le **nom** de la boîte (l'étiquette).
- À droite : la **valeur** qu'on range dedans.
- Le signe `=` ne veut **pas** dire « égal » au sens mathématique. Il veut dire
  **« range la valeur de droite dans la boîte de gauche »**.

### `let` ou `const` ? Et pourquoi pas `var` ?

| Mot-clé | Quand l'utiliser |
|---------|------------------|
| `const` | **Par défaut.** La valeur ne sera **pas** réassignée. C'est le plus sûr. |
| `let`   | Quand tu auras **besoin de changer** la valeur plus tard (un compteur, par ex.). |
| `var`   | **À éviter.** Ancienne façon de faire, avec des pièges. On ne l'utilise plus. |

```javascript
const pi = 3.14;     // une constante : pi = 4 plus tard provoquerait une erreur.

let compteur = 0;    // une variable qu'on va modifier...
compteur = compteur + 1; // ...ici on lit 0, on ajoute 1, on remet 1. OK car c'est 'let'.
```

> 💡 **Règle simple : commence toujours par `const`.** Si tu t'aperçois que tu dois
> changer la valeur, remplace par `let`. N'utilise **jamais** `var`.

---

## 2. Les types : la nature d'une valeur

Toute valeur a un **type** : sa « nature ». Les types de base à connaître :

| Type | Nom JS | Exemple | C'est quoi |
|------|--------|---------|------------|
| Nombre | `number` | `42` ou `3.14` | Un nombre (entier OU à virgule : un seul type !) |
| Texte | `string` | `"bonjour"` | Une *chaîne de caractères*, entre guillemets |
| Booléen | `boolean` | `true` / `false` | Vrai ou faux (en **minuscules** en JS !) |
| Rien | `null` | `null` | « Volontairement vide » (j'ai mis rien, exprès) |
| Indéfini | `undefined` | `undefined` | « Pas encore de valeur » (boîte jamais remplie) |

> 💬 `null` vs `undefined` : `undefined` veut dire « cette boîte n'a jamais reçu de valeur ».
> `null` veut dire « j'ai **décidé** de la mettre à vide ». Subtil, mais utile à savoir.

⚠️ **Le type compte.** `5` (nombre) et `"5"` (texte) ne sont pas la même chose :
- `5 + 5` donne `10`
- `"5" + "5"` donne `"55"` (JavaScript colle les deux textes !)

On **convertit** du texte vers un nombre avec `Number(...)` :

```javascript
const reponse = "42";        // du texte
const nombre = Number(reponse); // devient le nombre 42, prêt pour les calculs
```

---

## 3. Les *template literals* : insérer des variables dans du texte

Pour construire une phrase avec des variables dedans, JavaScript offre une syntaxe très
pratique : les **template literals**. On utilise des **accents graves** `` ` `` (backticks,
touche en haut à gauche du clavier, pas des guillemets) et on insère les variables avec
`${...}` :

```javascript
const prenom = "Alice";
const age = 30;
console.log(`${prenom} a ${age} ans.`); // affiche : Alice a 30 ans.
```

Chaque `${ }` est **remplacé** par la valeur de la variable à l'intérieur. C'est l'équivalent
des *f-strings* de Python.

---

## 4. Les conditions : prendre des décisions

Un programme doit souvent **choisir** quoi faire selon une situation. C'est le rôle de
`if` (si), `else if` (sinon si) et `else` (sinon).

```javascript
const note = 12;

if (note >= 10) {
  console.log("Reçu ✅");
} else {
  console.log("Recalé ❌");
}
```

Points clés :
- La condition est entre **parenthèses** `( )`.
- Le bloc qui dépend du `if` est entre **accolades** `{ }`.
- (En Python l'indentation était obligatoire ; en JavaScript ce sont les **accolades** qui
  délimitent le bloc. On indente quand même, pour la lisibilité.)

Les opérateurs de comparaison renvoient `true` ou `false` :

| Opérateur | Signifie |
|-----------|----------|
| `===` | égal à (**trois** `=` en JS ! voir l'encadré) |
| `!==` | différent de |
| `>` `<` | supérieur / inférieur |
| `>=` `<=` | supérieur ou égal / inférieur ou égal |

> ⚠️ En JavaScript, on compare avec **`===`** (triple égal), pas `==`. Le triple égal compare
> la valeur **et** le type, sans conversions surprises. Garde le réflexe `===` et `!==`.

---

## 5. Les boucles : répéter sans se fatiguer

L'automatisation, c'est **répéter une action**. Les boucles servent exactement à ça.

### La boucle `for` : répéter un nombre précis de fois

```javascript
for (let i = 0; i < 3; i++) {  // i = 0, puis 1, puis 2 (s'arrête avant 3)
  console.log(`Tour numéro ${i}`);
}
```

La parenthèse du `for` contient **trois parties**, séparées par `;` :
1. `let i = 0` → on part de 0,
2. `i < 3` → on continue **tant que** c'est vrai,
3. `i++` → après chaque tour, on ajoute 1 à `i` (`i++` = « `i = i + 1` »).

### La boucle `while` : « tant que… »

```javascript
let compteur = 0;
while (compteur < 3) {
  console.log(compteur);
  compteur++;   // ⚠️ sans ça, la boucle tournerait à l'infini !
}
```

### La boucle `for...of` : « pour chaque élément… »

Pour parcourir une liste (un *tableau*), `for...of` est le plus lisible :

```javascript
const fruits = ["pomme", "banane", "cerise"];
for (const fruit of fruits) {
  console.log(`J'aime la ${fruit}`);
}
```

Lis-le comme une phrase : *« pour chaque `fruit` de la liste `fruits`, affiche… »*.

---

## 6. Les fonctions : emballer du code réutilisable

Une **fonction** est un **bloc de code qu'on nomme** pour le réutiliser, comme un bouton
« faire le café ». On la **définit une fois**, puis on l'**appelle** autant de fois qu'on veut.

Il y a **deux façons** d'écrire une fonction en JavaScript.

### Façon classique : le mot-clé `function`

```javascript
function direBonjour(prenom) {     // 'prenom' est un PARAMÈTRE (une entrée)
  return `Bonjour ${prenom} !`;    // 'return' renvoie un RÉSULTAT
}

const message = direBonjour("Alice"); // ici on APPELLE la fonction avec "Alice"
console.log(message);                 // affiche : Bonjour Alice !
```

### Façon moderne : la fonction fléchée `=>`

La **fonction fléchée** (*arrow function*) fait la même chose, en plus court. La flèche `=>`
remplace le mot `function` :

```javascript
const direBonjour = (prenom) => {
  return `Bonjour ${prenom} !`;
};
```

Quand le corps tient en une seule expression, on peut même retirer les accolades et le
`return` (il est sous-entendu) :

```javascript
const doubler = (x) => x * 2;   // renvoie automatiquement x * 2
console.log(doubler(5));        // affiche : 10
```

Pourquoi les fonctions sont essentielles :
- **Éviter de répéter** le même code (principe DRY : *Don't Repeat Yourself*).
- **Donner un nom** à une idée → le code se lit comme du texte.
- **Corriger à un seul endroit** si quelque chose change.

---

## ▶️ À toi de jouer

```bash
node js-ts/01_les_bases/bases.js
node js-ts/01_les_bases/mini_calculatrice.js
```

Pour la calculatrice, on te demandera une opération puis deux nombres. Tu peux aussi lui
donner les réponses d'un coup avec un « tube » (`|`) :

```bash
printf "+\n7\n5\n" | node js-ts/01_les_bases/mini_calculatrice.js
```

Lis les deux fichiers, puis **modifie-les** : ajoute une opération à la calculatrice,
change les conditions, crée ta propre fonction fléchée.

➡️ La suite du parcours (TypeScript, fichiers, etc.) arrivera dans les prochains modules.
