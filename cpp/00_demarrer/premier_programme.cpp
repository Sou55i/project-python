/*
 * MODULE 00 - Premier programme en C++
 * ====================================
 * Ton tout premier programme C++. Objectif : voir le cycle
 * « écrire -> COMPILER -> lancer » en action.
 *
 * Pour le compiler PUIS le lancer, ouvre un terminal et tape :
 *     g++ cpp/00_demarrer/premier_programme.cpp -o premier_programme && ./premier_programme
 *
 * Rappel : les commentaires (comme ce bloc) sont ignorés par le compilateur.
 * En C++ on écrit  // pour une ligne   ou   ... pour plusieurs lignes.
 */

// (1) On "inclut" la boîte à outils d'entrée/sortie standard.
//     Elle contient std::cout (afficher) et std::cin (lire).
//     C'est l'équivalent d'un import en Python (en C, c'était <stdio.h>).
#include <iostream>

// (2) main = le POINT DE DÉPART de tout programme C++. L'exécution commence ici.
//     'int' = la fonction renvoie un entier au système ; () = elle ne prend rien.
//     L'accolade { ouvre le corps de la fonction (fermé par } tout en bas).
int main() {

    // (3) std::cout affiche du texte à l'écran.
    //     - std::cout = la "sortie console" (l'écran), std = bibliothèque standard.
    //     - <<        = "envoie ceci vers l'écran" (on peut en enchaîner plusieurs).
    //     - std::endl = un retour à la ligne (l'équivalent du \n du C).
    //     Chaque instruction se termine par un point-virgule ;
    std::cout << "Bonjour le monde !" << std::endl;
    std::cout << "Je viens de compiler et lancer mon premier programme C++." << std::endl;

    // On peut enchaîner texte et retour à la ligne sur une seule instruction.
    std::cout << "Cette ligne s'affiche apres les precedentes." << std::endl;

    // (4) return 0 signale au système : "tout s'est bien passe" (0 = succes).
    return 0;
}

/*
 * À TOI DE MODIFIER :
 *   - change le texte des std::cout,
 *   - ajoute un nouveau std::cout avec ton message,
 *   - RECOMPILE (g++ ... -o ...) puis relance (./premier_programme).
 * En C++, il faut TOUJOURS recompiler après une modification pour la voir.
 */
