// MODULE 01 - Les briques de base
// ================================
// Ce script illustre, dans l'ordre, les notions du README :
// variables, types, template literals, conditions, boucles et fonctions.
//
// Lance-le :  node js-ts/01_les_bases/bases.js

// ─────────────────────────────────────────────
// 1. VARIABLES ET TYPES
// ─────────────────────────────────────────────
// Une variable = une boîte étiquetée. Le '=' RANGE la valeur de droite dans
// la boîte nommée à gauche.
//   const -> la valeur ne changera PAS (à utiliser par défaut, c'est le plus sûr).
//   let   -> la valeur POURRA changer plus tard.
//   var   -> ancienne façon, pleine de pièges : on ne l'utilise PLUS.
const prenom = "Alice";   // string  : du texte (entre guillemets "...")
const age = 30;           // number  : un nombre (entier OU à virgule, même type)
const taille = 1.68;      // number  : ici un nombre à virgule (on écrit un POINT)
const majeur = true;      // boolean : vrai/faux, en minuscules (true ou false)

// null et undefined : deux façons de dire "il n'y a pas de valeur".
const surnom = null;        // null      : volontairement vide (j'ai mis rien, exprès)
let adresse;                // undefined : déclarée mais jamais remplie pour l'instant

// ─────────────────────────────────────────────
// 2. TEMPLATE LITERALS : insérer des variables dans du texte
// ─────────────────────────────────────────────
// On utilise des ACCENTS GRAVES `...` (pas des guillemets) et ${ } pour
// insérer la valeur d'une variable directement dans le texte.
console.log(`${prenom}, ${age} ans, ${taille} m. Majeur ? ${majeur}`);
console.log(`Surnom : ${surnom}, adresse : ${adresse}`);

// typeof révèle la NATURE (le type) d'une valeur. Utile pour comprendre un bug.
console.log(`Le type de 'age' est : ${typeof age}`);

// ATTENTION au type : "5" (texte) et 5 (nombre) ne se comportent pas pareil.
console.log("5" + "5"); // affiche 55 : avec du texte, '+' COLLE les deux morceaux
console.log(5 + 5);     // affiche 10 : avec des nombres, '+' ADDITIONNE

// ─────────────────────────────────────────────
// 3. CONDITIONS (if / else if / else)
// ─────────────────────────────────────────────
const note = 12;
// 'if' = "si". La condition est entre PARENTHÈSES ( ), et le bloc qui en
// dépend est entre ACCOLADES { }.
if (note >= 16) {                 // >= signifie "supérieur ou égal à"
  console.log("Très bien 🌟");
} else if (note >= 10) {          // 'else if' = "sinon si" (testé si le if était faux)
  console.log("Reçu ✅");
} else {                          // 'else' = "sinon" (dans tous les autres cas)
  console.log("À retravailler ❌");
}

// ─────────────────────────────────────────────
// 4. BOUCLES (répéter une action)
// ─────────────────────────────────────────────
// Boucle 'for' : répète un nombre PRÉCIS de fois. La parenthèse a 3 parties :
//   let i = 0  -> on part de 0
//   i < 3      -> on continue tant que c'est vrai
//   i++        -> après chaque tour, on ajoute 1 à i (i++ veut dire i = i + 1)
for (let i = 0; i < 3; i++) {
  console.log(`Répétition ${i}`);
}

// Boucle 'while' : "TANT QUE la condition est vraie, répète".
let compteur = 0;
while (compteur < 3) {
  console.log(`compteur = ${compteur}`);
  compteur++;     // sans cette ligne, compteur resterait à 0 et la boucle
  //                tournerait à l'infini !
}

// Boucle 'for...of' : "POUR CHAQUE élément de la liste (le tableau)".
// Un tableau = une suite ordonnée de valeurs, entre crochets [ ].
const fruits = ["pomme", "banane", "cerise"];
for (const fruit of fruits) {
  console.log(`- ${fruit}`);
}

// ─────────────────────────────────────────────
// 5. FONCTIONS (emballer du code réutilisable)
// ─────────────────────────────────────────────
// Façon CLASSIQUE avec le mot-clé 'function'.
//   saluer    = le nom qu'on donne à la fonction
//   (prenom)  = le PARAMÈTRE : une information donnée en entrée
//   return    = la valeur que la fonction RENVOIE à celui qui l'a appelée
function saluer(prenom) {
  return `Bonjour ${prenom} !`;
}

// Ici on APPELLE la fonction : on lui donne une valeur, elle renvoie le message.
console.log(saluer("Alice"));
console.log(saluer("Bob"));

// Façon MODERNE : la fonction fléchée (=>). Elle fait la même chose, en plus court.
// Quand le corps tient en une expression, le 'return' est sous-entendu.
const doubler = (x) => x * 2;
console.log(`Le double de 21 est ${doubler(21)}`);
