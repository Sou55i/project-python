# Module 06 — Les génériques `<T>` : écrire une fois, réutiliser partout

Imagine que tu veuilles une **boîte** capable de ranger un objet. Tu pourrais écrire une
`BoiteDeTexte`, puis une `BoiteDeNombre`, puis une `BoiteDeCompte`… et copier-coller le
même code à chaque fois. Quel gâchis ! Les **génériques** résolvent ça : tu écris **une
seule** classe `Boite<T>`, où `T` est un **type laissé en blanc**, et tu le remplis au
moment de l'utiliser.

> Fichier du module : `Generics.java`. On compile, puis on lance (voir en bas).

---

## 1. C'est quoi un GÉNÉRIQUE ?

Un générique, c'est un **paramètre de TYPE**. Au lieu de fixer le type à l'avance, tu le
laisses en blanc avec des chevrons `<...>`. Par convention, on le note d'une seule lettre
majuscule :

- `T` pour *Type* (le plus courant),
- `E` pour *Element*, `K` pour *Key* (clé), `V` pour *Value* (valeur).

Tu en as **déjà vu** au module 04 : `List<String>`, `Map<String, Integer>`. Le `<String>`
disait « cette liste ne contient QUE des String ». Ici, on apprend à en **fabriquer**.

---

## 2. Une CLASSE générique

On déclare le type blanc juste après le nom de la classe :

```java
class Boite<T> {        // <T> : "je travaille avec un type que j'appelle T"
    private T contenu;  // l'attribut a le type T

    public Boite(T contenu) { this.contenu = contenu; }
    public T getContenu() { return this.contenu; }
}
```

À l'utilisation, on **remplit la case** :

```java
Boite<String>  b1 = new Boite<>("salut"); // T devient String
Boite<Integer> b2 = new Boite<>(42);      // T devient Integer
String s = b1.getContenu();               // renvoie un String, garanti
```

---

## 3. Une MÉTHODE générique

Une méthode peut, à elle seule, être générique : on met le `<T>` **avant** le type de
retour.

```java
static <T> T premier(List<T> liste) {  // marche pour List<String>, List<Integer>...
    return liste.get(0);
}
```

```java
premier(List.of("a", "b"));   // renvoie "a"  (T = String)
premier(List.of(10, 20));     // renvoie 10   (T = Integer)
```

---

## 4. Pourquoi c'est UTILE ?

1. **Réutilisation** : un seul code pour des dizaines de types. Pas de copier-coller.
2. **Sécurité de type** : le **compilateur** vérifie. Si tu mets un nombre dans une
   `Boite<String>`, ça **refuse de compiler** — l'erreur est attrapée AVANT l'exécution,
   pas pendant.
3. **Pas de conversion manuelle** : `getContenu()` sur une `Boite<String>` renvoie
   **directement** un `String`. Sans génériques, tu manipulerais des `Object` et devrais
   convertir partout (source classique de bugs).

```java
Boite<String> b = new Boite<>("texte");
// b.setContenu(123); // ❌ le compilateur REFUSE : 123 n'est pas un String
```

> 🆚 En Python, les listes acceptent **tout** mélangé (`[1, "deux", 3.0]`) et les erreurs
> de type n'apparaissent qu'à l'exécution. Java, lui, te protège dès la compilation grâce
> aux génériques. C'est plus strict, mais ça attrape les bugs plus tôt.

---

## ▶️ À toi de jouer

```bash
# classe générique Boite<T> + méthodes génériques
javac -d /tmp/jb java/06_generics/Generics.java
java -cp /tmp/jb Generics
```

Lis le fichier, puis **modifie-le** : crée une `Boite<Double>`, ou décommente la ligne
`boiteTexte.setContenu(123);` et observe le compilateur la **refuser**. Tu peux aussi
écrire ta propre méthode générique `dernier(List<T> liste)`.

➡️ Prochaine étape : le module **07_debugger**, pour traquer les erreurs quand le code ne
fait pas ce qu'on croit.
