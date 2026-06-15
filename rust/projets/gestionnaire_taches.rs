/*
 * PROJET CAPSTONE - Un gestionnaire de tâches en mémoire
 * ======================================================
 * Ce projet COMBINE tout le parcours Rust :
 *   - struct + enum (module 03) pour modéliser une tâche et son statut,
 *   - Vec (module 04) pour stocker les tâches,
 *   - match (module 03) pour réagir selon les cas,
 *   - Result (module 05) pour signaler "tâche introuvable" proprement,
 *   - itérateurs (module 08) pour filtrer et compter.
 *
 * Il n'est PAS interactif : on remplit des données de démo, on agit dessus,
 * et on affiche le résultat. La sortie est donc toujours la même.
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/projets/gestionnaire_taches.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// LE MODÈLE DE DONNÉES
// ─────────────────────────────────────────────

// Un enum : une tâche est SOIT à faire, SOIT terminée. Pas d'autre cas possible.
#[derive(Debug, Clone, PartialEq)]   // permet d'afficher ({:?}), copier, comparer
enum Statut {
    AFaire,
    Terminee,
}

// Une struct : une tâche regroupe un identifiant, un titre et un statut.
#[derive(Debug, Clone)]
struct Tache {
    id: u32,
    titre: String,
    statut: Statut,
}

// Le gestionnaire : il contient la liste des tâches et le prochain id à attribuer.
struct Gestionnaire {
    taches: Vec<Tache>,
    prochain_id: u32,
}

impl Gestionnaire {
    // Crée un gestionnaire vide.
    fn nouveau() -> Gestionnaire {
        Gestionnaire { taches: Vec::new(), prochain_id: 1 }
    }

    // Ajoute une tâche "à faire" et renvoie son id.
    fn ajouter(&mut self, titre: &str) -> u32 {
        let id = self.prochain_id;
        self.taches.push(Tache {
            id,
            titre: String::from(titre),
            statut: Statut::AFaire,
        });
        self.prochain_id += 1;   // on prépare l'id suivant
        id
    }

    // Marque une tâche comme terminée. Renvoie un Result : Ok si trouvée,
    // Err (avec un message) si l'id n'existe pas -> l'appelant DOIT gérer le cas.
    fn terminer(&mut self, id: u32) -> Result<(), String> {
        for tache in self.taches.iter_mut() {
            if tache.id == id {
                tache.statut = Statut::Terminee;
                return Ok(());
            }
        }
        Err(format!("Aucune tache avec l'id {}", id))
    }

    // Compte les tâches encore à faire (itérateur + filter, module 08).
    fn nombre_a_faire(&self) -> usize {
        self.taches
            .iter()
            .filter(|t| t.statut == Statut::AFaire)
            .count()
    }

    // Affiche toutes les tâches, avec une coche selon le statut (match, module 03).
    fn afficher(&self) {
        for tache in &self.taches {
            let marque = match tache.statut {
                Statut::AFaire   => "[ ]",
                Statut::Terminee => "[x]",
            };
            println!("  {} #{} {}", marque, tache.id, tache.titre);
        }
    }
}

fn main() {
    println!("=== Gestionnaire de taches (donnees de demo) ===");
    let mut gest = Gestionnaire::nouveau();

    // 1. On ajoute trois tâches de démo.
    gest.ajouter("Apprendre les traits");
    gest.ajouter("Ecrire un programme concurrent");
    gest.ajouter("Relire le module erreurs");

    println!();
    println!("Etat initial :");
    gest.afficher();

    // 2. On termine deux tâches. terminer() renvoie un Result : on le gère.
    println!();
    println!("On termine les taches #1 et #3 :");
    for id in [1, 3] {
        match gest.terminer(id) {
            Ok(())  => println!("  tache #{} terminee", id),
            Err(e)  => println!("  erreur : {}", e),
        }
    }

    // 3. On tente de terminer une tâche inexistante : l'Err remonte proprement.
    println!();
    println!("On tente de terminer une tache inexistante (#99) :");
    match gest.terminer(99) {
        Ok(())  => println!("  tache #99 terminee"),
        Err(e)  => println!("  erreur attendue : {}", e),
    }

    // 4. État final + statistique.
    println!();
    println!("Etat final :");
    gest.afficher();
    println!();
    println!("Il reste {} tache(s) a faire.", gest.nombre_a_faire());
}
