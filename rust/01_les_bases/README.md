# Module 01 — Les bases de Rust : variables, types, conditions, boucles, fonctions

Maintenant que tu sais compiler et lancer, découvrons les **briques de base** du langage.
On explique ici, puis tu liras le code **commenté ligne par ligne** dans `bases.rs`.

---

## 1. Les variables : `let`, et **immuables par défaut** !

En Rust, on crée une variable avec **`let`** :

```rust
let age = 30;
```

⚠️ **La grande surprise** : par défaut, une variable est **immuable** (on ne peut PAS la
modifier après coup). C'est un choix de sécurité de Rust.

```rust
let age = 30;
age = 31;        // ❌ ERREUR de compilation : age est immuable !
```

Pour pouvoir la modifier, il faut explicitement ajouter **`mut`** (*mutable*) :

```rust
let mut age = 30;
age = 31;        // ✅ OK, age est mutable
```

> 💡 Pourquoi ? Parce que « ça ne change pas » est plus sûr et plus facile à comprendre.
> Tu n'autorises le changement que quand tu en as **vraiment** besoin.

---

## 2. Les types

Rust est **typé**, mais il **devine** souvent le type tout seul (*inférence*). Tu peux aussi
l'écrire explicitement après `:` (par ex. `let age: i32 = 30;`).

| Type | C'est quoi | Exemple |
|------|-----------|---------|
| `i32` | entier (32 bits) | `let n: i32 = -5;` |
| `f64` | nombre à virgule | `let prix: f64 = 1.99;` |
| `bool` | vrai/faux | `let ok: bool = true;` |
| `char` | UN caractère (apostrophes) | `let lettre: char = 'A';` |
| `&str` | texte **fixe** (emprunté) | `let nom: &str = "Alice";` |
| `String` | texte **modifiable** (possédé) | `let s = String::from("salut");` |

> 📌 `&str` vs `String` : retiens pour l'instant que `&str` est un texte « tel quel » (souvent
> écrit entre guillemets dans le code), et `String` est un texte qu'on peut **construire et
> agrandir**. On approfondira plus tard (c'est lié à l'*ownership*).

---

## 3. Les conditions : `if` / `else`

La condition s'écrit **sans parenthèses** (mais le bloc est entre `{ }`) :

```rust
if note >= 16 {
    println!("Tres bien");
} else if note >= 10 {
    println!("Recu");
} else {
    println!("A retravailler");
}
```

✨ **Particularité de Rust** : `if` est une **expression**, c'est-à-dire qu'il **renvoie une
valeur**. On peut donc s'en servir directement dans un `let` :

```rust
let message = if reussi { "gagné" } else { "perdu" };
```

---

## 4. Les boucles : `loop`, `while`, `for ... in`

Rust a **trois** sortes de boucles :

```rust
loop {                 // boucle INFINIE ; on en sort avec 'break'
    break;
}

while compteur < 3 {   // tant que la condition est vraie
    compteur += 1;
}

for i in 0..3 {        // pour chaque i dans la plage 0,1,2 (le 3 est EXCLU)
    println!("{}", i);
}
```

> 💡 `0..3` est une **plage** (*range*) : elle va de 0 **jusqu'à 3 exclu**. Pour inclure 3,
> on écrit `0..=3`.

---

## 5. Les fonctions : `fn` et le type de retour `->`

On définit une fonction avec **`fn`**. Le type de chaque paramètre s'écrit après `:`, et le
type **renvoyé** après une **flèche `->`** :

```rust
fn additionner(a: i32, b: i32) -> i32 {
    a + b        // PAS de point-virgule : la dernière expression est la valeur renvoyée
}
```

> ✨ Astuce Rust : une ligne **sans point-virgule** à la fin d'une fonction est la **valeur
> renvoyée**. On peut aussi écrire `return a + b;` (avec `;`), les deux marchent.

---

## ▶️ À toi de jouer

1. Lis et lance le tour d'horizon des bases :

```bash
rustc rust/01_les_bases/bases.rs -o bases && ./bases
```

2. Puis le mini-projet, une vraie petite calculatrice interactive :

```bash
rustc rust/01_les_bases/mini_calculatrice.rs -o calc && ./calc
```

(Tu peux aussi lui « souffler » la saisie d'un coup pour tester :
`printf "+\n7\n5\n" | ./calc`.)

➡️ Module précédent : [`00_demarrer`](../00_demarrer/).
