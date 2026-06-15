/*
 * MODULE 02 - La propriété (ownership) : move, emprunt &, emprunt &mut
 * ===================================================================
 * Illustre, dans l'ordre du README :
 *   1. le MOVE (déplacement de propriété)
 *   2. la COPY des types simples
 *   3. l'emprunt IMMUABLE (&) pour lire
 *   4. l'emprunt MUTABLE (&mut) pour modifier
 *   5. la règle d'or des emprunts
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/02_propriete/propriete.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// FONCTIONS qui EMPRUNTENT (elles ne prennent pas la propriété)
// ─────────────────────────────────────────────

// '&String' = on EMPRUNTE le texte pour le LIRE. On ne le possède pas.
// '-> usize' = on renvoie un nombre (le type des longueurs/tailles en Rust).
fn longueur(texte: &String) -> usize {
    texte.len() // on a le droit de LIRE la valeur empruntée
}

// '&mut String' = on EMPRUNTE en MODIFICATION : on peut changer l'original.
fn ajouter_point(texte: &mut String) {
    texte.push('!'); // on ajoute un caractère AU texte de l'appelant
}

fn main() {

    // ─────────────────────────────────────────────
    // 1. LE MOVE : donner la propriété (pas une copie)
    // ─────────────────────────────────────────────
    let a = String::from("salut");
    let b = a; // la propriété du texte est DÉPLACÉE de 'a' vers 'b' (move)

    // println!("{}", a); // ❌ ERREUR : 'a' ne possède plus rien. Enlève le // pour voir !
    println!("1. move    : b = {}", b); // 'b' est le nouveau propriétaire, lui est valide

    // ─────────────────────────────────────────────
    // 2. LA COPY : les types simples sont COPIÉS, pas déplacés
    // ─────────────────────────────────────────────
    let x = 5;
    let y = x; // i32 est minuscule -> COPIE (pas de move)
    println!("2. copy    : x = {}, y = {}", x, y); // ✅ x ET y sont valides

    // ─────────────────────────────────────────────
    // 3. EMPRUNT IMMUABLE & : prêter pour LIRE
    // ─────────────────────────────────────────────
    let mot = String::from("bonjour");
    let n = longueur(&mot); // on PRÊTE 'mot' (le '&'), on ne le donne pas
    // Comme on a juste prêté, 'mot' est ENCORE à nous après l'appel :
    println!("3. emprunt &   : '{}' fait {} lettres", mot, n);

    // ─────────────────────────────────────────────
    // 4. EMPRUNT MUTABLE &mut : prêter pour MODIFIER
    // ─────────────────────────────────────────────
    let mut phrase = String::from("salut"); // 'mut' obligatoire pour pouvoir la modifier
    ajouter_point(&mut phrase); // on prête EN ÉCRITURE (note le '&mut')
    println!("4. emprunt &mut : '{}'", phrase); // "salut!" -> modifié à travers l'emprunt

    // ─────────────────────────────────────────────
    // 5. LA RÈGLE D'OR : plusieurs '&' OU un seul '&mut', jamais les deux
    // ─────────────────────────────────────────────
    let mut v = String::from("hej");

    let r1 = &v; // emprunt immuable : OK
    let r2 = &v; // un autre emprunt immuable EN MÊME TEMPS : OK (lecture à plusieurs)
    println!("5. lecture x2  : {} et {}", r1, r2);
    // 'r1' et 'r2' ne servent plus après cette ligne : Rust le sait.

    let m = &mut v; // emprunt MUTABLE : OK maintenant, car plus aucun '&' actif
    m.push('!');
    println!("5. apres &mut  : {}", m);
}
