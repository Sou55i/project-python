# Module 00 — Démarrer en assembleur : le squelette d'un programme

Avant d'écrire des calculs, comprenons **la forme** d'un programme en assembleur et
**comment afficher du texte** puis **quitter**. Ce module est surtout théorique, avec un
premier programme à assembler à la fin.

> Fichier du module : [`hello.s`](./hello.s) — tout est commenté ligne par ligne.

---

## 1. Un programme = deux « sections »

Un programme en assembleur est rangé en **sections** (des zones séparées) :

- **`.section .data`** : les **données** qui ne bougent pas, comme notre **texte** à
  afficher. C'est un peu le « garde-manger » du programme.
- **`.section .text`** : le **code**, c'est-à-dire les **instructions** que le processeur
  va exécuter, une par une.

```
   .data   →  les données (ex : le texte "Bonjour")
   .text   →  les instructions (le déroulé du programme)
```

---

## 2. Le point de départ : `_start`

En C, tout commençait par la fonction `main`. En assembleur, **tout commence à l'étiquette
`_start`**. On doit la rendre **visible** pour l'éditeur de liens avec `.global _start` :

```asm
.global _start      # rend _start visible
_start:             # ici commence l'exécution
    ...
```

> 📌 Une **étiquette** (ou *label*) est juste un **nom posé sur un endroit** du programme,
> suivi de `:`. Ça permet de s'y référer (par son nom plutôt que par une adresse compliquée).

---

## 3. Afficher du texte : l'appel système `write`

L'assembleur ne sait pas afficher tout seul : il **demande à Linux** de le faire, via un
**appel système**. Pour `write`, Linux attend qu'on **prépare 4 registres**, puis qu'on
déclenche avec `syscall` :

| Registre | Valeur | Signification |
|----------|--------|---------------|
| `rax` | `1` | **quel** service : `1` = `write` (écrire) |
| `rdi` | `1` | **où** écrire : `1` = l'écran (sortie standard) |
| `rsi` | adresse du texte | **quoi** écrire : où commence le texte |
| `rdx` | longueur | **combien** d'octets écrire |

```asm
mov rax, 1            # service write
mov rdi, 1            # vers l'écran
lea rsi, [message]    # adresse du texte
mov rdx, 8            # nombre d'octets ("Bonjour\n" = 8)
syscall               # on demande à Linux d'exécuter
```

> 🔢 **Pourquoi 8 ?** On compte les **caractères** : `B o n j o u r` = 7, plus le retour à
> la ligne `\n` qui compte pour **1** seul caractère = **8** au total. Si tu changes le
> texte, **pense à ajuster ce nombre**.

> 🔎 `lea` (« charger l'adresse ») met dans `rsi` **l'endroit où se trouve** le texte, et non
> le texte lui-même. Le service `write` a besoin de savoir **où** lire en mémoire.

---

## 4. Quitter proprement : l'appel système `exit`

Un programme en assembleur **doit dire explicitement** qu'il s'arrête. Sinon, le processeur
continue sur ce qui suit en mémoire et… plante. On utilise l'appel système `exit` :

| Registre | Valeur | Signification |
|----------|--------|---------------|
| `rax` | `60` | service `exit` (quitter) |
| `rdi` | `0`  | le **code de sortie** (`0` = succès) |

```asm
mov rax, 60     # service exit
mov rdi, 0      # code de sortie = 0
syscall         # le programme s'arrête ici
```

---

## ▶️ À toi de jouer

Assemble, lie et lance le programme du module :

```bash
as asm/00_demarrer/hello.s -o /tmp/p.o && ld /tmp/p.o -o /tmp/p && /tmp/p ; echo "code de sortie = $?"
```

Tu dois voir s'afficher :

```
Bonjour
code de sortie = 0
```

Lis ensuite [`hello.s`](./hello.s) (tout est commenté), puis **change le texte** (par
exemple `"Salut\n"`), **ajuste le nombre d'octets** dans `rdx`, et **réassemble** pour voir
le changement.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
