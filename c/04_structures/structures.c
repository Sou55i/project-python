/*
 * MODULE 04 - Les structures (struct)
 * ===================================
 * Déclarer une structure, créer une variable, lire/écrire ses champs avec le
 * point '.', la passer à une fonction, et la modifier via un pointeur (flèche '->').
 *
 * Compiler puis lancer :
 *     gcc -Wall c/04_structures/structures.c -o structures
 *     ./structures
 */

#include <stdio.h>
#include <string.h>   // pour strcpy (copier dans un champ chaîne)

// On définit un MODELE de fiche nommé "Personne".
// typedef = on lui donne un surnom court : on pourra écrire "Personne"
// au lieu de "struct Personne".
typedef struct {
    char nom[50];   // un champ "nom" : une chaîne (tableau de char)
    int  age;       // un champ "age" : un entier
} Personne;

// Reçoit une COPIE de la fiche : parfait pour LIRE/afficher.
void afficher(Personne p) {
    printf("%s, %d ans\n", p.nom, p.age);
}

// Reçoit l'ADRESSE de la fiche (un pointeur) : permet de MODIFIER l'original.
// Avec un pointeur, on accède aux champs avec la flèche '->'
// (ptr->age est le raccourci de (*ptr).age).
void vieillir(Personne *ptr) {
    ptr->age = ptr->age + 1;
}

int main(void) {

    // 1. Créer une fiche et la remplir champ par champ.
    Personne p;
    strcpy(p.nom, "Alice");   // champ chaîne -> strcpy (le '=' est interdit ici)
    p.age = 30;               // champ nombre  -> '=' suffit
    printf("Fiche remplie : %s a %d ans\n", p.nom, p.age);

    // 2. Créer une fiche en remplissant tout d'un coup (dans l'ordre des champs).
    Personne bob = {"Bob", 25};
    printf("Autre fiche  : %s a %d ans\n", bob.nom, bob.age);

    // 3. Passer une fiche à une fonction (copie) pour l'afficher.
    afficher(p);

    // 4. Modifier l'original via un POINTEUR : on passe l'ADRESSE avec &.
    vieillir(&p);
    printf("Apres vieillir(&p), Alice a %d ans\n", p.age);   // 31

    return 0;
}
