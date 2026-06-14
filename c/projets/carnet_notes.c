/*
 * PROJET CAPSTONE - Carnet de notes scolaires
 * ===========================================
 * Un petit gestionnaire de notes : on garde plusieurs matières avec leur
 * note dans un TABLEAU de STRUCTURES, on calcule la moyenne, on SAUVEGARDE
 * le tout dans un fichier, puis on le RELIT et on l'affiche.
 *
 * 🧩 MODULES COMBINÉS (c'est ça, un "capstone") :
 *    - Module 02 (tableaux/chaines) : un tableau de matières, calcul de moyenne.
 *    - Module 04 (structures)        : chaque ligne = une struct (matiere + note).
 *    - Module 05 (fichiers)          : sauvegarde (fopen "w") puis relecture (fopen "r").
 *
 * ⚠️ NON INTERACTIF : le programme remplit lui-même des données d'exemple,
 *    les sauvegarde, les recharge et les affiche. Tu peux donc le lancer
 *    directement, sans rien taper.
 *
 * Compiler puis lancer (DEPUIS LA RACINE du dépôt) :
 *     gcc -Wall c/projets/carnet_notes.c -o carnet_notes
 *     ./carnet_notes
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE   : stdio.h (fichiers + printf), string.h (copier des chaines),
 *                   sys/stat.h (mkdir pour créer le dossier exemples/).
 *    2. STRUCT    : on définit le modèle "Note" (matiere + valeur).
 *    3. DONNÉES   : on remplit un tableau de Note avec des exemples.
 *    4. CALCUL    : on parcourt le tableau pour faire la moyenne (module 02).
 *    5. DOSSIER   : on crée exemples/ (anti-pollution) avec mkdir.
 *    6. SAUVER    : on écrit chaque note dans exemples/notes.dat (module 05).
 *    7. RELIRE    : on rouvre le fichier et on lit ligne par ligne (module 05).
 *    8. AFFICHER  : on montre ce qu'on a rechargé, plus la moyenne.
 */

#include <stdio.h>     // fopen, fprintf, fgets, fclose, printf
#include <string.h>    // strcpy (copier le nom de la matiere dans la struct)
#include <sys/stat.h>  // mkdir (créer le dossier exemples/)

// (2) STRUCT : le modèle d'une note. Une "fiche" = une matière et sa note.
typedef struct {
    char matiere[50];  // le nom de la matière (ex: "Maths")
    float note;        // la note sur 20
} Note;

int main(void) {

    // (3) DONNÉES d'exemple : un TABLEAU de structures (module 04).
    //     Pas de saisie clavier : tout est rempli ici, donc testable direct.
    Note notes[4] = {
        {"Maths",    15.5f},
        {"Francais", 12.0f},
        {"Histoire", 14.0f},
        {"Sport",    18.5f}
    };
    int nb = 4;  // combien de notes dans le tableau

    // (4) CALCUL de la moyenne en parcourant le tableau (module 02).
    float somme = 0.0f;
    for (int i = 0; i < nb; i++) {
        somme += notes[i].note;   // on additionne chaque note
    }
    float moyenne = somme / nb;   // total divisé par le nombre de notes

    // (5) DOSSIER : on crée exemples/ pour NE PAS polluer le dépôt.
    //     mkdir renvoie -1 si le dossier existe déjà : ce n'est PAS grave,
    //     on continue quand même.
    mkdir("exemples", 0777);

    // (6) SAUVEGARDE : on ouvre en mode "w" (write = on (ré)écrit le fichier).
    FILE *f = fopen("exemples/notes.dat", "w");
    if (f == NULL) {   // réflexe : toujours vérifier que l'ouverture a marché
        printf("Erreur : impossible d'ecrire exemples/notes.dat\n");
        printf("Lance le programme DEPUIS LA RACINE du depot.\n");
        return 1;
    }
    // On écrit une ligne par note : "matiere note". fprintf = printf vers fichier.
    for (int i = 0; i < nb; i++) {
        fprintf(f, "%s %.1f\n", notes[i].matiere, notes[i].note);
    }
    fclose(f);  // on referme : les données sont bien rangées sur le disque
    printf("Sauvegarde OK -> exemples/notes.dat (%d notes)\n\n", nb);

    // (7) RELECTURE : on rouvre le MÊME fichier en mode "r" (read = lecture).
    FILE *g = fopen("exemples/notes.dat", "r");
    if (g == NULL) {
        printf("Erreur : impossible de relire exemples/notes.dat\n");
        return 1;
    }

    // (8) AFFICHAGE de ce qu'on vient de RECHARGER depuis le fichier.
    printf("=== Carnet de notes (recharge depuis le fichier) ===\n");
    char ligne_matiere[50];  // boite pour le nom lu
    float ligne_note;        // boite pour la note lue
    // fscanf lit "un mot puis un nombre" à chaque tour ; il renvoie 2 quand
    // il a bien lu les 2 valeurs, et autre chose à la fin du fichier.
    while (fscanf(g, "%49s %f", ligne_matiere, &ligne_note) == 2) {
        printf("  %-10s : %.1f / 20\n", ligne_matiere, ligne_note);
    }
    fclose(g);  // on referme le fichier de lecture

    // La moyenne, elle, a été calculée en mémoire (étape 4).
    printf("---------------------------------------------\n");
    printf("  Moyenne generale : %.2f / 20\n", moyenne);

    return 0;
}
