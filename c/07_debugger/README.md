# Module 07 — Débugger : trouver et corriger les bugs en C

En C, un bug n'affiche pas toujours un joli message : un programme peut **planter d'un coup**
(le fameux *Segmentation fault*) ou, pire, **donner un faux résultat sans rien dire**. Bonne
nouvelle : tu as deux super-pouvoirs. D'abord le **compilateur**, qui te prévient AVANT que ça
tourne si tu le lui demandes. Ensuite **gdb**, un outil qui met ton programme **au ralenti**
pour regarder ce qui se passe à l'intérieur. Ce module est surtout théorique, avec un petit
programme à explorer.

> Fichier du module : `demo_gdb.c` (un programme **correct** mais instructif, pensé pour être
> parcouru pas à pas sous gdb).

---

## 1. Compiler en mode « débogage » : `-g` et `-Wall`

Deux options à ajouter à `gcc`. Elles ne changent rien à ton code, juste à la façon de compiler.

- **`-Wall`** = *Warnings all* → **active les avertissements**. Le compilateur te signale les
  trucs louches (variable jamais utilisée, oubli probable…). **À TOUJOURS lire** : un warning
  est très souvent un bug qui sommeille. Vise **zéro warning**.
- **`-g`** = ajoute les **infos de débogage** (noms de variables, numéros de ligne) dans
  l'exécutable. Sans `-g`, gdb fonctionne quand même, mais « à l'aveugle » : il ne pourra pas
  te montrer tes lignes de code ni le nom de tes variables.

```bash
gcc -g -Wall demo_gdb.c -o demo
```

> 🔑 **À retenir :** pendant l'apprentissage, compile **toujours** avec `-g -Wall`. Lis chaque
> avertissement avant même de lancer le programme.

---

## 2. Les erreurs FRÉQUENTES en C (cause → solution)

| Erreur | Cause (ce qui s'est passé) | Solution |
|--------|-----------------------------|----------|
| **Segmentation fault** | Accès à une zone mémoire **interdite**, souvent en **déréférençant un pointeur `NULL`** (`*p` alors que `p` ne pointe sur rien). | Vérifie qu'un pointeur n'est pas `NULL` **avant** de faire `*p` ou `p->...`. Lance gdb et tape `bt` : il te montre la ligne du crash. |
| **Variable non initialisée** | Tu lis une variable avant de lui avoir donné une valeur → elle contient du **« n'importe quoi »** (un résidu de la mémoire). Résultats différents à chaque exécution. | **Initialise** dès la déclaration : `int total = 0;`. `-Wall` t'avertit souvent. |
| **Dépassement de tableau** | Index **hors limites** : `t[5]` alors que le tableau a 5 cases (indices **0 à 4**). Tu lis/écris à côté → crash ou corruption silencieuse. | Souviens-toi : un tableau de taille `n` va de l'indice `0` à `n-1`. Garde la taille dans une variable et compare. |
| **Oubli du `&` dans `scanf`** | `scanf("%d", x)` au lieu de `scanf("%d", &x)`. `scanf` a besoin de l'**adresse** où ranger la valeur ; sans `&`, il écrit n'importe où → Segmentation fault. | Mets **toujours** `&` devant la variable : `scanf("%d", &x);` (sauf pour une chaîne `char[]`, qui est déjà une adresse). |
| **Fuite mémoire** | Un `malloc(...)` **sans `free(...)`** correspondant : la mémoire réservée n'est jamais rendue. Le programme grossit jusqu'à manquer de mémoire. | Pour **chaque** `malloc`, prévois un `free`. Vérifie avec **`valgrind`** (voir plus bas). |

> 💡 Beaucoup de ces bugs ne font **pas** planter tout de suite : le programme tourne mais ment.
> D'où l'intérêt des outils ci-dessous.

---

## 3. L'essentiel de gdb (le « ralenti » de ton programme)

**gdb** (*GNU Debugger*) lance ton programme et te laisse l'arrêter, avancer pas à pas et
**regarder la valeur des variables** à tout moment. Le strict nécessaire :

```bash
gcc -g prog.c -o prog    # 1. compiler AVEC -g (sinon gdb est aveugle)
gdb ./prog               # 2. ouvrir le programme dans gdb (invite "(gdb)")
```

Une fois l'invite `(gdb)` affichée, les commandes à connaître :

| Commande | Abrégé | Ce qu'elle fait |
|----------|--------|-----------------|
| `run` | `r` | **Lance** le programme. S'il plante, gdb s'arrête pile à l'endroit du crash. |
| `backtrace` | `bt` | Affiche **la pile des appels** : « on a planté dans telle fonction, appelée par telle autre… ». **Le réflexe n°1 après un crash** pour voir OÙ ça a planté. |
| `break <ligne>` | `b` | Pose un **point d'arrêt** (*breakpoint*) : `break 21` ou `break somme`. Le programme s'arrêtera là tout seul. |
| `next` | `n` | Exécute **la ligne suivante** (sans entrer dans les fonctions appelées). |
| `step` | `s` | Comme `next`, mais **ENTRE dans la fonction** appelée pour la suivre de l'intérieur. |
| `print <variable>` | `p` | **Affiche la valeur** d'une variable : `print total`, `print notes[2]`. |
| `continue` | `c` | **Repart** jusqu'au prochain point d'arrêt (ou la fin). |
| `quit` | `q` | **Quitte** gdb. |

> 🧠 Mémo : `bt` répond à **« où ça a planté ? »**, `print` répond à **« que vaut cette
> variable ? »**, `break` + `next`/`step` servent à **avancer au ralenti**.

---

## 4. `valgrind` : le détecteur de problèmes mémoire

gdb sert à **suivre** le programme ; **`valgrind`** sert à **traquer les bugs mémoire** : fuites
(`malloc` sans `free`), lectures de mémoire non initialisée, dépassements de tableau. On le
lance simplement devant le programme (toujours compilé avec `-g`) :

```bash
valgrind ./prog
```

Il liste les erreurs avec leur ligne, et un bilan « *All heap blocks were freed* » si tout va
bien. Indispensable dès que tu utilises `malloc`/`free`.

---

## 5. Exemple de session gdb sur `demo_gdb.c`

On va explorer le programme du module **sans qu'il plante** (il est correct), juste pour voir
comment on inspecte. Ce qu'on tape est précédé de `(gdb)`.

```bash
gcc -g -Wall demo_gdb.c -o demo   # compiler avec les infos de débogage
gdb ./demo                         # ouvrir gdb
```

```text
(gdb) break somme            ← on s'arrête à l'entrée de la fonction somme()
Breakpoint 1 at 0x...: file demo_gdb.c, line 20.

(gdb) run                    ← on lance ; gdb s'arrête au breakpoint
Breakpoint 1, somme (notes=0x..., n=5) at demo_gdb.c:20
20          int total = 0;

(gdb) print n                ← combien de notes ? on inspecte le paramètre
$1 = 5

(gdb) print notes[0]         ← la première note du tableau
$2 = 12

(gdb) next                   ← on exécute la ligne courante (total = 0)
21          for (int i = 0; i < n; i++) {

(gdb) next                   ← on entre dans la boucle (i = 0)
22              total = total + notes[i];

(gdb) print i                ← où en est le compteur de boucle ?
$3 = 0

(gdb) next                   ← on additionne notes[0] dans total
21          for (int i = 0; i < n; i++) {

(gdb) print total            ← total vaut maintenant 12 (la 1re note)
$4 = 12

(gdb) continue               ← on repart jusqu'à la fin
Continuing.
Nombre de notes : 5
Total des notes : 62
Moyenne         : 12.40
[Inferior 1 (process ...) exited normally]

(gdb) quit                   ← on quitte gdb
```

On a vu, **en direct**, le tableau (`notes[0] = 12`), le compteur de boucle (`i`) et le cumul
(`total`) grandir pas à pas. C'est exactement comme ça qu'on coince un bug : on s'arrête juste
avant l'endroit suspect et on **regarde si les valeurs sont bien celles qu'on attend**.

> 💡 Astuce : si le programme **plante**, ne pose même pas de breakpoint. Tape juste `run`,
> laisse-le crasher, puis `bt` : gdb t'indique la fonction et la ligne exactes du plantage.

---

## ▶️ À toi de jouer

```bash
# Compiler AVEC les infos de débogage, puis vérifier qu'il tourne (DEPUIS LA RACINE) :
gcc -g -Wall c/07_debugger/demo_gdb.c -o demo && ./demo
```

Tu dois voir le nombre de notes, le total et la moyenne. Ensuite, **explore-le sous gdb** en
rejouant la session ci-dessus : pose un `break somme`, fais `run`, puis `print notes[0]`,
`print total`, `next`, `step`… N'aie pas peur, tu ne casses rien : gdb ne fait que **regarder**.
Pour t'entraîner à un vrai bug, essaie aussi : remplace `int total = 0;` par `int total;` (non
initialisée) et recompile avec `-Wall` pour voir l'avertissement.

➡️ La suite du parcours (projets plus complets…) arrivera dans le même style.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
