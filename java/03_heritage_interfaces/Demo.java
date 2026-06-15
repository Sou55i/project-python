/*
 * MODULE 03 - Héritage, classes abstraites, interfaces, polymorphisme
 * ===================================================================
 * Une classe ABSTRAITE Animal (modèle commun), deux classes FILLES Chien et
 * Chat qui en HÉRITENT (extends) et REDÉFINISSENT parler(), plus une INTERFACE
 * Nageur que seul le Chien IMPLÉMENTE. Le main montre le POLYMORPHISME : on
 * range des animaux variés dans un tableau d'Animal et on les fait tous parler.
 *
 * ⚠️ RÈGLE JAVA : un fichier ne peut contenir qu'UNE classe publique, du même
 *    nom que le fichier. On met donc Animal/Chien/Chat/Nageur SANS 'public'
 *    (visibles dans le fichier) et SEULE Demo est 'public' (elle a le main).
 *
 * Compiler puis lancer :
 *     javac -d /tmp/jb java/03_heritage_interfaces/Demo.java
 *     java -cp /tmp/jb Demo
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. CRÉER un Chien et un Chat (chacun reçoit un nom via le constructeur).
 *   2. Appeler une méthode HÉRITÉE de la mère (decrire()).
 *   3. Appeler parler() : chacun répond à SA façon (polymorphisme direct).
 *   4. Appeler une méthode AJOUTÉE par la fille (aboyer() du Chien).
 *   5. Ranger les animaux dans un TABLEAU d'Animal et tous les faire parler.
 *   6. Utiliser l'INTERFACE : seul le Chien sait nager().
 */

// ─────────────────────────────────────────────
// CLASSE ABSTRAITE : un MODÈLE commun qu'on ne peut pas instancier seul.
// 'abstract' = "on ne crée jamais un Animal tout court, seulement un Chien,
// un Chat…". Elle regroupe ce que TOUS les animaux ont en commun.
// ─────────────────────────────────────────────
abstract class Animal {
    protected String nom;   // 'protected' = accessible par la classe ET ses filles

    // CONSTRUCTEUR de la mère : les filles l'appelleront avec super(...).
    Animal(String nom) {
        this.nom = nom;
    }

    // Méthode CONCRÈTE (avec un corps) : héritée telle quelle par les filles.
    void decrire() {
        System.out.println("Je m'appelle " + nom + ".");
    }

    // Méthode ABSTRAITE : pas de corps, juste un ";". Chaque fille DOIT la
    // redéfinir. C'est ce qui force chacun à "parler" à sa façon.
    abstract void parler();
}

// ─────────────────────────────────────────────
// INTERFACE : un CONTRAT de capacités, sans aucun code.
// "Toute classe qui se dit Nageur DOIT fournir une méthode nager()."
// ─────────────────────────────────────────────
interface Nageur {
    void nager();   // pas de corps : juste la signature à respecter
}

// ─────────────────────────────────────────────
// CLASSE FILLE Chien : HÉRITE d'Animal (extends) ET respecte le contrat
// Nageur (implements). Elle peut faire les deux en même temps.
// ─────────────────────────────────────────────
class Chien extends Animal implements Nageur {

    // Le constructeur de la fille appelle d'abord celui de la mère via super(...).
    Chien(String nom) {
        super(nom);   // construit la partie "Animal" (range le nom)
    }

    // On REDÉFINIT la méthode abstraite de la mère.
    // @Override = "je redéfinis une méthode héritée" (le compilateur vérifie).
    @Override
    void parler() {
        System.out.println(nom + " fait : Wouf !");
    }

    // Méthode AJOUTÉE, propre au chien (pas dans la mère).
    void aboyer() {
        System.out.println(nom + " aboie sur le facteur.");
    }

    // On HONORE le contrat de l'interface Nageur.
    @Override
    public void nager() {
        System.out.println(nom + " nage joyeusement.");
    }
}

// ─────────────────────────────────────────────
// CLASSE FILLE Chat : hérite d'Animal, mais N'IMPLÉMENTE PAS Nageur
// (la plupart des chats détestent l'eau !).
// ─────────────────────────────────────────────
class Chat extends Animal {
    Chat(String nom) {
        super(nom);
    }

    @Override
    void parler() {
        System.out.println(nom + " fait : Miaou !");
    }
}

// ─────────────────────────────────────────────
// La SEULE classe publique du fichier : elle contient le main.
// Le fichier s'appelle donc Demo.java (règle Java).
// ─────────────────────────────────────────────
public class Demo {
    public static void main(String[] args) {

        // 1. CRÉER les objets (le constructeur de chaque fille reçoit le nom).
        Chien rex = new Chien("Rex");
        Chat felix = new Chat("Felix");

        // 2. Méthode HÉRITÉE de la mère, identique pour les deux.
        rex.decrire();
        felix.decrire();

        // 3. parler() : chacun répond à SA façon (la version de sa classe).
        rex.parler();     // Wouf
        felix.parler();   // Miaou

        // 4. Méthode AJOUTÉE par la fille Chien (le Chat ne l'a pas).
        rex.aboyer();

        System.out.println("---");

        // 5. POLYMORPHISME : un tableau de la classe MÈRE peut contenir
        //    n'importe quelle fille. À l'appel de parler(), Java choisit
        //    automatiquement la BONNE version (celle de la vraie classe).
        Animal[] animaux = { new Chien("Medor"), new Chat("Minou"), rex };
        for (Animal a : animaux) {   // boucle for-each : "pour chaque animal a"
            a.parler();              // chacun parle à sa manière, sans qu'on connaisse son type
        }

        System.out.println("---");

        // 6. INTERFACE : seul ce qui implémente Nageur sait nager().
        Nageur n = rex;   // un Chien EST un Nageur (il implémente le contrat)
        n.nager();
    }
}
