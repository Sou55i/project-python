/*
 * PROJET CAPSTONE - Gestionnaire de tâches (la "to-do list")
 * ==========================================================
 * Ce projet RASSEMBLE tout le parcours Java : une CLASSE Tache (module 02), une
 * ArrayList<Tache> avec génériques (modules 04 & 06), des STREAMS pour filtrer
 * et compter (module 08), de la gestion d'EXCEPTIONS pour les fichiers (module
 * 05), et la lecture/écriture d'un FICHIER de sauvegarde.
 *
 * Programme NON INTERACTIF : il utilise des données de démo, sauvegarde dans un
 * fichier, le recharge, puis affiche. La sortie est DÉTERMINISTE.
 *
 * RÈGLE JAVA : classe publique 'GestionnaireDeTaches' => fichier de même nom.
 *
 * Compiler puis lancer (les DEUX fichiers ensemble) :
 *     javac -d /tmp/jb java/projets/Tache.java java/projets/GestionnaireDeTaches.java
 *     java -cp /tmp/jb GestionnaireDeTaches
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer un gestionnaire (qui contient une liste de tâches, vide au départ).
 *   2. AJOUTER quelques tâches de démo (id attribué automatiquement).
 *   3. Marquer une tâche comme FAITE.
 *   4. AFFICHER toutes les tâches + un résumé (faites / restantes) via streams.
 *   5. SAUVEGARDER la liste dans un fichier (sous-dossier exemples/).
 *   6. RECHARGER depuis ce fichier dans un NOUVEAU gestionnaire, et réafficher
 *      pour prouver que la sauvegarde/chargement fonctionne.
 */

import java.io.IOException;                 // exception VÉRIFIÉE des entrées/sorties
import java.nio.file.Files;                 // lecture/écriture de fichiers (simple)
import java.nio.file.Path;                  // un chemin de fichier
import java.util.ArrayList;                 // la liste qui grandit
import java.util.List;                      // le type "liste"

public class GestionnaireDeTaches {

    // La liste des tâches : ArrayList générique (modules 04 & 06).
    private List<Tache> taches = new ArrayList<>();

    // Pour attribuer un id unique et croissant à chaque nouvelle tâche.
    private int prochainId = 1;

    // ─────────────────────────────────────────────
    // AJOUTER une tâche à partir d'un simple titre.
    // L'id est attribué automatiquement, la tâche est "non faite" au départ.
    // ─────────────────────────────────────────────
    public void ajouter(String titre) {
        Tache t = new Tache(this.prochainId, titre, false);
        this.taches.add(t);
        this.prochainId++;
    }

    // ─────────────────────────────────────────────
    // MARQUER FAITE une tâche par son id (si elle existe).
    // ─────────────────────────────────────────────
    public void marquerFaite(int id) {
        for (Tache t : this.taches) {
            if (t.getId() == id) {
                t.marquerFaite();
                return;
            }
        }
    }

    // ─────────────────────────────────────────────
    // AFFICHER toutes les tâches + un résumé calculé avec des STREAMS (module 08).
    // ─────────────────────────────────────────────
    public void afficher() {
        System.out.println("--- Mes taches ---");
        for (Tache t : this.taches) {
            System.out.println("  " + t.versAffichage());
        }
        // STREAMS : compter les tâches faites (filter + count).
        long nbFaites = this.taches.stream()
                .filter(Tache::estFaite)   // référence de méthode : "t -> t.estFaite()"
                .count();
        long nbRestantes = this.taches.size() - nbFaites;
        System.out.println("Resume : " + nbFaites + " faite(s), " + nbRestantes + " restante(s).");
    }

    // ─────────────────────────────────────────────
    // SAUVEGARDER dans un fichier : une tâche par ligne (format versLigne()).
    // 'throws IOException' : l'écriture peut échouer (disque plein...), c'est
    // une exception VÉRIFIÉE (module 05) que l'appelant devra gérer.
    // ─────────────────────────────────────────────
    public void sauvegarder(Path chemin) throws IOException {
        List<String> lignes = new ArrayList<>();
        for (Tache t : this.taches) {
            lignes.add(t.versLigne());
        }
        Files.write(chemin, lignes);   // écrit toutes les lignes dans le fichier
    }

    // ─────────────────────────────────────────────
    // CHARGER depuis un fichier : on relit chaque ligne et on reconstruit les
    // Tache. On remet aussi 'prochainId' à jour pour éviter les doublons d'id.
    // ─────────────────────────────────────────────
    public void charger(Path chemin) throws IOException {
        this.taches.clear();                       // on repart d'une liste vide
        List<String> lignes = Files.readAllLines(chemin);
        for (String ligne : lignes) {
            if (ligne.isBlank()) {
                continue;                          // on ignore les lignes vides
            }
            Tache t = Tache.depuisLigne(ligne);
            this.taches.add(t);
            if (t.getId() >= this.prochainId) {
                this.prochainId = t.getId() + 1;   // le prochain id reste unique
            }
        }
    }

    public static void main(String[] args) {

        // 1. Créer un gestionnaire (liste vide au départ).
        GestionnaireDeTaches gestion = new GestionnaireDeTaches();

        // 2. Ajouter des tâches de démo (NON interactif : pas de saisie clavier).
        gestion.ajouter("Apprendre les generiques");
        gestion.ajouter("Lire une stack trace");
        gestion.ajouter("Ecrire un stream");
        gestion.ajouter("Lancer un thread");

        // 3. Marquer deux tâches comme faites.
        gestion.marquerFaite(1);
        gestion.marquerFaite(3);

        // 4. Afficher l'état courant.
        gestion.afficher();

        // 5. Sauvegarder dans le sous-dossier exemples/.
        // On entoure d'un try/catch car l'écriture peut lever une IOException.
        Path fichier = Path.of("java/projets/exemples/taches.txt");
        try {
            // S'assurer que le dossier exemples/ existe (sinon on le crée).
            Files.createDirectories(fichier.getParent());
            gestion.sauvegarder(fichier);
            System.out.println("Sauvegarde dans : " + fichier);
        } catch (IOException e) {
            System.out.println("Echec de la sauvegarde : " + e.getMessage());
            return;   // inutile de continuer si on n'a pas pu sauvegarder
        }

        System.out.println("---");

        // 6. Recharger dans un NOUVEAU gestionnaire pour prouver que ça marche.
        GestionnaireDeTaches rechargé = new GestionnaireDeTaches();
        try {
            rechargé.charger(fichier);
            System.out.println("Recharge depuis le fichier :");
            rechargé.afficher();
        } catch (IOException e) {
            System.out.println("Echec du chargement : " + e.getMessage());
        }
    }
}
