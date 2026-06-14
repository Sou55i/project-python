/*
 * MODULE 02 - Les tableaux en C
 * =============================
 * Illustre les notions du README : déclarer un tableau, le parcourir avec
 * une boucle for, et s'en servir pour calculer une somme puis une moyenne.
 *
 * Compiler puis lancer :
 *     gcc -Wall c/02_tableaux_chaines/tableaux.c -o tableaux
 *     ./tableaux
 */

#include <stdio.h>   // pour printf

int main(void) {

    // 1. DÉCLARER ET REMPLIR un tableau de 5 entiers, d'un seul coup.
    //    Les 5 valeurs sont rangées dans des cases côte à côte.
    int notes[5] = {12, 8, 15, 10, 18};

    // 2. ACCÉDER à une case par son INDICE. On compte à PARTIR DE 0 :
    //    notes[0] = la 1re case, notes[4] = la 5e (et dernière) case.
    printf("Premiere note : %d\n", notes[0]);   // 12
    printf("Derniere note : %d\n", notes[4]);   // 18

    // 3. MODIFIER une case : ici on corrige la 2e note (indice 1).
    notes[1] = 9;   // la valeur 8 devient 9

    // 4. PARCOURIR le tableau avec un for : i va de 0 à 4 (i < 5).
    //    Le "i < 5" (et non "<= 5") nous évite de DÉPASSER le tableau.
    printf("\nToutes les notes :\n");
    for (int i = 0; i < 5; i++) {
        printf("  notes[%d] = %d\n", i, notes[i]);
    }

    // 5. CALCULER LA SOMME : on repart d'un total à 0, puis on ajoute
    //    chaque case au passage pendant le parcours.
    int somme = 0;                       // l'accumulateur, vide au départ
    for (int i = 0; i < 5; i++) {
        somme = somme + notes[i];        // on ajoute la case courante
    }
    printf("\nSomme des notes : %d\n", somme);

    // 6. CALCULER LA MOYENNE : somme / nombre de notes.
    //    Attention : 'somme' et '5' sont des entiers, donc la division
    //    serait ENTIÈRE (elle couperait les décimales). On convertit
    //    'somme' en double avec (double) pour obtenir une vraie moyenne.
    double moyenne = (double) somme / 5;
    printf("Moyenne        : %.2f\n", moyenne);   // %.2f = 2 decimales

    return 0;   // succès
}
