/*
 * demo_gdb.c — un petit programme CORRECT, fait pour être EXPLORÉ pas à pas sous gdb.
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME
 *   1. main() prépare un tableau de notes (des entiers).
 *   2. Il appelle somme() qui additionne toutes les notes une à une (boucle).
 *   3. Il appelle moyenne() qui se sert de somme() puis divise par le nombre de notes.
 *   4. Il affiche le total et la moyenne.
 *
 *   Le but n'est PAS de trouver un bug (il n'y en a pas !), mais d'apprendre à
 *   POSER UN BREAKPOINT, AVANCER LIGNE PAR LIGNE et INSPECTER les variables sous gdb.
 *   Compile avec les infos de débogage :  gcc -g -Wall demo_gdb.c -o demo
 *   Puis explore :                         gdb ./demo
 */

#include <stdio.h>   /* pour printf */

/* Additionne les `n` premières cases du tableau `notes` et renvoie le total. */
int somme(const int notes[], int n)
{
    int total = 0;                  /* on part de zéro... */
    for (int i = 0; i < n; i++) {   /* ...et on parcourt chaque case */
        total = total + notes[i];   /* ⏸️ bon endroit pour inspecter `i` et `total` */
    }
    return total;                   /* on renvoie le cumul */
}

/* Calcule la moyenne (en nombre à virgule) des `n` premières notes. */
double moyenne(const int notes[], int n)
{
    if (n == 0) {                   /* prudence : ne JAMAIS diviser par zéro */
        return 0.0;
    }
    int total = somme(notes, n);    /* on réutilise la fonction du dessus */
    return (double) total / n;      /* le (double) force un calcul à virgule */
}

int main(void)
{
    /* Nos données de départ : 5 notes sur 20. */
    int notes[] = {12, 15, 8, 17, 10};
    int nb = 5;                     /* combien de notes dans le tableau */

    int total = somme(notes, nb);   /* étape 2 du cheminement */
    double moy = moyenne(notes, nb);/* étape 3 du cheminement */

    printf("Nombre de notes : %d\n", nb);
    printf("Total des notes : %d\n", total);
    printf("Moyenne         : %.2f\n", moy);

    return 0;                       /* 0 = tout s'est bien passé */
}
