/*
 * MODULE 01 - Mini-projet : une calculatrice en C
 * ===============================================
 * On combine ce qu'on a vu (variables, scanf, conditions, fonctions) dans un
 * petit programme utile : il lit une opération et deux nombres, puis calcule.
 *
 * Compiler puis lancer :
 *     gcc c/01_les_bases/mini_calculatrice.c -o calc
 *     ./calc
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE    : stdio.h pour printf / scanf.
 *    2. FONCTIONS  : une fonction par opération (additionner, soustraire...).
 *    3. main       : (a) demander l'opération, (b) demander deux nombres,
 *                    (c) choisir le calcul selon l'opération, (d) afficher.
 */

#include <stdio.h>

// Une fonction par opération : code clair et réutilisable.
// Ici on travaille avec des 'double' pour gérer aussi les nombres à virgule.
double additionner(double a, double b) { return a + b; }
double soustraire(double a, double b) { return a - b; }
double multiplier(double a, double b) { return a * b; }

double diviser(double a, double b) {
    // On se protège de la division par zéro.
    if (b == 0) {
        printf("Erreur : division par zero impossible.\n");
        return 0;
    }
    return a / b;
}

int main(void) {
    char operation;   // un seul caractère : +, -, * ou /
    double n1, n2, resultat;

    // 1. DEMANDER l'opération. Le " %c" (avec une espace devant) évite un piège
    //    classique de scanf avec les caractères. Tape par exemple : +
    printf("Operation (+, -, *, /) : ");
    scanf(" %c", &operation);   // le & = "range la saisie À L'ADRESSE de operation"

    // 2. DEMANDER les deux nombres (%lf = lire un double).
    printf("Premier nombre  : ");
    scanf("%lf", &n1);
    printf("Deuxieme nombre : ");
    scanf("%lf", &n2);

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
        printf("Operation inconnue.\n");
        return 1;   // on quitte avec un code d'erreur (différent de 0)
    }

    // 4. AFFICHER le résultat (%.2f = 2 chiffres après la virgule).
    printf("Resultat : %.2f\n", resultat);

    return 0;
}
