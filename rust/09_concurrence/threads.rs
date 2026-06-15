/*
 * MODULE 09 - Concurrence : threads, channels, Arc<Mutex<>>
 * =========================================================
 * Un THREAD est un "fil d'exécution" qui tourne EN MÊME TEMPS que les autres.
 * Pour communiquer sans se marcher dessus, Rust offre :
 *   - les CHANNELS (mpsc)  : envoyer des messages d'un thread à un autre,
 *   - Arc<Mutex<...>>      : partager une donnée modifiable entre threads, en sécurité.
 *
 * NOTE : la sortie est rendue DÉTERMINISTE (on attend les threads et on trie),
 * pour que le résultat soit toujours le même à chaque exécution.
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/09_concurrence/threads.rs -o /tmp/r && /tmp/r
 */

use std::thread;                  // pour créer des threads
use std::sync::mpsc;              // mpsc = "multi producer, single consumer" (channel)
use std::sync::{Arc, Mutex};     // Arc = compteur de partage ; Mutex = verrou

fn main() {
    println!("=== 1. Lancer des threads et les ATTENDRE ===");
    // On garde les "poignées" (handles) pour pouvoir attendre la fin de chaque thread.
    let mut poignees = Vec::new();
    for i in 1..=3 {
        // thread::spawn lance la closure dans un nouveau thread. 'move' donne à la
        // closure la propriété des variables qu'elle utilise (ici i).
        let p = thread::spawn(move || {
            i * 10   // chaque thread calcule i * 10 et le renvoie
        });
        poignees.push(p);
    }
    // .join() ATTEND la fin du thread et récupère sa valeur. En les attendant
    // dans l'ordre 1,2,3, la sortie est toujours la même.
    for p in poignees {
        let resultat = p.join().unwrap();
        println!("un thread a calcule : {}", resultat);
    }

    println!();
    println!("=== 2. CHANNEL : envoyer des messages entre threads ===");
    // tx = émetteur (transmitter), rx = récepteur (receiver).
    let (tx, rx) = mpsc::channel();
    let envoyeur = thread::spawn(move || {
        for n in 1..=3 {
            tx.send(n).unwrap();   // envoie n dans le tuyau
        }
        // tx est "lâché" ici : le tuyau se ferme, le récepteur saura que c'est fini.
    });
    envoyeur.join().unwrap();      // on attend que tout soit envoyé
    // rx se comporte comme une liste de messages reçus, dans l'ordre d'envoi.
    let recus: Vec<i32> = rx.iter().collect();
    println!("messages recus : {:?}", recus);

    println!();
    println!("=== 3. Arc<Mutex<>> : compter ENSEMBLE sans se tromper ===");
    // Arc : permet à PLUSIEURS threads de partager la MÊME donnée (copie du pointeur).
    // Mutex : un VERROU. Un seul thread à la fois peut modifier la donnée -> pas de bug.
    let compteur = Arc::new(Mutex::new(0));
    let mut poignees = Vec::new();
    for _ in 0..5 {
        let compteur = Arc::clone(&compteur);   // on partage le pointeur (pas la donnée)
        let p = thread::spawn(move || {
            let mut valeur = compteur.lock().unwrap();  // on PREND le verrou
            *valeur += 1;                               // on incrémente en sécurité
            // le verrou est rendu automatiquement à la fin du bloc
        });
        poignees.push(p);
    }
    for p in poignees {
        p.join().unwrap();         // on attend les 5 threads
    }
    // Peu importe l'ordre des threads : le total est TOUJOURS 5.
    println!("compteur final (5 threads, +1 chacun) = {}", *compteur.lock().unwrap());
}
