# Module 02 — La propriété (*ownership*) : LE cœur de Rust

Voici **la** notion qui rend Rust unique. Si tu ne devais comprendre qu'une seule chose dans
tout ce parcours, ce serait celle-ci : l'**ownership** (la « propriété » des données).

C'est elle qui permet à Rust d'être **rapide comme le C** tout en étant **sûr en mémoire**,
**sans garbage collector** (rappel du module 00). Au début ça surprend, mais une fois l'idée
attrapée, tout le reste devient logique. On y va doucement, avec des analogies.

> Fichiers du module : `propriete.rs` (le *move*, l'emprunt immuable `&`, l'emprunt mutable
> `&mut`) et `exemple_panier.rs` (un petit exemple complet et commenté).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Le problème que Rust veut résoudre

Quand un programme range une donnée en mémoire, il faut bien, un jour, **libérer** cette
place (sinon la mémoire se remplit — la « fuite » vue côté C avec `malloc`/`free`).

- En **C** : c'est **toi** qui libères (`free`). Si tu oublies → fuite. Si tu libères deux
  fois ou trop tôt → plantage. C'est puissant mais dangereux.
- En **Python/Java** : un **garbage collector** (programme en arrière-plan) nettoie pour toi.
  C'est confortable, mais ça **ralentit** et c'est **imprévisible**.
- En **Rust** : ni l'un ni l'autre ! Le compilateur applique des **règles de propriété**
  vérifiées **à la compilation**. La mémoire est libérée **automatiquement** au bon moment,
  **sans GC** et **sans risque**. Magique ? Non : juste 3 règles à comprendre.

---

## 2. Les 3 règles de la propriété

🏠 **Analogie : chaque donnée est une maison, et elle a UN seul propriétaire.**

1. **Chaque valeur a un propriétaire** (la variable qui la « possède »).
2. **Il ne peut y avoir qu'UN SEUL propriétaire à la fois.**
3. **Quand le propriétaire disparaît** (sort de son bloc `{ }`), la valeur est
   **automatiquement libérée** (Rust appelle ça « *drop* »).

```rust
{
    let s = String::from("bonjour"); // 's' devient propriétaire du texte
    // ... on utilise 's' ...
} // ICI 's' sort du bloc → Rust libère AUTOMATIQUEMENT la mémoire. Pas de 'free' à écrire !
```

> 💡 Tu n'écris jamais `free`. Le compilateur sait, **rien qu'en lisant ton code**, à quel
> moment chaque valeur n'est plus utilisée, et insère la libération pour toi.

---

## 3. Le *move* : donner la propriété (et non copier)

Regarde ce code, qui **surprend** quand on vient d'un autre langage :

```rust
let a = String::from("salut");
let b = a;          // on ne COPIE pas : on DONNE la propriété de 'a' à 'b'
println!("{}", a);  // ❌ ERREUR de compilation : 'a' ne possède plus rien !
```

🎁 **Analogie : offrir un cadeau.** Tu donnes ton livre à un ami. Maintenant **c'est lui qui
l'a** — tu ne peux plus dire « c'est mon livre ». La propriété a été **déplacée** (*moved*).

Pourquoi Rust fait ça ? Pour respecter la règle 2 (**un seul propriétaire**). Si `a` et `b`
possédaient tous les deux le même texte, au moment de libérer, on libérerait **deux fois** la
même mémoire → le bug classique du C. Rust l'empêche **par construction**.

> ⚠️ Attention, ça ne concerne que les types « avec un contenu en mémoire » comme `String`,
> `Vec`, etc. Les types **simples** (`i32`, `bool`, `char`, `f64`…) sont si petits qu'ils
> sont **copiés** (on appelle ça `Copy`). Là, pas de souci :
>
> ```rust
> let x = 5;
> let y = x;          // COPIE (i32 est minuscule)
> println!("{} {}", x, y); // ✅ x ET y sont valides
> ```

---

## 4. L'emprunt immuable `&` : prêter pour LIRE

Donner la propriété à chaque fois serait pénible (il faudrait toujours « rendre » la valeur).
La solution : **prêter** sans donner. On appelle ça **emprunter** (*borrow*), et on l'écrit
avec **`&`**.

📖 **Analogie : prêter ton livre.** Ton ami peut **lire** ton livre, mais il reste **à toi**.
Quand il a fini, il te le rend, et tu peux continuer à t'en servir.

```rust
fn longueur(texte: &String) -> usize { // '&String' = on EMPRUNTE, on ne possède pas
    texte.len()                         // on peut LIRE...
}

let mot = String::from("bonjour");
let n = longueur(&mot);     // on PRÊTE 'mot' (note le '&')
println!("{} fait {} lettres", mot, n); // ✅ 'mot' est encore à nous : on peut l'utiliser !
```

Comme on a juste **prêté** (`&mot`), la propriété **n'a pas bougé** : après l'appel, `mot`
est toujours valide. C'est le cas le plus courant en Rust.

---

## 5. L'emprunt mutable `&mut` : prêter pour MODIFIER

Et si on veut que la fonction **modifie** la valeur empruntée ? On prête « en écriture » avec
**`&mut`** (et la variable d'origine doit être `mut`).

✏️ **Analogie : prêter ton cahier pour qu'on y écrive.** Tu confies ton cahier, on ajoute une
ligne dedans, puis on te le rend modifié.

```rust
fn ajouter_point(texte: &mut String) { // '&mut' = emprunt MODIFIABLE
    texte.push('!');                    // on modifie le texte de l'appelant
}

let mut phrase = String::from("salut"); // 'mut' obligatoire
ajouter_point(&mut phrase);             // on prête EN ÉCRITURE (note '&mut')
println!("{}", phrase);                 // "salut!"  -> modifié !
```

C'est l'équivalent **sûr** du pointeur du C qui permet à une fonction de modifier l'original.

---

## 6. La règle d'or des emprunts (l'anti-bug ultime)

Rust impose **une** règle simple sur les emprunts, vérifiée à la compilation :

> 🛡️ À un instant donné, on peut avoir **SOIT** plusieurs emprunts **immuables** (`&`, pour
> lire à plusieurs), **SOIT** UN SEUL emprunt **mutable** (`&mut`, pour modifier). **Jamais
> les deux en même temps.**

🚧 **Analogie : un document partagé.** Beaucoup de gens peuvent **lire** le même document en
même temps, sans problème. Mais si **quelqu'un écrit** dedans, il faut qu'il soit **seul** —
sinon les autres liraient un texte en train de changer (incohérent).

```rust
let mut v = String::from("hej");
let r1 = &v;          // emprunt immuable : OK
let r2 = &v;          // un autre emprunt immuable : OK aussi (lecture à plusieurs)
println!("{} {}", r1, r2);

let m = &mut v;       // emprunt MUTABLE : OK car r1/r2 ne servent plus
m.push('!');
println!("{}", m);
```

Cette règle élimine **à la compilation** toute une famille de bugs (les « accès concurrents »)
qui hantent les autres langages. Tu n'as rien à faire : le compilateur veille.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `propriete.rs`

Voici dans quel ordre `propriete.rs` déroule les idées, pour que tu suives sans te perdre :

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. MOVE      : let b = a;  → 'a' n'est plus utilisable         │
   │                (la propriété est DÉPLACÉE vers 'b')            │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. COPY      : les types simples (i32...) sont COPIÉS,         │
   │                pas déplacés → l'original reste valide          │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. EMPRUNT & : fn longueur(&String)  → on PRÊTE pour LIRE,     │
   │                la variable reste à nous après l'appel          │
   ├──────────────────────────────────────────────────────────────┤
   │ 4. EMPRUNT &mut : fn ajouter(&mut String) → on prête pour      │
   │                MODIFIER l'original                             │
   ├──────────────────────────────────────────────────────────────┤
   │ 5. RÈGLE D'OR : plusieurs '&' OU un seul '&mut', jamais les    │
   │                deux à la fois                                  │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
# Les 3 mécanismes : move, emprunt immuable &, emprunt mutable &mut
rustc --edition 2021 rust/02_propriete/propriete.rs -o /tmp/r && /tmp/r

# Un petit exemple complet et commenté : un panier de courses
rustc --edition 2021 rust/02_propriete/exemple_panier.rs -o /tmp/r && /tmp/r
```

Lis les deux fichiers (tout est commenté), puis **expérimente** : dans `propriete.rs`,
enlève les commentaires des lignes marquées `// ❌` pour **provoquer une erreur** et **lire
le message du compilateur** — il explique très bien le problème ! C'est la meilleure façon de
comprendre l'ownership : se faire « gronder » gentiment par `rustc`.

➡️ Module suivant : [`03_structs_enums`](../03_structs_enums/).
