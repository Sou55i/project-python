/*
 * MODULE 06 - Les TRAITS (comme des interfaces)
 * =============================================
 * Un trait, c'est un CONTRAT : il dit "tout type qui veut être un X DOIT savoir
 * faire ces choses-là". On définit le contrat une fois, puis plusieurs types
 * différents le respectent, chacun à sa manière.
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/06_traits_generics/traits.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// 1. DÉFINIR UN TRAIT (le contrat)
// ─────────────────────────────────────────────
// 'trait Decrire' dit : tout type qui veut "être Decrire" doit fournir une
// méthode 'decrire' qui renvoie un String. C'est juste la PROMESSE, pas le code.
trait Decrire {
    fn decrire(&self) -> String;   // &self = "moi-même", l'objet sur lequel on appelle

    // Un trait peut aussi fournir une méthode TOUTE FAITE (par défaut).
    // Les types qui le veulent pourront la garder telle quelle.
    fn presentation(&self) -> String {
        format!("Voici : {}", self.decrire())   // réutilise decrire() ci-dessus
    }
}

// ─────────────────────────────────────────────
// 2. DES TYPES QUI RESPECTENT LE CONTRAT
// ─────────────────────────────────────────────
struct Chien {
    nom: String,
}

struct Voiture {
    marque: String,
    chevaux: u32,
}

// 'impl Decrire for Chien' = "Chien respecte le contrat Decrire, voici COMMENT".
impl Decrire for Chien {
    fn decrire(&self) -> String {
        format!("un chien nomme {}", self.nom)
    }
    // On ne réécrit PAS presentation() : Chien garde la version par défaut du trait.
}

impl Decrire for Voiture {
    fn decrire(&self) -> String {
        format!("une {} de {} chevaux", self.marque, self.chevaux)
    }
}

// ─────────────────────────────────────────────
// 3. UNE FONCTION QUI ACCEPTE "N'IMPORTE QUEL TYPE Decrire"
// ─────────────────────────────────────────────
// 'item: &impl Decrire' = "je prends une référence vers N'IMPORTE QUEL type
// qui respecte le contrat Decrire". Peu importe que ce soit un Chien ou une Voiture !
fn afficher(item: &impl Decrire) {
    println!("{}", item.presentation());
}

fn main() {
    println!("=== 1. Plusieurs types, un seul contrat ===");

    let medor = Chien { nom: String::from("Medor") };
    let clio = Voiture { marque: String::from("Renault"), chevaux: 90 };

    // Les deux ont une méthode decrire(), chacun la sienne :
    println!("{}", medor.decrire());
    println!("{}", clio.decrire());

    println!();
    println!("=== 2. La fonction 'afficher' marche pour les DEUX ===");
    // Une seule fonction, deux types différents : c'est tout l'intérêt du trait.
    afficher(&medor);
    afficher(&clio);

    println!();
    println!("=== 3. La methode par defaut 'presentation' ===");
    // Chien n'a pas redéfini presentation() : il utilise celle du trait.
    println!("{}", medor.presentation());
}
