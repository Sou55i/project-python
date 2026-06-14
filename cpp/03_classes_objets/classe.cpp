/*
 * MODULE 03 - Une premiere classe : Rectangle
 * ===========================================
 * Illustre les notions du README : definir une CLASSE (un "plan") avec des
 * ATTRIBUTS (largeur, hauteur), un CONSTRUCTEUR (initialise l'objet a sa
 * creation), et des METHODES (aire(), perimetre()). Puis CREER un objet a
 * partir de la classe et APPELER ses methodes avec le point .
 *
 * Compiler puis lancer :
 *     g++ -Wall cpp/03_classes_objets/classe.cpp -o classe && ./classe
 */

#include <iostream>   // pour std::cout (afficher)

// ====================================================================
// LA CLASSE = LE PLAN. Elle decrit ce qu'aura TOUT rectangle, mais
// elle n'est pas elle-meme un rectangle (comme le plan d'une maison).
// ====================================================================
class Rectangle {
public:
    // ATTRIBUTS : les donnees que possede chaque objet Rectangle.
    int largeur;
    int hauteur;

    // CONSTRUCTEUR : meme nom que la classe, AUCUN type de retour.
    // Appele automatiquement quand on cree un objet. Il range les
    // valeurs recues (l, h) dans les attributs de l'objet.
    Rectangle(int l, int h) {
        largeur = l;
        hauteur = h;
    }

    // METHODE : une action de l'objet. Elle utilise directement les
    // attributs largeur et hauteur de l'objet sur lequel on l'appelle.
    int aire() {
        return largeur * hauteur;
    }

    // Une seconde methode : le perimetre = 2 * (largeur + hauteur).
    int perimetre() {
        return 2 * (largeur + hauteur);
    }
};   // <-- POINT-VIRGULE obligatoire apres la fermeture d'une classe.

int main() {

    // CREER un objet 'r' de type Rectangle. Le type, c'est le nom de la
    // classe. Entre parentheses : les valeurs passees au CONSTRUCTEUR.
    Rectangle r(4, 3);   // -> largeur = 4, hauteur = 3

    // ACCEDER aux attributs et APPELER les methodes avec le point .
    std::cout << "Rectangle de " << r.largeur << " x " << r.hauteur << std::endl;
    std::cout << "Aire      : " << r.aire()      << std::endl;   // 12
    std::cout << "Perimetre : " << r.perimetre() << std::endl;   // 14

    // A partir du MEME plan, on peut creer AUTANT d'objets qu'on veut,
    // chacun avec ses propres valeurs.
    Rectangle carre(5, 5);   // un autre rectangle, independant du premier
    std::cout << std::endl;
    std::cout << "Carre de " << carre.largeur << " x " << carre.hauteur << std::endl;
    std::cout << "Aire      : " << carre.aire()      << std::endl;   // 25
    std::cout << "Perimetre : " << carre.perimetre() << std::endl;   // 20

    return 0;   // succes
}
