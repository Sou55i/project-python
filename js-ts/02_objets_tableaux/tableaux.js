// MODULE 02 - Les tableaux [ ] et leurs méthodes
// ==============================================
// Un tableau est une suite ORDONNÉE de valeurs. On compte à partir de 0 !
//
// Lance-le :  node js-ts/02_objets_tableaux/tableaux.js

// ─────────────────────────────────────────────
// 1. CRÉER ET LIRE UN TABLEAU
// ─────────────────────────────────────────────
const fruits = ["pomme", "banane", "cerise"]; // 3 valeurs entre crochets
console.log(`Premier fruit (indice 0) : ${fruits[0]}`); // "pomme"
console.log(`Nombre de fruits         : ${fruits.length}`); // 3

// ─────────────────────────────────────────────
// 2. push : AJOUTER à la fin
// ─────────────────────────────────────────────
fruits.push("kiwi"); // modifie le tableau en place
console.log(`Après push : ${fruits.join(", ")}`); // pomme, banane, cerise, kiwi

// ─────────────────────────────────────────────
// 3. map : TRANSFORMER chaque élément (-> nouveau tableau)
// ─────────────────────────────────────────────
// On donne à map une fonction. Elle est appelée pour CHAQUE élément, et map
// renvoie un NOUVEAU tableau avec les résultats. L'original n'est pas touché.
const nombres = [1, 2, 3, 4];
const doubles = nombres.map((n) => n * 2); // pour chaque n, on calcule n * 2
console.log(`Doublés : ${doubles.join(", ")}`); // 2, 4, 6, 8

// ─────────────────────────────────────────────
// 4. filter : GARDER ceux qui passent un test (-> nouveau tableau)
// ─────────────────────────────────────────────
// La fonction doit renvoyer true (on garde) ou false (on jette).
const pairs = nombres.filter((n) => n % 2 === 0); // % donne le reste : 0 = pair
console.log(`Nombres pairs : ${pairs.join(", ")}`); // 2, 4

// ─────────────────────────────────────────────
// 5. reduce : COMBINER tout en UNE seule valeur
// ─────────────────────────────────────────────
// reduce prend (1) une fonction (accumulateur, élément) et (2) une valeur de départ.
// L'accumulateur garde le résultat d'un tour à l'autre.
const somme = nombres.reduce((acc, n) => acc + n, 0); // 0 puis +1 +2 +3 +4
console.log(`Somme totale : ${somme}`); // 10

// ─────────────────────────────────────────────
// 6. find : trouver le PREMIER élément qui passe un test
// ─────────────────────────────────────────────
const premierGrand = nombres.find((n) => n > 2); // le premier qui dépasse 2
console.log(`Premier nombre > 2 : ${premierGrand}`); // 3

// ─────────────────────────────────────────────
// 7. ON COMBINE TOUT : un tableau d'objets
// ─────────────────────────────────────────────
const equipe = [
  { prenom: "Alice", age: 30 },
  { prenom: "Bob", age: 25 },
  { prenom: "Chloé", age: 35 },
];

// On enchaîne filter puis map : garder les 30+, puis ne garder que le prénom.
const noms30plus = equipe
  .filter((p) => p.age >= 30) // garde Alice et Chloé
  .map((p) => p.prenom); // -> ["Alice", "Chloé"]
console.log(`30 ans ou plus : ${noms30plus.join(", ")}`);

// La moyenne d'âge avec reduce, puis une division par le nombre de personnes.
const sommeAges = equipe.reduce((acc, p) => acc + p.age, 0);
console.log(`Âge moyen : ${sommeAges / equipe.length} ans`); // 30
