/*
 * PROJET CAPSTONE - La classe Tache (une tâche du gestionnaire)
 * =============================================================
 * Cette classe représente UNE tâche : un identifiant, un titre, et un état
 * "faite ou non". C'est une classe au sens du module 02 (POO) : attributs
 * privés, constructeur, getters, et quelques méthodes. Elle sait aussi se
 * convertir en une ligne de texte (pour la sauvegarde) et se reconstruire à
 * partir d'une ligne de texte (pour le chargement).
 *
 * RÈGLE JAVA : classe publique 'Tache' => fichier 'Tache.java'.
 * Cette classe n'a PAS de main : elle est UTILISÉE par GestionnaireDeTaches.
 */

public class Tache {

    // ─────────────────────────────────────────────
    // ATTRIBUTS privés (encapsulation, comme au module 02).
    // ─────────────────────────────────────────────
    private int id;          // numéro unique de la tâche
    private String titre;    // ce qu'il y a à faire
    private boolean faite;   // true si la tâche est terminée

    // ─────────────────────────────────────────────
    // CONSTRUCTEUR : crée une tâche. Par défaut, elle n'est pas faite.
    // ─────────────────────────────────────────────
    public Tache(int id, String titre, boolean faite) {
        this.id = id;
        this.titre = titre;
        this.faite = faite;
    }

    // ─────────────────────────────────────────────
    // GETTERS : pour lire les attributs sans les abîmer.
    // ─────────────────────────────────────────────
    public int getId() {
        return this.id;
    }

    public String getTitre() {
        return this.titre;
    }

    public boolean estFaite() {
        return this.faite;
    }

    // Marquer la tâche comme terminée.
    public void marquerFaite() {
        this.faite = true;
    }

    // ─────────────────────────────────────────────
    // SAUVEGARDE : transformer la tâche en UNE ligne de texte.
    // Format choisi : "id;0ou1;titre"  (ex : "3;1;Acheter du pain").
    // Le ';' sépare les champs. On le réutilisera au chargement.
    // ─────────────────────────────────────────────
    public String versLigne() {
        int drapeau = this.faite ? 1 : 0;          // booléen -> 1 ou 0
        return this.id + ";" + drapeau + ";" + this.titre;
    }

    // ─────────────────────────────────────────────
    // CHARGEMENT : reconstruire une Tache à partir d'une ligne de texte.
    // 'static' car on l'appelle SANS objet existant : Tache.depuisLigne(...).
    // split(";", 3) découpe en AU PLUS 3 morceaux (le titre peut contenir ' ').
    // ─────────────────────────────────────────────
    public static Tache depuisLigne(String ligne) {
        String[] champs = ligne.split(";", 3);     // ["id", "0ou1", "titre"]
        int id = Integer.parseInt(champs[0]);      // texte -> nombre
        boolean faite = champs[1].equals("1");     // "1" -> true, sinon false
        String titre = champs[2];
        return new Tache(id, titre, faite);
    }

    // ─────────────────────────────────────────────
    // AFFICHAGE lisible : une case [x] si faite, [ ] sinon.
    // ─────────────────────────────────────────────
    public String versAffichage() {
        String case_ = this.faite ? "[x]" : "[ ]";
        return case_ + " #" + this.id + " " + this.titre;
    }
}
