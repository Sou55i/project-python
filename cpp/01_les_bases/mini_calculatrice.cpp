/*
 * MODULE 01 - Mini-projet : une calculatrice en C++
 * =================================================
 * On combine ce qu'on a vu (variables, std::cin, conditions, fonctions) dans un
 * petit programme utile : il lit une opération et deux nombres, puis calcule.
 *
 * Compiler puis lancer :
 *     g++ cpp/01_les_bases/mini_calculatrice.cpp -o calc && ./calc
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE    : <iostream> pour std::cout / std::cin.
 *    2. FONCTIONS  : une fonction par opération (additionner, soustraire...).
 *    3. main       : (a) demander l'opération, (b) demander deux nombres,
 *                    (c) choisir le calcul selon l'opération, (d) afficher.
 */

#include <iostream>

// Une fonction par opération : code clair et réutilisable.
// Ici on travaille avec des 'double' pour gérer aussi les nombres à virgule.
double additionner(double a, double b) { return a + b; }
double soustraire(double a, double b) { return a - b; }
double multiplier(double a, double b) { return a * b; }

double diviser(double a, double b) {
    // On se protège de la division par zéro.
    if (b == 0) {
        std::cout << "Erreur : division par zero impossible." << std::endl;
        return 0;
    }
    return a / b;
}

int main() {
    char operation;   // un seul caractère : +, -, * ou /
    double n1, n2, resultat;

    // 1. DEMANDER l'opération. Avec std::cin, pas de %c ni de & : on lit
    //    directement dans la variable. Tape par exemple : +
    std::cout << "Operation (+, -, *, /) : ";
    std::cin >> operation;

    // 2. DEMANDER les deux nombres (std::cin range directement un double).
    std::cout << "Premier nombre  : ";
    std::cin >> n1;
    std::cout << "Deuxieme nombre : ";
    std::cin >> n2;

    // 3. CHOISIR le calcul selon l'opération.
    if (operation == '+') {
        resultat = additionner(n1, n2);
    } else if (operation == '-') {
        resultat = soustraire(n1, n2);
    } else if (operation == '*') {
        resultat = multiplier(n1, n2);
    } else if (operation == '/') {
        resultat = diviser(n1, n2);
    } else {
        std::cout << "Operation inconnue." << std::endl;
        return 1;   // on quitte avec un code d'erreur (différent de 0)
    }

    // 4. AFFICHER le résultat.
    std::cout << "Resultat : " << resultat << std::endl;

    return 0;
}
