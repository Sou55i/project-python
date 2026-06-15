# Module 01 — Les briques de base en Java

Maintenant que tu sais compiler et lancer, découvrons les **briques fondamentales** de tout
programme : les **types**, les **variables**, les **conditions**, les **boucles** et les
**méthodes**. Java étant **typé**, on doit toujours annoncer le type de ce qu'on manipule.

> Fichiers du module : [`Bases.java`](./Bases.java) (toutes les briques, commentées ligne à
> ligne) et [`MiniCalculatrice.java`](./MiniCalculatrice.java) (un vrai mini-programme
> interactif). Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. Les types et les variables

Une **variable**, c'est une boîte étiquetée qui contient une valeur. En Java, on doit
préciser le **type** de la boîte (ce qu'elle a le droit de contenir), puis son **nom**,
puis sa valeur :

```java
int age = 30;   // type 'int', nom 'age', valeur 30
```

Les types de base à connaître :

| Type | Contient | Exemple |
|------|----------|---------|
| `int` | un nombre entier | `int age = 30;` |
| `double` | un nombre à virgule | `double taille = 1.68;` |
| `char` | **un seul** caractère (apostrophes simples) | `char initiale = 'A';` |
| `boolean` | un booléen : `true` ou `false` | `boolean majeur = true;` |
| `String` | du texte (guillemets doubles) | `String nom = "Lou";` |

> 💡 Attention : `String` commence par une **majuscule** (c'est une classe), alors que
> `int`, `double`, `char`, `boolean` s'écrivent en **minuscules** (ce sont des types
> « primitifs »). Et `'A'` (un `char`, apostrophes) n'est pas `"A"` (un `String`,
> guillemets) !

---

## 2. Afficher des valeurs

On colle du texte et des variables avec le **`+`** :

```java
String nom = "Lou";
int age = 30;
System.out.println("Nom : " + nom + ", age : " + age);   // Nom : Lou, age : 30
```

Ici le `+` **concatène** (met bout à bout) plutôt que d'additionner, parce qu'il y a du
texte autour.

---

## 3. Les conditions : `if` / `else if` / `else`

On exécute du code **seulement si** une condition est vraie. La condition va entre
parenthèses `( )`, le bloc entre accolades `{ }` :

```java
int note = 12;
if (note >= 16) {
    System.out.println("Mention : Tres bien");
} else if (note >= 10) {          // 'else if' (et non 'elif' comme en Python)
    System.out.println("Mention : Recu");
} else {
    System.out.println("Mention : A retravailler");
}
```

Les comparaisons : `==` (égal), `!=` (différent), `<`, `>`, `<=`, `>=`. On combine les
conditions avec `&&` (ET) et `||` (OU).

---

## 4. Les boucles : `for` et `while`

Une **boucle** répète des instructions. Le `for` est idéal quand on connaît le nombre de
tours ; il s'écrit `(début ; condition de continuation ; pas)` :

```java
for (int i = 0; i < 3; i++) {   // i++ veut dire i = i + 1
    System.out.println("Tour numero " + i);
}
```

Le `while` répète **tant que** sa condition reste vraie :

```java
int compteur = 0;
while (compteur < 3) {
    System.out.println("compteur = " + compteur);
    compteur++;   // INDISPENSABLE, sinon la boucle ne s'arrête jamais
}
```

---

## 5. Les méthodes

Une **méthode** est un bloc de code réutilisable, avec un **nom**. En Java, une méthode
indique le **type de la valeur qu'elle renvoie** (ou `void` si elle ne renvoie rien) :

```java
// 'int' = type renvoyé ; (int a, int b) = deux paramètres entiers.
static int additionner(int a, int b) {
    return a + b;   // 'return' renvoie le résultat à l'appelant
}

// 'void' = ne renvoie rien ; se contente d'agir.
static void saluer() {
    System.out.println("Bonjour depuis une methode !");
}
```

> 💡 Le mot `static` permet d'appeler la méthode directement depuis `main` (qui est lui
> aussi `static`), sans avoir à créer d'objet. On verra les méthodes **non** statiques
> quand on abordera les classes et les objets.

On appelle une méthode par son nom, avec ses arguments entre parenthèses :

```java
saluer();                         // affiche le message
int somme = additionner(7, 5);    // somme vaut 12
```

---

## 6. Lire au clavier avec `Scanner`

Pour rendre un programme **interactif** (lire ce que tape l'utilisateur), Java fournit
l'outil `Scanner`. On l'importe en haut du fichier, puis on le branche sur le clavier
(`System.in`) :

```java
import java.util.Scanner;   // tout en haut du fichier

Scanner clavier = new Scanner(System.in);   // on branche le scanner sur le clavier
System.out.print("Ton age : ");
int age = clavier.nextInt();   // lit un entier ; nextDouble() pour un double, next() pour un mot
```

C'est exactement ce que fait [`MiniCalculatrice.java`](./MiniCalculatrice.java).

---

## ▶️ À toi de jouer

```bash
# Toutes les briques de base
javac java/01_les_bases/Bases.java
java -cp java/01_les_bases Bases

# La mini-calculatrice interactive (tape une operation, puis deux nombres)
javac java/01_les_bases/MiniCalculatrice.java
java -cp java/01_les_bases MiniCalculatrice
```

Lis les deux fichiers, puis **modifie-les** : ajoute une mention dans le `if`, change le
nombre de tours d'une boucle, écris ta propre méthode (ex : `multiplier(a, b)`).

➡️ La suite du parcours (classes, objets, projets…) arrivera dans le même style.
