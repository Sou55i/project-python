/*
 * MODULE 05 - Lire un fichier ligne par ligne
 * ===========================================
 * On rouvre "exemples/notes.txt" (créé par ecrire.c) et on l'affiche,
 * une ligne à la fois, avec fgets.
 * (Analogie : on rouvre le cahier et on lit ce qui y est déjà écrit.)
 *
 * Compiler puis lancer (DEPUIS LA RACINE du dépôt) :
 *     gcc -Wall c/05_fichiers/lire.c -o lire
 *     ./lire
 *
 * ⚠️ Lance D'ABORD ecrire (pour créer le fichier), PUIS lire.
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE  : stdio.h (fopen/fgets/fclose/printf).
 *    2. OUVRIR   : fopen en mode "r" (lecture, ne modifie rien).
 *    3. VÉRIFIER : si le retour est NULL, fichier introuvable -> message + arrêt.
 *    4. LIRE     : boucle while + fgets, une ligne à chaque tour, jusqu'à la fin.
 *    5. REFERMER : fclose.
 */

#include <stdio.h>   // fopen, fgets, fclose, printf

int main(void) {

    // (2) On OUVRE le fichier en mode "r" (read = lecture seule).
    FILE *f = fopen("exemples/notes.txt", "r");

    // (3) RÉFLEXE OBLIGATOIRE : en lecture, NULL veut souvent dire
    //     "fichier introuvable" (oublié de lancer ecrire ? mauvais dossier ?).
    if (f == NULL) {
        printf("Erreur : fichier exemples/notes.txt introuvable.\n");
        printf("Lance d'abord ./ecrire, et DEPUIS LA RACINE du depot.\n");
        return 1;   // on s'arrête proprement
    }

    // (4) On LIT ligne par ligne. "ligne" est la boîte qui reçoit chaque ligne.
    char ligne[256];
    printf("--- Contenu de exemples/notes.txt ---\n");

    // fgets puise UNE ligne par tour ; il renvoie NULL à la fin du fichier,
    // ce qui arrête la boucle tout seul.
    while (fgets(ligne, sizeof(ligne), f) != NULL) {
        // ligne contient déjà son retour à la ligne \n : on n'en remet pas.
        printf("%s", ligne);
    }

    printf("--- (fin) ---\n");

    // (5) On REFERME le fichier.
    fclose(f);

    return 0;
}
