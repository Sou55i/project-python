// ===========================================================
//  MODULE 01 - Mini-projet : une calculatrice en JavaScript (Node.js)
//  ==========================================================
//  On combine la lecture de l'entrée (readline), les conditions et le calcul.
//
//  Lance-le :  node js-ts/01_les_bases/mini_calculatrice.js
//  Saisie simulée : printf "+\n7\n5\n" | node js-ts/01_les_bases/mini_calculatrice.js
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. Ouvrir la lecture de l'entrée standard avec le module "readline".
//     2. Poser 3 questions à la suite : opération, puis deux nombres.
//     3. Choisir le calcul selon l'opération (switch), gérer la division par zéro.
//     4. Afficher le résultat et fermer proprement.

// 'require' importe un module fourni par Node. 'readline' lit l'entrée ligne par ligne.
const readline = require("readline");

// On crée une interface reliée à l'entrée (stdin) et à la sortie (stdout).
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

// rl.question(texte, callback) pose une question et appelle la fonction quand la
// réponse arrive. Comme c'est asynchrone, on imbrique les questions.
rl.question("Operation (+, -, *, /) : ", (op) => {
  rl.question("Premier nombre  : ", (a) => {
    rl.question("Deuxieme nombre : ", (b) => {
      // Number(...) convertit le texte saisi en nombre (sinon "7"+"5" donnerait "75").
      const n1 = Number(a);
      const n2 = Number(b);
      let resultat;

      // switch choisit le bloc correspondant à la valeur de op.
      switch (op.trim()) {
        case "+": resultat = n1 + n2; break;
        case "-": resultat = n1 - n2; break;
        case "*": resultat = n1 * n2; break;
        case "/":
          // On se protège de la division par zéro.
          if (n2 === 0) {
            console.log("Erreur : division par zero impossible.");
            rl.close();
            return;
          }
          resultat = n1 / n2;
          break;
        default:
          console.log("Operation inconnue.");
          rl.close();
          return;
      }

      console.log(`Resultat : ${resultat}`);
      rl.close(); // ferme l'interface -> le programme se termine proprement
    });
  });
});
