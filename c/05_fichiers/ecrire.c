/*
 * MODULE 05 - Écrire dans un fichier
 * ==================================
 * On crée un fichier "exemples/notes.txt" et on y écrit quelques lignes.
 * (Analogie : on ouvre un cahier, on écrit dedans, on le referme.)
 *
 * Compiler puis lancer (DEPUIS LA RACINE du dépôt) :
 *     gcc -Wall c/05_fichiers/ecrire.c -o ecrire
 *     ./ecrire
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE  : stdio.h (fopen/fprintf/fputs/fclose) + sys/stat.h (mkdir).
 *    2. DOSSIER  : créer le sous-dossier "exemples/" pour ne pas polluer le dépôt.
 *    3. OUVRIR   : fopen en mode "w" (écrit ; ÉCRASE l'ancien contenu).
 *    4. VÉRIFIER : si le retour est NULL, l'ouverture a échoué -> on s'arrête.
 *    5. ÉCRIRE   : quelques lignes avec fprintf et fputs.
 *    6. REFERMER : fclose, sinon rien n'est garanti enregistré.
 */

#include <stdio.h>      // fopen, fprintf, fputs, fclose, printf
#include <sys/stat.h>   // mkdir

int main(void) {

    // (2) On crée le dossier "exemples". S'il existe déjà, mkdir renvoie une
    //     erreur qu'on ignore volontairement : ce n'est pas grave ici.
    mkdir("exemples", 0777);

    // (3) On OUVRE le fichier en mode "w" : on repart d'un cahier vide.
    //     fopen renvoie une "poignée" FILE* vers le fichier ouvert.
    FILE *f = fopen("exemples/notes.txt", "w");

    // (4) RÉFLEXE OBLIGATOIRE : vérifier que l'ouverture a réussi.
    if (f == NULL) {
        printf("Erreur : impossible de creer exemples/notes.txt\n");
        printf("(Lance bien la commande DEPUIS LA RACINE du depot.)\n");
        return 1;   // on s'arrête proprement (1 = il y a eu un souci)
    }

    // (5) On ÉCRIT dedans. fprintf marche comme printf, mais vers le fichier f.
    fprintf(f, "Liste de notes\n");          // un titre
    fprintf(f, "Math : %d/20\n", 15);        // %d -> un nombre, comme printf
    fprintf(f, "Histoire : %d/20\n", 12);

    // fputs écrit une chaîne telle quelle (sans format). Pratique et simple.
    fputs("Bravo, continue !\n", f);

    // (6) On REFERME le cahier : maintenant tout est bien enregistré sur le disque.
    fclose(f);

    // Petit message à l'écran pour confirmer (ceci NE va PAS dans le fichier).
    printf("OK : 4 lignes ecrites dans exemples/notes.txt\n");

    return 0;
}
