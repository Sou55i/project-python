# Module 09 — La concurrence : threads, channels et `Arc<Mutex<>>`

Jusqu'ici, ton programme faisait **une** chose à la fois, de haut en bas. La **concurrence**,
c'est faire **plusieurs** choses **en même temps** : pendant qu'un calcul tourne, un autre
avance aussi. Rust est célèbre pour ça : il rend la concurrence **sûre**, en refusant à la
compilation les bugs classiques (deux threads qui modifient la même donnée n'importe comment).

> Fichier du module : `threads.rs` (threads, channels `mpsc`, puis `Arc<Mutex<>>`).
> La sortie est rendue **déterministe** (toujours la même) pour faciliter l'apprentissage.
> On **compile** puis on **lance** (voir en bas).

> ⚠️ En vrai, l'ordre d'exécution des threads est **imprévisible**. Dans ce module, on
> **attend** chaque thread et on agrège proprement, pour que le résultat soit reproductible.

---

## 1. Un thread : un fil d'exécution parallèle

🧵 **Analogie : plusieurs cuisiniers.** Au lieu d'un seul cuisinier qui fait tout dans
l'ordre, plusieurs travaillent **en même temps**. Chaque cuisinier est un **thread**.

On lance un thread avec `thread::spawn` et une closure (le travail à faire) :

```rust
use std::thread;

let poignee = thread::spawn(move || {   // 'move' = la closure PREND ses variables
    42                                   // le thread calcule et renvoie 42
});

let resultat = poignee.join().unwrap(); // .join() ATTEND la fin et récupère la valeur
```

> 🔑 `.join()` est essentiel : sans lui, `main` pourrait se terminer **avant** les threads.
> En attendant les threads dans un ordre choisi, on rend la sortie déterministe.

---

## 2. Les channels (`mpsc`) : s'envoyer des messages

📮 **Analogie : une boîte aux lettres.** Un thread **dépose** des messages, un autre les
**relève**. C'est plus sûr que de partager une variable : chacun garde le sien, on ne fait que
se **transmettre** des valeurs.

`mpsc` = *multi producer, single consumer*. On crée une paire **émetteur / récepteur** :

```rust
use std::sync::mpsc;

let (tx, rx) = mpsc::channel();   // tx = émetteur, rx = récepteur

thread::spawn(move || {
    tx.send(1).unwrap();          // dépose un message dans le tuyau
});

let recu = rx.recv().unwrap();    // relève un message (attend qu'il arrive)
```

Quand l'émetteur `tx` est lâché (fin du thread), le tuyau se ferme et le récepteur sait que
c'est terminé — pratique pour collecter tous les messages avec `rx.iter().collect()`.

---

## 3. `Arc<Mutex<>>` : partager une donnée modifiable, en sécurité

Parfois, plusieurs threads doivent **modifier la même** donnée (un compteur partagé). Là,
deux protections se combinent :

- **`Arc`** (*Atomic Reference Counted*) : permet à plusieurs threads de **partager** la même
  donnée. On en fait une copie « légère » (un pointeur) avec `Arc::clone`.
- **`Mutex`** (*MUTual EXclusion*) : un **verrou**. Un seul thread à la fois peut « prendre le
  verrou » et modifier la donnée. Les autres **attendent** leur tour. Plus de bug de course !

🔐 **Analogie : une seule clé pour une pièce.** Pour entrer modifier la donnée, il faut la
clé. Tant que tu l'as, personne d'autre n'entre. Tu sors → tu rends la clé au suivant.

```rust
use std::sync::{Arc, Mutex};

let compteur = Arc::new(Mutex::new(0));        // donnée partagée, protégée par un verrou

let c = Arc::clone(&compteur);                 // chaque thread reçoit sa copie du pointeur
thread::spawn(move || {
    let mut valeur = c.lock().unwrap();        // PREND le verrou (les autres attendent)
    *valeur += 1;                              // modifie en sécurité
    // le verrou est rendu AUTOMATIQUEMENT à la fin du bloc
});
```

Cinq threads qui font `+1` chacun → le total vaut **toujours 5**, quel que soit leur ordre.

> 🛡️ Rust **vérifie à la compilation** que tu protèges bien les données partagées. Oublier le
> `Mutex` ou le `Arc` provoque une erreur claire — pas un bug mystérieux à l'exécution.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `threads.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. Threads : on en lance 3, on les ATTEND (join) dans l'ordre │
   │              -> chacun renvoie i*10 (sortie déterministe)      │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. Channel : un thread ENVOIE 1,2,3 ; on les RÉCOLTE en liste │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. Arc<Mutex<>> : 5 threads font +1 chacun sur un compteur     │
   │                   partagé -> total TOUJOURS égal à 5           │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
rustc --edition 2021 rust/09_concurrence/threads.rs -o /tmp/r && /tmp/r
```

Lis le fichier (tout est commenté), puis **expérimente** : passe la boucle du compteur de
`0..5` à `0..100` et vérifie que le total est toujours exact (essaie de retirer le `Mutex`
pour voir Rust **refuser** de compiler). C'est là qu'on mesure la sûreté de la concurrence
en Rust.

➡️ Prochaine étape : le **projet capstone** (`rust/projets/`), qui combine tout le parcours.
