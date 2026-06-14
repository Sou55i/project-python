# Module 02 — Tableaux & chaînes de caractères

Jusqu'ici, chaque variable retenait **une seule** valeur. Mais comment ranger **plusieurs**
notes, plusieurs noms, ou un mot entier ? C'est le rôle des **tableaux** (et les chaînes de
caractères ne sont qu'un cas particulier de tableau).

> Fichiers du module : `tableaux.c` (les tableaux de nombres) et `chaines.c` (le texte).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Un tableau, c'est une rangée de boîtes du même type

En Python tu avais les *listes* (`[10, 20, 30]`). En C, l'équivalent le plus simple est le
**tableau** : une suite de cases **du même type**, rangées **côte à côte** en mémoire.

🧊 **Analogie : une boîte d'œufs.** Un tableau, c'est une boîte avec un nombre **fixe**
d'alvéoles. Chaque alvéole contient une valeur, et on les repère par leur **numéro de place**.

```c
int notes[5];   // un tableau de 5 entiers (5 cases, encore vides)
```

On peut aussi le remplir tout de suite :

```c
int notes[5] = {12, 8, 15, 10, 18};   // 5 cases, déjà remplies
```

⚠️ La **taille est fixe** : `int notes[5]` aura **toujours** 5 cases. Contrairement aux
listes Python, on ne peut pas faire `.append()` pour l'agrandir. La taille fait partie du
type.

---

## 2. On accède aux cases par leur INDICE — et on compte à partir de 0

Chaque case a un **indice** (son numéro de place). ⚠️ Comme en Python, **on compte à partir
de 0** : la 1ʳᵉ case est `notes[0]`, la 2ᵉ est `notes[1]`…

```c
int notes[5] = {12, 8, 15, 10, 18};

printf("%d\n", notes[0]);   // 12  (la PREMIÈRE case)
printf("%d\n", notes[4]);   // 18  (la CINQUIÈME et DERNIÈRE case)

notes[1] = 9;               // on MODIFIE la 2ᵉ case (8 devient 9)
```

Donc pour un tableau de taille 5, les indices valides vont de **0 à 4**.

> 🧠 Astuce mémo : **le dernier indice = la taille moins 1.** Pour 5 cases → dernier indice = 4.

---

## 3. ⚠️ Le dépassement de tableau : le piège n°1 du C

Que se passe-t-il si tu écris `notes[5]` (ou `notes[10]`) alors que le tableau n'a que 5
cases (indices 0 à 4) ? **Le C ne te prévient pas.** Il n'y a aucun garde-fou : tu lis ou
écris **en dehors** de la boîte, dans une zone mémoire qui ne t'appartient pas.

Résultat : valeurs farfelues, plantage (`Segmentation fault`), ou bug aléatoire difficile à
trouver. C'est l'une des grosses différences avec Python (qui, lui, lève une erreur claire
`IndexError`).

> 🛡️ **Règle d'or :** c'est à TOI de rester dans les bornes `0` à `taille - 1`. Toujours.

---

## 4. Parcourir un tableau avec une boucle `for`

Comme la taille est connue, le `for` est l'outil parfait : on fait varier l'indice `i` de
`0` jusqu'à `taille - 1`.

```c
int notes[5] = {12, 8, 15, 10, 18};

for (int i = 0; i < 5; i++) {     // i va de 0 à 4 (i < 5 s'arrête à 4)
    printf("notes[%d] = %d\n", i, notes[i]);
}
```

📌 Remarque le `i < 5` (et **pas** `i <= 5`) : il garantit qu'on s'arrête à l'indice 4 et
qu'on ne **dépasse** pas. C'est le motif standard pour parcourir un tableau sans danger.

C'est exactement ce qu'on fait pour calculer une **somme** ou une **moyenne** : on parcourt,
on additionne au passage (voir `tableaux.c`).

---

## 5. Les chaînes de caractères : un tableau de `char` terminé par `'\0'`

Voici LA grande idée du C concernant le texte : **une chaîne de caractères n'est pas un type
à part**, c'est juste un **tableau de `char`** (de caractères).

```c
char mot[6] = {'S', 'a', 'l', 'u', 't', '\0'};
// ... ou, en plus simple, exactement la même chose :
char mot[] = "Salut";
```

🚂 **Analogie : un train de wagons.** Chaque wagon porte une lettre. Mais comment savoir où
le mot **se termine** ? Le C ajoute un **wagon spécial de fin** : le caractère `'\0'`
(prononcé « antislash zéro »), aussi appelé **caractère nul** ou **terminateur**.

```
  'S'   'a'   'l'   'u'   't'   '\0'
 [ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ]   ← le '\0' marque la FIN
```

> ⚠️ C'est pour ça que `"Salut"` (5 lettres) a besoin de **6 cases** : 5 pour les lettres
> + 1 pour le `'\0'`. N'oublie jamais cette case en plus quand tu dimensionnes un tableau.

Pour afficher une chaîne entière, on utilise `%s` (vu au module 01) :

```c
char nom[] = "Alice";
printf("Bonjour %s\n", nom);   // %s s'arrête tout seul au '\0'
```

---

## 6. La boîte à outils des chaînes : `<string.h>`

Manipuler des chaînes « à la main » (case par case) est possible, mais fastidieux. La
bibliothèque standard `<string.h>` fournit des fonctions toutes prêtes. Il faut l'inclure :

```c
#include <string.h>
```

| Fonction | Ce qu'elle fait | Exemple |
|----------|-----------------|---------|
| `strlen(s)` | **longueur** : compte les lettres (sans le `'\0'`) | `strlen("Salut")` → `5` |
| `strcpy(dest, src)` | **copie** la chaîne `src` dans `dest` | `strcpy(copie, nom);` |
| `strcmp(a, b)` | **compare** deux chaînes ; renvoie `0` si elles sont **identiques** | `strcmp("oui", "oui")` → `0` |

> ⚠️ Piège fréquent : on **ne compare pas** deux chaînes avec `==` en C ! `==` comparerait
> des adresses mémoire, pas le texte. Pour comparer le **contenu**, c'est `strcmp` (et
> « égales » correspond au résultat `0`).

> 💡 `strcpy` ne crée pas la place : la chaîne de destination doit déjà être un tableau
> **assez grand** pour accueillir la copie (lettres **+** le `'\0'`).

---

## ▶️ À toi de jouer

```bash
# Les tableaux de nombres (somme et moyenne)
gcc -Wall c/02_tableaux_chaines/tableaux.c -o tableaux && ./tableaux

# Les chaînes de caractères (longueur, comparaison, copie, parcours)
gcc -Wall c/02_tableaux_chaines/chaines.c -o chaines && ./chaines
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : change les valeurs du
tableau, ajoute une note, compare d'autres mots, écris ta propre chaîne lettre par lettre.

➡️ La suite du parcours (pointeurs & mémoire, fichiers…) arrivera dans le même style.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
