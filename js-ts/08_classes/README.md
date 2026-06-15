# Module 08 — Les classes : créer ses propres « moules » d'objets

Au module 02, tu as manipulé des **objets** : des sacs de données avec des clés
(`{ prenom: "Alice", age: 30 }`). Quand on a besoin de **beaucoup** d'objets qui se
ressemblent (plein de comptes bancaires, plein de joueurs…), on aimerait un **moule**
pour les fabriquer tous pareil. Ce moule, c'est une **classe**.

---

## 1. L'idée : un moule (la classe) et des objets (les instances)

- Une **classe** décrit **à quoi ressemble** un objet : ses **données** et ce qu'il
  sait **faire**.
- À partir de ce moule, on **fabrique** autant d'objets qu'on veut. Chaque objet
  fabriqué s'appelle une **instance**.

Image : la classe `Gâteau` est la **recette** ; chaque gâteau réel sorti du four est
une **instance** de cette recette.

---

## 2. `class`, `constructor` et `this`

On déclare une classe avec le mot-clé **`class`**. Dedans, une méthode spéciale, le
**`constructor`**, est appelée **automatiquement** au moment de la fabrication : c'est
là qu'on **remplit** les données de l'objet.

```javascript
class Personne {
  constructor(prenom, age) {
    this.prenom = prenom; // "this" = l'objet en cours de fabrication
    this.age = age;
  }
}

const alice = new Personne("Alice", 30); // "new" déclenche le constructor
console.log(alice.prenom); // Alice
```

> 📌 **`this`** est le mot le plus important ici : il désigne **l'objet lui-même**,
> celui qu'on est en train de créer ou d'utiliser. `this.prenom = prenom` veut dire
> « range le prénom reçu **dans cet objet-ci** ».
>
> 📌 **`new`** est l'ordre « fabrique-moi un nouvel objet à partir de ce moule ».

---

## 3. Les méthodes : ce que l'objet sait faire

Une **méthode** est une **fonction rangée dans la classe**. Elle peut utiliser `this`
pour lire les données de l'objet.

```javascript
class Personne {
  constructor(prenom) {
    this.prenom = prenom;
  }
  saluer() {
    // une méthode : pas de mot "function", juste son nom et ( )
    return `Bonjour, je suis ${this.prenom}`;
  }
}

const bob = new Personne("Bob");
console.log(bob.saluer()); // Bonjour, je suis Bob
```

---

## 4. `extends` : créer une version spécialisée

`extends` permet de fabriquer une classe **à partir d'une autre** : la nouvelle
**hérite** de tout ce que fait la première, et peut **ajouter** ou **changer** des
choses. On parle de classe **parente** et de classe **enfant**.

```javascript
class Animal {
  constructor(nom) {
    this.nom = nom;
  }
  decrire() {
    return `${this.nom} est un animal`;
  }
}

class Chien extends Animal {   // Chien hérite de Animal
  aboyer() {
    return `${this.nom} fait Wouf !`;
  }
}

const rex = new Chien("Rex");
console.log(rex.decrire()); // hérité d'Animal : "Rex est un animal"
console.log(rex.aboyer());  // propre à Chien : "Rex fait Wouf !"
```

> 💡 Dans une classe enfant, `super(...)` appelle le **constructor du parent** pour
> ne pas réécrire ce qu'il fait déjà. Tu en verras un exemple dans le fichier `.js`.

---

## ▶️ À toi de jouer

Le fichier `classes.js` reprend tout ça pas à pas : une classe `CompteBancaire`
avec son constructor, ses méthodes (déposer, retirer), puis une classe enfant
`CompteEpargne` qui l'étend avec `extends` et `super`.

```bash
node --check js-ts/08_classes/classes.js   # vérifier la syntaxe
node js-ts/08_classes/classes.js           # lancer la démo
```

➡️ Module suivant : [`09_http`](../09_http/) — aller chercher des données sur internet.
