/*
 * MODULE 02 - Programmation Orientée Objet (POO)
 * ==============================================
 * Une CLASSE CompteBancaire : des attributs PRIVÉS (titulaire, solde), un
 * CONSTRUCTEUR pour initialiser, des MÉTHODES publiques (deposer, retirer) et
 * des GETTERS pour lire l'intérieur sans pouvoir l'abîmer (encapsulation).
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/02_poo/CompteBancaire.java
 *     java -cp /tmp/jb CompteBancaire
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. CRÉER un objet 'compte' à partir de la classe (via le constructeur).
 *   2. LIRE l'état de l'objet grâce aux getters (getTitulaire, getSolde).
 *   3. DÉPOSER de l'argent (méthode qui modifie un attribut privé).
 *   4. RETIRER de l'argent (avec une VÉRIFICATION : pas plus que le solde).
 *   5. ESSAYER une opération invalide pour voir la protection à l'œuvre.
 *   6. CRÉER un 2e compte pour montrer que chaque objet est INDÉPENDANT.
 */

// En Java, tout vit dans une classe. La classe PUBLIQUE s'appelle CompteBancaire,
// donc le fichier DOIT s'appeler CompteBancaire.java (règle Java).
public class CompteBancaire {

    // ─────────────────────────────────────────────
    // ATTRIBUTS : les DONNÉES que possède chaque objet.
    // 'private' = inaccessibles directement depuis l'extérieur (encapsulation).
    // On ne pourra donc PAS écrire compte.solde = -9999 depuis main.
    // ─────────────────────────────────────────────
    private String titulaire;   // le nom du propriétaire du compte
    private double solde;       // l'argent disponible

    // ─────────────────────────────────────────────
    // CONSTRUCTEUR : méthode spéciale appelée AUTOMATIQUEMENT à la création.
    // Il porte le MÊME NOM que la classe et n'a AUCUN type de retour.
    // 'this.titulaire' = l'attribut de l'objet ; 'titulaire' = le paramètre reçu.
    // ─────────────────────────────────────────────
    public CompteBancaire(String titulaire, double soldeInitial) {
        this.titulaire = titulaire;     // on range le nom dans l'attribut
        this.solde = soldeInitial;      // on range le solde de départ
    }

    // ─────────────────────────────────────────────
    // GETTERS : des méthodes publiques pour LIRE un attribut privé.
    // On peut ainsi consulter sans pouvoir modifier n'importe comment.
    // ─────────────────────────────────────────────
    public String getTitulaire() {
        return this.titulaire;
    }

    public double getSolde() {
        return this.solde;
    }

    // ─────────────────────────────────────────────
    // MÉTHODES D'ACTION : des PORTES D'ENTRÉE contrôlées pour modifier l'objet.
    // Elles peuvent VÉRIFIER que l'opération est valide avant d'agir.
    // ─────────────────────────────────────────────

    // Déposer de l'argent : on refuse les montants négatifs ou nuls.
    public void deposer(double montant) {
        if (montant <= 0) {
            System.out.println("Depot refuse : le montant doit etre positif.");
            return;   // on sort de la méthode sans rien changer
        }
        this.solde += montant;   // l'intérieur de la classe, LUI, a le droit
        System.out.println("Depot de " + montant + " euros. Solde : " + this.solde);
    }

    // Retirer de l'argent : on refuse si le solde est insuffisant.
    public void retirer(double montant) {
        if (montant <= 0) {
            System.out.println("Retrait refuse : le montant doit etre positif.");
            return;
        }
        if (montant > this.solde) {
            System.out.println("Retrait refuse : solde insuffisant.");
            return;
        }
        this.solde -= montant;
        System.out.println("Retrait de " + montant + " euros. Solde : " + this.solde);
    }

    // ─────────────────────────────────────────────
    // main : le point de départ du programme.
    // ─────────────────────────────────────────────
    public static void main(String[] args) {

        // 1. CRÉER un objet avec 'new' : le constructeur s'exécute.
        CompteBancaire compte = new CompteBancaire("Lou", 100.0);

        // 2. LIRE l'état via les getters (pas d'accès direct aux attributs).
        System.out.println("Titulaire : " + compte.getTitulaire());
        System.out.println("Solde initial : " + compte.getSolde() + " euros");

        // 3. DÉPOSER de l'argent.
        compte.deposer(50.0);

        // 4. RETIRER de l'argent (opération valide).
        compte.retirer(30.0);

        // 5. ESSAYER une opération invalide : la protection refuse.
        compte.retirer(10000.0);

        // ✋ Décommente la ligne suivante : le compilateur la REFUSE,
        //    car 'solde' est private (c'est ça, l'encapsulation).
        // compte.solde = 1000000;

        // 6. CRÉER un 2e compte : chaque objet a SES propres attributs.
        CompteBancaire autre = new CompteBancaire("Sam", 0.0);
        autre.deposer(200.0);
        System.out.println("Solde de " + compte.getTitulaire() + " : " + compte.getSolde());
        System.out.println("Solde de " + autre.getTitulaire() + " : " + autre.getSolde());
    }
}
