/*
 * MODULE 01 - Les briques de base en Java
 * =======================================
 * Illustre, dans l'ordre, les notions du README : types et variables,
 * affichage, conditions, boucles, methodes.
 *
 * Compiler puis lancer :
 *     javac java/01_les_bases/Bases.java
 *     java -cp java/01_les_bases Bases
 */

// En Java, tout vit dans une classe. Le fichier s'appelle Bases.java
// car la classe publique s'appelle Bases.
public class Bases {

    // ─────────────────────────────────────────────
    // MÉTHODES (définies dans la classe, en dehors de main)
    // 'static' = appelables directement depuis main, sans créer d'objet.
    // ─────────────────────────────────────────────

    // 'int' = type de la valeur renvoyée ; (int a, int b) = deux paramètres entiers.
    static int additionner(int a, int b) {
        return a + b;   // 'return' renvoie le résultat à l'appelant
    }

    // 'void' = cette méthode ne renvoie rien ; elle se contente d'afficher.
    static void saluer() {
        System.out.println("Bonjour depuis une methode !");
    }

    // ─────────────────────────────────────────────
    // main : le point de départ du programme
    // ─────────────────────────────────────────────
    public static void main(String[] args) {

        // 1. VARIABLES ET TYPES (on annonce le type, puis le nom, puis la valeur ; finit par ;)
        int age = 30;             // entier
        double taille = 1.68;     // nombre à virgule
        char initiale = 'A';      // UN caractère, entre apostrophes simples
        boolean majeur = true;    // un booléen : true (vrai) ou false (faux)
        String nom = "Lou";       // du TEXTE, entre guillemets doubles

        // 2. AFFICHER : on colle texte et variables avec le + (concaténation).
        System.out.println("Nom : " + nom);
        System.out.println("Age : " + age + " ans");
        System.out.println("Taille : " + taille + " m");
        System.out.println("Initiale : " + initiale);
        System.out.println("Majeur : " + majeur);

        // 3. CONDITIONS : la condition entre ( ), le bloc entre { }.
        int note = 12;
        if (note >= 16) {
            System.out.println("Mention : Tres bien");
        } else if (note >= 10) {   // 'else if' (et non 'elif')
            System.out.println("Mention : Recu");
        } else {
            System.out.println("Mention : A retravailler");
        }

        // 4. BOUCLE for : (début ; condition de continuation ; pas)
        for (int i = 0; i < 3; i++) {   // i++ = i = i + 1
            System.out.println("Tour numero " + i);
        }

        // 5. BOUCLE while : tant que la condition est vraie.
        int compteur = 0;
        while (compteur < 3) {
            System.out.println("compteur = " + compteur);
            compteur++;   // indispensable, sinon boucle infinie
        }

        // 6. APPELER NOS MÉTHODES définies plus haut dans la classe.
        saluer();
        int somme = additionner(7, 5);
        System.out.println("7 + 5 = " + somme);
    }
}
