# 🃏 Aide-mémoire Java (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases`, `02_poo`…

> ⚠️ En Java : chaque instruction finit par un **`;`**, les blocs sont entre **`{ }`**, et
> **tout** le code vit à l'intérieur d'une **`class`**.

---

## Compiler et lancer (javac / java)

```bash
javac Mon.java                 # compile -> crée Mon.class (du bytecode)
java -cp . Mon                 # lance la classe Mon (PAS de .class ni .java)
# ⚠️ Une classe public DOIT être dans un fichier du MÊME NOM :
# class Mon  ->  fichier Mon.java
```

## Structure type d'un programme

```java
public class Mon {                               // 1. tout vit dans une CLASSE
    static int additionner(int a, int b) {       // 2. les méthodes
        return a + b;
    }
    public static void main(String[] args) {     // 3. main : le point de départ
        System.out.println("Bonjour");
    }
}
```

## Afficher / lire

```java
System.out.println("Bonjour");            // afficher AVEC retour à la ligne
System.out.print("sans saut de ligne");   // afficher SANS retour à la ligne
System.out.println("Age : " + age);       // coller texte et variables avec +

import java.util.Scanner;                  // en haut du fichier
Scanner sc = new Scanner(System.in);
int age = sc.nextInt();                    // lire un nombre tapé au clavier
String nom = sc.nextLine();                // lire une ligne entière de texte
```

## Variables et types

```java
int age = 30;            // int     : entier
double prix = 9.99;      // double  : nombre à virgule
char lettre = 'A';       // char    : UN caractère, entre apostrophes ' '
String nom = "Lou";      // String  : du texte, entre guillemets " " (avec un grand S)
boolean actif = true;    // boolean : true (vrai) / false (faux)
```

## Opérateurs

```java
+  -  *  /        // addition, soustraction, multiplication, division
%                 // reste (modulo) : 7 % 2 == 1
==  !=            // égal / différent (mais pour String : .equals())
<  >  <=  >=      // comparaisons
&&   ||   !       // ET / OU / NON logiques
```

## Conditions

```java
if (age >= 18) {
    System.out.println("Majeur");
} else if (age >= 13) {           // 'else if' (et non 'elif')
    System.out.println("Ado");
} else {
    System.out.println("Enfant");
}
```

## Boucles

```java
for (int i = 0; i < 5; i++) {           // (début ; condition ; pas) -> 0,1,2,3,4
    System.out.println(i);
}

while (x < 10) {                        // tant que la condition est vraie
    x++;                                // sinon : boucle infinie !
}

for (int note : notes) {                // for-each : "pour chaque note de notes"
    System.out.println(note);
}
```

## Méthodes

```java
// type_de_retour nom(paramètres typés) { ... }
static int additionner(int a, int b) {
    return a + b;       // renvoie un résultat
}

static void saluer() {  // void = ne renvoie rien
    System.out.println("Bonjour !");
}
```

## Classes et objets

```java
public class Chien {
    private String nom;                 // attribut (privé = encapsulation)

    public Chien(String nom) {          // CONSTRUCTEUR (même nom que la classe)
        this.nom = nom;                 // this.nom = l'attribut ; nom = le paramètre
    }
    public String getNom() {            // getter : lire sans modifier
        return this.nom;
    }
}
Chien c = new Chien("Rex");             // créer un objet avec 'new'
System.out.println(c.getNom());
```

## Héritage & interfaces

```java
class Animal { void crier() { System.out.println("..."); } }
class Chat extends Animal {             // 'extends' : Chat hérite d'Animal
    @Override void crier() { System.out.println("Miaou"); }   // redéfinit
}

interface Volant { void voler(); }      // un CONTRAT à respecter
class Oiseau implements Volant {        // 'implements' : Oiseau tient le contrat
    public void voler() { System.out.println("Je vole"); }
}
```

## Listes & dictionnaires — `import java.util.*;`

```java
List<Integer> notes = new ArrayList<>();   // une liste qui grandit
notes.add(12);                             // ajouter à la fin (comme .append())
notes.get(0);                              // accès par index (dès 0)
notes.size();                              // nombre d'éléments
for (int n : notes) { ... }                // parcourir avec for-each

Map<String, Integer> ages = new HashMap<>();   // un dictionnaire clé -> valeur
ages.put("Lou", 30);                           // ranger une valeur sous une clé
ages.get("Lou");                               // récupérer (renvoie 30)
```

## Gérer les erreurs (try / catch)

```java
try {
    int x = Integer.parseInt("abc");     // peut lever une exception
} catch (NumberFormatException e) {
    System.out.println("Pas un nombre : " + e.getMessage());
} finally {
    System.out.println("Toujours exécuté");
}
```

## Génériques `<T>`

```java
class Boite<T> {                         // T = un type quelconque
    private T contenu;
    public void ranger(T c) { this.contenu = c; }
    public T sortir() { return this.contenu; }
}
Boite<String> b = new Boite<>();         // une boîte SPÉCIALISÉE pour du texte
```

## Lambdas & streams — `import java.util.stream.*;`

```java
List<Integer> notes = List.of(8, 12, 15, 4);
long bonnes = notes.stream()             // ouvrir un flux
                   .filter(n -> n >= 10) // lambda : garder les notes >= 10
                   .count();             // compter -> 2
notes.forEach(n -> System.out.println(n));  // pour chaque, faire...
```

## Threads (faire plusieurs choses à la fois)

```java
Thread t = new Thread(() -> System.out.println("dans un fil"));
t.start();                               // lance le fil EN PARALLÈLE
t.join();                                // attend qu'il ait fini
```

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) pour les définitions.
