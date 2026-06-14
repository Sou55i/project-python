/*
 * MODULE 01 - Les briques de base en C++
 * ======================================
 * Illustre, dans l'ordre, les notions du README : types et variables,
 * std::cout, std::cin, conditions, boucles, fonctions.
 *
 * Compiler puis lancer :
 *     g++ cpp/01_les_bases/bases.cpp -o bases && ./bases
 */

#include <iostream>   // pour std::cout (afficher) et std::cin (lire)
#include <string>     // pour le type std::string (du texte)

// ─────────────────────────────────────────────
// FONCTIONS (définies AVANT main, car le C++ doit les connaître avant l'appel)
// ─────────────────────────────────────────────

// 'int' = type de la valeur renvoyée ; (int a, int b) = deux paramètres entiers.
int additionner(int a, int b) {
    return a + b;   // 'return' renvoie le résultat à l'appelant
}

// 'void' = cette fonction ne renvoie rien ; elle se contente d'afficher.
void saluer() {
    std::cout << "Bonjour depuis une fonction !" << std::endl;
}

// ─────────────────────────────────────────────
// main : le point de départ du programme
// ─────────────────────────────────────────────
int main() {

    // 1. VARIABLES ET TYPES (on déclare le type, puis on termine par ;)
    int age = 30;             // entier
    double taille = 1.68;     // nombre à virgule
    char initiale = 'A';      // UN caractère, entre apostrophes simples
    std::string nom = "Lou";  // du TEXTE, entre guillemets doubles
    bool majeur = true;       // un vrai booléen : true (vrai) ou false (faux)

    // 2. AFFICHER avec std::cout : on ENCHAÎNE texte et variables avec <<.
    //    Pas de %d / %f / %s à gérer : le C++ devine le type tout seul.
    std::cout << "Nom : " << nom << std::endl;
    std::cout << "Age : " << age << " ans" << std::endl;
    std::cout << "Taille : " << taille << " m" << std::endl;
    std::cout << "Initiale : " << initiale << std::endl;
    std::cout << "Majeur (1 = vrai) : " << majeur << std::endl;

    // 3. CONDITIONS : la condition entre ( ), le bloc entre { }.
    int note = 12;
    if (note >= 16) {
        std::cout << "Mention : Tres bien" << std::endl;
    } else if (note >= 10) {   // 'else if' (et non 'elif')
        std::cout << "Mention : Recu" << std::endl;
    } else {
        std::cout << "Mention : A retravailler" << std::endl;
    }

    // 4. BOUCLE for : (début ; condition de continuation ; pas)
    for (int i = 0; i < 3; i++) {   // i++ = i = i + 1
        std::cout << "Tour numero " << i << std::endl;
    }

    // 5. BOUCLE while : tant que la condition est vraie.
    int compteur = 0;
    while (compteur < 3) {
        std::cout << "compteur = " << compteur << std::endl;
        compteur++;   // indispensable, sinon boucle infinie
    }

    // 6. APPELER NOS FONCTIONS définies plus haut.
    saluer();
    int somme = additionner(7, 5);
    std::cout << "7 + 5 = " << somme << std::endl;

    return 0;   // succès
}
