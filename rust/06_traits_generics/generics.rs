/*
 * MODULE 06 - Les GÉNÉRIQUES <T>
 * ==============================
 * Un générique, c'est écrire du code UNE SEULE FOIS qui marche pour PLUSIEURS
 * types. Le <T> est un "type à trous" : Rust remplira le trou (i32, f64, String...)
 * selon ce que tu lui donnes. Tu connais déjà Vec<T> et Option<T> : c'est ça !
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/06_traits_generics/generics.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// 1. UNE FONCTION GÉNÉRIQUE
// ─────────────────────────────────────────────
// '<T: PartialOrd>' se lit : "pour un type T, à condition qu'on puisse COMPARER
// ses valeurs (PartialOrd)". Sans cette condition, Rust ne saurait pas faire '>'.
// La fonction renvoie le plus grand des deux, quel que soit le type.
fn plus_grand<T: PartialOrd>(a: T, b: T) -> T {
    if a > b {
        a
    } else {
        b
    }
}

// ─────────────────────────────────────────────
// 2. UNE STRUCT GÉNÉRIQUE
// ─────────────────────────────────────────────
// Une 'Paire<T>' contient deux valeurs DU MÊME type T (deux i32, ou deux String...).
struct Paire<T> {
    premier: T,
    second: T,
}

// On peut ajouter des méthodes à une struct générique.
// 'impl<T: std::fmt::Display>' : on impose que T soit AFFICHABLE (Display),
// sinon on ne pourrait pas l'écrire dans un println!.
impl<T: std::fmt::Display> Paire<T> {
    fn afficher(&self) {
        println!("Paire : ({}, {})", self.premier, self.second);
    }
}

fn main() {
    println!("=== 1. Une fonction, plusieurs types ===");

    // Le MÊME code 'plus_grand' marche pour des entiers...
    let max_entier = plus_grand(3, 9);
    println!("plus_grand(3, 9)       = {}", max_entier);

    // ...pour des nombres à virgule...
    let max_flottant = plus_grand(2.5, 1.1);
    println!("plus_grand(2.5, 1.1)   = {}", max_flottant);

    // ...et même pour du texte (l'ordre alphabétique) !
    let max_texte = plus_grand("abricot", "banane");
    println!("plus_grand(abricot, banane) = {}", max_texte);

    println!();
    println!("=== 2. Une struct generique ===");

    // Une paire d'entiers...
    let paire_nombres = Paire { premier: 10, second: 20 };
    paire_nombres.afficher();

    // ...et une paire de textes : la MÊME struct, un autre type.
    let paire_mots = Paire {
        premier: String::from("gauche"),
        second: String::from("droite"),
    };
    paire_mots.afficher();
}
