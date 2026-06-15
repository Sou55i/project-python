# Module 00 — Démarrer en Rust : compiler et exécuter

Avant d'écrire du code, comprenons **ce qu'est Rust** et **ce qui se passe** quand on
programme avec. Ce module est surtout théorique, avec un premier programme à compiler à la
fin.

---

## 1. C'est quoi Rust ?

**Rust** est un langage moderne (créé chez Mozilla) qui vise un objectif rare : être à la
fois **rapide** et **sûr**.

- **Compilé** (comme le C) : ton code `.rs` est traduit en **langage machine** par le
  compilateur `rustc`. Le résultat est un **exécutable** ultra-rapide, proche de la machine.
- **Sûr en mémoire SANS « ramasse-miettes »** : la plupart des langages sûrs (Python, Java…)
  utilisent un **garbage collector** (un programme qui nettoie la mémoire en arrière-plan,
  ce qui ralentit). Rust, lui, n'en a pas. Il garantit la sécurité grâce à une idée
  géniale appelée l'**« ownership »** (la *propriété* des données), vérifiée **à la
  compilation**. Résultat : pas de plantage mémoire à l'exécution, et pas de ralentissement.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, compile, lance, modifie.

---

## 2. C'est quoi « compiler » ? (rappel)

L'ordinateur ne comprend pas directement le texte que tu écris (`println!(...)`). Il ne
comprend que le **langage machine** (des 0 et des 1). En Rust, comme en C, il faut donc une
étape de **traduction** appelée **compilation** :

```
   premier_programme.rs   ──[ rustc ]──►   premier   ──►   exécution
   (TON code, lisible)     compilateur      (machine)       (ça tourne)
```

> 📌 Conséquence importante : si ton code contient une faute, **le compilateur refuse de
> traduire** et t'affiche des erreurs (souvent très bien expliquées en Rust !). Rien ne
> s'exécute tant que ça ne compile pas. C'est normal et utile.

---

## 3. 🆚 Différences avec Python et avec le C

C'est la grande nouveauté si tu viens de Python, et la grande tranquillité si tu viens du C.

| | Python | C | **Rust** |
|--|--------|---|----------|
| Exécution | *interprété* | **compilé** | **compilé** |
| Types | dynamiques (`x = 5`) | statiques (`int x = 5;`) | **statiques** (souvent *devinés* : `let x = 5;`) |
| Mémoire | *garbage collector* | **manuelle** (pointeurs, `malloc`/`free`) | **automatique ET sûre** grâce à l'*ownership*, vérifiée à la compilation |
| Erreurs mémoire | rares (GC) | fréquentes (segfault, fuites…) | **empêchées dès la compilation** |
| Vitesse | lente | très rapide | **très rapide** (comme le C) |

En résumé :
- vs **Python** : Rust est **compilé** et **typé** (plus strict, mais plus rapide et plus sûr).
- vs **C** : Rust offre la **même vitesse**, mais la **sécurité mémoire est garantie par le
  compilateur** — fini les segfaults et les fuites mémoire silencieuses.

---

## 4. Installer Rust

L'outil officiel s'appelle **`rustup`** (il installe `rustc` le compilateur et `cargo` le
gestionnaire de projet).

- **Linux / macOS** : `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- **Windows** : télécharge `rustup-init.exe` depuis <https://rustup.rs>.

Vérifie l'installation :

```bash
rustc --version
cargo --version
```

---

## 5. Compiler et lancer

Deux manières de faire.

### a) Avec `rustc` (compilateur direct, pratique pour un seul fichier)

```bash
# Compiler : -o donne le NOM de l'exécutable à créer
rustc rust/00_demarrer/premier_programme.rs -o premier && ./premier
```

### b) Avec `cargo` (l'outil de projet, recommandé pour les vrais projets)

`cargo` crée un projet complet, gère les dépendances, compile et lance :

```bash
cargo new mon_projet   # crée un dossier prêt à l'emploi
cd mon_projet
cargo run              # compile PUIS lance, en une seule commande
```

> Dans ce parcours d'apprentissage, on utilise surtout `rustc` (un fichier = un programme),
> car c'est plus simple pour découvrir. `cargo` deviendra ton ami pour les vrais projets.

Le cycle de travail est donc : **écrire → compiler → (corriger les erreurs) → lancer**.

---

## 📚 Les modules (fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./) | Qu'est-ce que Rust, compiler/exécuter (`rustc`, `cargo`), `println!` |
| 1 | [`01_les_bases`](../01_les_bases/) | Variables (`let`/`let mut`), types, `if`/`else`, boucles (`loop`/`while`/`for`), fonctions |

---

## ▶️ À toi de jouer

Compile et lance le programme de ce module :

```bash
rustc rust/00_demarrer/premier_programme.rs -o premier && ./premier
```

Lis ensuite [`premier_programme.rs`](./premier_programme.rs) (tout est commenté), puis
**modifie le texte** et **recompile** pour voir le changement.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
