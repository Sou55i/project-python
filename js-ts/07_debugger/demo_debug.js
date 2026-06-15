// MODULE 07 - demo_debug.js : les outils pour traquer les bugs
// ============================================================
// Ce script ne PLANTE PAS : il MONTRE volontairement les bugs classiques et la
// façon de les observer / les gérer. Lis chaque section, puis lance :
//   node js-ts/07_debugger/demo_debug.js
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. console.log / console.error / console.table : observer les valeurs.
//     2. Le bug "undefined" : lire une clé qui n'existe pas.
//     3. Le bug "NaN" : un calcul avec quelque chose qui n'est pas un nombre.
//     4. L'asynchrone non attendu : oublier "await".
//     5. try / catch : attraper une erreur pour ne pas planter.

// ─────────────────────────────────────────────
// 1. OBSERVER : console.log, console.error, console.table
// ─────────────────────────────────────────────
console.log("1) Observer les valeurs");
console.log("   log normal :", "tout va bien");
console.error("   ceci est un message d'ERREUR (sortie d'erreur)");

// console.table affiche une liste d'objets sous forme de GRILLE lisible.
const personnes = [
  { prenom: "Alice", age: 30 },
  { prenom: "Bob", age: 25 },
];
console.table(personnes);

// ─────────────────────────────────────────────
// 2. LE BUG "undefined" : lire une clé qui n'existe pas
// ─────────────────────────────────────────────
console.log("\n2) Le bug undefined");
const personne = { nom: "Alice" }; // pas de clé "age"
console.log("   personne.age =", personne.age); // undefined : la clé n'existe pas
// Le réflexe pour comprendre : afficher l'objet ENTIER pour voir ce qu'il contient.
console.log("   contenu réel de personne :", personne);

// ─────────────────────────────────────────────
// 3. LE BUG "NaN" : Not a Number ("pas un nombre")
// ─────────────────────────────────────────────
console.log("\n3) Le bug NaN");
const resultat = 10 * "abc"; // on multiplie un nombre par du texte -> impossible
console.log("   10 * 'abc' =", resultat); // NaN
// Number.isNaN(...) permet de TESTER si une valeur est ce fameux NaN.
console.log("   est-ce un NaN ? ", Number.isNaN(resultat)); // true

// ─────────────────────────────────────────────
// 4. L'ASYNCHRONE NON ATTENDU : oublier "await"
// ─────────────────────────────────────────────
console.log("\n4) Oublier await");
async function donnerValeur() {
  return 42;
}
// SANS await : on récupère la PROMESSE, pas la valeur. Piège classique !
const sansAwait = donnerValeur();
console.log("   sans await ->", sansAwait); // affiche un objet Promise, pas 42

// ─────────────────────────────────────────────
// 5. try / catch : attraper une erreur sans planter
// ─────────────────────────────────────────────
console.log("\n5) try / catch");
const texteAbime = "{ ceci n'est pas du JSON }";
try {
  // JSON.parse "casse" si le texte n'est pas un JSON valide -> il LANCE une erreur.
  const data = JSON.parse(texteAbime);
  console.log("   données :", data);
} catch (erreur) {
  // On ATTRAPE l'erreur ici : le programme continue au lieu de planter.
  console.error("   erreur attrapée :", erreur.message);
}

// ─────────────────────────────────────────────
// 6. Bien faire : AVEC await, on obtient la vraie valeur, puis on se termine
// ─────────────────────────────────────────────
async function main() {
  const avecAwait = await donnerValeur(); // cette fois on ATTEND la valeur
  console.log("\n6) Avec await ->", avecAwait); // 42, comme prévu
  console.log("\n✅ Fin de la démo : aucun bug n'a fait planter le script.");
}
main();
