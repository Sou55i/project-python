/*
 * MODULE 00 - Premier programme en Rust
 * =====================================
 * Ton tout premier programme Rust. Objectif : voir le cycle
 * « écrire -> COMPILER -> lancer » en action.
 *
 * Pour le compiler puis le lancer, ouvre un terminal et tape :
 *     rustc rust/00_demarrer/premier_programme.rs -o premier && ./premier
 *
 * (Pour un vrai projet, on utiliserait plutôt `cargo run`.)
 *
 * Rappel : les commentaires (comme ce bloc) sont ignorés par le compilateur.
 * En Rust on écrit  // pour une ligne   ou   ... pour plusieurs lignes.
 */

// (1) fn main = le POINT DE DÉPART de tout programme Rust. L'exécution commence ici.
//     'fn' veut dire "fonction". 'main' est le nom obligatoire du point d'entrée.
//     L'accolade { ouvre le corps de la fonction (fermé par } tout en bas).
fn main() {

    // (2) println! affiche du texte à l'écran, suivi d'un retour à la ligne.
    //     Le '!' indique que println! est une MACRO (un outil spécial de Rust),
    //     pas une fonction classique. Pour l'instant, retiens juste : ça affiche.
    //     Chaque instruction se termine par un point-virgule ;
    println!("Bonjour le monde !");
    println!("Je viens de compiler et lancer mon premier programme Rust.");

    // On peut afficher plusieurs lignes : le programme s'exécute de haut en bas.
    println!("Cette ligne s'affiche apres les precedentes.");

    // (3) Pas de "return 0" obligatoire ici : si tout va bien, Rust signale
    //     automatiquement le succès au système quand main se termine.
}

/*
 * À TOI DE MODIFIER :
 *   - change le texte des println!,
 *   - ajoute un nouveau println! avec ton message,
 *   - RECOMPILE (rustc ... -o ...) puis relance (./premier).
 * En Rust, il faut TOUJOURS recompiler après une modification pour la voir.
 */
