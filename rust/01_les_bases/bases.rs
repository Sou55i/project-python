/*
 * MODULE 01 - Les briques de base en Rust
 * =======================================
 * Illustre, dans l'ordre, les notions du README : variables (let / let mut),
 * types, if/else (et if comme expression), boucles (loop/while/for), fonctions.
 *
 * Compiler puis lancer :
 *     rustc rust/01_les_bases/bases.rs -o bases && ./bases
 */

// ─────────────────────────────────────────────
// FONCTIONS (on peut les définir avant OU après main, Rust s'y retrouve)
// ─────────────────────────────────────────────

// 'fn' = fonction. (a: i32, b: i32) = deux paramètres entiers.
// '-> i32' = le type de la valeur RENVOYÉE.
fn additionner(a: i32, b: i32) -> i32 {
    a + b   // dernière ligne SANS ';' = c'est la valeur renvoyée (pas besoin de 'return')
}

// Sans '->', la fonction ne renvoie rien : elle se contente d'afficher.
fn saluer() {
    println!("Bonjour depuis une fonction !");
}

// ─────────────────────────────────────────────
// main : le point de départ du programme
// ─────────────────────────────────────────────
fn main() {

    // 1. VARIABLES ET TYPES
    //    'let' crée une variable. Le type est souvent DEVINÉ, mais on peut l'écrire après ':'.
    let age: i32 = 30;        // entier
    let taille: f64 = 1.68;   // nombre à virgule
    let initiale: char = 'A'; // UN caractère, entre apostrophes simples
    let actif: bool = true;   // vrai / faux
    let prenom: &str = "Alice"; // un texte fixe

    // 2. AFFICHER avec println! : chaque {} est remplacé par une variable, dans l'ordre.
    println!("Prenom : {}", prenom);
    println!("Age : {} ans", age);
    println!("Taille : {} m", taille);
    println!("Initiale : {}", initiale);
    println!("Actif : {}", actif);

    // 3. IMMUABLE PAR DÉFAUT, sauf si on ajoute 'mut'.
    //    Sans 'mut', on ne pourrait PAS faire "compteur = ..." plus loin.
    let mut compteur = 0;   // 'mut' = on a le droit de la modifier

    // 4. CONDITIONS : la condition SANS parenthèses, le bloc entre { }.
    let note = 12;
    if note >= 16 {
        println!("Mention : Tres bien");
    } else if note >= 10 {   // 'else if' (et non 'elif')
        println!("Mention : Recu");
    } else {
        println!("Mention : A retravailler");
    }

    // 5. if EST UNE EXPRESSION : il peut renvoyer une valeur rangée dans un 'let'.
    let reussi = note >= 10;
    let message = if reussi { "gagne" } else { "perdu" };
    println!("Resultat : {}", message);

    // 6. BOUCLE for : pour chaque i dans la plage 0..3 (0, 1, 2 ; le 3 est EXCLU).
    for i in 0..3 {
        println!("Tour numero {}", i);
    }

    // 7. BOUCLE while : tant que la condition est vraie.
    while compteur < 3 {
        println!("compteur = {}", compteur);
        compteur += 1;   // indispensable, sinon boucle infinie
    }

    // 8. BOUCLE loop : infinie par nature ; on en sort avec 'break'.
    let mut tours = 0;
    loop {
        if tours == 2 {
            break;   // on quitte la boucle
        }
        println!("loop, tour {}", tours);
        tours += 1;
    }

    // 9. APPELER NOS FONCTIONS définies plus haut.
    saluer();
    let somme = additionner(7, 5);
    println!("7 + 5 = {}", somme);
}
