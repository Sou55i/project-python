/*
 * threads.c — plusieurs threads incrémentent un compteur PARTAGÉ, protégé par un MUTEX.
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME
 *   1. main() prépare un compteur partagé (= 0) et un verrou (mutex).
 *   2. Il LANCE NB_THREADS threads avec pthread_create() : chacun exécute la
 *      fonction travailleur().
 *   3. Chaque travailleur() fait NB_INCREMENTS fois : "je verrouille, j'ajoute 1,
 *      je déverrouille" sur le compteur partagé.
 *   4. main() ATTEND la fin de tous les threads avec pthread_join().
 *   5. Il affiche le total. Comme l'accès est protégé par le mutex, le résultat est
 *      DÉTERMINISTE : total = NB_THREADS * NB_INCREMENTS, à chaque exécution.
 *
 *   ⚠️ IMPORTANT : ce fichier utilise les threads POSIX (pthreads). Il faut compiler
 *   avec l'option -pthread :
 *       gcc -Wall -pthread c/08_threads/threads.c -o threads && ./threads
 */

#include <stdio.h>     /* pour printf */
#include <pthread.h>   /* pour pthread_create, pthread_join, pthread_mutex_*  */

/* Combien de threads on lance, et combien de fois chacun incrémente le compteur. */
#define NB_THREADS     4      /* 4 "cuisiniers" qui travaillent en parallèle */
#define NB_INCREMENTS  100000 /* chacun ajoute 1 cent mille fois */

/* LA variable PARTAGÉE : tous les threads vont la modifier en même temps.
 * C'est exactement le genre de variable qu'il FAUT protéger. */
long compteur_partage = 0;

/* LE VERROU (mutex). Un seul thread à la fois pourra "tenir" ce verrou.
 * PTHREAD_MUTEX_INITIALIZER initialise le mutex sans effort, dès la déclaration. */
pthread_mutex_t verrou = PTHREAD_MUTEX_INITIALIZER;

/*
 * La fonction exécutée par CHAQUE thread.
 * Signature imposée par pthreads : reçoit un void* et renvoie un void*.
 * Ici on n'utilise pas l'argument : on le marque (void) pour éviter un warning.
 */
void *travailleur(void *arg)
{
    (void) arg;                                  /* on ignore l'argument proprement */

    for (int i = 0; i < NB_INCREMENTS; i++) {
        pthread_mutex_lock(&verrou);             /* 🔒 je prends le verrou (j'attends si occupé) */
        compteur_partage = compteur_partage + 1; /* zone PROTÉGÉE : moi seul touche au compteur */
        pthread_mutex_unlock(&verrou);           /* 🔓 je rends le verrou : un autre peut entrer */
    }

    return NULL;                                 /* ce thread n'a rien à renvoyer */
}

int main(void)
{
    pthread_t threads[NB_THREADS];   /* un "identifiant" par thread, pour le retrouver après */

    /* Étape 2 : on LANCE les threads. Chacun part exécuter travailleur(). */
    for (int i = 0; i < NB_THREADS; i++) {
        /* pthread_create(&id, attributs, fonction, argument) ; renvoie 0 si OK. */
        if (pthread_create(&threads[i], NULL, travailleur, NULL) != 0) {
            printf("Erreur : impossible de creer le thread %d\n", i);
            return 1;                /* on arrête proprement en cas d'échec */
        }
    }

    /* Étape 4 : on ATTEND que chaque thread ait FINI (sinon main pourrait s'arrêter
     * avant eux et afficher un total incomplet). pthread_join "rejoint" le thread. */
    for (int i = 0; i < NB_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    /* Étape 5 : tous les threads sont finis. On peut lire le compteur sans risque. */
    long attendu = (long) NB_THREADS * NB_INCREMENTS;
    printf("Nombre de threads     : %d\n", NB_THREADS);
    printf("Increments par thread : %d\n", NB_INCREMENTS);
    printf("Total attendu         : %ld\n", attendu);
    printf("Total obtenu          : %ld\n", compteur_partage);

    if (compteur_partage == attendu) {
        printf("=> CORRECT : le mutex a bien protege le compteur.\n");
    } else {
        printf("=> FAUX : il manque des increments (course aux donnees !).\n");
    }

    return 0;                        /* 0 = tout s'est bien passé */
}
