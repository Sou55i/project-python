# Module 06 — Les `trait` (interfaces) et les génériques `<T>`

Jusqu'ici, chaque fonction travaillait sur **un** type précis. Mais souvent, on veut écrire
du code qui marche pour **plusieurs** types à la fois : afficher aussi bien un chien qu'une
voiture, trouver le plus grand de deux nombres **ou** de deux mots… Rust offre deux outils
complémentaires pour ça : les **traits** (des *contrats* que des types s'engagent à respecter)
et les **génériques** (du code « à trous » qui s'adapte au type qu'on lui donne).

> Fichiers du module : `traits.rs` (les contrats) et `generics.rs` (le `<T>`).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

> 🧠 Rappel : tu utilises déjà des génériques sans le savoir ! `Vec<T>` (une liste de T) et
> `Option<T>` (un T peut-être présent) sont génériques : le `<T>` se remplit selon le contenu.

---

## 1. Un `trait` : un contrat que des types respectent

🤝 **Analogie : un permis de conduire.** Le permis ne dit pas QUELLE voiture tu conduis ; il
garantit juste que **tu sais conduire**. Un `trait`, c'est pareil : il liste des capacités
(« savoir se décrire »), et tout type qui les fournit « a le permis ».

On **définit** le contrat (la promesse, sans le code) :

```rust
trait Decrire {
    fn decrire(&self) -> String;   // tout type "Decrire" DOIT fournir cette méthode
}
```

Puis chaque type explique **comment** il respecte le contrat, avec `impl ... for ...` :

```rust
struct Chien { nom: String }

impl Decrire for Chien {
    fn decrire(&self) -> String {
        format!("un chien nomme {}", self.nom)
    }
}
```

> 💡 `&self` veut dire « moi-même » : c'est l'objet sur lequel on appelle la méthode
> (`medor.decrire()` → à l'intérieur, `self` est `medor`).

---

## 2. Une méthode **par défaut** dans le trait

Un trait peut fournir une méthode **toute faite**, que les types récupèrent gratuitement (ils
peuvent la garder ou la remplacer). Pratique pour éviter de réécrire la même chose partout :

```rust
trait Decrire {
    fn decrire(&self) -> String;

    fn presentation(&self) -> String {       // méthode par défaut
        format!("Voici : {}", self.decrire())  // réutilise decrire()
    }
}
```

Un `Chien` qui ne redéfinit pas `presentation()` utilisera **automatiquement** cette version.

---

## 3. Une fonction qui accepte « n'importe quel type qui respecte le contrat »

C'est là que les traits brillent. `&impl Decrire` se lit : « une référence vers **n'importe
quel** type qui respecte `Decrire` ». Une **seule** fonction marche alors pour tous ces types :

```rust
fn afficher(item: &impl Decrire) {       // accepte un Chien, une Voiture...
    println!("{}", item.presentation());
}
```

---

## 4. Les génériques `<T>` : écrire le code une fois, pour plusieurs types

🧩 **Analogie : un moule à gâteaux.** Le même moule fait un gâteau au chocolat **ou** à la
vanille selon la pâte que tu verses. Le `<T>` est ce moule : Rust « verse » le vrai type
(i32, f64, String…) au moment où tu appelles la fonction.

```rust
// '<T: PartialOrd>' = "pour un type T, à condition qu'on puisse le COMPARER".
fn plus_grand<T: PartialOrd>(a: T, b: T) -> T {
    if a > b { a } else { b }
}
```

Le même `plus_grand` marche pour `(3, 9)`, `(2.5, 1.1)` **et** `("abricot", "banane")` !

> 🔒 La partie `: PartialOrd` est une **contrainte** (un *trait bound*) : « T est autorisé,
> **à condition** de respecter le trait `PartialOrd` (savoir se comparer) ». Sans elle, Rust
> refuserait le `>` : il ne saurait pas comparer un type inconnu. Traits et génériques
> travaillent donc main dans la main.

Une **struct** aussi peut être générique :

```rust
struct Paire<T> {          // deux valeurs DU MÊME type T
    premier: T,
    second: T,
}
```

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `traits.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. Un contrat 'Decrire' + deux types (Chien, Voiture)         │
   │    chacun fournit SA version de decrire()                      │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. Une fonction 'afficher' qui accepte les DEUX types         │
   │    (grâce à &impl Decrire)                                     │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. La méthode par défaut 'presentation' du trait,             │
   │    utilisée telle quelle par Chien                             │
   └──────────────────────────────────────────────────────────────┘
```

## 🗺️ CHEMINEMENT DU PROGRAMME — `generics.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. La fonction générique plus_grand<T> testée sur des         │
   │    entiers, des flottants ET du texte                          │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. La struct générique Paire<T> : une paire d'entiers,        │
   │    puis une paire de textes (même struct, types différents)    │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
# Les traits (contrats partagés par plusieurs types)
rustc --edition 2021 rust/06_traits_generics/traits.rs -o /tmp/r && /tmp/r

# Les génériques <T> (un code, plusieurs types)
rustc --edition 2021 rust/06_traits_generics/generics.rs -o /tmp/r && /tmp/r
```

Lis les fichiers (tout est commenté), puis **expérimente** : ajoute un troisième type (un
`Robot` ?) qui respecte `Decrire`, et passe-le à `afficher` — sans toucher à `afficher`.
C'est ça, la puissance des traits : du code ouvert à de nouveaux types.

➡️ Prochaine étape : le module 07, pour apprendre à **déboguer** en Rust.
