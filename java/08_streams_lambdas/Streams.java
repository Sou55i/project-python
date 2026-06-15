/*
 * MODULE 08 - LAMBDAS (->) et l'API STREAM : traiter des données élégamment
 * =========================================================================
 * Une LAMBDA, c'est une mini-fonction écrite en une ligne, sans nom. On l'écrit
 * avec une flèche : (parametre) -> resultat. Un STREAM, c'est un "tapis roulant"
 * sur une collection : on enchaîne des étapes (garder certains éléments, les
 * transformer, les rassembler) sans écrire de boucle à la main.
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/08_streams_lambdas/Streams.java
 *     java -cp /tmp/jb Streams
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Définir une lambda toute simple et l'appeler (pour comprendre la flèche).
 *   2. FILTER : ne garder que les nombres pairs d'une liste.
 *   3. MAP : transformer chaque élément (mettre des mots en MAJUSCULES).
 *   4. COLLECT : rassembler le résultat d'un stream dans une nouvelle liste.
 *   5. REDUCE : combiner tous les éléments en une seule valeur (la somme).
 *   6. Chaîner filter + map + collect en une seule "chaîne" lisible.
 */

import java.util.List;                    // le type "liste"
import java.util.function.Function;       // pour stocker une lambda dans une variable
import java.util.stream.Collectors;       // pour rassembler un stream (toList, etc.)

public class Streams {

    public static void main(String[] args) {

        // ─────────────────────────────────────────────
        // 1. UNE LAMBDA : une fonction sans nom, écrite avec une FLÈCHE ->.
        // À gauche : le(s) paramètre(s). À droite : ce qu'on renvoie.
        // 'Function<Integer, Integer>' = "fonction qui prend un Integer et en
        // renvoie un". Ici : "x -> x * x" se lit "à x, j'associe x au carré".
        // ─────────────────────────────────────────────
        Function<Integer, Integer> carre = x -> x * x;
        System.out.println("Lambda carre(5) = " + carre.apply(5));   // apply = "exécute la lambda"

        System.out.println("---");

        // Une liste de nombres qui servira d'exemple (List.of = liste figée).
        List<Integer> nombres = List.of(1, 2, 3, 4, 5, 6);

        // ─────────────────────────────────────────────
        // 2. FILTER : garder seulement les éléments qui passent un TEST.
        // .stream() pose la liste sur le "tapis roulant".
        // La lambda "n -> n % 2 == 0" renvoie true pour les nombres pairs.
        // .toList() rassemble le résultat dans une nouvelle liste.
        // ─────────────────────────────────────────────
        List<Integer> pairs = nombres.stream()
                .filter(n -> n % 2 == 0)   // ne garde que si le test est vrai
                .toList();                 // rassemble en liste
        System.out.println("Nombres pairs : " + pairs);

        // ─────────────────────────────────────────────
        // 3. MAP : TRANSFORMER chaque élément par une lambda.
        // Ici on passe chaque mot en majuscules.
        // ─────────────────────────────────────────────
        List<String> mots = List.of("chat", "chien", "oiseau");
        List<String> majuscules = mots.stream()
                .map(mot -> mot.toUpperCase())   // transforme chaque mot
                .toList();
        System.out.println("En majuscules : " + majuscules);

        // ─────────────────────────────────────────────
        // 4. COLLECT : rassembler autrement (ici, joindre en une seule String).
        // Collectors.joining(", ") colle les éléments séparés par ", ".
        // ─────────────────────────────────────────────
        String phrase = mots.stream()
                .collect(Collectors.joining(", "));
        System.out.println("Joint : " + phrase);

        // ─────────────────────────────────────────────
        // 5. REDUCE : COMBINER tous les éléments en UNE seule valeur.
        // Ici la somme : on part de 0, et on ajoute chaque nombre.
        // (a, b) -> a + b : "le cumul a, plus l'élément b".
        // ─────────────────────────────────────────────
        int somme = nombres.stream()
                .reduce(0, (a, b) -> a + b);   // 0 = valeur de départ
        System.out.println("Somme (reduce) : " + somme);

        System.out.println("---");

        // ─────────────────────────────────────────────
        // 6. CHAÎNER plusieurs étapes : la vraie force des streams.
        // "garder les nombres > 2, les mettre au carré, rassembler en liste".
        // Une boucle for ferait pareil, mais en bien plus de lignes.
        // ─────────────────────────────────────────────
        List<Integer> resultat = nombres.stream()
                .filter(n -> n > 2)        // 3, 4, 5, 6
                .map(n -> n * n)           // 9, 16, 25, 36
                .toList();
        System.out.println("Chaine filter+map : " + resultat);
    }
}
