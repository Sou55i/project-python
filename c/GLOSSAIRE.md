# 📖 Glossaire — les mots du C expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours de C ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent avec
une mini-analogie.

---

**Argument** — La valeur concrète que tu donnes à une fonction quand tu l'appelles. Dans
`additionner(7, 5)`, `7` et `5` sont les arguments. (Côté définition, on parle de *paramètre*.)

**Bibliothèque standard** — La boîte à outils livrée avec le C. On y pioche des fonctions
toutes prêtes en incluant des fichiers d'en-tête : `<stdio.h>` (entrées/sorties),
`<string.h>` (chaînes), `<stdlib.h>`…

**Boucle** — Une instruction qui répète des actions : `for` (« pour chaque… ») ou `while`
(« tant que… »). En C, la condition est entre `( )` et le bloc entre `{ }`.

**Caractère** (`char`) — Un seul signe (lettre, chiffre, ponctuation), écrit entre apostrophes
simples : `'A'`, `'7'`, `' '`. Techniquement, c'est un tout petit nombre entier.

**Caractère nul** (`'\0'`) — Le caractère spécial, invisible, qui marque la **fin** d'une
chaîne de caractères. Sans lui, le C ne saurait pas où le texte s'arrête. (Voir *Chaîne*.)

**Chaîne de caractères** (*string*) — Du texte. En C, ce n'est pas un type à part : c'est un
**tableau de `char` terminé par `'\0'`**. `"Salut"` (5 lettres) occupe donc 6 cases.

**Commentaire** — Une note pour les humains, ignorée par le compilateur. Sur une ligne avec
`// ...`, ou sur plusieurs lignes entre `/* ... */`.

**Compilateur** — Le programme (`gcc`, `clang`) qui **traduit** ton code `.c` en langage
machine. C'est lui qui fabrique l'exécutable.

**Compilation** — L'étape de **traduction** du code source en exécutable. Spécificité du C
(en Python, il n'y a pas cette étape). Tant que ça ne compile pas, rien ne tourne.

**Condition** — Un test qui oriente le programme : `if`, `else if`, `else`. « Si… alors… ».

**double** — Un nombre à virgule, précis (le choix par défaut pour les décimaux) : `3.14`.

**Exécutable** — Le fichier produit par la compilation, que l'ordinateur peut lancer
directement (`./programme`). C'est la version « langage machine » de ton code.

**Fonction** — Un bloc de code nommé et réutilisable. On déclare son **type de retour** et
le **type de chaque paramètre**. Comme une recette qu'on peut refaire à volonté.

**`#include`** — La directive qui **inclut** une boîte à outils en haut du fichier, pour
pouvoir s'en servir : `#include <stdio.h>` donne accès à `printf`.

**Indice (index)** — La position d'une case dans un tableau. ⚠️ On compte **à partir de 0** :
`notes[0]` est la première case. Le dernier indice vaut **taille − 1**.

**int** — Un nombre entier (sans virgule) : `42`, `-7`, `0`.

**main** — La fonction de **départ** obligatoire : l'exécution du programme commence toujours
par `main`. Elle renvoie `0` quand tout s'est bien passé.

**Paramètre** — Le nom d'une entrée dans la *définition* d'une fonction :
`int additionner(int a, int b)` → `a` et `b` sont des paramètres. (La valeur fournie à
l'appel est l'*argument*.)

**Pointeur** — Une variable qui contient l'**adresse** d'une autre valeur en mémoire (« où
elle habite »), plutôt que la valeur elle-même. Notion centrale du C, vue plus tard. Le `&`
de `scanf("%d", &age)` donne justement l'adresse de `age`.

**printf** — La fonction qui **affiche** du texte à l'écran. Chaque `%...` (spécificateur)
y est remplacé par une variable donnée ensuite, dans l'ordre.

**Prototype** — L'annonce d'une fonction (sa signature suivie d'un `;`) placée en haut du
fichier : `int additionner(int a, int b);`. Elle permet de l'utiliser avant sa définition,
car le C exige qu'une fonction soit connue avant d'être appelée.

**scanf** — La fonction qui **lit** une saisie au clavier. On met un `&` devant la variable
qui recevra la valeur.

**Spécificateur de format** — Le code commençant par `%` dans `printf`/`scanf` qui indique le
**type** à afficher ou lire : `%d` (entier), `%f` (décimal), `%c` (caractère), `%s` (chaîne).

**strcmp** — Fonction de `<string.h>` qui **compare** deux chaînes. Renvoie `0` si elles sont
identiques. ⚠️ On n'utilise jamais `==` pour comparer des chaînes en C.

**strcpy** — Fonction de `<string.h>` qui **copie** une chaîne dans un tableau de
destination (qui doit être assez grand : lettres + `'\0'`).

**strlen** — Fonction de `<string.h>` qui donne la **longueur** d'une chaîne (le nombre de
lettres, sans compter le `'\0'`).

**Tableau** — Une rangée de cases **du même type**, de **taille fixe**, rangées côte à côte :
`int notes[5]`. On accède à chaque case par son indice : `notes[0]`, `notes[1]`…

**Type** — La nature d'une valeur, **déclarée** en C : `int`, `double`, `char`… Le type fixe
la place réservée en mémoire et la façon d'interpréter la valeur.

**Variable** — Une boîte étiquetée qui retient une valeur. En C, on **déclare son type** :
`int age = 30;`. Le `=` *range* la valeur de droite dans la boîte de gauche.

**void** — Le « rien » du C. `void` comme type de retour = la fonction ne renvoie rien ;
`main(void)` = la fonction ne prend aucun paramètre.

**`-Wall`** — Une option de `gcc` qui **active tous les avertissements** (*warnings*) utiles.
Compile toujours avec : ces messages t'évitent beaucoup de bugs.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi [AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md)
pour la syntaxe.
