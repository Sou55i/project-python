// PROJET CAPSTONE - gestionnaire_taches.js
// =========================================
// Une mini todo list qui SE SOUVIENT de ses tâches grâce à un fichier JSON.
// Non interactif : il ajoute des tâches de démo, sauvegarde, recharge, affiche.
// Lance :
//   node js-ts/projets/gestionnaire_taches.js
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. On importe les outils : fs (fichiers) et path (chemins) de Node.
//     2. Une classe GestionnaireTaches : ajouter, marquer comme faite, afficher.
//     3. sauvegarder() : objets -> texte JSON -> fichier dans exemples/.
//     4. charger() : fichier -> texte JSON -> objets (la persistance !).
//     5. Le scénario : on ajoute des tâches, on sauvegarde, on RECHARGE, on affiche.

// ─────────────────────────────────────────────
// 1. LES OUTILS DE NODE (modules intégrés, rien à installer)
// ─────────────────────────────────────────────
// fs/promises = lire/écrire des fichiers avec des Promesses (await).
const fs = require("node:fs/promises");
// path = construire des chemins de fichiers de façon fiable.
const path = require("node:path");

// __dirname = le dossier où se trouve CE fichier. On range les données à côté,
// dans un sous-dossier "exemples/".
const DOSSIER = path.join(__dirname, "exemples");
const FICHIER = path.join(DOSSIER, "taches.json");

// ─────────────────────────────────────────────
// 2. LA CLASSE : le cœur de l'application
// ─────────────────────────────────────────────
class GestionnaireTaches {
  constructor() {
    this.taches = []; // au départ, aucune tâche : un tableau vide
  }

  // Ajouter une tâche. Chaque tâche est un objet { id, titre, faite }.
  ajouter(titre) {
    const nouvelle = {
      id: this.taches.length + 1, // un identifiant simple, basé sur le nombre actuel
      titre: titre,
      faite: false, // par défaut, une nouvelle tâche n'est pas faite
    };
    this.taches.push(nouvelle); // push = ajoute à la fin du tableau
    return nouvelle;
  }

  // Marquer une tâche comme faite, à partir de son id.
  marquerFaite(id) {
    // find = trouve le PREMIER élément qui correspond à la condition.
    const tache = this.taches.find((t) => t.id === id);
    if (tache) {
      tache.faite = true;
    }
  }

  // Afficher les tâches de façon lisible.
  afficher() {
    console.log("📋 Mes tâches :");
    for (const t of this.taches) {
      const coche = t.faite ? "[x]" : "[ ]"; // [x] si faite, [ ] sinon
      console.log(`   ${coche} (#${t.id}) ${t.titre}`);
    }
  }

  // ─────────────────────────────────────────────
  // 3. SAUVEGARDER : objets -> texte JSON -> fichier
  // ─────────────────────────────────────────────
  async sauvegarder() {
    // On crée le dossier exemples/ s'il n'existe pas (recursive: pas d'erreur s'il existe).
    await fs.mkdir(DOSSIER, { recursive: true });
    // On transforme le tableau d'objets en texte JSON joliment indenté (le 2).
    const texte = JSON.stringify(this.taches, null, 2);
    await fs.writeFile(FICHIER, texte, "utf-8"); // on écrit ce texte dans le fichier
    console.log(`💾 Sauvegardé ${this.taches.length} tâche(s) dans exemples/taches.json`);
  }

  // ─────────────────────────────────────────────
  // 4. CHARGER : fichier -> texte JSON -> objets
  // ─────────────────────────────────────────────
  async charger() {
    try {
      const texte = await fs.readFile(FICHIER, "utf-8"); // on lit le fichier
      this.taches = JSON.parse(texte); // on retransforme le texte en tableau d'objets
      console.log(`📂 Rechargé ${this.taches.length} tâche(s) depuis le disque.`);
    } catch (erreur) {
      // Si le fichier n'existe pas encore (1re fois), on repart d'une liste vide.
      console.log("ℹ️  Aucun fichier existant : on démarre avec une liste vide.");
      this.taches = [];
    }
  }
}

// ─────────────────────────────────────────────
// 5. LE SCÉNARIO DE DÉMONSTRATION (non interactif)
// ─────────────────────────────────────────────
async function main() {
  // On crée une première instance, on la remplit, on la sauvegarde.
  const gestionnaire = new GestionnaireTaches();
  gestionnaire.ajouter("Apprendre les modules");
  gestionnaire.ajouter("Comprendre les classes");
  gestionnaire.ajouter("Faire une requête fetch");
  gestionnaire.marquerFaite(1); // on marque la première comme faite

  console.log("--- Avant sauvegarde ---");
  gestionnaire.afficher();
  await gestionnaire.sauvegarder();

  // Preuve de la PERSISTANCE : on crée une instance TOUTE NEUVE (liste vide),
  // puis on la remplit en RECHARGEANT le fichier écrit juste avant.
  console.log("\n--- Après rechargement (nouvelle instance vide) ---");
  const apresRedemarrage = new GestionnaireTaches();
  await apresRedemarrage.charger();
  apresRedemarrage.afficher();

  console.log("\n✅ Fin du projet : tâches sauvegardées puis rechargées depuis le disque.");
}

main();
