/*
 * MODULE 03 - Les enums, le match, et Option<T>
 * =============================================
 * Voir le bloc "CHEMINEMENT DU PROGRAMME" du README. Dans l'ordre :
 *   1. enum SIMPLE (Feu) + match pour réagir
 *   2. enum AVEC DONNÉES (Message) + match qui extrait les données
 *   3. Option<T> : Some / None + match qui force à gérer le cas vide
 *   4. cas concret : une fonction qui cherche et renvoie un Option
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/03_structs_enums/enums_match.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// 1. enum SIMPLE : une valeur parmi une liste fixe
// ─────────────────────────────────────────────
enum Feu {
    Rouge,
    Orange,
    Vert,
}

// ─────────────────────────────────────────────
// 2. enum AVEC DONNÉES : chaque variante peut transporter des valeurs
// ─────────────────────────────────────────────
enum Message {
    Quitter,                     // ne transporte rien
    Ecrire(String),              // transporte un texte
    Deplacer { x: i32, y: i32 }, // transporte deux nombres nommés
}

// ─────────────────────────────────────────────
// 4. Fonction qui CHERCHE un âge selon un nom et renvoie un Option :
//    Some(age) si trouvé, None si inconnu. (pas de 'null' en Rust !)
// ─────────────────────────────────────────────
fn age_de(nom: &str) -> Option<u32> {
    match nom {
        "Alice" => Some(30),
        "Bob" => Some(25),
        _ => None, // '_' = tous les autres cas : inconnu
    }
}

fn main() {

    // ── 1. match sur un enum simple ─────────────────
    // On parcourt les trois états du feu pour voir chaque branche du match.
    let feux = [Feu::Rouge, Feu::Orange, Feu::Vert];
    for etat in feux {
        // match doit couvrir TOUTES les variantes, sinon ça ne compile pas.
        match etat {
            Feu::Rouge => println!("1. Feu rouge  -> Stop !"),
            Feu::Orange => println!("1. Feu orange -> Ralentis..."),
            Feu::Vert => println!("1. Feu vert   -> Passe !"),
        }
    }

    println!("---");

    // ── 2. match qui EXTRAIT les données portées par les variantes ──
    let messages = [
        Message::Ecrire(String::from("salut")),
        Message::Deplacer { x: 3, y: 7 },
        Message::Quitter,
    ];

    for msg in messages {
        match msg {
            Message::Quitter => println!("2. Quitter -> au revoir."),
            // 'texte' récupère la String portée par Ecrire :
            Message::Ecrire(texte) => println!("2. Ecrire  -> \"{}\"", texte),
            // 'x' et 'y' récupèrent les deux nombres portés par Deplacer :
            Message::Deplacer { x, y } => println!("2. Deplacer -> aller en ({}, {})", x, y),
        }
    }

    println!("---");

    // ── 3. Option<T> : on DOIT gérer Some ET None ───
    let boite_pleine: Option<i32> = Some(42);
    let boite_vide: Option<i32> = None;

    match boite_pleine {
        Some(n) => println!("3. boite_pleine -> contient {}", n),
        None => println!("3. boite_pleine -> vide"),
    }
    match boite_vide {
        Some(n) => println!("3. boite_vide   -> contient {}", n),
        None => println!("3. boite_vide   -> vide"),
    }

    println!("---");

    // ── 4. cas concret : utiliser la fonction qui renvoie un Option ──
    for nom in ["Alice", "Charlie"] {
        match age_de(nom) {
            Some(age) => println!("4. {} a {} ans", nom, age),
            None => println!("4. {} : inconnu", nom),
        }
    }
}
