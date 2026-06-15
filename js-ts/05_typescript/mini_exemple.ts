// MODULE 05 - Mini-exemple TypeScript
// ===================================
// Un tout petit fichier pour s'entraîner : une interface + une fonction typée.
//
//   tsc js-ts/05_typescript/mini_exemple.ts
//   node js-ts/05_typescript/mini_exemple.js

// Une interface décrit la forme d'un produit.
interface Produit {
  nom: string;
  prix: number; // en euros
}

// Une fonction typée : prend un Produit, renvoie un string (l'étiquette).
function etiquette(p: Produit): string {
  return `${p.nom} : ${p.prix} €`;
}

// On crée un produit conforme à l'interface, puis on l'affiche.
const cafe: Produit = { nom: "Café", prix: 3 };
console.log(etiquette(cafe));
