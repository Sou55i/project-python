// ===========================================================
//  MODULE 03 - Fonctions avancées
//  ==========================================================
//  Fonctions fléchées, callbacks, fonctions d'ordre supérieur, closures.
//
//  Lance-le :  node js-ts/03_fonctions_avancees/fonctions.js
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. Comparer une fonction classique et sa version fléchée.
//     2. Passer une fonction à une autre : le callback.
//     3. Écrire une fonction d'ordre supérieur (qui reçoit un callback).
//     4. Découvrir une closure : une fonction qui SE SOUVIENT (un compteur).
//     5. Une closure qui FABRIQUE des fonctions (un multiplicateur paramétré).

// ─────────────────────────────────────────────
// 1. FONCTION CLASSIQUE vs FONCTION FLÉCHÉE
// ─────────────────────────────────────────────
// Les deux font EXACTEMENT la même chose ; la fléchée est juste plus courte.
function doublerClassique(x) {
  return x * 2;
}
const doublerFleche = (x) => x * 2; // return sous-entendu (corps sur une ligne)

console.log(`classique : ${doublerClassique(10)}`); // 20
console.log(`fléchée   : ${doublerFleche(10)}`); // 20

// ─────────────────────────────────────────────
// 2. LE CALLBACK : une fonction passée en argument
// ─────────────────────────────────────────────
// Ici "saluer" est une fonction... qu'on donne à "appliquerA" comme un argument.
const saluer = (nom) => `Bonjour ${nom} !`;

// appliquerA prend une valeur ET une fonction, puis appelle la fonction.
const appliquerA = (valeur, fonction) => fonction(valeur);

console.log(appliquerA("Alice", saluer)); // "Bonjour Alice !"

// ─────────────────────────────────────────────
// 3. FONCTION D'ORDRE SUPÉRIEUR : elle reçoit un callback
// ─────────────────────────────────────────────
// "repeter" ne sait pas QUOI faire : c'est l'appelant qui fournit le comportement.
function repeter(n, action) {
  for (let i = 0; i < n; i++) {
    action(i); // on appelle le callback à chaque tour, avec l'indice
  }
}

// On lui donne, sur place, une fonction fléchée comme comportement.
repeter(3, (i) => console.log(`tour numéro ${i}`)); // tours 0, 1, 2

// ─────────────────────────────────────────────
// 4. CLOSURE : une fonction qui SE SOUVIENT
// ─────────────────────────────────────────────
// creerCompteur fabrique et RENVOIE une fonction. Cette fonction garde un accès
// à la variable "compte", même après que creerCompteur a terminé son travail.
function creerCompteur() {
  let compte = 0; // variable "privée", invisible de l'extérieur
  return () => {
    compte = compte + 1; // la fonction renvoyée se souvient de "compte"
    return compte;
  };
}

const compteur = creerCompteur();
console.log(`compteur : ${compteur()}`); // 1
console.log(`compteur : ${compteur()}`); // 2
console.log(`compteur : ${compteur()}`); // 3  -> l'état a survécu entre les appels

// Chaque compteur a SON propre "compte" : ils sont indépendants.
const autreCompteur = creerCompteur();
console.log(`autre compteur : ${autreCompteur()}`); // 1 (et non 4)

// ─────────────────────────────────────────────
// 5. CLOSURE QUI FABRIQUE DES FONCTIONS
// ─────────────────────────────────────────────
// creerMultiplicateur "se souvient" du facteur qu'on lui a donné.
function creerMultiplicateur(facteur) {
  return (x) => x * facteur; // la fonction renvoyée mémorise "facteur"
}

const fois3 = creerMultiplicateur(3); // une fonction qui multiplie par 3
const fois10 = creerMultiplicateur(10); // une fonction qui multiplie par 10
console.log(`fois3(5)  = ${fois3(5)}`); // 15
console.log(`fois10(5) = ${fois10(5)}`); // 50
