/*
 * MODULE 07 - DÉBOGUER en Java : lire une stack trace et reconnaître les erreurs
 * ==============================================================================
 * Déboguer, c'est l'art de TROUVER pourquoi un programme se comporte mal. La
 * première arme : savoir LIRE une "stack trace" (la pile d'appels affichée quand
 * une exception survient). On verra aussi les 3 erreurs les plus fréquentes pour
 * un débutant, et l'astuce du "println de debug".
 *
 * NOTE : pour que la sortie reste DÉTERMINISTE, on PROVOQUE chaque erreur à
 * l'intérieur d'un try/catch et on AFFICHE proprement sa stack trace. Le
 * programme ne plante donc jamais : il te MONTRE les erreurs sans mourir.
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/07_debugger/DemoDebug.java
 *     java -cp /tmp/jb DemoDebug
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Provoquer une NullPointerException et lire sa stack trace.
 *   2. Provoquer une ArrayIndexOutOfBoundsException (indice hors limites).
 *   3. Provoquer une ClassCastException (mauvaise conversion de type).
 *   4. Montrer le "println de debug" : afficher l'état d'une variable.
 *   5. Mention du débogueur jdb pour aller plus loin.
 */

public class DemoDebug {

    // Une petite chaîne d'appels VOLONTAIRE : main -> niveau1 -> niveau2.
    // But : montrer que la stack trace liste TOUTES les méthodes traversées.
    static void niveau1() {
        niveau2();              // niveau1 appelle niveau2
    }

    static void niveau2() {
        String texte = null;    // 'texte' ne pointe sur RIEN (null)
        // Appeler une méthode sur null => NullPointerException ICI, ligne ci-dessous.
        int taille = texte.length();
        System.out.println(taille);   // jamais atteint
    }

    public static void main(String[] args) {

        // ─────────────────────────────────────────────
        // 1. NullPointerException : on utilise un objet qui vaut null.
        // LIRE LA STACK TRACE (de haut en bas) :
        //   - 1re ligne : le TYPE de l'exception + le message.
        //   - puis "at DemoDebug.niveau2(...)" : l'endroit EXACT du crash.
        //   - puis "at DemoDebug.niveau1(...)" : qui a appelé niveau2.
        //   - puis "at DemoDebug.main(...)" : qui a appelé niveau1.
        // => On lit du HAUT (où ça casse) vers le BAS (d'où on vient).
        // ─────────────────────────────────────────────
        System.out.println("=== 1. NullPointerException ===");
        try {
            niveau1();
        } catch (NullPointerException e) {
            System.out.println("Type : " + e.getClass().getSimpleName());
            System.out.println("Pile d'appels (stack trace) :");
            e.printStackTrace();   // affiche la pile complète sur la sortie d'erreur
        }

        System.out.println("---");

        // ─────────────────────────────────────────────
        // 2. ArrayIndexOutOfBoundsException : indice en dehors du tableau.
        // Un tableau de taille 3 a les indices 0, 1, 2. L'indice 5 n'existe pas.
        // ─────────────────────────────────────────────
        System.out.println("=== 2. ArrayIndexOutOfBoundsException ===");
        try {
            int[] notes = {12, 15, 9};   // indices valides : 0, 1, 2
            int x = notes[5];            // 5 n'existe pas => exception ICI
            System.out.println(x);       // jamais atteint
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Type : " + e.getClass().getSimpleName());
            System.out.println("Message : " + e.getMessage());
            // Astuce : pour un tableau, vérifie toujours indice >= 0 && indice < length.
        }

        System.out.println("---");

        // ─────────────────────────────────────────────
        // 3. ClassCastException : on force un objet vers un type incompatible.
        // 'objet' contient un String, mais on tente de le voir comme un Integer.
        // ─────────────────────────────────────────────
        System.out.println("=== 3. ClassCastException ===");
        try {
            Object objet = "je suis un texte";   // un String rangé dans un Object
            Integer nombre = (Integer) objet;    // conversion IMPOSSIBLE => exception
            System.out.println(nombre);          // jamais atteint
        } catch (ClassCastException e) {
            System.out.println("Type : " + e.getClass().getSimpleName());
            System.out.println("Message : " + e.getMessage());
        }

        System.out.println("---");

        // ─────────────────────────────────────────────
        // 4. Le "println de debug" : la technique la plus simple du monde.
        // Quand un calcul donne un résultat bizarre, AFFICHE les valeurs
        // intermédiaires pour voir où ça dérape.
        // ─────────────────────────────────────────────
        System.out.println("=== 4. println de debug ===");
        int a = 7;
        int b = 3;
        System.out.println("[debug] a = " + a + ", b = " + b);   // on espionne les variables
        int somme = a + b;
        System.out.println("[debug] somme calculee = " + somme);
        System.out.println("Resultat final : " + somme);

        System.out.println("---");

        // ─────────────────────────────────────────────
        // 5. Pour aller plus loin : le DÉBOGUEUR jdb (livré avec le JDK).
        // Un débogueur permet de METTRE EN PAUSE le programme et d'inspecter les
        // variables ligne par ligne, sans ajouter de println partout.
        //   javac -g -d /tmp/jb java/07_debugger/DemoDebug.java   (le -g garde les infos de debug)
        //   jdb -classpath /tmp/jb DemoDebug
        // Puis, dans jdb :  stop in DemoDebug.niveau2   (poser un point d'arrêt)
        //                   run                          (lancer jusqu'au point d'arrêt)
        //                   print texte                  (afficher une variable)
        //                   cont                         (continuer)
        // Les IDE (IntelliJ, VS Code, Eclipse) offrent la même chose en cliquant.
        // ─────────────────────────────────────────────
        System.out.println("=== 5. Debogueur jdb ===");
        System.out.println("Pour inspecter pas a pas : jdb (voir les commentaires du code).");
    }
}
