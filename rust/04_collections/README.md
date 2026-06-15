# Module 04 — Les collections : `Vec<T>`, `String`, `HashMap`

Jusqu'ici, une variable = une valeur. Mais souvent on veut **regrouper plusieurs valeurs** :
une liste de courses, une phrase (suite de lettres), un annuaire (nom → numéro)… Ce sont les
**collections**. Rust en fournit trois incontournables : **`Vec<T>`** (la liste),
**`String`** (le texte modifiable) et **`HashMap`** (l'annuaire clé → valeur).

> Fichier du module : `collections.rs` (les trois collections, l'une après l'autre).
> On **compile** puis on **lance** (voir en bas).

> 🧠 Rappel du module 02 : ces collections **possèdent** leurs données. Quand tu parcours une
> collection avec `for`, pense à **emprunter** (`&`) si tu veux la réutiliser après.

---

## 1. `Vec<T>` : une liste qui peut grandir

📚 **Analogie : une étagère extensible.** Tu y ranges des livres **dans l'ordre**, tu peux en
**ajouter** au bout, en **enlever**, et accéder à celui de la position *n*.

Le `<T>` veut dire « un `Vec` **de** quelque chose » : `Vec<i32>` (liste d'entiers),
`Vec<String>` (liste de textes)… `T` est le **type des éléments**.

```rust
let mut nombres: Vec<i32> = Vec::new(); // une liste vide d'entiers ('mut' pour la remplir)
nombres.push(10);   // ajoute 10 au bout
nombres.push(20);
nombres.push(30);

println!("{}", nombres[0]);   // 10  -> accès par INDICE (on compte à partir de 0)
println!("{}", nombres.len()); // 3   -> le nombre d'éléments
```

> 💡 Raccourci pratique : la macro `vec![]` crée et remplit en une fois :
> `let v = vec![10, 20, 30];`

Pour parcourir tous les éléments, on utilise `for` (en empruntant avec `&` pour ne pas
« consommer » la liste) :

```rust
for n in &nombres {
    println!("{}", n);
}
```

> ⚠️ Accéder à `nombres[99]` (indice qui n'existe pas) fait **planter** le programme. Pour un
> accès **sûr**, on utilise `.get(99)` qui renvoie un `Option` (`Some(valeur)` ou `None`) —
> exactement le `Option<T>` du module 03 !

---

## 2. `String` : du texte qu'on peut modifier

Tu connais déjà `&str` (un texte **fixe**, écrit en dur : `"bonjour"`). La **`String`**, elle,
est un texte **possédé et modifiable** : on peut y ajouter, le construire petit à petit.

✍️ **Analogie : un cahier (String) vs une affiche imprimée (&str).** Sur le cahier tu écris,
tu ajoutes des lignes ; l'affiche, elle, est figée.

```rust
let mut texte = String::from("Bonjour"); // String modifiable (note le 'mut')
texte.push_str(", monde");  // ajoute un bout de texte
texte.push('!');            // ajoute UN caractère
println!("{}", texte);      // "Bonjour, monde!"

println!("{}", texte.len());     // longueur en octets
println!("{}", texte.to_uppercase()); // "BONJOUR, MONDE!"
```

> 💡 En pratique : `&str` quand le texte ne change pas (paramètres de fonction, constantes),
> et `String` quand tu dois **construire** ou **modifier** un texte.

---

## 3. `HashMap` : associer une clé à une valeur (l'annuaire)

🗂️ **Analogie : un annuaire / dictionnaire.** Au lieu de retrouver une valeur par sa
**position** (comme dans un `Vec`), tu la retrouves par une **clé** : un *nom* → un *numéro*,
un *produit* → un *prix*…

`HashMap` n'est pas chargé par défaut : il faut l'**importer** en haut du fichier avec
`use std::collections::HashMap;`.

```rust
use std::collections::HashMap;

let mut scores: HashMap<String, i32> = HashMap::new(); // clé = String, valeur = i32
scores.insert(String::from("Alice"), 90); // associe "Alice" -> 90
scores.insert(String::from("Bob"), 75);

// Récupérer une valeur par sa clé : .get() renvoie un Option (la clé existe... ou pas).
match scores.get("Alice") {
    Some(score) => println!("Alice : {}", score),
    None => println!("Alice : inconnue"),
}
```

Là encore, `.get()` renvoie un **`Option`** : la clé peut **ne pas exister**. Rust t'oblige à
prévoir ce cas → pas de plantage surprise. On parcourt un `HashMap` avec `for (cle, valeur)` :

```rust
for (nom, score) in &scores {
    println!("{} a {} points", nom, score);
}
```

> ⚠️ L'ordre de parcours d'un `HashMap` n'est **pas garanti** (ce n'est pas une liste
> ordonnée). On l'utilise pour la **recherche rapide par clé**, pas pour l'ordre.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `collections.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. Vec<T>    : créer, push, accès par indice, .len(),         │
   │                parcours avec for, accès SÛR avec .get()        │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. String    : créer, push_str / push, .len(),                │
   │                .to_uppercase()                                 │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. HashMap   : import 'use', insert (clé -> valeur),          │
   │                .get() qui renvoie un Option, parcours          │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
# Les trois collections : Vec, String, HashMap
rustc --edition 2021 rust/04_collections/collections.rs -o /tmp/r && /tmp/r
```

Lis le fichier (tout est commenté), puis **expérimente** : ajoute des éléments à la liste,
construis ton propre texte avec `push_str`, crée un mini-annuaire `nom → ville`. Essaie
`.get()` sur une clé qui n'existe pas pour voir le `None` (le `Option` du module 03 revient !).

➡️ Module suivant : [`05_erreurs`](../05_erreurs/).
