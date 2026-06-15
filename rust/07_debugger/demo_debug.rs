/*
 * MODULE 07 - Déboguer en Rust (programme correct et instructif)
 * ==============================================================
 * Ce programme NE PLANTE PAS : il te MONTRE les outils de débogage de Rust.
 * Le plus puissant ? Le compilateur lui-même : il refuse de compiler un code
 * douteux et t'explique, en français clair, comment le corriger.
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/07_debugger/demo_debug.rs -o /tmp/r && /tmp/r
 */

fn main() {
    println!("=== 1. La macro dbg! : inspecter une valeur ===");
    // dbg!(...) AFFICHE la valeur (avec le fichier + la ligne) ET la RENVOIE.
    // Donc on peut l'insérer EN PLEIN MILIEU d'un calcul sans rien casser.
    // La sortie de dbg! part sur la "sortie d'erreur" (stderr) : c'est normal.
    let a = 5;
    let b = 3;
    let somme = dbg!(a) + dbg!(b);   // affiche a, affiche b, puis additionne
    println!("somme = {}", somme);

    println!();
    println!("=== 2. Inspecter une structure entiere ===");
    // dbg! sait aussi afficher des structures, listes, etc. (vue "debug" {:?}).
    let scores = vec![12, 7, 20, 4];
    dbg!(&scores);   // on passe &scores (une référence) pour ne PAS donner la liste
    println!("nombre de scores : {}", scores.len());

    println!();
    println!("=== 3. L'affichage debug {{:?}} (sans dbg!) ===");
    // Pour une liste/struct, {} ne marche pas : on utilise {:?} (mode "debug").
    println!("scores = {:?}", scores);

    println!();
    println!("=== 4. Lire un Result au lieu de planter ===");
    // Plutôt que .unwrap() (qui panique en cas d'erreur), on inspecte le Result.
    let essais = ["42", "abc"];
    for texte in essais {
        match texte.parse::<i32>() {
            Ok(n)  => println!("'{}' -> nombre {}", texte, n),
            Err(e) => println!("'{}' -> ECHEC ({}) -- voila pourquoi ca aurait panique", texte, e),
        }
    }

    println!();
    println!("Programme termine correctement. Lis le README pour les erreurs frequentes.");
}
