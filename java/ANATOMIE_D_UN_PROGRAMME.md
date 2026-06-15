# 🧭 Anatomie d'un programme Java : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire des lignes de Java, mais ne savent pas **dans quel
ordre les ranger** pour former un programme complet et propre. Ce guide explique le
**cheminement logique** d'un programme `.java`, du début à la fin.

> 📌 À lire après les modules [`00_demarrer`](./00_demarrer/) et
> [`01_les_bases`](./01_les_bases/), et à garder sous la main comme aide-mémoire.

---

## 1. LA règle d'or : en Java, TOUT vit dans une classe

C'est LA grande différence avec Python, et la première chose à intégrer.

> En Java, tu **ne peux rien écrire** en dehors d'une **classe**. Pas une variable, pas une
> méthode, pas même un simple « bonjour ». Le fichier **commence** par `public class ...`.

Et une règle qui surprend souvent : une classe `public` **doit** se trouver dans un fichier
qui porte **exactement son nom**. La classe `CompteBancaire` va donc dans le fichier
`CompteBancaire.java`. Si tu te trompes de nom de fichier, le compilateur refuse.

---

## 2. Le squelette standard d'un programme Java

Presque tous les programmes Java bien écrits suivent **ce même ordre**, de haut en bas :

```java
// (1) PACKAGE (optionnel) + IMPORTS : on ouvre les boîtes à outils
import java.util.ArrayList;      // pour ArrayList
import java.util.List;           // pour le type List

// (2) LA CLASSE : tout vit à l'intérieur. Classe publique = nom du fichier.
public class Banque {

    // (3) ATTRIBUTS : les DONNÉES de l'objet (souvent 'private').
    private String nom;
    private double solde;

    // (4) CONSTRUCTEUR : initialise un nouvel objet (même nom que la classe).
    public Banque(String nom, double soldeInitial) {
        this.nom = nom;                  // this.nom = l'attribut ; nom = le paramètre
        this.solde = soldeInitial;
    }

    // (5) MÉTHODES : les ACTIONS de l'objet.
    public void deposer(double montant) {
        this.solde += montant;
    }
    public double getSolde() {           // getter : lire un attribut privé
        return this.solde;
    }

    // (6) main : le POINT DE DÉPART. C'est ICI que tout DÉMARRE.
    public static void main(String[] args) {
        Banque b = new Banque("Lou", 100.0);   // on CRÉE un objet avec 'new'
        b.deposer(50.0);                        // on APPELLE ses méthodes
        System.out.println("Solde : " + b.getSolde());
    }
}
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 1 | **`package` / `import`** | On **ouvre les caisses à outils** avant de s'en servir. `import java.util.ArrayList;` apporte les listes. Le `package` (optionnel ici) range la classe dans un « dossier logique ». |
| 2 | **`public class`** | L'enveloppe : **tout** le code Java vit dedans. ⚠️ Classe `public` = fichier du **même nom**. |
| 3 | **Attributs** | Les **données** que possède chaque objet, déclarées en haut de la classe. Souvent `private` (encapsulation). |
| 4 | **Constructeur** | La méthode qui **initialise** un objet neuf à la création (`new`). Même nom que la classe, aucun type de retour. |
| 5 | **Méthodes** | Les **actions** réutilisables de l'objet. ⚠️ Définir ≠ exécuter : une méthode ne tourne que lorsqu'on l'**appelle**. |
| 6 | **`main`** | Le **point d'entrée** et le **chef d'orchestre** : il crée les objets et appelle les méthodes dans le bon ordre. |

> 💡 « Définir une méthode/classe » = écrire la recette. « L'appeler/l'utiliser » =
> cuisiner le plat. On écrit toutes les recettes, puis on cuisine dans `main`.

> 🧩 **Astuce pour les plus grands projets :** chaque classe importante va dans **son propre
> fichier** (`Tache.java`, `GestionnaireDeTaches.java`…). Une seule contient le `main`. Les
> autres sont juste « disponibles » : elles ne s'exécutent que lorsqu'on les utilise. Au
> début, garde tout simple.

---

## 3. Le cycle de travail : écrire → COMPILER → corriger → lancer

Contrairement à Python (qui se lance directement), le Java doit être **compilé** en
**bytecode** avant de tourner. Le va-et-vient est :

```
   écrire le .java  ──►  COMPILER (javac)  ──►  corriger les erreurs  ──►  lancer (java)
        ▲                       │                       │
        └───────────────────────┴───────────────────────┘
              (on recommence tant qu'il y a des erreurs)
```

```bash
# Compiler : crée le .class (du bytecode)
javac Banque.java

# Lancer : -cp dit OÙ chercher le .class, suivi du NOM DE LA CLASSE (sans extension)
java -cp . Banque
```

- `javac` = le compilateur ; il produit `Banque.class` (du bytecode) ;
- `java` = la **JVM** qui exécute ce bytecode ;
- `-cp .` (*classpath*) = « cherche les `.class` dans le dossier courant ».

> 💬 Si la compilation **échoue**, aucun `.class` n'est mis à jour : lis le message d'erreur
> (il indique souvent la ligne), corrige, et **recompile**. C'est normal d'y revenir
> plusieurs fois !

---

## 4. Le rôle de `main` : le point d'entrée

```java
public static void main(String[] args) {
    // ... ton programme ...
}
```

- **`main` est le point d'entrée** : quand tu lances avec `java`, la JVM cherche `main` et
  commence par là. **Tout part de `main`.**
- Sa signature est **toujours** `public static void main(String[] args)`. On détaillera
  chaque mot plus tard ; pour l'instant, retiens que c'est la formule exacte à recopier.
- Il n'y a qu'**un seul** `main` qui sert de départ. Les autres classes et méthodes sont
  juste « disponibles » : elles ne s'exécutent que lorsqu'on les **appelle**.

---

## 5. La logique INTERNE : entrée → traitement → sortie

À l'intérieur de `main` (ou d'une méthode), le code suit presque toujours **3 phases**,
dans cet ordre :

```
   1. ENTRÉE              2. TRAITEMENT             3. SORTIE
   (je récupère           (je calcule, je décide,   (j'affiche ou
    les données)           je transforme)            j'enregistre)
   ──────────             ───────────────          ──────────
   Scanner.nextInt()      if / else                 System.out.println(...)
   Scanner.nextLine()     for / while               écrire un fichier
   lire un fichier        calculs, appels           (java.io / java.nio)
```

Exemple complet des 3 phases :

```java
import java.util.Scanner;

public class Majorite {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Quel est ton age ? ");   // invite
        int age = sc.nextInt();                      // 1. ENTRÉE : on lit au clavier

        boolean majeur = (age >= 18);                // 2. TRAITEMENT : on décide

        if (majeur) {                                // 3. SORTIE : on affiche
            System.out.println("Tu es majeur.");
        } else {
            System.out.println("Tu es mineur.");
        }
    }
}
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

---

## 6. Comment lire un programme Java qu'on découvre

Quand un programme te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va directement à `main`.** C'est le **point de départ** réel : il montre l'enchaînement
   principal du programme.
2. **Suis les appels** depuis `main`. Quand tu vois `b.deposer(50.0)` ou `new Banque(...)`,
   remonte lire la **méthode** `deposer` ou la **classe** `Banque` pour comprendre ce
   qu'elles font.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes de `main`), puis seulement après, plonge dans chaque méthode/classe.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le contenu de
> `main`), puis tu ouvres les chapitres qui t'intéressent (les méthodes et les classes).

---

## 7. Récapitulatif visuel

```
┌─────────────────────────────────────────────┐
│ 1. import ...        : les boîtes à outils    │  ← on prépare
├─────────────────────────────────────────────┤
│ 2. public class Mon {                         │  ← l'enveloppe (= nom du fichier)
│ 3.    attributs      : les DONNÉES            │
│ 4.    constructeur   : on INITIALISE          │  ← on outille
│ 5.    méthodes       : on DÉFINIT les actions │
├─────────────────────────────────────────────┤
│ 6.    public static void main(String[] args) {│
│           entrée -> traitement -> sortie      │  ← on EXÉCUTE
│       }                                       │
│    }                                          │
└─────────────────────────────────────────────┘
        (tout vit dans la classe ; tout part de main)

    écrire  ──►  COMPILER (javac)  ──►  corriger  ──►  lancer (java)
```

➡️ Garde ce squelette en tête pour démarrer tes propres programmes du bon pied, et n'oublie
pas : **tout vit dans une classe, et tout démarre dans `main`.**
