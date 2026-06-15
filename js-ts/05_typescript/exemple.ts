// MODULE 05 - Introduction à TypeScript
// ======================================
// TypeScript = JavaScript + les TYPES. On ajoute des étiquettes (": type")
// qui aident à repérer les erreurs AVANT de lancer le programme.
//
// Compiler puis lancer :
//   tsc js-ts/05_typescript/exemple.ts        (vérifie les types et génère exemple.js)
//   node js-ts/05_typescript/exemple.js        (exécute le résultat)
// Vérifier les types sans rien générer :
//   tsc --noEmit js-ts/05_typescript/exemple.ts

// ─────────────────────────────────────────────
// 1. TYPES DE BASE ET ANNOTATIONS
// ─────────────────────────────────────────────
// On écrit "nom: type". TypeScript refusera toute valeur du mauvais type.
const prenom: string = "Alice"; // string  : du texte
const age: number = 30; // number  : un nombre
const majeur: boolean = true; // boolean : true ou false

console.log(`${prenom}, ${age} ans, majeur ? ${majeur}`);

// ─────────────────────────────────────────────
// 2. TYPER UNE FONCTION (paramètres + retour)
// ─────────────────────────────────────────────
// (a: number, b: number) annote les paramètres ; ": number" annote le RETOUR.
function additionner(a: number, b: number): number {
  return a + b;
}
console.log(`3 + 4 = ${additionner(3, 4)}`);

// Une fonction qui n'affiche que du texte ne renvoie rien : son retour est "void".
function direBonjour(nom: string): void {
  console.log(`Bonjour ${nom} !`);
}
direBonjour(prenom);

// ─────────────────────────────────────────────
// 3. INTERFACE : décrire la FORME d'un objet
// ─────────────────────────────────────────────
// Une interface est un modèle : elle liste les clés attendues et leurs types.
interface Personne {
  prenom: string;
  age: number;
  ville?: string; // le "?" rend cette clé OPTIONNELLE
}

// Cet objet DOIT respecter le modèle Personne (sinon tsc se plaint).
const bob: Personne = { prenom: "Bob", age: 25, ville: "Lyon" };
const chloe: Personne = { prenom: "Chloé", age: 35 }; // ville est facultative

// ─────────────────────────────────────────────
// 4. TYPE D'UNE FONCTION PASSÉE EN ARGUMENT
// ─────────────────────────────────────────────
// On peut typer un callback : "(p: Personne) => string" se lit
// "une fonction qui prend une Personne et renvoie un string".
function decrire(p: Personne, format: (p: Personne) => string): string {
  return format(p);
}

// Une fonction fléchée typée, donnée comme comportement.
const enLigne = (p: Personne): string => `${p.prenom} (${p.age} ans)`;

console.log(decrire(bob, enLigne));
console.log(decrire(chloe, enLigne));

// Un tableau typé : "Personne[]" = un tableau de Personne.
const equipe: Personne[] = [bob, chloe];
console.log(`L'équipe compte ${equipe.length} personnes.`);
