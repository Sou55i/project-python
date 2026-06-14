/*
 * MODULE 01 - Les briques de base en C
 * ====================================
 * Illustre, dans l'ordre, les notions du README : types et variables,
 * printf et ses spécificateurs, conditions, boucles, fonctions.
 *
 * Compiler puis lancer :
 *     gcc c/01_les_bases/bases.c -o bases
 *     ./bases
 */

#include <stdio.h>   // pour printf

// ─────────────────────────────────────────────
// FONCTIONS (définies AVANT main, car le C doit les connaître avant l'appel)
// ─────────────────────────────────────────────

// 'int' = type de la valeur renvoyée ; (int a, int b) = deux paramètres entiers.
int additionner(int a, int b) {
    return a + b;   // 'return' renvoie le résultat à l'appelant
}

// 'void' = cette fonction ne renvoie rien ; elle se contente d'afficher.
void saluer(void) {
    printf("Bonjour depuis une fonction !\n");
}

// ─────────────────────────────────────────────
// main : le point de départ du programme
// ─────────────────────────────────────────────
int main(void) {

    // 1. VARIABLES ET TYPES (on déclare le type, puis on termine par ;)
    int age = 30;          // entier
    double taille = 1.68;  // nombre à virgule
    char initiale = 'A';   // UN caractère, entre apostrophes simples

    // 2. AFFICHER avec printf : chaque %... correspond à une variable, dans l'ordre.
    //    %d = entier, %.2f = décimal à 2 chiffres, %c = caractère.
    printf("Age : %d ans\n", age);
    printf("Taille : %.2f m\n", taille);
    printf("Initiale : %c\n", initiale);

    // 3. CONDITIONS : la condition entre ( ), le bloc entre { }.
    int note = 12;
    if (note >= 16) {
        printf("Mention : Tres bien\n");
    } else if (note >= 10) {   // 'else if' (et non 'elif')
        printf("Mention : Recu\n");
    } else {
        printf("Mention : A retravailler\n");
    }

    // 4. BOUCLE for : (début ; condition de continuation ; pas)
    for (int i = 0; i < 3; i++) {   // i++ = i = i + 1
        printf("Tour numero %d\n", i);
    }

    // 5. BOUCLE while : tant que la condition est vraie.
    int compteur = 0;
    while (compteur < 3) {
        printf("compteur = %d\n", compteur);
        compteur++;   // indispensable, sinon boucle infinie
    }

    // 6. APPELER NOS FONCTIONS définies plus haut.
    saluer();
    int somme = additionner(7, 5);
    printf("7 + 5 = %d\n", somme);

    return 0;   // succès
}
