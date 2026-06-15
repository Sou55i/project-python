# Module 08 — Closures `|x| ...` et itérateurs (`map` / `filter` / `collect` / `sum`)

Tu sais déjà parcourir une liste avec une boucle `for`. Ce module t'apprend une façon
**plus courte et plus lisible** de transformer des listes : on **enchaîne** des opérations
(« garde les pairs », « double-les », « additionne »), chacune décrite par une mini-fonction
écrite sur place — une **closure**. C'est le style « pipeline » : la donnée traverse une
suite d'étapes.

> Fichier du module : `iterateurs.rs` (closures, puis `map`, `filter`, `sum`, et tout enchaîner).
> On **compile** puis on **lance** (voir en bas).

---

## 1. Une closure : une fonction-éclair sans nom

⚡ **Analogie : une note griffonnée.** Au lieu de créer une fonction complète avec un nom,
tu écris une **mini-fonction sur place**. Les `|...|` remplacent les parenthèses des
paramètres :

```rust
let doubler = |x: i32| x * 2;   // "prends x, renvoie x * 2"
println!("{}", doubler(5));     // affiche 10
```

Mieux : une closure peut **capturer** une variable de l'extérieur (l'utiliser sans qu'on la
lui passe en paramètre) :

```rust
let tva = 20;
let avec_tva = |prix: i32| prix + prix * tva / 100;   // 'tva' vient du dehors
println!("{}", avec_tva(100));                         // affiche 120
```

---

## 2. Un itérateur : parcourir, étape par étape

Un **itérateur** sait fournir les éléments d'une collection **un par un**. On le démarre avec
`.iter()`, puis on lui branche des opérations. Rien ne se calcule tant qu'on n'a pas
**récolté** le résultat à la fin (avec `.collect()`, `.sum()`, etc.).

🏭 **Analogie : un tapis roulant d'usine.** Les éléments défilent ; chaque machine au-dessus
du tapis fait une opération ; au bout, on ramasse le résultat dans un carton.

---

## 3. `map` : transformer **chaque** élément

`.map(|n| ...)` applique la closure à **tous** les éléments et produit de nouvelles valeurs.
`.collect()` les range dans une nouvelle liste :

```rust
let nombres = vec![1, 2, 3, 4, 5];
let carres: Vec<i32> = nombres.iter().map(|n| n * n).collect();  // [1, 4, 9, 16, 25]
```

> 💡 Le type `: Vec<i32>` avant le `=` aide `.collect()` à savoir **dans quoi** ranger.

---

## 4. `filter` : ne **garder** que certains éléments

`.filter(|n| ...)` garde l'élément seulement si la closure renvoie `true` :

```rust
let pairs: Vec<i32> = nombres.iter().filter(|n| *n % 2 == 0).cloned().collect(); // [2, 4]
```

> ℹ️ Le `*n` et le `.cloned()` viennent du fait qu'on manipule des **références** (`&`) vers
> les éléments. Au début, retiens juste la forme ; le « pourquoi » remonte au module 02
> (propriété et emprunts).

---

## 5. `sum` : tout **additionner**

`.sum()` additionne tous les éléments parcourus :

```rust
let total: i32 = nombres.iter().sum();   // 1+2+3+4+5 = 15
```

---

## 6. Tout enchaîner (la vraie force)

On peut **chaîner** les étapes : la donnée traverse `filter`, puis `map`, puis `sum`, en une
seule expression qui se lit presque comme une phrase :

```rust
let resultat: i32 = nombres
    .iter()                     // parcourir la liste
    .filter(|n| *n % 2 == 0)    // ne garder que les pairs : 2 et 4
    .map(|n| n * 10)            // les multiplier par 10 : 20 et 40
    .sum();                     // additionner : 60
```

> 🆚 Avec une boucle `for`, il faudrait une variable d'accumulation, un `if`, etc. Ici, chaque
> ligne dit **une** chose. À toi de juger : parfois le `for` reste plus clair, souvent le
> pipeline gagne. Avoir les deux dans ta boîte à outils, c'est l'idéal.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `iterateurs.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. Closures : |x| x*2, puis une closure qui CAPTURE 'tva'     │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. map    : transformer chaque nombre en son carré            │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. filter : ne garder que les nombres pairs                   │
   ├──────────────────────────────────────────────────────────────┤
   │ 4. sum    : additionner tous les nombres                     │
   ├──────────────────────────────────────────────────────────────┤
   │ 5. Tout enchaîner : filter -> map -> sum en une expression    │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
rustc --edition 2021 rust/08_closures_iterateurs/iterateurs.rs -o /tmp/r && /tmp/r
```

Lis le fichier (tout est commenté), puis **expérimente** : change la closure de `filter` pour
garder les nombres `> 2`, ou ajoute un `.map(|n| n + 1)` dans la chaîne et observe le total
changer. Joue avec l'ordre des étapes : le résultat dépend de l'enchaînement.

➡️ Prochaine étape : le module 09, la **concurrence** (faire tourner plusieurs choses à la fois).
