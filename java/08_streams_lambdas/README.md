# Module 08 — Lambdas `->` et l'API Stream : traiter des données élégamment

Parcourir une liste pour garder certains éléments, en transformer d'autres, calculer une
somme… On peut le faire avec des boucles `for`, mais ça devient vite long et répétitif. Java
offre deux outils modernes qui rendent ça **court et lisible** : les **lambdas** (de mini
fonctions) et les **streams** (un « tapis roulant » sur les données).

> Fichier du module : `Streams.java`. On compile, puis on lance (voir en bas).

---

## 1. La LAMBDA : une fonction sans nom

Une lambda, c'est une **fonction écrite en une ligne**, avec une **flèche** `->` :

```java
x -> x * x          // "à x, j'associe x au carré"
(a, b) -> a + b     // "à a et b, j'associe leur somme"
mot -> mot.toUpperCase()
```

- À **gauche** de la flèche : le(s) paramètre(s).
- À **droite** : la valeur renvoyée.

On peut la **stocker** dans une variable et l'appeler avec `.apply(...)` :

```java
Function<Integer, Integer> carre = x -> x * x;
carre.apply(5);   // -> 25
```

> 🆚 C'est exactement le `lambda x: x * x` de Python, avec une syntaxe différente (`->` au
> lieu de `:`).

---

## 2. Le STREAM : un tapis roulant sur une collection

`.stream()` pose une collection sur un « tapis roulant ». On enchaîne ensuite des **étapes**,
et chaque élément passe dans chacune. Les 4 étapes à connaître :

| Étape | Rôle | Exemple |
|-------|------|---------|
| `filter` | **garder** les éléments qui passent un test | `.filter(n -> n % 2 == 0)` (les pairs) |
| `map` | **transformer** chaque élément | `.map(mot -> mot.toUpperCase())` |
| `collect` / `toList` | **rassembler** le résultat | `.toList()` |
| `reduce` | **combiner** tout en une seule valeur | `.reduce(0, (a, b) -> a + b)` (la somme) |

```java
List<Integer> pairs = nombres.stream()
        .filter(n -> n % 2 == 0)   // garde les pairs
        .toList();                 // rassemble en liste
```

---

## 3. Chaîner les étapes (la vraie force)

On enchaîne les étapes les unes après les autres, ce qui se lit **comme une phrase** :

```java
List<Integer> resultat = nombres.stream()
        .filter(n -> n > 2)   // garder ceux > 2
        .map(n -> n * n)      // les mettre au carré
        .toList();            // rassembler
```

La même chose avec une boucle `for` prendrait plus de lignes et serait moins claire. Le
stream **décrit ce qu'on veut**, pas le « comment » du parcours.

---

## 🗺️ CHEMINEMENT du programme

1. Définir une **lambda** simple (`x -> x * x`) et l'appeler, pour comprendre la flèche.
2. **`filter`** : ne garder que les nombres pairs.
3. **`map`** : transformer chaque mot en MAJUSCULES.
4. **`collect`** : rassembler (joindre les mots en une phrase).
5. **`reduce`** : combiner tous les nombres en une somme.
6. **Chaîner** `filter` + `map` + `collect` en une seule chaîne lisible.

---

## ▶️ À toi de jouer

```bash
# lambdas + streams : filter / map / collect / reduce
javac -d /tmp/jb java/08_streams_lambdas/Streams.java
java -cp /tmp/jb Streams
```

Lis le fichier, puis **modifie-le** : filtre les nombres **impairs**, ou utilise `reduce`
pour calculer le **produit** au lieu de la somme (départ à `1`, lambda `(a, b) -> a * b`).

➡️ Prochaine étape : le module **09_threads**, pour faire plusieurs choses « en même temps ».
