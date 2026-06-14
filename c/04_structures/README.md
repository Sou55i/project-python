# Module 04 — Les structures (`struct`)

Jusqu'ici, une variable contenait **une seule** information : un `int`, un `char`, une chaîne…
Mais dans la vraie vie, les informations vont souvent **ensemble**. Un contact, par exemple,
c'est un **nom** ET un **âge** ET un **numéro**… La **structure** (`struct`) sert exactement à
ça : **regrouper plusieurs informations liées sous un même type**. On y va doucement.

> Fichiers du module : `structures.c` (déclarer un `struct`, l'utiliser, le passer à une
> fonction) et `agenda.c` (un petit tableau de structures qu'on parcourt et affiche).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Le problème : des infos qui vont ensemble

Imagine que tu veuilles stocker une personne : son nom et son âge. Avec ce que tu connais, tu
ferais deux variables **séparées** :

```c
char nom[50] = "Alice";
int age = 30;
```

Ça marche pour **une** personne. Mais pour 3 personnes ? 100 ? Rien ne dit que `nom` et `age`
« vont ensemble ». On aimerait un **seul** objet « personne » qui contient les deux. C'est le
rôle de la **structure**.

---

## 2. La STRUCTURE : une fiche cartonnée avec plusieurs champs

🗂️ **Analogie : une fiche cartonnée.** Pense à une fiche de bibliothèque ou un carton
d'adhérent. Sur **une seule fiche**, il y a plusieurs cases pré-imprimées : « Nom : ___ »,
« Âge : ___ ». Chaque case s'appelle un **champ** (*field* en anglais). La fiche regroupe
tout ce qui concerne **une** personne au même endroit.

Une `struct`, c'est exactement ça : un **modèle de fiche** qui dit quels champs existent et de
quel type ils sont.

```c
struct Personne {     // on définit un MODELE de fiche appelé "Personne"
    char nom[50];     // un champ "nom"  (une chaine de caracteres)
    int  age;         // un champ "age"  (un entier)
};                    // ⚠️ ne pas oublier le point-virgule a la fin !
```

> ⚠️ Définir un `struct` ne crée **aucune** variable : on a juste dessiné le **modèle** de
> fiche. Tant qu'on n'a pas rempli de fiche, il n'y a rien dedans.

---

## 3. Créer une variable et accéder aux champs avec le point `.`

Maintenant qu'on a le modèle, on peut **créer une fiche** (une variable) et la **remplir**.
Pour atteindre un champ, on écrit le nom de la variable, un **point `.`**, puis le nom du champ.

```c
struct Personne p;          // on cree UNE fiche "p" (encore vide)

strcpy(p.nom, "Alice");     // on ECRIT dans le champ "nom"  (chaine -> strcpy)
p.age = 30;                 // on ECRIT dans le champ "age"

printf("%s a %d ans\n", p.nom, p.age);   // on LIT les champs : "Alice a 30 ans"
```

🗂️ **Reprends l'analogie :** `p` est la fiche, `p.nom` c'est la case « Nom » de cette fiche,
`p.age` la case « Âge ». Le point `.` veut dire « le champ … de cette fiche ».

> 💡 Pour les champs **chaîne**, on n'écrit pas `p.nom = "Alice"` (interdit avec les tableaux
> de `char`) : on utilise **`strcpy`** de `<string.h>`, comme au module 02. Pour les champs
> nombres, un simple `=` suffit (`p.age = 30`).

On peut aussi tout remplir **à la création**, dans l'ordre des champs :

```c
struct Personne p = {"Alice", 30};   // nom = "Alice", age = 30
```

---

## 4. `typedef` : un nom plus court pour la structure

Écrire `struct Personne` à chaque fois, c'est long. Le mot-clé **`typedef`** permet de donner
un **surnom** (un alias) au type, pour pouvoir écrire juste `Personne`.

```c
typedef struct {
    char nom[50];
    int  age;
} Personne;          // <- "Personne" devient un type a part entiere

Personne p;          // plus besoin d'ecrire "struct" devant !
```

🏷️ **Analogie :** `typedef`, c'est coller une **étiquette** courte sur le modèle de fiche pour
ne plus avoir à répéter sa longue description. On utilisera **cette** forme dans la suite : elle
est plus simple à lire.

---

## 5. Passer un `struct` à une fonction

Comme n'importe quelle variable, on peut passer une fiche à une fonction. La fonction reçoit
alors une **copie** de toute la fiche (souviens-toi du module 03 : par défaut, C copie).

```c
void afficher(Personne p) {            // p est une COPIE de la fiche
    printf("%s, %d ans\n", p.nom, p.age);
}

Personne alice = {"Alice", 30};
afficher(alice);                       // on passe la fiche a la fonction
```

C'est parfait pour **lire/afficher**. En revanche, comme c'est une copie, modifier `p` à
l'intérieur ne changerait **pas** l'original — exactement le problème vu au module 03.

---

## 6. La flèche `->` : accéder à un champ via un POINTEUR de structure

Pour **modifier** vraiment une fiche depuis une fonction (ou simplement éviter de copier une
grosse fiche), on passe son **adresse** : un **pointeur de structure**. Et là, petite nouveauté
de syntaxe.

Avec un pointeur `ptr` vers une fiche, on **pourrait** écrire `(*ptr).age` (« va voir la fiche
pointée, puis son champ age »). Mais c'est lourd, alors le C offre un raccourci : la **flèche
`->`**.

```c
void vieillir(Personne *ptr) {     // ptr = ADRESSE d'une fiche
    ptr->age = ptr->age + 1;       // ptr->age  <=>  (*ptr).age
}

Personne alice = {"Alice", 30};
vieillir(&alice);                  // on donne l'ADRESSE de la fiche
printf("%d\n", alice.age);         // 31  -> l'original a bien change !
```

> 🔑 **Règle simple à retenir :**
> - avec une **fiche** (la variable elle-même) → le **point** : `alice.age`
> - avec un **pointeur** vers une fiche → la **flèche** : `ptr->age`

| Tu as… | Pour le champ `age`, tu écris… |
|--------|-------------------------------|
| une structure `alice` | `alice.age` |
| un pointeur `ptr` vers une structure | `ptr->age` (raccourci de `(*ptr).age`) |

---

## 7. Tableaux de structures

Le vrai intérêt arrive ici : un **tableau de fiches**. Un classeur, c'est plein de fiches
identiques rangées les unes derrière les autres. En C :

```c
Personne contacts[3] = {
    {"Alice", 30},
    {"Bob",   25},
    {"Chloe", 42}
};

for (int i = 0; i < 3; i++) {
    // contacts[i] est UNE fiche ; on accede a ses champs avec le point
    printf("%s, %d ans\n", contacts[i].nom, contacts[i].age);
}
```

🗄️ **Analogie : un classeur de fiches.** `contacts` est le classeur, `contacts[0]` la première
fiche, `contacts[0].nom` la case « Nom » de cette première fiche. On parcourt le classeur avec
une boucle, exactement comme un tableau d'entiers au module 02 — sauf que chaque case contient
maintenant **plusieurs** informations.

C'est précisément ce que fait le programme `agenda.c` de ce module.

---

## ▶️ À toi de jouer

```bash
# Les bases : definir un struct, lire/ecrire les champs, point '.' et fleche '->'
gcc -Wall c/04_structures/structures.c -o structures && ./structures

# Un petit agenda : un tableau de contacts qu'on parcourt et affiche
gcc -Wall c/04_structures/agenda.c -o agenda && ./agenda
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : ajoute un champ (un `numero` de
téléphone, par exemple), ajoute un 4ᵉ contact, écris une fonction qui trouve le contact le plus
âgé, ou une fonction qui modifie l'âge d'un contact via un pointeur `->`.

➡️ La suite du parcours (fichiers, projets…) arrivera dans le même style.
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
