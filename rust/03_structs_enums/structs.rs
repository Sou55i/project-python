/*
 * MODULE 03 - Les structures (struct)
 * ===================================
 * Illustre, dans l'ordre du README :
 *   1. définir un modèle (struct) et créer des instances
 *   2. lire et modifier les champs
 *   3. attacher des méthodes avec un bloc impl
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/03_structs_enums/structs.rs -o /tmp/r && /tmp/r
 */

// ─────────────────────────────────────────────
// 1. DÉFINIR le modèle : une Personne a 3 champs (le "moule")
// ─────────────────────────────────────────────
struct Personne {
    nom: String, // un texte possédé
    age: u32,    // u32 = entier positif (un âge n'est jamais négatif)
    actif: bool, // vrai / faux
}

// ─────────────────────────────────────────────
// 3. MÉTHODES : des fonctions attachées à la struct, dans un bloc impl
// ─────────────────────────────────────────────
impl Personne {
    // '&self' = la fiche elle-même, EMPRUNTÉE (on prête, on ne prend pas la propriété).
    fn se_presenter(&self) {
        println!("Bonjour, je m'appelle {} et j'ai {} ans.", self.nom, self.age);
    }

    // Une méthode peut RENVOYER une valeur calculée à partir des champs.
    fn est_majeur(&self) -> bool {
        self.age >= 18
    }
}

fn main() {

    // ─────────────────────────────────────────────
    // 2a. CRÉER une instance (remplir les champs du moule)
    // ─────────────────────────────────────────────
    let alice = Personne {
        nom: String::from("Alice"),
        age: 30,
        actif: true,
    };

    // On LIT un champ avec un point :
    println!("Nom   : {}", alice.nom);
    println!("Age   : {}", alice.age);
    println!("Actif : {}", alice.actif);

    // On APPELLE les méthodes (avec un point + parenthèses) :
    alice.se_presenter();
    println!("Majeure ? {}", alice.est_majeur());

    println!("---");

    // ─────────────────────────────────────────────
    // 2b. MODIFIER un champ : l'instance doit être 'mut'
    // ─────────────────────────────────────────────
    let mut bob = Personne {
        nom: String::from("Bob"),
        age: 15,
        actif: false,
    };

    bob.se_presenter();
    println!("Majeur ? {}", bob.est_majeur()); // false

    bob.age = 18;       // on change un champ (possible car 'bob' est 'mut')
    bob.actif = true;
    println!("(un an plus tard...)");
    bob.se_presenter();
    println!("Majeur ? {}", bob.est_majeur()); // true maintenant
}
