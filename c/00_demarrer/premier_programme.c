/*
 * MODULE 00 - Premier programme en C
 * ==================================
 * Ton tout premier programme C. Objectif : voir le cycle
 * « écrire -> COMPILER -> lancer » en action.
 *
 * Pour le compiler puis le lancer, ouvre un terminal et tape :
 *     gcc c/00_demarrer/premier_programme.c -o premier_programme
 *     ./premier_programme
 *
 * Rappel : les commentaires (comme ce bloc) sont ignorés par le compilateur.
 * En C on écrit  // pour une ligne   ou   ... pour plusieurs lignes.
 */

// (1) On "inclut" la boîte à outils d'entrée/sortie standard.
//     Elle contient printf(). C'est l'équivalent d'un import en Python.
#include <stdio.h>

// (2) main = le POINT DE DÉPART de tout programme C. L'exécution commence ici.
//     'int' = la fonction renvoie un entier au système ; (void) = elle ne prend rien.
//     L'accolade { ouvre le corps de la fonction (fermé par } tout en bas).
int main(void) {

    // (3) printf affiche du texte à l'écran.
    //     \n est UN caractère spécial : le "retour à la ligne".
    //     Chaque instruction se termine par un point-virgule ;
    printf("Bonjour le monde ! \n");
    printf("Je viens de compiler et lancer mon premier programme C.\n");

    // On peut afficher plusieurs lignes : le programme s'exécute de haut en bas.
    printf("Cette ligne s'affiche apres les precedentes.\n");

    // (4) return 0 signale au système : "tout s'est bien passe" (0 = succes).
    return 0;
}

/*
 * À TOI DE MODIFIER :
 *   - change le texte des printf,
 *   - ajoute un nouveau printf avec ton message,
 *   - RECOMPILE (gcc ... -o ...) puis relance (./premier_programme).
 * En C, il faut TOUJOURS recompiler après une modification pour la voir.
 */
