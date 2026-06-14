/*
 * MODULE 04 - Mini-projet : un agenda (tableau de structures)
 * ===========================================================
 * On range plusieurs contacts dans un TABLEAU de structures, puis on le
 * parcourt pour afficher chaque fiche et trouver le plus âgé.
 *
 * Compiler puis lancer :
 *     gcc -Wall c/04_structures/agenda.c -o agenda
 *     ./agenda
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE   : stdio.h pour printf.
 *    2. STRUCT    : on définit le modèle de fiche "Contact" (nom + age).
 *    3. main      : (a) créer un tableau de contacts,
 *                   (b) le parcourir pour tout afficher,
 *                   (c) chercher le contact le plus âgé,
 *                   (d) afficher le résultat.
 */

#include <stdio.h>

// Le modèle de fiche, avec un surnom court grâce à typedef.
typedef struct {
    char nom[50];
    int  age;
} Contact;

int main(void) {

    // (a) Un tableau de 3 fiches : un "classeur" de contacts.
    Contact contacts[3] = {
        {"Alice", 30},
        {"Bob",   25},
        {"Chloe", 42}
    };

    // (b) Parcourir le classeur. contacts[i] est UNE fiche ;
    //     on accède à ses champs avec le point '.'.
    printf("=== Agenda ===\n");
    for (int i = 0; i < 3; i++) {
        printf("  %s, %d ans\n", contacts[i].nom, contacts[i].age);
    }

    // (c) Chercher le plus âgé : on garde l'indice du meilleur trouvé.
    int indice_plus_age = 0;
    for (int i = 1; i < 3; i++) {
        if (contacts[i].age > contacts[indice_plus_age].age) {
            indice_plus_age = i;
        }
    }

    // (d) Afficher le résultat.
    printf("Le plus age est %s (%d ans)\n",
           contacts[indice_plus_age].nom,
           contacts[indice_plus_age].age);

    return 0;
}
