// MODULE 06 - outils.js : un module qui EXPORTE des fonctions (CommonJS)
// ======================================================================
// Ce fichier ne fait RIEN tout seul : il se contente de DÉFINIR des outils
// et de les METTRE À DISPOSITION. C'est un autre fichier (utiliser.js) qui
// viendra les chercher pour s'en servir.

// Une petite fonction toute simple : additionner deux nombres.
function additionner(a, b) {
  return a + b;
}

// Une autre : mettre la première lettre d'un mot en majuscule.
//   mot[0]            -> la première lettre
//   .toUpperCase()    -> la passe en MAJUSCULE
//   mot.slice(1)      -> tout le reste du mot, à partir de la 2e lettre
function capitaliser(mot) {
  return mot[0].toUpperCase() + mot.slice(1);
}

// ─────────────────────────────────────────────
// L'EXPORT : la ligne la plus importante du fichier
// ─────────────────────────────────────────────
// "module.exports" est la VITRINE du module : ce qu'on range dedans devient
// visible depuis l'extérieur. Ici, on expose un objet avec nos deux fonctions.
// Tout ce qui n'est PAS dans module.exports reste privé à ce fichier.
module.exports = { additionner, capitaliser };
