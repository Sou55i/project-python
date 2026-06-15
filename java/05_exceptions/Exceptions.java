/*
 * MODULE 05 - Les exceptions : gérer les erreurs proprement
 * =========================================================
 * Une exception, c'est un PROBLÈME qui survient pendant l'exécution (division
 * par zéro, texte non numérique, fichier absent…). Plutôt que de planter, on
 * l'ATTRAPE avec try/catch, on nettoie avec finally, et on peut DÉCLENCHER nos
 * propres erreurs avec throw. On distingue les exceptions VÉRIFIÉES (le
 * compilateur force à les gérer) des NON VÉRIFIÉES.
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/05_exceptions/Exceptions.java
 *     java -cp /tmp/jb Exceptions
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Provoquer une division par zéro et l'ATTRAPER (try/catch).
 *   2. Convertir un texte invalide en nombre et attraper l'erreur.
 *   3. Voir le bloc FINALLY s'exécuter quoi qu'il arrive.
 *   4. Appeler une méthode qui DÉCLENCHE sa propre erreur avec throw.
 *   5. Appeler une méthode à exception VÉRIFIÉE (déclarée avec throws).
 *   6. Constater que le programme continue malgré toutes ces erreurs.
 */

public class Exceptions {

    // ─────────────────────────────────────────────
    // Méthode qui DÉCLENCHE elle-même une erreur avec 'throw'.
    // IllegalArgumentException est NON VÉRIFIÉE : on n'est pas OBLIGÉ
    // de la déclarer ni de l'attraper (mais c'est plus prudent de le faire).
    // ─────────────────────────────────────────────
    static int racineDePositif(int n) {
        if (n < 0) {
            // 'throw new ...' crée et lance l'erreur ; la méthode s'arrête net.
            throw new IllegalArgumentException("nombre negatif interdit : " + n);
        }
        return (int) Math.sqrt(n);
    }

    // ─────────────────────────────────────────────
    // Méthode à exception VÉRIFIÉE : Exception est "checked".
    // Le mot 'throws Exception' AVERTIT l'appelant "je peux échouer" :
    // le compilateur l'OBLIGERA à gérer (try/catch ou re-throws).
    // ─────────────────────────────────────────────
    static void verifierAge(int age) throws Exception {
        if (age < 0) {
            throw new Exception("age impossible : " + age);
        }
        System.out.println("Age valide : " + age);
    }

    public static void main(String[] args) {

        // ─────────────────────────────────────────────
        // 1. TRY/CATCH : on TENTE un code risqué dans 'try' ; si une erreur
        //    survient, on saute dans 'catch' au lieu de planter.
        // ─────────────────────────────────────────────
        try {
            int x = 10 / 0;             // division par zéro => ArithmeticException
            System.out.println(x);      // jamais atteint
        } catch (ArithmeticException e) {
            // 'e' contient l'erreur ; e.getMessage() donne sa description.
            System.out.println("Erreur attrapee : " + e.getMessage());
        }

        // 2. Conversion d'un texte non numérique => NumberFormatException.
        try {
            int n = Integer.parseInt("douze");   // "douze" n'est pas un nombre
            System.out.println(n);
        } catch (NumberFormatException e) {
            System.out.println("Conversion impossible : " + e.getMessage());
        }

        // 3. FINALLY : ce bloc s'exécute TOUJOURS, qu'il y ait eu erreur ou non.
        //    Idéal pour "ranger après soi" (fermer un fichier, par ex.).
        try {
            System.out.println("On tente quelque chose...");
            int[] t = new int[2];
            t[5] = 1;   // indice hors limites => ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Indice hors limites attrape.");
        } finally {
            System.out.println("FINALLY : je m'exécute quoi qu'il arrive.");
        }

        // 4. Attraper une erreur DÉCLENCHÉE par notre propre méthode (throw).
        try {
            racineDePositif(-4);
        } catch (IllegalArgumentException e) {
            System.out.println("Refuse par racineDePositif : " + e.getMessage());
        }
        System.out.println("racine de 9 = " + racineDePositif(9));   // cas valide

        // 5. Exception VÉRIFIÉE : comme verifierAge déclare 'throws Exception',
        //    le compilateur nous OBLIGE à entourer l'appel d'un try/catch.
        try {
            verifierAge(20);
            verifierAge(-3);   // celui-ci déclenche l'erreur
        } catch (Exception e) {
            System.out.println("Age refuse : " + e.getMessage());
        }

        // 6. Malgré toutes ces erreurs, le programme a CONTINUÉ jusqu'ici.
        System.out.println("Fin du programme : on a survecu a toutes les erreurs.");
    }
}
