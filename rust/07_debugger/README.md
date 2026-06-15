# Module 07 — Débugger en Rust : le compilateur est ton meilleur ami

En Python, on découvre les bugs **en lançant** le programme (le fameux pavé rouge). En Rust,
c'est différent et formidable : le **compilateur** attrape énormément de bugs **avant même**
que le programme tourne, et il t'explique en français clair quoi corriger. Apprendre à
**lire ses messages** est la compétence qui te fera le plus progresser en Rust.

> Fichier du module : `demo_debug.rs` (un programme **correct** qui te montre les outils de
> débogage : `dbg!`, l'affichage `{:?}`, et la lecture d'un `Result`).

> 🧠 Rappel du module Python : « une erreur n'est pas un échec, c'est une explication ». En
> Rust c'est encore plus vrai, parce que le compilateur t'explique **avant** l'exécution.

---

## 1. `cargo check` (ou `rustc`) : vérifier sans tout exécuter

Avant de lancer quoi que ce soit, demande à Rust de **vérifier** ton code. Sur un vrai projet
Cargo, on tape :

```bash
cargo check     # vérifie que tout compile, SANS produire l'exécutable (donc rapide)
```

Dans ce parcours on utilise `rustc`, qui fait la même vérification en compilant le fichier :

```bash
rustc --edition 2021 mon_fichier.rs -o /tmp/r
```

Si Rust ne dit rien → le code compile. S'il y a un souci, il l'affiche **maintenant**, pas
au pire moment.

---

## 2. Lire un message d'erreur de Rust (ils sont exceptionnels)

Les messages de Rust sont parmi les plus pédagogiques de tous les langages. Exemple typique :

```
error[E0382]: borrow of moved value: `nom`
 --> src/main.rs:4:20
  |
2 |     let nom = String::from("Alice");
  |         --- move occurs because `nom` has type `String`...
3 |     let autre = nom;          // <- la valeur est DÉPLACÉE ici
  |                 --- value moved here
4 |     println!("{}", nom);      // <- on essaie de réutiliser nom...
  |                    ^^^ value borrowed here after move
  |
help: consider cloning the value
  |
3 |     let autre = nom.clone();
  |                    ++++++++
```

> 🔑 **Comment le lire :**
> - **La 1re ligne** donne le **code** (`E0382`) et le **résumé** du problème.
> - **Le `-->`** indique le **fichier et la ligne** fautive.
> - **Les flèches `^^^` et `---`** pointent **exactement** le code concerné.
> - **Le `help:`** propose souvent **la correction toute prête** (ici : `.clone()`).

Donc : *quoi* (1re ligne) → *où* (`-->` et flèches) → *comment corriger* (`help:`). Souvent,
tu n'as qu'à suivre le `help:`.

---

## 3. La macro `dbg!` : inspecter une valeur en plein vol

🔎 **Analogie : une loupe.** `dbg!(x)` **affiche** la valeur de `x` (avec le fichier et le
numéro de ligne) **et la renvoie** : tu peux donc la glisser **au milieu** d'un calcul sans
rien casser.

```rust
let a = 5;
let b = 3;
let somme = dbg!(a) + dbg!(b);   // affiche a, affiche b, puis additionne normalement
```

> 💡 `dbg!` écrit sur la **sortie d'erreur** (stderr), pas la sortie normale : c'est voulu,
> ça permet de séparer tes vrais affichages de tes traces de débogage.

Pour afficher une liste ou une struct **sans** `dbg!`, utilise `{:?}` (mode « debug ») dans un
`println!` : `println!("{:?}", ma_liste);`. Le `{}` simple, lui, ne marche que pour les
valeurs « affichables pour l'humain ».

---

## 4. Les erreurs d'emprunt (*borrow*) : les plus fréquentes au début

Le système de **propriété** (module 02) fait que Rust refuse certains codes. Pas de panique :
les messages t'expliquent tout. Les trois cas les plus courants :

### « value borrowed here after move » (valeur déjà déplacée)
Tu as **donné** une valeur (`let autre = nom;`) puis tu essaies de la réutiliser.
➡️ Soit tu prêtes au lieu de donner (`&nom`), soit tu copies (`nom.clone()`).

### « cannot borrow `x` as mutable... » (emprunt mutable impossible)
Tu veux **modifier** une variable empruntée, mais elle n'est pas déclarée modifiable.
➡️ Ajoute `mut` à la déclaration (`let mut x = ...`) et emprunte en `&mut x`.

### « cannot borrow `x` as mutable because it is also borrowed as immutable »
Tu as un prêt **en lecture** ET un prêt **en écriture** en même temps : interdit (règle des
emprunts). ➡️ Termine d'utiliser le prêt en lecture **avant** de modifier la valeur.

> ⚠️ Ces erreurs sont **frustrantes au début**, mais elles attrapent de vrais bugs (données
> modifiées pendant qu'on les lit ailleurs) que d'autres langages laissent passer. Lis le
> message, suis le `help:`, et ça rentre vite.

---

## 5. `rust-gdb` : pour aller plus loin (info)

Pour un débogage « pas à pas » (poser des points d'arrêt, avancer ligne par ligne), Rust
fournit **`rust-gdb`** (une version de l'outil `gdb` adaptée à Rust) :

```bash
rustc -g mon_fichier.rs -o /tmp/r   # -g = ajoute les infos de débogage
rust-gdb /tmp/r                     # lance le débogueur
```

> 🧭 C'est un outil **avancé** : au début, `dbg!` et la lecture des messages suffisent
> largement à 95 % des situations. Garde `rust-gdb` dans un coin de ta tête pour plus tard.

---

## 6. La méthode pour débugger calmement

1. **Lis le message en entier**, surtout la 1re ligne (le quoi) et le `help:` (la solution).
2. **Suis le `-->` et les flèches** : Rust te montre la ligne ET la colonne exactes.
3. **Saupoudre des `dbg!`** sur les valeurs suspectes pour voir ce qu'elles contiennent.
4. **Corrige une erreur à la fois**, puis relance `cargo check` / `rustc`.
5. **Cherche le code d'erreur** (`E0382`…) sur Internet : Rust a une doc dédiée par code.

---

## ▶️ À toi de jouer

```bash
rustc --edition 2021 rust/07_debugger/demo_debug.rs -o /tmp/r && /tmp/r
```

Le programme est **correct** : il te montre `dbg!`, `{:?}` et la lecture d'un `Result`.
Ensuite, **provoque** une vraie erreur pour t'entraîner à lire les messages : remplace
`let autre = &nom;` par `let autre = nom;` puis réutilise `nom` — et savoure le message de
Rust. C'est en cassant (volontairement) qu'on apprend à réparer.

➡️ Prochaine étape : le module 08, les **closures et itérateurs**.
