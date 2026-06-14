/*
 * MODULE 02 - Les chaines de caracteres en C
 * ==========================================
 * Illustre les notions du README : une chaine est un tableau de char
 * termine par '\0'. On mesure sa longueur, on la compare, on la copie,
 * et on la parcourt caractere par caractere.
 *
 * Compiler puis lancer :
 *     gcc -Wall c/02_tableaux_chaines/chaines.c -o chaines
 *     ./chaines
 *
 * ─────────────────────────────────────────────────────────────────────
 * 🗺️  CHEMINEMENT DU PROGRAMME (ce qui se passe, dans l'ordre)
 * ─────────────────────────────────────────────────────────────────────
 *   1. On crée une chaine "Alice" (un tableau de char + un '\0' final).
 *   2. On l'affiche en entier avec %s.
 *   3. On mesure sa LONGUEUR avec strlen (le '\0' n'est pas compté).
 *   4. On la COMPARE à un autre mot avec strcmp (0 = identiques).
 *   5. On la COPIE dans un autre tableau avec strcpy.
 *   6. On la PARCOURT lettre par lettre avec un for, jusqu'au '\0'.
 * ─────────────────────────────────────────────────────────────────────
 */

#include <stdio.h>    // pour printf
#include <string.h>   // pour strlen, strcmp, strcpy

int main(void) {

    // 1. CRÉER UNE CHAÎNE. Écrire "Alice" entre guillemets crée pour nous
    //    un tableau de char contenant 'A','l','i','c','e' PUIS '\0'.
    //    Les [] vides : le compilateur calcule la taille tout seul (6 cases).
    char nom[] = "Alice";

    // 2. AFFICHER la chaine entiere avec %s (il s'arrete tout seul au '\0').
    printf("Bonjour %s !\n", nom);

    // 3. LONGUEUR avec strlen : compte les lettres SANS le '\0'.
    //    "Alice" a 5 lettres -> strlen renvoie 5.
    printf("Longueur de \"%s\" : %lu\n", nom, strlen(nom));
    //    %lu car strlen renvoie un entier non signe de type size_t.

    // 4. COMPARER deux chaines avec strcmp.
    //    ⚠️ On NE compare PAS avec == (ça comparerait des adresses).
    //    strcmp renvoie 0 quand les deux chaines sont IDENTIQUES.
    char mot_de_passe[] = "secret";
    if (strcmp(mot_de_passe, "secret") == 0) {
        printf("Mot de passe correct.\n");
    } else {
        printf("Mot de passe refuse.\n");
    }

    // 5. COPIER une chaine avec strcpy(destination, source).
    //    'copie' doit etre ASSEZ GRAND pour accueillir nom + le '\0'.
    char copie[20];                // 20 cases : largement assez
    strcpy(copie, nom);            // copie "Alice" (et son '\0') dans 'copie'
    printf("Copie obtenue : %s\n", copie);

    // 6. PARCOURIR caractere par caractere avec un for.
    //    On avance tant que la case n'est pas le '\0' (la fin de la chaine).
    printf("Lettre par lettre : ");
    for (int i = 0; nom[i] != '\0'; i++) {
        printf("[%c]", nom[i]);    // %c = UN caractere
    }
    printf("\n");

    return 0;   // succès
}
