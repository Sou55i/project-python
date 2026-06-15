/*
 * MODULE 06 - Les GÉNÉRIQUES <T> : écrire une fois, réutiliser pour tous les types
 * ================================================================================
 * Un générique, c'est un TYPE qu'on laisse en blanc, comme un formulaire avec une
 * case "type : ____". On l'écrit <T> (pour "Type"). Au moment où on l'utilise, on
 * remplit la case (<String>, <Integer>...). Avantages : on écrit le code UNE SEULE
 * FOIS et on le réutilise pour plusieurs types, et le compilateur VÉRIFIE le type
 * (fini les mauvaises surprises à l'exécution).
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/06_generics/Generics.java
 *     java -cp /tmp/jb Generics
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer une BOÎTE générique qui range un String, puis le relire.
 *   2. Créer une AUTRE Boîte qui range un Integer : MÊME classe, autre type.
 *   3. Appeler une MÉTHODE générique 'premier' sur une liste de String.
 *   4. Réutiliser cette MÊME méthode sur une liste d'Integer.
 *   5. Utiliser une méthode générique 'sontEgaux' qui compare deux T.
 */

import java.util.List;   // le type "liste" (on l'utilise dans les exemples)

public class Generics {

    // ─────────────────────────────────────────────
    // CLASSE GÉNÉRIQUE : le <T> juste après le nom annonce "cette classe
    // travaille avec un type laissé en blanc, qu'on appellera T à l'intérieur".
    // Ici, une Boîte qui peut contenir N'IMPORTE QUEL type d'objet.
    // ─────────────────────────────────────────────
    static class Boite<T> {
        // L'attribut a le type T : son vrai type sera fixé à l'utilisation.
        private T contenu;

        // Le constructeur reçoit un T et le range.
        public Boite(T contenu) {
            this.contenu = contenu;
        }

        // Le getter RENVOIE un T : le compilateur saura le type exact.
        public T getContenu() {
            return this.contenu;
        }

        // On peut remplacer le contenu, toujours par un T.
        public void setContenu(T contenu) {
            this.contenu = contenu;
        }
    }

    // ─────────────────────────────────────────────
    // MÉTHODE GÉNÉRIQUE : le <T> AVANT le type de retour déclare le type blanc
    // pour cette méthode-là. Ici "renvoyer le premier élément d'une liste de T".
    // Elle marche pour une List<String>, une List<Integer>, etc.
    // ─────────────────────────────────────────────
    static <T> T premier(List<T> liste) {
        return liste.get(0);   // get(0) renvoie un T : type garanti
    }

    // Autre méthode générique : compare deux valeurs de MÊME type T.
    // 'equals' existe sur tout objet, donc ça marche pour n'importe quel T.
    static <T> boolean sontEgaux(T a, T b) {
        return a.equals(b);
    }

    public static void main(String[] args) {

        // 1. Une Boîte de String : on remplit la "case type" avec String.
        Boite<String> boiteTexte = new Boite<>("bonjour");
        // getContenu() renvoie un String : pas besoin de conversion.
        String texte = boiteTexte.getContenu();
        System.out.println("Boite de texte : " + texte);

        // 2. La MÊME classe Boîte, mais pour des Integer cette fois.
        Boite<Integer> boiteNombre = new Boite<>(42);
        int nombre = boiteNombre.getContenu();   // renvoie un Integer
        System.out.println("Boite de nombre : " + nombre);

        // ✋ Décommente : le compilateur REFUSE, car la boîte est <String>.
        //    C'est ça, la SÉCURITÉ DE TYPE offerte par les génériques.
        // boiteTexte.setContenu(123);

        System.out.println("---");

        // 3. Méthode générique sur une liste de String.
        List<String> mots = List.of("alpha", "beta", "gamma");
        System.out.println("Premier mot : " + premier(mots));

        // 4. La MÊME méthode 'premier', réutilisée pour des Integer.
        List<Integer> nombres = List.of(10, 20, 30);
        System.out.println("Premier nombre : " + premier(nombres));

        System.out.println("---");

        // 5. Méthode générique de comparaison, pour deux types différents.
        System.out.println("\"chat\" == \"chat\" ? " + sontEgaux("chat", "chat"));
        System.out.println("7 == 8 ? " + sontEgaux(7, 8));
    }
}
