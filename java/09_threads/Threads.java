/*
 * MODULE 09 - La CONCURRENCE : faire plusieurs choses "en même temps"
 * ===================================================================
 * Un THREAD (fil d'exécution), c'est une tâche qui s'exécute en PARALLÈLE des
 * autres. Plusieurs threads peuvent tourner simultanément. Mais attention :
 * quand ils touchent à la MÊME donnée partagée, ça peut se mélanger. On verra
 * comment lancer des threads, comment les ATTENDRE (join), et comment protéger
 * une donnée partagée pour obtenir un résultat FIABLE.
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/09_threads/Threads.java
 *     java -cp /tmp/jb Threads
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer un compteur PARTAGÉ et sûr (AtomicInteger), commun à tous.
 *   2. Créer plusieurs threads ; CHACUN ajoute 1000 fois au compteur (Runnable).
 *   3. DÉMARRER tous les threads (start) : ils tournent en parallèle.
 *   4. ATTENDRE qu'ils finissent tous (join) avant de lire le résultat.
 *   5. Afficher la somme finale : DÉTERMINISTE grâce à AtomicInteger.
 */

import java.util.concurrent.atomic.AtomicInteger;   // un compteur "thread-safe"

public class Threads {

    // Combien de threads et combien d'incréments chacun.
    static final int NB_THREADS = 4;
    static final int INCREMENTS_PAR_THREAD = 1000;

    public static void main(String[] args) throws InterruptedException {

        // ─────────────────────────────────────────────
        // 1. UN COMPTEUR PARTAGÉ et SÛR.
        // Un simple 'int compteur' partagé entre threads donnerait un résultat
        // FAUX et imprévisible : deux threads peuvent l'incrémenter "en même
        // temps" et s'écraser. AtomicInteger garantit des additions ATOMIQUES
        // (indivisibles) => le total est toujours correct et DÉTERMINISTE.
        // ─────────────────────────────────────────────
        AtomicInteger compteur = new AtomicInteger(0);

        // On range les threads dans un tableau pour pouvoir les attendre ensuite.
        Thread[] threads = new Thread[NB_THREADS];

        // ─────────────────────────────────────────────
        // 2. CRÉER les threads. Chaque thread reçoit un RUNNABLE : un bout de
        // code à exécuter. Ici, une lambda qui incrémente le compteur en boucle.
        // incrementAndGet() ajoute 1 de façon sûre, même si d'autres threads le
        // font au même instant.
        // ─────────────────────────────────────────────
        for (int i = 0; i < NB_THREADS; i++) {
            Runnable tache = () -> {
                for (int j = 0; j < INCREMENTS_PAR_THREAD; j++) {
                    compteur.incrementAndGet();   // +1, garanti sans collision
                }
            };
            threads[i] = new Thread(tache);   // on emballe la tâche dans un Thread
        }

        // ─────────────────────────────────────────────
        // 3. DÉMARRER tous les threads. start() lance l'exécution EN PARALLÈLE
        // (ne pas confondre avec run(), qui s'exécuterait sans parallélisme).
        // ─────────────────────────────────────────────
        for (Thread t : threads) {
            t.start();
        }

        // ─────────────────────────────────────────────
        // 4. ATTENDRE la fin de chaque thread avec join().
        // Sans ce join, main pourrait lire le compteur AVANT que les threads
        // aient fini => résultat partiel. join() = "j'attends que tu termines".
        // ─────────────────────────────────────────────
        for (Thread t : threads) {
            t.join();
        }

        // ─────────────────────────────────────────────
        // 5. LIRE le résultat final. Comme on a attendu tout le monde et que le
        // compteur est atomique, la somme est TOUJOURS la même.
        // Attendu : 4 threads * 1000 = 4000.
        // ─────────────────────────────────────────────
        int attendu = NB_THREADS * INCREMENTS_PAR_THREAD;
        System.out.println("Nombre de threads      : " + NB_THREADS);
        System.out.println("Increments par thread  : " + INCREMENTS_PAR_THREAD);
        System.out.println("Somme finale (compteur): " + compteur.get());
        System.out.println("Valeur attendue        : " + attendu);
        System.out.println("Resultat correct ?     : " + (compteur.get() == attendu));
    }
}
