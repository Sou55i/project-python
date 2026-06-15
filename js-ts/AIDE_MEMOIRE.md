# 🃏 Aide-mémoire JavaScript / TypeScript (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases` et suivants.

---

## Lancer / afficher

```bash
node mon_script.js          # exécuter un fichier JavaScript
node --check mon_script.js  # vérifier la syntaxe SANS exécuter
```

```javascript
console.log("Bonjour");        // afficher du texte
console.log(`Âge : ${age}`);   // template literal : insère une variable entre ${ }
console.error("Problème !");   // afficher un message d'erreur
```

## Variables et types

```javascript
const age = 30;        // const : la valeur NE change PAS (à privilégier)
let score = 0;         // let   : la valeur POURRA changer
// var : ancienne façon, pleine de pièges -> on ne l'utilise PLUS

const prix = 9.99;     // number  : entier OU décimal (même type)
const nom = "Alice";   // string  : du texte
const actif = true;    // boolean : true / false (minuscules)
const rien = null;     // null      : volontairement vide
let vide;              // undefined : déclarée mais pas encore remplie

typeof age;            // connaître le type -> "number"
Number("42");          // texte -> nombre
String(42);            // nombre -> texte
parseInt("42", 10);    // texte -> entier
```

## Opérateurs

```javascript
+  -  *  /        // addition, soustraction, multiplication, division
%                 // reste (modulo) (7 % 2 === 1)
**                // puissance (2 ** 3 === 8)

===  !==          // égal / différent (STRICT : compare AUSSI le type, à privilégier)
<  >  <=  >=      // comparaisons
&&  ||  !         // ET / OU / NON logiques

"5" + 5           // "55" : avec du texte, + COLLE (attention !)
5 + 5             // 10   : avec des nombres, + ADDITIONNE
```

## Conditions

```javascript
if (age >= 18) {
  console.log("Majeur");
} else if (age >= 13) {
  console.log("Ado");
} else {
  console.log("Enfant");
}
```

## Boucles

```javascript
for (let i = 0; i < 5; i++) {        // 0,1,2,3,4
  console.log(i);
}

for (const fruit of ["pomme", "kiwi"]) {  // pour chaque élément
  console.log(fruit);
}

while (x < 10) {                     // tant que la condition est vraie
  x++;                               // x++ veut dire x = x + 1
}
```

## Tableaux (suite ordonnée, entre `[ ]`)

```javascript
const courses = ["pain", "lait"];
courses.push("œufs");     // ajouter à la fin
courses[0];               // premier élément (on compte à partir de 0)
courses.at(-1);           // dernier élément
courses.length;           // nombre d'éléments
courses.includes("pain"); // test d'appartenance -> true
courses.slice(1, 3);      // "tranche" : du 1 au 2
```

## Objets (clé → valeur, entre `{ }`)

```javascript
const personne = { nom: "Alice", age: 30 };
personne.nom;                 // accès par point -> "Alice"
personne["nom"];              // accès par crochets (même chose)
personne.ville = "Paris";     // ajouter / modifier
for (const [cle, valeur] of Object.entries(personne)) {
  console.log(cle, valeur);
}
```

## map / filter / reduce (transformer un tableau)

```javascript
const nombres = [1, 2, 3, 4];
nombres.map((n) => n * 2);             // [2, 4, 6, 8]   : transformer chaque élément
nombres.filter((n) => n % 2 === 0);    // [2, 4]         : garder ceux qui passent le test
nombres.reduce((total, n) => total + n, 0); // 10        : tout réduire à UNE valeur
nombres.forEach((n) => console.log(n)); // juste parcourir
```

## Fonctions

```javascript
// Façon CLASSIQUE
function saluer(nom, poli = true) {     // poli a une valeur par défaut
  if (poli) return `Bonjour ${nom}`;
  return `Salut ${nom}`;
}
saluer("Alice");                        // appel
saluer("Bob", false);                   // sans politesse

// Façon MODERNE : fonction fléchée (=>). Le 'return' est sous-entendu si une seule expression.
const doubler = (x) => x * 2;
const additionner = (a, b) => a + b;
```

## Asynchrone : Promise / async / await

```javascript
// Une PROMESSE = un résultat qui arrivera plus tard.
fetch(url)
  .then((reponse) => reponse.json())   // quand c'est prêt...
  .catch((err) => console.error(err)); // en cas d'erreur

// Version moderne, plus lisible : async / await
async function charger() {
  try {
    const reponse = await fetch(url);  // "attends" le résultat ici
    const data = await reponse.json();
    return data;
  } catch (err) {
    console.error(err);
  }
}
```

## Classes

```javascript
class Compte {
  constructor(titulaire, solde = 0) {  // appelé à la création
    this.titulaire = titulaire;        // this = l'objet courant
    this.solde = solde;
  }
  deposer(montant) {                   // une méthode
    this.solde += montant;
  }
}
const c = new Compte("Alice", 100);    // new fabrique un objet à partir du moule
c.deposer(50);
```

## Modules (découper son code)

```javascript
// --- Façon MODERNE : ES Modules (fichiers .mjs, ou "type": "module") ---
export function additionner(a, b) { return a + b; }   // dans outils.js
import { additionner } from "./outils.js";            // dans un autre fichier

// --- Façon CLASSIQUE : CommonJS (fichiers .js par défaut) ---
module.exports = { additionner };                     // dans outils.js
const { additionner } = require("./outils.js");       // dans un autre fichier
```

## npm (installer des outils)

```bash
npm init -y               # créer un fichier package.json
npm install nom-du-paquet # installer une dépendance (crée node_modules/)
npm install               # installer tout ce qui est listé dans package.json
```

## TypeScript : ajouter des types

```typescript
// Annotations : on précise la NATURE après ':'
let age: number = 30;
let nom: string = "Alice";
let actif: boolean = true;
let scores: number[] = [12, 15, 18];      // tableau de nombres

// Une fonction typée : types des paramètres ET du retour
function saluer(nom: string): string {
  return `Bonjour ${nom}`;
}

// Une interface : la FORME attendue d'un objet (un contrat)
interface Personne {
  nom: string;
  age: number;
  ville?: string;          // le '?' rend ce champ optionnel
}
const alice: Personne = { nom: "Alice", age: 30 };
```

## Structure type d'un script Node

```javascript
// Description du script : à quoi il sert, comment le lancer.
import fs from "node:fs";        // 1. imports (les outils)
const DOSSIER = "resultats";     // 2. constantes (EN_MAJUSCULES)
function traiter(data) { ... }   // 3. fonctions (on les DÉFINIT)
function main() {                // 4. point d'entrée
  // entrée -> traitement -> sortie
}
main();                          //    on APPELLE le point d'entrée
```

➡️ Voir aussi : [ANATOMIE_D_UN_SCRIPT.md](./ANATOMIE_D_UN_SCRIPT.md) et [GLOSSAIRE.md](./GLOSSAIRE.md).
