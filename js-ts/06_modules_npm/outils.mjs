// MODULE 06 - outils.mjs : le MÊME module, en syntaxe MODERNE (ES Modules)
// ========================================================================
// L'extension .mjs dit à Node : "ici, on utilise export / import".
// Compare avec outils.js : c'est la même idée, une autre écriture.

// "export" devant une fonction = elle devient disponible à l'extérieur.
export function additionner(a, b) {
  return a + b;
}

export function capitaliser(mot) {
  return mot[0].toUpperCase() + mot.slice(1);
}
