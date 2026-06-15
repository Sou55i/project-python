# Projet capstone — Un gestionnaire de tâches en mémoire

Bravo : tu as parcouru les modules 00 à 09 ! Ce **projet de synthèse** (« capstone ») rassemble
les grandes notions du parcours dans **un seul** programme utile : un petit **gestionnaire de
tâches** (une mini *to-do list*) qui vit en mémoire. On y crée des tâches, on en termine
certaines, on gère proprement le cas « tâche introuvable », et on affiche un récapitulatif.

> Fichier du projet : `gestionnaire_taches.rs`.
> Le programme n'est **pas interactif** : il utilise des **données de démo**, agit dessus, et
> affiche le résultat. La sortie est donc **toujours la même**. On **compile** puis on **lance**.

---

## 1. Ce que le projet combine

| Notion | Module | Où dans le code |
|--------|--------|-----------------|
| `struct` (regrouper des données) | 03 | `struct Tache`, `struct Gestionnaire` |
| `enum` (un choix parmi des cas) | 03 | `enum Statut { AFaire, Terminee }` |
| `match` (réagir selon le cas) | 03 | choix de la coche `[ ]` / `[x]` |
| `Vec<T>` (une liste qui grandit) | 04 | `taches: Vec<Tache>` |
| `Result<T, E>` (signaler un échec) | 05 | `terminer()` renvoie `Ok` / `Err` |
| Itérateurs (`filter`, `count`) | 08 | `nombre_a_faire()` |
| Méthodes (`impl`) | 03 | toutes les méthodes du `Gestionnaire` |

C'est exactement comme ça qu'on construit un vrai programme : pas une notion isolée, mais
**plusieurs briques assemblées**.

---

## 2. L'idée de la conception

📋 **Analogie : un cahier de tâches.** Le `Gestionnaire` est le cahier ; chaque `Tache` est une
ligne (un numéro, un titre, une case à cocher). Le `Statut` est la case : soit vide (`AFaire`),
soit cochée (`Terminee`).

- **Ajouter** une tâche → on l'empile dans le `Vec` avec un nouvel identifiant.
- **Terminer** une tâche → on cherche son `id` ; si on la trouve, on coche ; sinon on renvoie
  une **erreur** (`Result`) que l'appelant **doit** gérer. Impossible d'oublier le cas d'échec :
  c'est la sûreté de Rust, vue au module 05.
- **Compter** ce qu'il reste → un itérateur `filter` + `count`, vu au module 08.

> 💡 `terminer()` renvoie `Result<(), String>`. Le `()` (« unité ») veut dire « en cas de
> succès, il n'y a rien d'intéressant à renvoyer, juste *ça a marché* ». L'info utile est dans
> le cas `Err`.

---

## 🗺️ CHEMINEMENT DU PROGRAMME — `gestionnaire_taches.rs`

```
   ┌──────────────────────────────────────────────────────────────┐
   │ 1. On crée un Gestionnaire vide                               │
   ├──────────────────────────────────────────────────────────────┤
   │ 2. On AJOUTE 3 tâches de démo (toutes "à faire")             │
   │    -> affichage de l'état initial                             │
   ├──────────────────────────────────────────────────────────────┤
   │ 3. On TERMINE les tâches #1 et #3 (Result -> Ok, géré au match)│
   ├──────────────────────────────────────────────────────────────┤
   │ 4. On tente de terminer #99 (inexistante)                     │
   │    -> Result -> Err, l'erreur est affichée proprement         │
   ├──────────────────────────────────────────────────────────────┤
   │ 5. Affichage final + statistique (nombre de tâches restantes) │
   └──────────────────────────────────────────────────────────────┘
```

---

## ▶️ À toi de jouer

```bash
rustc --edition 2021 rust/projets/gestionnaire_taches.rs -o /tmp/r && /tmp/r
```

Lis le fichier (tout est commenté), puis **fais-le grandir** — c'est ton projet maintenant :
- ajoute une méthode `supprimer(id)` qui retire une tâche (et renvoie un `Result`) ;
- ajoute un statut `EnCours` à l'`enum` et adapte le `match` (le compilateur te **rappellera**
  les endroits à compléter — encore un cadeau de Rust) ;
- affiche le **pourcentage** de tâches terminées avec un itérateur.

➡️ Tu as bouclé le parcours Rust : des bases jusqu'à un vrai petit programme. Félicitations ! 🦀
