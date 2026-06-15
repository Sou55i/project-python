// MODULE 06 - utiliser.mjs : importer en syntaxe MODERNE (ES Modules)
// ==================================================================
// À lancer :  node js-ts/06_modules_npm/utiliser.mjs

// "import { ... } from" récupère, par leur nom, les fonctions exportées ailleurs.
// Avec les ES Modules, on précise le nom de fichier COMPLET (avec .mjs).
import { additionner, capitaliser } from "./outils.mjs";

console.log("2 + 3 =", additionner(2, 3));
console.log("capitaliser('alice') =>", capitaliser("alice"));

console.log("\n✅ Même résultat que utiliser.js, mais avec import/export.");
