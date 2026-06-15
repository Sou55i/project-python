/*
 * MODULE 04 - Les collections : Vec<T>, String, HashMap
 * =====================================================
 * Voir le bloc "CHEMINEMENT DU PROGRAMME" du README. Dans l'ordre :
 *   1. Vec<T>   : liste extensible (push, indice, len, for, get)
 *   2. String   : texte modifiable (push_str, push, to_uppercase)
 *   3. HashMap  : annuaire clé -> valeur (insert, get, parcours)
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/04_collections/collections.rs -o /tmp/r && /tmp/r
 */

// HashMap n'est pas chargé par défaut : on l'IMPORTE en haut du fichier.
use std::collections::HashMap;

fn main() {

    // ─────────────────────────────────────────────
    // 1. Vec<T> : une liste qui peut grandir
    // ─────────────────────────────────────────────
    let mut nombres: Vec<i32> = Vec::new(); // liste vide d'entiers ('mut' pour la remplir)
    nombres.push(10); // ajoute au bout
    nombres.push(20);
    nombres.push(30);

    println!("1. Vec<T>");
    println!("   premier element (indice 0) : {}", nombres[0]); // accès par indice
    println!("   nombre d'elements          : {}", nombres.len());

    // Parcours : on EMPRUNTE (&) pour ne pas consommer la liste (module 02).
    print!("   tous les elements          :");
    for n in &nombres {
        print!(" {}", n);
    }
    println!();

    // Accès SÛR avec .get() : renvoie un Option (Some si l'indice existe, None sinon).
    match nombres.get(99) {
        Some(valeur) => println!("   indice 99 : {}", valeur),
        None => println!("   indice 99 : n'existe pas (None)"),
    }

    println!("---");

    // ─────────────────────────────────────────────
    // 2. String : du texte qu'on peut modifier
    // ─────────────────────────────────────────────
    let mut texte = String::from("Bonjour"); // String modifiable
    texte.push_str(", monde"); // ajoute un bout de texte
    texte.push('!'); // ajoute UN caractère

    println!("2. String");
    println!("   texte           : {}", texte);
    println!("   longueur (octets): {}", texte.len());
    println!("   en majuscules   : {}", texte.to_uppercase());

    println!("---");

    // ─────────────────────────────────────────────
    // 3. HashMap : associer une clé à une valeur
    // ─────────────────────────────────────────────
    let mut scores: HashMap<String, i32> = HashMap::new(); // clé = String, valeur = i32
    scores.insert(String::from("Alice"), 90); // "Alice" -> 90
    scores.insert(String::from("Bob"), 75);

    println!("3. HashMap");

    // .get() renvoie un Option : la clé existe... ou pas.
    match scores.get("Alice") {
        Some(score) => println!("   Alice   : {} points", score),
        None => println!("   Alice   : inconnue"),
    }
    match scores.get("Charlie") {
        Some(score) => println!("   Charlie : {} points", score),
        None => println!("   Charlie : inconnu (None)"),
    }

    // Parcours d'un HashMap : (cle, valeur). L'ordre n'est PAS garanti.
    println!("   --- tout l'annuaire ---");
    for (nom, score) in &scores {
        println!("   {} a {} points", nom, score);
    }
}
