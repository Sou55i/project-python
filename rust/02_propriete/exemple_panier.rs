/*
 * MODULE 02 - Exemple complet : un panier de courses
 * ==================================================
 * Un petit programme qui réutilise les 3 mécanismes du module dans un cas concret :
 *   - on AJOUTE des articles (emprunt &mut : on modifie le panier)
 *   - on AFFICHE le panier (emprunt & : on lit seulement)
 *   - on DONNE le panier à une autre variable (move)
 * But : voir que "prêter" (&) permet de réutiliser le panier ensuite, alors que
 * "donner" (move) en transfère définitivement la propriété.
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/02_propriete/exemple_panier.rs -o /tmp/r && /tmp/r
 */

// AJOUTER : on EMPRUNTE le panier en mutable (&mut) pour y mettre un article.
// 'article: &str' = un texte fixe qu'on copie dans le panier.
fn ajouter_article(panier: &mut Vec<String>, article: &str) {
    // .push() ajoute un élément à la fin. On transforme le &str en String possédée.
    panier.push(String::from(article));
}

// AFFICHER : on EMPRUNTE le panier en immuable (&), car on veut juste LIRE.
fn afficher_panier(panier: &Vec<String>) {
    println!("--- Panier ({} article(s)) ---", panier.len());
    // 'for x in panier' parcourt les éléments empruntés (on ne prend pas la propriété).
    for article in panier {
        println!("  - {}", article);
    }
}

fn main() {

    // On crée un panier vide. 'Vec<String>' = une liste de textes (voir module 04).
    let mut panier: Vec<String> = Vec::new();

    // 1. On le MODIFIE via des emprunts &mut. Après chaque appel, 'panier' reste à nous.
    ajouter_article(&mut panier, "pain");
    ajouter_article(&mut panier, "lait");
    ajouter_article(&mut panier, "pommes");

    // 2. On le LIT via un emprunt &. 'panier' n'est PAS donné : on pourra le réutiliser.
    afficher_panier(&panier);

    // 3. Comme on n'avait que PRÊTÉ, 'panier' est toujours valide ici :
    println!("Le panier est toujours utilisable, il a {} articles.", panier.len());

    // 4. MOVE : on DONNE la propriété du panier à 'panier_caisse'.
    let panier_caisse = panier; // déplacement (move) : 'panier' ne possède plus rien
    // afficher_panier(&panier); // ❌ ERREUR : 'panier' a été donné. Enlève le // pour voir !
    println!("A la caisse : {} articles a payer.", panier_caisse.len());
}
