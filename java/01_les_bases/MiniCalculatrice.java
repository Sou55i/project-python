/*
 * MODULE 01 - Mini-calculatrice interactive
 * =========================================
 * Lit une opération (+, -, *, /) et deux nombres au clavier, puis affiche
 * le résultat. Gère le cas de la division par zéro.
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME
 * ---------------------------
 *   1. Brancher un Scanner sur le clavier (System.in).
 *   2. DEMANDER l'opération (+, -, *, /) et la LIRE.
 *   3. DEMANDER le premier nombre, puis le second, et les LIRE.
 *   4. Selon l'opération choisie (switch) :
 *        - + : addition
 *        - - : soustraction
 *        - * : multiplication
 *        - / : division, MAIS on vérifie d'abord que le diviseur n'est pas 0.
 *        - autre : opération inconnue -> message d'erreur.
 *   5. AFFICHER le résultat (ou le message d'erreur).
 *   6. Fermer le Scanner.
 *
 * Compiler puis lancer :
 *     javac java/01_les_bases/MiniCalculatrice.java
 *     java -cp java/01_les_bases MiniCalculatrice
 *
 * Exemple de test automatique (envoie  +  puis 7 puis 5) :
 *     printf "+\n7\n5\n" | java -cp java/01_les_bases MiniCalculatrice
 */

import java.util.Scanner;   // l'outil pour LIRE ce que tape l'utilisateur

public class MiniCalculatrice {

    public static void main(String[] args) {

        // 1. On branche le Scanner sur le clavier (System.in).
        Scanner clavier = new Scanner(System.in);

        // 2. On demande l'opération et on lit le PREMIER caractère tapé.
        System.out.print("Operation (+, -, *, /) : ");
        char operation = clavier.next().charAt(0);   // next() lit un mot ; charAt(0) = son 1er caractère

        // 3. On demande les deux nombres (des double, pour accepter les virgules).
        System.out.print("Premier nombre : ");
        double a = clavier.nextDouble();
        System.out.print("Second nombre : ");
        double b = clavier.nextDouble();

        // 4. Selon l'opération, on calcule. Le switch compare 'operation' à chaque cas.
        double resultat = 0;   // contiendra le résultat
        boolean valide = true; // passe à false si l'opération est impossible

        switch (operation) {
            case '+':
                resultat = a + b;
                break;          // 'break' = on sort du switch une fois le cas traité
            case '-':
                resultat = a - b;
                break;
            case '*':
                resultat = a * b;
                break;
            case '/':
                // ⚠️ Division par zéro impossible : on vérifie AVANT de diviser.
                if (b == 0) {
                    System.out.println("Erreur : division par zero impossible.");
                    valide = false;
                } else {
                    resultat = a / b;
                }
                break;
            default:            // 'default' = aucun cas ci-dessus ne correspond
                System.out.println("Erreur : operation inconnue.");
                valide = false;
                break;
        }

        // 5. On affiche le résultat seulement si le calcul était valide.
        if (valide) {
            System.out.println(a + " " + operation + " " + b + " = " + resultat);
        }

        // 6. On ferme le Scanner (bonne habitude : on libère la ressource clavier).
        clavier.close();
    }
}
