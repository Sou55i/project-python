// MODULE 02 - Les objets { clé: valeur }
// ======================================
// Un objet regroupe des informations sous forme de paires "clé: valeur".
//
// Lance-le :  node js-ts/02_objets_tableaux/objets.js

// ─────────────────────────────────────────────
// 1. CRÉER UN OBJET
// ─────────────────────────────────────────────
// Entre ACCOLADES { }, on liste des paires "clé: valeur" séparées par des virgules.
const personne = {
  prenom: "Alice", // la clé "prenom" -> la valeur "Alice" (un string)
  age: 30, // la clé "age" -> 30 (un number)
  majeur: true, // la clé "majeur" -> true (un boolean)
};

// ─────────────────────────────────────────────
// 2. LIRE UNE VALEUR
// ─────────────────────────────────────────────
// Deux notations équivalentes : le POINT (la plus courante) ou les CROCHETS.
console.log(`Prénom : ${personne.prenom}`); // notation avec un point
console.log(`Âge    : ${personne["age"]}`); // notation avec des crochets

// ─────────────────────────────────────────────
// 3. MODIFIER ET AJOUTER
// ─────────────────────────────────────────────
// On peut changer une valeur existante...
personne.age = 31; // on a fêté un anniversaire
// ...ou AJOUTER une nouvelle clé qui n'existait pas encore.
personne.ville = "Lyon";
console.log(`${personne.prenom} a ${personne.age} ans et habite à ${personne.ville}.`);

// ─────────────────────────────────────────────
// 4. PARCOURIR LES CLÉS ET LES VALEURS
// ─────────────────────────────────────────────
// Object.keys(obj)   -> un tableau des CLÉS    : ["prenom", "age", ...]
// Object.values(obj) -> un tableau des VALEURS  : ["Alice", 31, ...]
// Object.entries(obj)-> un tableau de paires [clé, valeur]
console.log("Les clés de l'objet :", Object.keys(personne));

// for...of sur Object.entries : on récupère la clé ET la valeur à chaque tour.
for (const [cle, valeur] of Object.entries(personne)) {
  console.log(`  ${cle} = ${valeur}`);
}

// ─────────────────────────────────────────────
// 5. OBJETS IMBRIQUÉS
// ─────────────────────────────────────────────
// Une valeur peut elle-même être un objet (ou un tableau) : on imbrique.
const livre = {
  titre: "Le Petit Prince",
  auteur: { prenom: "Antoine", nom: "de Saint-Exupéry" }, // un objet dans l'objet
  genres: ["conte", "philosophie"], // un tableau dans l'objet
};
console.log(`"${livre.titre}" par ${livre.auteur.prenom} ${livre.auteur.nom}`);
console.log(`Genres : ${livre.genres.join(", ")}`); // join colle les éléments avec ", "
