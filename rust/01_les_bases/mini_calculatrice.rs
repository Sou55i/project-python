/*
 * MODULE 01 - Mini-projet : une calculatrice en Rust
 * ==================================================
 * On combine ce qu'on a vu (variables, lecture au clavier, conditions, fonctions)
 * dans un petit programme utile : il lit une opération et deux nombres, puis calcule.
 *
 * Compiler puis lancer :
 *     rustc rust/01_les_bases/mini_calculatrice.rs -o calc && ./calc
 *
 * Tu peux aussi lui "souffler" la saisie pour tester :
 *     printf "+\n7\n5\n" | ./calc
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. USE        : on importe std::io pour lire au clavier (entrée standard).
 *    2. FONCTIONS  : une fonction par opération (additionner, soustraire...).
 *    3. lire_ligne : un petit outil pour lire UNE ligne tapée par l'utilisateur.
 *    4. main       : (a) demander l'opération, (b) demander deux nombres,
 *                    (c) choisir le calcul selon l'opération, (d) afficher.
 */

// 1. On importe l'outil d'entrée/sortie standard (pour lire au clavier).
use std::io;
// 'Write' nous permet de "vider" l'affichage (flush) pour que la question
// apparaisse AVANT que l'utilisateur tape sa réponse.
use std::io::Write;

// 2. Une fonction par opération : code clair et réutilisable.
//    On travaille avec des 'f64' pour gérer aussi les nombres à virgule.
fn additionner(a: f64, b: f64) -> f64 { a + b }
fn soustraire(a: f64, b: f64) -> f64 { a - b }
fn multiplier(a: f64, b: f64) -> f64 { a * b }

// 3. Un petit outil : afficher une question, puis lire la ligne tapée.
//    '-> String' = la fonction renvoie le texte saisi (sans le retour à la ligne).
fn lire_ligne(question: &str) -> String {
    // Afficher la question SANS retour à la ligne, puis forcer l'affichage.
    print!("{}", question);
    io::stdout().flush().unwrap();   // 'unwrap' = "si ça rate, on s'arrête" (suffisant ici)

    // On prépare un texte vide et MODIFIABLE pour y ranger la saisie.
    let mut entree = String::new();
    // read_line lit une ligne au clavier et l'ajoute dans 'entree'.
    io::stdin().read_line(&mut entree).unwrap();

    // .trim() enlève les espaces et le retour à la ligne au début/à la fin.
    // .to_string() renvoie une copie propre sous forme de String.
    entree.trim().to_string()
}

fn main() {
    // (a) DEMANDER l'opération (un seul caractère : +, -, * ou /).
    let operation = lire_ligne("Operation (+, -, *, /) : ");

    // (b) DEMANDER les deux nombres, puis les CONVERTIR de texte en f64.
    //     .parse() transforme "7" en nombre. Comme ça peut échouer (texte invalide),
    //     on gère le cas avec match : Ok(valeur) si réussi, Err(_) si raté.
    let texte1 = lire_ligne("Premier nombre  : ");
    let n1: f64 = match texte1.parse() {
        Ok(valeur) => valeur,
        Err(_) => {
            println!("Erreur : '{}' n'est pas un nombre valide.", texte1);
            return;   // on quitte le programme
        }
    };

    let texte2 = lire_ligne("Deuxieme nombre : ");
    let n2: f64 = match texte2.parse() {
        Ok(valeur) => valeur,
        Err(_) => {
            println!("Erreur : '{}' n'est pas un nombre valide.", texte2);
            return;
        }
    };

    // (c) CHOISIR le calcul selon l'opération.
    //     operation est une String ; on compare avec .as_str() face aux textes "+", "-"...
    let resultat = if operation == "+" {
        additionner(n1, n2)
    } else if operation == "-" {
        soustraire(n1, n2)
    } else if operation == "*" {
        multiplier(n1, n2)
    } else if operation == "/" {
        // On se protège de la division par zéro.
        if n2 == 0.0 {
            println!("Erreur : division par zero impossible.");
            return;
        }
        n1 / n2
    } else {
        println!("Operation inconnue : '{}'.", operation);
        return;
    };

    // (d) AFFICHER le résultat. {:.2} = 2 chiffres après la virgule.
    println!("Resultat : {:.2}", resultat);
}
