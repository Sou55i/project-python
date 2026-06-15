# Module 03 — `struct`, `enum`, `match` et `Option<T>`

Jusqu'ici on a manipulé des valeurs simples (un nombre, un texte). Mais dans la vraie vie,
une donnée est souvent **composée** : un utilisateur a un *nom* ET un *âge* ET un *email*…
Ce module t'apprend à **regrouper** des données (`struct`), à représenter des **choix**
(`enum`), à **réagir** selon les cas (`match`), et à gérer proprement l'**absence** de
valeur (`Option<T>`).

> Fichiers du module : `structs.rs` (créer et utiliser des structures) et `enums_match.rs`
> (les énumérations, le `match`, et le fameux `Option<T>`).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. `struct` : regrouper des données qui vont ensemble

📦 **Analogie : une fiche d'identité.** Au lieu de trimballer trois variables séparées
(`nom`, `age`, `actif`), on les range dans **une seule** fiche. Une `struct` (structure),
c'est ce modèle de fiche.

```rust
// On DÉFINIT le modèle (le "moule") : une Personne a 3 champs.
struct Personne {
    nom: String,
    age: u32,      // u32 = entier positif (un âge n'est jamais négatif)
    actif: bool,
}
```

On **crée** ensuite une fiche concrète (on dit « une instance ») en remplissant les champs :

```rust
let alice = Personne {
    nom: String::from("Alice"),
    age: 30,
    actif: true,
};

// On accède à un champ avec un point :
println!("{} a {} ans", alice.nom, alice.age);
```

> 💡 Pour **modifier** un champ, l'instance doit être `let mut` (immuable par défaut, comme
> toutes les variables Rust). Puis `alice.age = 31;`.

---

## 2. Des fonctions liées à la struct : les méthodes (`impl`)

On peut attacher des **fonctions** à une `struct`, dans un bloc `impl` (implémentation).
On les appelle des **méthodes** : ce sont des actions « propres » à la structure.

```rust
impl Personne {
    // '&self' = la fiche elle-même, EMPRUNTÉE (souviens-toi du module 02 : on prête).
    fn se_presenter(&self) {
        println!("Bonjour, je m'appelle {} et j'ai {} ans.", self.nom, self.age);
    }
}

// Appel : avec un point, comme un champ, mais avec des parenthèses.
alice.se_presenter();
```

🤝 **Analogie :** la `struct` est l'objet, la **méthode** est ce que l'objet **sait faire**.
Une `Personne` *sait se présenter*.

---

## 3. `enum` : choisir parmi plusieurs possibilités

Un **`enum`** (énumération) sert quand une donnée ne peut prendre qu'**une valeur parmi une
liste fixe** de possibilités.

🚦 **Analogie : un feu tricolore.** Il est forcément *rouge*, *orange* OU *vert* — jamais
autre chose, jamais deux à la fois.

```rust
enum Feu {
    Rouge,
    Orange,
    Vert,
}

let etat = Feu::Vert; // on choisit UNE des variantes (avec '::')
```

Mieux : en Rust, une variante d'`enum` peut **transporter des données** ! Par exemple, un
message peut être un texte, ou un déplacement avec des coordonnées :

```rust
enum Message {
    Quitter,                       // ne transporte rien
    Ecrire(String),                // transporte un texte
    Deplacer { x: i32, y: i32 },   // transporte deux nombres nommés
}
```

---

## 4. `match` : réagir selon le cas (le `switch` surpuissant)

Pour **agir différemment selon la variante**, on utilise **`match`**. Il compare une valeur
à des **motifs** (*patterns*) et exécute la branche qui correspond.

🔀 **Analogie : un aiguillage de train.** Selon la valeur, le train part sur **une** voie
précise.

```rust
let etat = Feu::Rouge;

match etat {
    Feu::Rouge  => println!("Stop !"),
    Feu::Orange => println!("Ralentis..."),
    Feu::Vert   => println!("Passe !"),
}
```

> 🛡️ **Sécurité Rust :** un `match` doit couvrir **TOUS** les cas. Si tu oublies une
> variante, le compilateur **refuse de compiler**. Impossible d'oublier un cas par accident !
> (Pour dire « tous les autres cas », on utilise le motif `_`, le joker.)

Et quand la variante **transporte** des données, `match` les **extrait** pour toi :

```rust
match msg {
    Message::Quitter            => println!("Au revoir."),
    Message::Ecrire(texte)      => println!("Message : {}", texte),     // on récupère le texte
    Message::Deplacer { x, y }  => println!("Aller en ({}, {})", x, y), // on récupère x et y
}
```

---

## 5. `Option<T>` : l'absence de valeur, SANS le `null` dangereux

Dans beaucoup de langages, quand une valeur peut « manquer », on utilise `null` / `None` /
`nil`. Et c'est **la source n°1 de plantages** (oublier de tester avant d'utiliser).

Rust supprime ce piège : il **n'y a pas de `null`**. À la place, un type spécial,
**`Option<T>`**, qui dit explicitement « il y a peut-être une valeur de type `T`, ou peut-être
pas ». C'est en réalité un `enum` tout simple :

```rust
enum Option<T> {   // (déjà fourni par Rust, tu n'as pas à le définir)
    Some(T),       // "Il y a quelque chose" + la valeur
    None,          // "Il n'y a rien"
}
```

🎁 **Analogie : une boîte cadeau.** Soit elle contient quelque chose (`Some(valeur)`), soit
elle est **vide** (`None`). Avant de t'en servir, tu **dois ouvrir la boîte** pour vérifier.

```rust
let trouve: Option<i32> = Some(42);
let rien: Option<i32> = None;

// Le compilateur t'OBLIGE à gérer les DEUX cas (avec match) avant d'utiliser la valeur :
match trouve {
    Some(n) => println!("Trouvé : {}", n),
    None    => println!("Rien du tout"),
}
```

C'est pour ça qu'en Rust on ne « plante » pas sur une valeur absente : le compilateur t'a
forcé à prévoir le cas « vide ». On approfondira la gestion d'erreurs au module 05.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `enums_match.rs`

Pour suivre `enums_match.rs` sans te perdre, voici l'ordre des idées :

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. enum SIMPLE   : Feu { Rouge, Orange, Vert }                │
   │                    + match pour réagir à chaque variante       │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. enum AVEC DONNÉES : Message { Ecrire(String), Deplacer{} } │
   │                    + match qui EXTRAIT les données portées     │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. Option<T>     : Some(valeur) ou None                       │
   │                    + match qui force à gérer le cas "vide"     │
   ├──────────────────────────────────────────────────────────────┤
   │ 4. cas concret   : une fonction qui CHERCHE et renvoie         │
   │                    Option<...> (trouvé / pas trouvé)           │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
# Les structures : définir un modèle, créer des instances, ajouter des méthodes
rustc --edition 2021 rust/03_structs_enums/structs.rs -o /tmp/r && /tmp/r

# Les enums, le match, et Option<T>
rustc --edition 2021 rust/03_structs_enums/enums_match.rs -o /tmp/r && /tmp/r
```

Lis les deux fichiers (tout est commenté), puis **expérimente** : ajoute un champ à la
`struct`, ajoute une variante à un `enum` et observe que le compilateur **t'oblige** à
compléter le `match`. Tu verras à quel point Rust t'empêche d'oublier un cas.

➡️ Module suivant : [`04_collections`](../04_collections/).
