/*
 * MODULE 03 - Plusieurs objets et ENCAPSULATION : CompteBancaire
 * ==============================================================
 * Exemple plus parlant : une classe CompteBancaire dont le 'solde' est
 * PRIVATE (protege). On ne peut PAS y toucher directement de l'exterieur :
 * on est oblige de passer par les methodes PUBLIC deposer(), retirer() et
 * afficher(), qui VERIFIENT que l'operation est valide. C'est ca,
 * l'encapsulation : cacher les details internes derriere des portes
 * d'entree controlees.
 *
 * On cree PLUSIEURS objets a partir du meme plan : chacun a son propre solde.
 *
 * Compiler puis lancer :
 *     g++ -Wall cpp/03_classes_objets/objets.cpp -o objets && ./objets
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce qui se passe, dans l'ordre) :
 *   1. On cree un objet 'compteAda' avec un solde de depart de 100.
 *   2. On depose 50 dessus, puis on l'affiche.
 *   3. On tente de retirer 500 : refuse (solde insuffisant) ; on affiche.
 *   4. On retire 30 (valide), puis on affiche le nouveau solde.
 *   5. On cree un 2e objet 'compteBob' INDEPENDANT, avec son propre solde.
 *   6. On affiche les deux comptes : chacun a garde SES valeurs.
 *   7. Le programme se termine.
 */

#include <iostream>   // pour std::cout (afficher)
#include <string>     // pour std::string (le nom du proprietaire)

class CompteBancaire {
private:
    // ATTRIBUTS PRIVES : caches. Impossible d'y acceder depuis main.
    // (Essaie d'ecrire 'compteAda.solde = 999;' dans main -> erreur de compil.)
    std::string proprietaire;
    double solde;

public:
    // CONSTRUCTEUR : initialise le compte avec un proprietaire et un
    // solde de depart. Meme nom que la classe, aucun type de retour.
    CompteBancaire(std::string nom, double soldeDepart) {
        proprietaire = nom;
        solde = soldeDepart;
    }

    // METHODE PUBLIC : deposer de l'argent. Une "porte d'entree" controlee :
    // elle refuse les montants negatifs ou nuls.
    void deposer(double montant) {
        if (montant > 0) {
            solde += montant;   // l'interieur de la classe a le droit de modifier solde
            std::cout << "[" << proprietaire << "] Depot de " << montant << std::endl;
        } else {
            std::cout << "[" << proprietaire << "] Depot refuse (montant invalide)" << std::endl;
        }
    }

    // METHODE PUBLIC : retirer de l'argent, en VERIFIANT le solde.
    void retirer(double montant) {
        if (montant <= 0) {
            std::cout << "[" << proprietaire << "] Retrait refuse (montant invalide)" << std::endl;
        } else if (montant > solde) {
            std::cout << "[" << proprietaire << "] Retrait refuse (solde insuffisant)" << std::endl;
        } else {
            solde -= montant;
            std::cout << "[" << proprietaire << "] Retrait de " << montant << std::endl;
        }
    }

    // METHODE PUBLIC : afficher l'etat du compte. C'est la seule facon, depuis
    // l'exterieur, de consulter le solde (qui reste prive).
    void afficher() {
        std::cout << "Compte de " << proprietaire << " : solde = " << solde << std::endl;
    }
};

int main() {

    // 1. CREER un premier objet (un compte) avec son solde de depart.
    CompteBancaire compteAda("Ada", 100.0);

    // 2. Deposer puis afficher.
    compteAda.deposer(50.0);     // 100 -> 150
    compteAda.afficher();

    // 3. Tenter un retrait trop gros : la methode le REFUSE (encapsulation utile).
    compteAda.retirer(500.0);    // refuse : solde insuffisant
    compteAda.afficher();        // toujours 150

    // 4. Un retrait valide.
    compteAda.retirer(30.0);     // 150 -> 120
    compteAda.afficher();

    std::cout << std::endl;

    // 5. CREER un 2e objet, totalement INDEPENDANT du premier.
    CompteBancaire compteBob("Bob", 20.0);
    compteBob.deposer(5.0);      // 20 -> 25

    // 6. Afficher les deux : chaque objet a garde SES propres valeurs.
    compteAda.afficher();        // Ada : 120
    compteBob.afficher();        // Bob : 25

    return 0;   // 7. succes
}
