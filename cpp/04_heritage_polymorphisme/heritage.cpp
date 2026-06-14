/*
 * MODULE 04 - L'héritage : réutiliser et spécialiser
 * ==================================================
 * Une classe FILLE (Chien) hérite de tout ce que possède une classe MÈRE
 * (Animal), puis ajoute ses propres capacités.
 *
 * Compiler puis lancer :
 *     g++ -Wall cpp/04_heritage_polymorphisme/heritage.cpp -o heritage
 *     ./heritage
 */

#include <iostream>
#include <string>

// La classe MÈRE : ce que TOUT animal possède.
class Animal {
public:
    std::string nom;

    void decrire() {
        std::cout << "Je suis " << nom << std::endl;
    }
};

// La classe FILLE : « Chien hérite de Animal » (les deux points = "hérite de").
// Chien récupère gratuitement 'nom' et 'decrire()', et ajoute 'aboyer()'.
class Chien : public Animal {
public:
    void aboyer() {
        // 'nom' n'est pas redéclaré ici : il vient de la classe mère Animal.
        std::cout << nom << " fait Wouf !" << std::endl;
    }
};

int main() {
    Chien rex;
    rex.nom = "Rex";   // champ HÉRITÉ d'Animal

    rex.decrire();     // méthode HÉRITÉE d'Animal  -> "Je suis Rex"
    rex.aboyer();      // méthode AJOUTÉE par Chien -> "Rex fait Wouf !"

    return 0;
}
