# 🐹 Apprendre le Go (Golang) — pour grands débutants

Le **Go** (souvent appelé *Golang*) est un langage **moderne**, créé chez Google. Il est
volontairement **simple** (peu de mots-clés à retenir), **rapide à compiler**, et excellent
pour écrire des **outils en ligne de commande**, des **serveurs** et tout ce qui touche à
l'**automatisation**. Beaucoup d'outils que tu utilises peut-être déjà (Docker, Kubernetes…)
sont écrits en Go.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, lance, modifie.

---

## 🆚 Différences avec Python

Si tu viens de Python, voici les deux grandes nouveautés :

- **Python est *interprété*** : tu lances `script.py` directement.
- **Go est *compilé*** : ton code est d'abord **traduit en langage machine**. Bonne nouvelle :
  avec `go run`, cette traduction se fait **automatiquement** juste avant de lancer (tu ne vois
  presque pas la différence).
- **Python a un typage *dynamique*** (`x = 5`) : le type peut changer.
- **Go a un typage *statique*** : chaque variable a un **type fixé** (un entier, du texte…).
  Bonne nouvelle encore : Go peut souvent **deviner le type tout seul** (avec `:=`).

| | Python | Go |
|--|--------|----|
| Exécution | interprété | **compilé** (mais `go run` le cache) |
| Types | dynamiques (`x = 5`) | **statiques** (mais souvent devinés avec `:=`) |
| Blocs | indentation | des **accolades `{ }`** |
| Fin d'instruction | retour à la ligne | retour à la ligne (Go ajoute le `;` tout seul) |

---

## 🆚 Différences avec le C

Si tu connais déjà notre parcours C, Go va te sembler **plus doux** :

| | C | Go |
|--|---|----|
| Mémoire | **souvent manuelle** (pointeurs, à la main) | **automatique** (un *ramasse-miettes* / *garbage collector* nettoie tout seul) |
| Syntaxe | beaucoup de détails | **plus simple** |
| Point-virgule `;` | obligatoire à chaque ligne | **invisible** (Go l'ajoute automatiquement) |
| Compiler + lancer | deux étapes (`gcc` puis `./prog`) | **une seule** commande : `go run` |

En clair : Go garde l'esprit du C (rapide, compilé) mais **enlève la plupart des corvées**.

---

## ▶️ Deux façons de lancer un programme Go

### 1. `go run` — compiler ET exécuter d'un coup (le plus simple)

C'est ce qu'on utilisera tout le temps au début. Go **compile en mémoire** puis **lance**
immédiatement, sans créer de fichier exécutable à garder :

```bash
go run go/00_demarrer/premier_programme.go
```

### 2. `go build` — fabriquer un exécutable à garder

Quand ton programme est prêt à être distribué, `go build` crée un **vrai fichier exécutable**
(que tu peux relancer sans Go installé) :

```bash
go build go/00_demarrer/premier_programme.go   # crée le fichier "premier_programme"
./premier_programme                            # on le lance
```

> 💡 Pour apprendre, **`go run` suffit largement.** On utilise `go build` plus tard, pour livrer.

---

## 📚 Le parcours (fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Lancer un programme Go, structure minimale, `fmt.Println` |
| 1 | [`01_les_bases`](./01_les_bases/) | Types, variables, `fmt.Printf`, conditions, boucle `for`, fonctions |
| 2 | [`02_collections`](./02_collections/) | Slices (listes dynamiques, `append`, `range`), maps (dictionnaires), package `strings` |
| 3 | [`03_structs_methodes`](./03_structs_methodes/) | Structs (regrouper des champs), méthodes, récepteur valeur vs pointeur `*T` |
| 4 | [`04_erreurs_interfaces`](./04_erreurs_interfaces/) | Gestion des erreurs (`error`, `if err != nil`), interfaces (contrats de comportement) |
| 5 | [`05_fichiers`](./05_fichiers/) | Lire & écrire des fichiers (`os.WriteFile`, `os.ReadFile`, `os.Open` + `bufio.Scanner`) |
| 6 | [`06_concurrence`](./06_concurrence/) | Concurrence : goroutines (`go`), synchronisation (`sync.WaitGroup`), channels (`chan`) |
| 7 | [`07_debugger`](./07_debugger/) | Débugger : lire une stack trace, bugs fréquents, `panic`/`recover`, `go vet`, `delve` |

### 🚀 Modules avancés

Une fois les fondations solides, va plus loin :

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 8 | [`08_generics`](./08_generics/) | Les génériques : écrire UNE fonction pour plusieurs types (`[T any]`), les contraintes (`any`, `comparable`, contrainte perso `~int \| ~float64`) |
| 9 | [`09_concurrence_avancee`](./09_concurrence_avancee/) | Concurrence avancée : `select` (attendre plusieurs channels, timeout), pool de *workers* |

> 💡 Comme pour les fondations : chaque fichier `.go` a son propre `package main` + `func main`
> dans le même dossier, et se lance **séparément** avec `go run go/08_generics/<fichier>.go`.

> ✅ **Parcours complet** : fondations (00→07), modules avancés (08–09), projet capstone et
> module sécurité (voir plus bas).

> 🛠️ **Prêt à assembler ?** Une fois les fondations digérées, passe au dossier
> [`projets/`](./projets/) : des mini-projets **capstone** qui COMBINENT plusieurs
> modules (structs + slices + fichiers + erreurs) pour fabriquer de vrais petits outils.

> 📎 **Ressources** (à garder sous la main) : l'[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md)
> (cheat-sheet de syntaxe), le [GLOSSAIRE.md](./GLOSSAIRE.md) (le sens des mots du Go) et
> l'[ANATOMIE_D_UN_PROGRAMME.md](./ANATOMIE_D_UN_PROGRAMME.md) (dans quel ordre ranger le
> code d'un fichier Go : `package`, imports, types, `func main()`…).

---

## ⚙️ Pré-requis : installer Go

Vérifie s'il est déjà là :

```bash
go version
```

Sinon, télécharge-le sur **<https://go.dev/dl/>** (Linux, macOS, Windows). L'installation
ajoute la commande `go` à ton terminal.

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).

## 🔐 Module sécurité (pentest)

Pour découvrir le rôle de ce langage en **sécurité informatique** — à usage
**strictement éducatif et autorisé** (tes propres systèmes, CTF, labs) — voir le
dossier [`pentest/`](./pentest/).
