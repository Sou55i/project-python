# Module 05 — Gérer les erreurs : `Result<T, E>`, `Option`, `?` et `panic!`

Un programme rencontre forcément des **situations qui peuvent échouer** : un fichier
introuvable, un texte qu'on n'arrive pas à convertir en nombre, une division par zéro… Les
langages classiques utilisent les *exceptions* (souvent invisibles, faciles à oublier). Rust,
fidèle à sa philosophie, rend l'échec **visible dans les types** : tu **vois** dans la
signature qu'une fonction peut échouer, et le compilateur t'**oblige** à t'en occuper.

> Fichier du module : `erreurs.rs` (Result, l'opérateur `?`, et `panic!`).
> On **compile** puis on **lance** (voir en bas).

> 🧠 Rappel : tu connais déjà `Option<T>` (module 03), qui gère l'**absence** de valeur
> (`Some`/`None`). Ici on ajoute `Result<T, E>`, qui gère l'**échec** (`Ok`/`Err`).

---

## 1. Deux familles de problèmes

Il y a deux situations bien différentes, et Rust leur donne deux outils :

| Situation | Question | Outil Rust |
|-----------|----------|------------|
| Une valeur **peut manquer** | « y a-t-il quelque chose ? » | **`Option<T>`** : `Some(v)` / `None` |
| Une opération **peut échouer** | « a-t-elle réussi, sinon pourquoi ? » | **`Result<T, E>`** : `Ok(v)` / `Err(e)` |

La différence : `Result` **explique pourquoi** ça a échoué (il transporte une erreur `E`),
alors que `Option` dit juste « vide ».

---

## 2. `Result<T, E>` : réussite ou échec (avec la raison)

✉️ **Analogie : une réponse à une demande.** Soit « OK, voilà le résultat » (`Ok(valeur)`),
soit « Échec, voici la raison » (`Err(message)`). C'est un `enum`, comme `Option` :

```rust
enum Result<T, E> {  // (déjà fourni par Rust)
    Ok(T),           // réussite + la valeur (de type T)
    Err(E),          // échec + l'erreur (de type E)
}
```

Exemple : convertir un texte en nombre peut échouer (« abc » n'est pas un nombre).

```rust
fn parser(texte: &str) -> Result<i32, String> {
    match texte.parse::<i32>() {            // .parse() renvoie déjà un Result
        Ok(n)  => Ok(n),                    // réussi : on renvoie le nombre
        Err(_) => Err(format!("'{}' n'est pas un nombre", texte)), // échec : on explique
    }
}
```

Et chez l'appelant, on **doit** gérer les deux cas (avec `match`) :

```rust
match parser("42") {
    Ok(n)  => println!("Nombre : {}", n),
    Err(e) => println!("Erreur : {}", e),
}
```

> 🛡️ Comme pour `Option`, le compilateur t'oblige à traiter le cas `Err`. **Impossible**
> d'oublier de gérer une erreur par mégarde — c'est ça, la sûreté de Rust.

---

## 3. L'opérateur `?` : propager l'erreur sans tout réécrire

Écrire un `match` à **chaque** appel qui peut échouer devient vite lourd, surtout quand on
enchaîne plusieurs opérations risquées. Rust offre un raccourci génial : l'opérateur **`?`**.

🔗 **Analogie : un toboggan d'échec.** Mets un `?` après une opération qui renvoie un
`Result`. Si c'est `Ok`, le `?` **déballe** la valeur et on continue. Si c'est `Err`, le `?`
**arrête tout de suite** la fonction et **renvoie l'erreur** à l'appelant — sans que tu aies
à l'écrire.

```rust
// Cette fonction additionne deux textes-nombres. Si l'un échoue, '?' renvoie l'erreur.
fn additionner(a: &str, b: &str) -> Result<i32, std::num::ParseIntError> {
    let x = a.parse::<i32>()?; // si échec -> on sort et on renvoie l'Err
    let y = b.parse::<i32>()?; // idem
    Ok(x + y)                  // tout a réussi -> on renvoie la somme dans un Ok
}
```

Sans le `?`, il aurait fallu deux `match` imbriqués. Avec, le code reste **droit et lisible**.

> 💡 Le `?` ne s'utilise que dans une fonction qui **renvoie elle-même** un `Result` (ou un
> `Option`) — logique : il faut bien que l'erreur ait où aller. C'est pourquoi même `main`
> peut renvoyer un `Result` (tu le verras dans le fichier).

---

## 4. `panic!` : l'arrêt brutal (à réserver aux cas désespérés)

Parfois, l'erreur est si grave qu'il vaut mieux **tout arrêter immédiatement**. C'est le rôle
de **`panic!`** : il stoppe le programme avec un message.

💥 **Analogie : l'arrêt d'urgence.** On l'utilise quand continuer n'aurait aucun sens (un bug
de programmation, une condition qui « ne devrait jamais arriver »).

```rust
fn racine_obligatoire(x: f64) -> f64 {
    if x < 0.0 {
        panic!("Impossible : racine d'un nombre négatif ({})", x); // arrêt immédiat
    }
    x.sqrt()
}
```

> ⚠️ **Règle de bon sens :** pour les erreurs **attendues** (fichier absent, saisie
> invalide…), utilise **`Result`** (le programme gère et continue). Réserve **`panic!`** aux
> situations **vraiment** anormales. Un programme robuste « panique » le moins possible.
>
> 📌 Les méthodes `.unwrap()` et `.expect("...")` sur un `Option`/`Result` font en réalité un
> `panic!` si la valeur est `None`/`Err`. Pratiques pour des essais rapides, mais à éviter en
> vrai code : préfère `match` ou `?`.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `erreurs.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. Result simple : une fonction qui renvoie Ok(...) / Err(...)│
   │                    + match chez l'appelant (réussite/échec)    │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. Option rappel : .get sur une liste -> Some / None          │
   │                    (l'absence, vue au module 03)               │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. Opérateur ?   : enchaîner des opérations risquées,         │
   │                    l'erreur "remonte" toute seule              │
   ├──────────────────────────────────────────────────────────────┤
   │ 4. panic!        : l'arrêt brutal, montré de façon CONTRÔLÉE   │
   │                    (on ne déclenche que le cas qui réussit)    │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
# Result, Option, l'opérateur ?, et panic!
rustc --edition 2021 rust/05_erreurs/erreurs.rs -o /tmp/r && /tmp/r
```

Lis le fichier (tout est commenté), puis **expérimente** : passe un texte invalide (« abc »)
à la fonction qui utilise `?` et observe l'`Err` remonter ; remplace un `match` par un
`.unwrap()` sur un `Err` pour **voir** un vrai `panic!`. C'est en cassant les choses
(volontairement) qu'on comprend la gestion d'erreurs.

➡️ Tu as terminé les fondations du parcours Rust. Bravo ! La suite (modules, généricité,
traits, projets…) arrivera dans le même style.
