/*
 * MODULE 03 - Les pointeurs en C
 * ==============================
 * Illustre les notions du README : une variable a une ADRESSE (&), un
 * pointeur contient une adresse, et l'etoile (*) sert a "aller voir" la
 * valeur pointee (derefencer). On montre surtout l'usage le plus utile :
 * MODIFIER une variable depuis une fonction grace a son pointeur.
 *
 * Compiler puis lancer :
 *     gcc -Wall c/03_pointeurs_memoire/pointeurs.c -o pointeurs
 *     ./pointeurs
 */

#include <stdio.h>    // pour printf

// Une fonction qui DOUBLE un nombre en passant par son pointeur.
// Parametre : int *n  -> n est un pointeur vers un int (il recoit une ADRESSE).
// Comme on a l'adresse de l'original, on peut le modifier pour de vrai.
void doubler(int *n) {
    // *n = "la valeur rangee a l'adresse n". On la remplace par son double.
    *n = *n * 2;
}

int main(void) {

    // 1. UNE VARIABLE NORMALE et son adresse.
    //    'age' contient 30 ; &age donne l'ADRESSE ou ce 30 est range.
    int age = 30;
    printf("La valeur de age : %d\n", age);
    printf("L'adresse de age : %p\n", (void *)&age);  // %p affiche une adresse

    // 2. DECLARER UN POINTEUR et lui donner l'adresse de age.
    //    "int *p" : p est un pointeur vers un int.
    //    "= &age" : on range l'ADRESSE de age dans p. p "pointe sur" age.
    int *p = &age;

    // 3. DEREFERENCER avec * : "va a l'adresse dans p, donne la valeur".
    printf("Valeur pointee par p (*p) : %d\n", *p);   // 30

    // 4. MODIFIER age A TRAVERS le pointeur.
    //    *p = 42 -> "ecris 42 a l'adresse pointee" -> donc dans age.
    *p = 42;
    printf("Apres *p = 42, age vaut : %d\n", age);     // 42

    // 5. LE CAS UTILE : modifier une variable DEPUIS une fonction.
    //    On donne l'ADRESSE de x (&x) pour que doubler() puisse l'ecrire.
    int x = 5;
    printf("\nAvant doubler(), x = %d\n", x);
    doubler(&x);                       // on passe l'ADRESSE de x
    printf("Apres doubler(), x = %d\n", x);   // 10 : x a vraiment change !

    return 0;   // succes
}
