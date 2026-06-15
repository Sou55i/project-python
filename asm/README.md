# 🛠️ Apprendre l'ASSEMBLEUR — pour grands débutants

L'**assembleur** est le langage le plus **proche du processeur** qui soit encore lisible par
un humain. Là où Python te cache tout, l'assembleur te met **les mains directement dans la
machine** : tu manipules toi-même les petites « cases » de calcul du processeur et tu
demandes des services au système d'exploitation.

> ⚠️ **Avertissement honnête** : c'est le parcours **le plus technique** du dépôt. C'est
> normal de trouver ça déroutant au début. Avance **lentement**, ligne par ligne. Le but
> n'est pas de devenir expert, mais de **comprendre ce qui se passe vraiment** sous Python
> et sous le C.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**.

---

## 🆚 En quoi c'est différent des autres langages ?

- En **Python**, tu écris `print("Bonjour")` et c'est fini : l'ordinateur fait des
  centaines de choses **pour toi** sans rien te montrer.
- En **C**, tu es déjà plus proche de la machine, mais le compilateur écrit encore beaucoup
  de détails à ta place.
- En **assembleur**, **tu écris toi-même** les ordres élémentaires que le processeur exécute.
  Une ligne d'assembleur = (presque) **une seule instruction du processeur**.

Conséquence : il faut **plus de lignes** pour faire la même chose, mais tu vois **tout**.

---

## 🧠 Le vocabulaire minimal (à lire absolument)

### Un **registre**
Une **case ultra-rapide** située **à l'intérieur du processeur**. Le processeur ne sait
calculer qu'avec ces cases (il ne calcule pas « directement » dans la mémoire). Sur un PC
moderne (architecture **x86-64**), on en utilise souvent quatre dans nos exemples :

| Registre | On s'en sert (dans ce parcours) pour… |
|----------|----------------------------------------|
| `rax` | numéro de l'appel système, et résultats de calculs |
| `rdi` | 1er argument d'un appel système |
| `rsi` | 2e argument d'un appel système |
| `rdx` | 3e argument d'un appel système |

> 🔎 Il en existe d'autres (`rbx`, `rcx`, `r8`…), mais ces quatre suffisent pour démarrer.

### Une **instruction**
Un **ordre élémentaire** donné au processeur. Quelques-unes que tu vas rencontrer :

| Instruction | Ce qu'elle fait (en mots simples) |
|-------------|------------------------------------|
| `mov`  | **met** une valeur dans un registre (copie) |
| `add`  | **additionne** une valeur à un registre |
| `sub`  | **soustrait** une valeur d'un registre |
| `cmp`  | **compare** deux valeurs (sans rien changer) |
| `jmp`  | **saute** vers une étiquette (toujours) |
| `syscall` | **demande un service au système** Linux |

### Un **appel système** (`syscall`)
L'assembleur seul ne sait **pas** afficher du texte à l'écran. Pour ça, il faut **demander
au système d'exploitation** (Linux) de le faire. Cette demande s'appelle un **appel système**.
On choisit le service en mettant son **numéro** dans `rax`, puis on déclenche avec `syscall` :

| Service | Numéro (dans `rax`) | Rôle |
|---------|---------------------|------|
| `write` | **1**  | écrire (afficher) du texte |
| `exit`  | **60** | quitter le programme |

### **Assembler** ≠ **compiler**
- *Compiler* (C, Python…) : traduire un langage de **haut niveau** vers le langage machine,
  ce qui demande beaucoup de travail au traducteur.
- *Assembler* : ta source est **déjà** quasiment du langage machine. L'outil `as` fait une
  traduction presque **mot à mot**. C'est pour ça qu'on parle d'**assemblage** et pas de
  compilation.

---

## ⚙️ Les outils (déjà présents sous Linux)

On utilise deux outils du paquet GNU Binutils :

- **`as`** : l'**assembleur**. Il transforme ton fichier `.s` en un fichier objet `.o`.
- **`ld`** : l'**éditeur de liens**. Il transforme le `.o` en un **exécutable** lançable.

> ℹ️ On n'utilise **pas** `nasm` ici. Tous les exemples sont en syntaxe **Intel** grâce à la
> ligne `.intel_syntax noprefix` en haut de chaque fichier (plus lisible pour débuter).

## ▶️ Assembler, lier et lancer un programme

```bash
# 1. Assembler le .s en fichier objet .o
as asm/00_demarrer/hello.s -o /tmp/p.o

# 2. Lier le .o en un exécutable
ld /tmp/p.o -o /tmp/p

# 3. Lancer, et afficher le code de sortie
/tmp/p ; echo "code de sortie = $?"
```

En une seule ligne (pratique pour tout enchaîner) :

```bash
as asm/00_demarrer/hello.s -o /tmp/p.o && ld /tmp/p.o -o /tmp/p && /tmp/p ; echo "code de sortie = $?"
```

> 💡 **`echo $?`** affiche le **code de sortie** du dernier programme : le nombre que le
> programme a renvoyé en quittant (par convention, `0` = tout s'est bien passé). On va s'en
> servir pour « voir » le résultat de nos calculs dans le module 01.

---

## 📚 Le parcours

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Squelette d'un programme, sections, afficher via `write`, quitter via `exit` |
| 1 | [`01_les_bases`](./01_les_bases/) | Registres, `mov`, `add`/`sub`, `cmp`, sauts (`jmp`/`jl`/`jne`), labels, code de sortie |
| 2 | [`02_pile_fonctions`](./02_pile_fonctions/) | La pile (`push`/`pop`, `rsp`), fonctions/sous-programmes (`call`/`ret`), passer un argument et récupérer un résultat |
| 3 | [`03_memoire_donnees`](./03_memoire_donnees/) | Sections `.data`/`.bss`, déclarer des données (`.byte`/`.word`/`.quad`/`.ascii`), adressage `[ ]` et `lea`, parcourir un tableau |
| 4 | [`04_entrees_sorties`](./04_entrees_sorties/) | Syscalls `read`/`write`, afficher un nombre (conversion par divisions), écho clavier |
| 5 | [`05_chaines`](./05_chaines/) | Chaînes = suites d'octets ASCII, parcours avec un pointeur (`inc`), fin par octet 0 ou longueur connue, mise en MAJUSCULES (−32) |
| 6 | [`06_interfacage_c`](./06_interfacage_c/) | Écrire une FONCTION asm appelée depuis le C, convention System V AMD64 (`rdi`/`rsi` → `rax`), `.global` sans `_start`, lier avec `gcc main.c somme.s -o prog` |
| 7 | [`07_debugger`](./07_debugger/) | Déboguer l'asm avec **gdb** : assembler avec `-g`, `break`/`run`/`stepi`, `info registers` pour « voir » les registres pas à pas, examiner la mémoire (`x/…`), pièges fréquents (`div`, syscalls, segfault) |

> ✅ **Parcours complet** : fondations (00→07), modules avancés (08–09), projets et module
> sécurité (voir plus bas).

## 🚀 Modules avancés

Une fois les **fondations** acquises, ces modules vont plus loin en combinant plusieurs
notions à la fois. Toujours la même pédagogie : on explique d'abord, on code ensuite.

| Module | Ce que tu apprends |
|--------|--------------------|
| [`08_recursion`](./08_recursion/) | La **récursion** (une fonction qui s'appelle elle-même) et le rôle crucial de la **pile** : sauvegarder (`push`) / restaurer (`pop`) ses valeurs autour de l'appel récursif. Exemple : `factorielle(5) = 120` |
| [`09_operations_bits`](./09_operations_bits/) | Les **opérations bit à bit** et les **masques** : un nombre vu comme une suite de **bits** (0/1), `and` (masque), `or` (allumer), `xor` (inverser/comparer), `not`, et les décalages `shl`/`shr` (multiplier/diviser par 2). Exemple : `12 AND 10`, puis `OR`/`XOR`/`SHL` → `20` |

## 🛠️ Mini-projets

Une fois les modules digérés, passe au dossier [`projets/`](./projets/) : des **programmes
complets** qui combinent plusieurs modules à la fois (boucle + conversion de nombres +
affichage de chaînes). C'est là qu'on relie enfin toutes les briques apprises.

| Projet | Ce qu'il fait | Modules combinés |
|--------|---------------|------------------|
| [`projets/table_multiplication.s`](./projets/table_multiplication.s) | Affiche la table de multiplication d'un nombre (`7 x 1 = 7` ... `7 x 10 = 70`) | 01/02, 04, 05 |

## 📎 Ressources

- [`ANATOMIE_D_UN_PROGRAMME.md`](./ANATOMIE_D_UN_PROGRAMME.md) — dans quel ordre écrire un programme : le squelette standard (sections, `_start`, exit), le cycle assembler/lier/lancer, et comment lire un programme asm.
- [`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md) — l'essentiel en une page (outils, registres, instructions, syscalls, squelette).
- [`GLOSSAIRE.md`](./GLOSSAIRE.md) — les termes clés expliqués simplement.

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).

## 🔐 Module sécurité (pentest)

Pour découvrir le rôle de ce langage en **sécurité informatique** — à usage
**strictement éducatif et autorisé** (tes propres systèmes, CTF, labs) — voir le
dossier [`pentest/`](./pentest/).
