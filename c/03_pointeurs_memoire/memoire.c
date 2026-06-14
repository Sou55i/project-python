/*
 * MODULE 03 - La memoire dynamique en C (malloc / free)
 * =====================================================
 * Illustre les notions du README : on RESERVE de la memoire a la volee
 * avec malloc (utile quand on ne connait la taille qu'a l'execution), on
 * s'en sert comme d'un tableau normal, puis on la LIBERE avec free.
 *
 * Compiler puis lancer :
 *     gcc -Wall c/03_pointeurs_memoire/memoire.c -o memoire
 *     ./memoire
 *
 * ─────────────────────────────────────────────────────────────────────
 * 🗺️  CHEMINEMENT DU PROGRAMME (ce qui se passe, dans l'ordre)
 * ─────────────────────────────────────────────────────────────────────
 *   1. On choisit une taille n (ici 5) connue a l'execution.
 *   2. On RESERVE la place pour n entiers avec malloc.
 *   3. On VERIFIE que malloc n'a pas echoue (sinon il renvoie NULL).
 *   4. On REMPLIT le tableau dynamique avec une boucle for.
 *   5. On l'AFFICHE avec une autre boucle for.
 *   6. On LIBERE la memoire avec free, puis on remet le pointeur a NULL.
 * ─────────────────────────────────────────────────────────────────────
 */

#include <stdio.h>    // pour printf
#include <stdlib.h>   // pour malloc, free, NULL

int main(void) {

    // 1. TAILLE voulue. Imagine qu'elle vienne d'une saisie utilisateur :
    //    on ne la connaitrait pas en ecrivant le code -> d'ou le malloc.
    int n = 5;

    // 2. RESERVER la memoire pour n entiers.
    //    sizeof(int)     = taille d'UN entier (en octets).
    //    n * sizeof(int) = place pour n entiers.
    //    malloc renvoie l'ADRESSE du debut de la zone reservee.
    int *tab = malloc(n * sizeof(int));

    // 3. VERIFIER : malloc renvoie NULL s'il n'a pas pu reserver la place.
    //    On ne se sert JAMAIS d'un pointeur sans avoir verifie ce cas.
    if (tab == NULL) {
        printf("Erreur : plus de memoire disponible.\n");
        return 1;   // on s'arrete proprement (code != 0 = echec)
    }

    // 4. REMPLIR le tableau dynamique. On l'utilise comme un tableau normal :
    //    tab[i] marche exactement pareil que pour "int tab[5]".
    for (int i = 0; i < n; i++) {
        tab[i] = (i + 1) * 10;   // 10, 20, 30, 40, 50
    }

    // 5. AFFICHER le contenu, case par case.
    printf("Tableau alloue dynamiquement (%d cases) :\n", n);
    for (int i = 0; i < n; i++) {
        printf("  tab[%d] = %d\n", i, tab[i]);
    }

    // 6. LIBERER la memoire : a chaque malloc doit correspondre un free.
    //    Sans ca, la memoire reste prise pour rien (fuite de memoire).
    free(tab);
    tab = NULL;   // bonne habitude : on n'utilise plus un pointeur "rendu"

    printf("Memoire liberee. Fin du programme.\n");

    return 0;   // succes
}
