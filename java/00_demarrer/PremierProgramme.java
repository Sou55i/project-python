/*
 * MODULE 00 - Premier programme en Java
 * =====================================
 * Le traditionnel "Hello world", commenté pour comprendre CHAQUE morceau.
 *
 * Compiler puis lancer :
 *     javac java/00_demarrer/PremierProgramme.java
 *     java -cp java/00_demarrer PremierProgramme
 */

// (1) En Java, TOUT le code vit à l'intérieur d'une CLASSE.
//     'public' = visible de partout. 'class' = on déclare une classe.
//     ⚠️ Une classe publique DOIT être dans un fichier du MÊME NOM :
//        la classe PremierProgramme est donc dans PremierProgramme.java.
public class PremierProgramme {

    // (2) 'main' est le POINT DE DÉPART : la JVM exécute ce qui est ici en premier.
    //     - public : accessible depuis l'extérieur (la JVM doit pouvoir l'appeler).
    //     - static : appartient à la classe, pas besoin de créer un objet pour l'appeler.
    //     - void   : cette méthode ne renvoie aucune valeur.
    //     - String[] args : les éventuels arguments passés au programme (vide ici).
    public static void main(String[] args) {

        // (3) System.out.println(...) affiche le texte PUIS un retour à la ligne.
        //     Le texte va entre guillemets doubles. L'instruction finit par un ;
        System.out.println("Bonjour, Java !");

        // On peut afficher plusieurs lignes : chaque println écrit sur sa propre ligne.
        System.out.println("Ce code a ete compile en bytecode...");
        System.out.println("...puis execute par la JVM.");

        /* print (sans 'ln') affiche SANS retour à la ligne :
           les deux morceaux ci-dessous restent donc sur la MÊME ligne. */
        System.out.print("Ecris une fois, ");
        System.out.println("execute partout.");
    }
}
