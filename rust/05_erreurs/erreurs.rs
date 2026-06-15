/*
 * MODULE 05 - Gérer les erreurs : Result, Option, l'opérateur ?, panic!
 * =====================================================================
 * Voir le bloc "CHEMINEMENT DU PROGRAMME" du README. Dans l'ordre :
 *   1. Result<T, E> : une fonction qui réussit (Ok) ou échoue (Err)
 *   2. Option<T>    : rappel de l'absence (Some / None) sur une liste
 *   3. l'opérateur ? : enchaîner des opérations risquées proprement
 *   4. panic!       : l'arrêt brutal, montré de façon contrôlée
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/05_erreurs/erreurs.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// 1. Result<T, E> : convertir un texte en nombre peut ÉCHOUER
//    Ok(nombre) si ça marche, Err(message) sinon.
// ─────────────────────────────────────────────
fn parser(texte: &str) -> Result<i32, String> {
    match texte.parse::<i32>() {
        // .parse() renvoie déjà un Result
        Ok(n) => Ok(n),                                          // réussi
        Err(_) => Err(format!("'{}' n'est pas un nombre", texte)), // échec : on explique
    }
}

// ─────────────────────────────────────────────
// 3. L'opérateur ? : additionne deux textes-nombres.
//    Si une conversion échoue, le '?' arrête la fonction et renvoie l'Err.
//    (Cette fonction renvoie un Result : c'est obligatoire pour utiliser '?'.)
// ─────────────────────────────────────────────
fn additionner(a: &str, b: &str) -> Result<i32, std::num::ParseIntError> {
    let x = a.parse::<i32>()?; // si Err -> on sort et on propage l'erreur
    let y = b.parse::<i32>()?; // idem
    Ok(x + y) // tout a réussi -> la somme dans un Ok
}

// ─────────────────────────────────────────────
// 4. panic! : arrêt brutal si on demande l'impossible.
//    Ici on ne l'appellera QUE sur un cas valide pour ne pas stopper le programme.
// ─────────────────────────────────────────────
fn racine_obligatoire(x: f64) -> f64 {
    if x < 0.0 {
        panic!("Impossible : racine d'un nombre negatif ({})", x);
    }
    x.sqrt()
}

fn main() {

    // ── 1. Result : on DOIT gérer Ok ET Err ─────────
    println!("1. Result");
    for entree in ["42", "abc"] {
        match parser(entree) {
            Ok(n) => println!("   parser(\"{}\") -> Ok : {}", entree, n),
            Err(e) => println!("   parser(\"{}\") -> Err : {}", entree, e),
        }
    }

    println!("---");

    // ── 2. Option : rappel de l'absence (Some / None) ──
    println!("2. Option (rappel)");
    let liste = vec![10, 20, 30];
    match liste.get(1) {
        Some(v) => println!("   liste[1] -> Some : {}", v),
        None => println!("   liste[1] -> None"),
    }
    match liste.get(99) {
        Some(v) => println!("   liste[99] -> Some : {}", v),
        None => println!("   liste[99] -> None (hors limites)"),
    }

    println!("---");

    // ── 3. L'opérateur ? en action ──────────────────
    println!("3. Operateur ?");
    // Cas qui réussit : les deux textes sont des nombres.
    match additionner("20", "22") {
        Ok(somme) => println!("   additionner(\"20\", \"22\") -> Ok : {}", somme),
        Err(e) => println!("   erreur : {}", e),
    }
    // Cas qui échoue : "x" n'est pas un nombre -> le '?' a fait remonter l'Err.
    match additionner("20", "x") {
        Ok(somme) => println!("   additionner(\"20\", \"x\") -> Ok : {}", somme),
        Err(e) => println!("   additionner(\"20\", \"x\") -> Err propagee par '?' : {}", e),
    }

    println!("---");

    // ── 4. panic! : on n'appelle QUE le cas valide pour ne pas couper le programme ──
    println!("4. panic! (on declenche seulement le cas SANS panique)");
    let r = racine_obligatoire(16.0); // 16 >= 0 -> pas de panique
    println!("   racine de 16 = {}", r);
    println!("   (passer un nombre negatif declencherait panic! et arreterait tout)");
}
