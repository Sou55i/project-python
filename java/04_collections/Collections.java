/*
 * MODULE 04 - Collections : List/ArrayList et Map/HashMap
 * =======================================================
 * Les collections sont des "boîtes" qui grandissent toutes seules, contrairement
 * aux tableaux de taille fixe. Ici : une LISTE (ArrayList) ordonnée, une MAP
 * (HashMap) clé→valeur, la boucle FOR-EACH pour les parcourir, et les
 * GÉNÉRIQUES <> qui annoncent le type du contenu.
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/04_collections/Collections.java
 *     java -cp /tmp/jb Collections
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer une LISTE de String et y ajouter des éléments (add).
 *   2. Lire sa taille (size) et un élément précis (get).
 *   3. Parcourir la liste avec une boucle FOR-EACH.
 *   4. Créer une MAP (clé String -> valeur Integer) et y ranger des paires.
 *   5. Lire une valeur par sa clé (get), tester une présence (containsKey).
 *   6. Parcourir la map (clés, puis paires clé/valeur).
 */

// Java range ces outils dans le "paquetage" java.util : il faut les IMPORTER.
import java.util.ArrayList;   // la LISTE qui grandit toute seule
import java.util.List;        // le TYPE général "liste" (bonne habitude : déclarer en List)
import java.util.HashMap;     // la MAP clé -> valeur
import java.util.Map;         // le TYPE général "map"

public class Collections {
    public static void main(String[] args) {

        // ─────────────────────────────────────────────
        // 1. LISTE : une suite ORDONNÉE d'éléments, taille variable.
        // Les <String> sont les GÉNÉRIQUES : ils annoncent "cette liste ne
        // contient QUE des String". Le compilateur l'impose => moins d'erreurs.
        // ─────────────────────────────────────────────
        List<String> courses = new ArrayList<>();   // <> vide à droite : Java devine le type
        courses.add("pain");      // ajouter à la fin
        courses.add("lait");
        courses.add("oeufs");

        // 2. Taille et accès par INDICE (le premier est à l'indice 0, comme les tableaux).
        System.out.println("Nombre d'articles : " + courses.size());
        System.out.println("Premier article : " + courses.get(0));

        // 3. Parcourir avec FOR-EACH : "pour chaque String c dans courses".
        System.out.println("Liste de courses :");
        for (String c : courses) {
            System.out.println("  - " + c);
        }

        System.out.println("---");

        // ─────────────────────────────────────────────
        // 4. MAP : associe une CLÉ à une VALEUR (comme un dictionnaire).
        // Ici, un nom (String) -> un âge (Integer). On range avec put.
        // 'Integer' = la version "objet" de int, requise dans les génériques.
        // ─────────────────────────────────────────────
        Map<String, Integer> ages = new HashMap<>();
        ages.put("Lou", 30);
        ages.put("Sam", 25);
        ages.put("Max", 42);

        // 5. Lire par CLÉ, et tester une présence.
        System.out.println("Age de Lou : " + ages.get("Lou"));
        System.out.println("On connait Sam ? " + ages.containsKey("Sam"));
        System.out.println("On connait Zoe ? " + ages.containsKey("Zoe"));

        // 6a. Parcourir uniquement les CLÉS avec keySet().
        System.out.println("Personnes connues :");
        for (String nom : ages.keySet()) {
            System.out.println("  - " + nom);
        }

        // 6b. Parcourir les PAIRES clé/valeur avec entrySet().
        //     Chaque 'e' est une Entry : e.getKey() et e.getValue().
        System.out.println("Detail des ages :");
        for (Map.Entry<String, Integer> e : ages.entrySet()) {
            System.out.println("  " + e.getKey() + " a " + e.getValue() + " ans");
        }
    }
}
