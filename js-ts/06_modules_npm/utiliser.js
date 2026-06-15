// MODULE 06 - utiliser.js : un module qui IMPORTE et se sert d'un autre (CommonJS)
// ===============================================================================
// Ce fichier-ci est celui qu'on LANCE :  node js-ts/06_modules_npm/utiliser.js
// Il ne réécrit pas les outils : il va les CHERCHER dans outils.js.

// ─────────────────────────────────────────────
// L'IMPORT : on récupère ce que outils.js a exporté
// ─────────────────────────────────────────────
// require("./outils.js") -> "va chercher le module à côté de moi nommé outils.js"
// Il renvoie exactement l'objet rangé dans module.exports là-bas.
const outils = require("./outils.js");

// On peut maintenant utiliser les fonctions via l'objet "outils".
console.log("2 + 3 =", outils.additionner(2, 3));
console.log("capitaliser('alice') =>", outils.capitaliser("alice"));

// ─────────────────────────────────────────────
// Variante : la DÉCONSTRUCTION à l'import
// ─────────────────────────────────────────────
// Au lieu de tout mettre dans "outils", on peut piocher directement les fonctions
// qui nous intéressent. C'est plus court à écrire ensuite.
const { additionner, capitaliser } = require("./outils.js");
console.log("10 + 5 =", additionner(10, 5));
console.log("capitaliser('bob') =>", capitaliser("bob"));

console.log("\n✅ Ce fichier s'est servi de fonctions écrites dans outils.js.");
