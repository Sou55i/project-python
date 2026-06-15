// MODULE 08 - classes.js : les classes ES6, pas à pas
// ===================================================
// On fabrique un "moule" CompteBancaire, on en sort des objets, puis on crée
// une version spécialisée CompteEpargne avec extends. Lance :
//   node js-ts/08_classes/classes.js
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. Une classe CompteBancaire : constructor (les données) + this.
//     2. Des méthodes : deposer, retirer, afficher (ce que l'objet sait faire).
//     3. On FABRIQUE deux comptes (deux instances) avec "new".
//     4. Une classe enfant CompteEpargne qui hérite avec "extends" et "super".
//     5. On vérifie que l'enfant a TOUT du parent + ses propres capacités.

// ─────────────────────────────────────────────
// 1 & 2. LA CLASSE PARENTE : données (constructor) + méthodes
// ─────────────────────────────────────────────
class CompteBancaire {
  // Le constructor est appelé automatiquement par "new". Il REMPLIT l'objet.
  constructor(titulaire, soldeInitial) {
    this.titulaire = titulaire;   // "this" = cet objet-ci ; on y range le titulaire
    this.solde = soldeInitial;    // ... et son solde de départ
  }

  // Une méthode = une fonction rangée dans la classe (pas de mot "function").
  deposer(montant) {
    this.solde = this.solde + montant; // on modifie LE solde DE CET objet
    return `Dépôt de ${montant} € -> nouveau solde : ${this.solde} €`;
  }

  retirer(montant) {
    if (montant > this.solde) {
      // On se protège : on ne retire pas plus que ce qu'il y a.
      return `Retrait refusé : solde insuffisant (${this.solde} €).`;
    }
    this.solde = this.solde - montant;
    return `Retrait de ${montant} € -> nouveau solde : ${this.solde} €`;
  }

  afficher() {
    return `Compte de ${this.titulaire} : ${this.solde} €`;
  }
}

// ─────────────────────────────────────────────
// 3. FABRIQUER DES OBJETS (instances) avec "new"
// ─────────────────────────────────────────────
const compteAlice = new CompteBancaire("Alice", 100); // new -> appelle le constructor
const compteBob = new CompteBancaire("Bob", 0);

console.log(compteAlice.afficher());        // Compte de Alice : 100 €
console.log(compteAlice.deposer(50));       // 150 €
console.log(compteAlice.retirer(200));      // refusé : solde insuffisant
console.log(compteAlice.retirer(30));       // 120 €
console.log(compteBob.afficher());          // Compte de Bob : 0 € (indépendant !)

// ─────────────────────────────────────────────
// 4. UNE CLASSE ENFANT : extends + super
// ─────────────────────────────────────────────
// CompteEpargne EST un CompteBancaire, mais avec un taux d'intérêt en plus.
class CompteEpargne extends CompteBancaire {
  constructor(titulaire, soldeInitial, taux) {
    // super(...) appelle le constructor du PARENT pour réutiliser son travail
    // (remplir titulaire et solde) au lieu de le réécrire.
    super(titulaire, soldeInitial);
    this.taux = taux; // donnée propre à l'enfant
  }

  // Une méthode supplémentaire, qui n'existe pas chez le parent.
  ajouterInterets() {
    const interets = this.solde * this.taux;
    this.solde = this.solde + interets;
    return `Intérêts (${this.taux * 100} %) : +${interets} € -> solde : ${this.solde} €`;
  }
}

// ─────────────────────────────────────────────
// 5. L'enfant a TOUT du parent + ses propres capacités
// ─────────────────────────────────────────────
console.log("\n--- Compte épargne ---");
const epargne = new CompteEpargne("Chloé", 1000, 0.05);
console.log(epargne.afficher());        // méthode HÉRITÉE du parent
console.log(epargne.deposer(500));      // méthode HÉRITÉE du parent
console.log(epargne.ajouterInterets()); // méthode PROPRE à l'enfant

console.log("\n✅ Fin de la démo : moules, instances et héritage.");
