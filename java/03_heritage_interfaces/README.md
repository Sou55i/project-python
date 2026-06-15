# Module 03 — Héritage & interfaces : réutiliser et spécialiser

Au module 02, tu as appris à ranger données et actions dans une **classe**. Mais quand
plusieurs classes se ressemblent beaucoup (un `Chien` et un `Chat` ont tous les deux un
nom, savent se décrire…), réécrire le même code dans chacune serait fastidieux et risqué.
Java propose plusieurs outils pour éviter ça : l'**héritage** (réutiliser), les **classes
abstraites** et les **interfaces** (imposer un modèle), et le **polymorphisme**
(spécialiser).

> Fichier du module : `Demo.java`. Il regroupe une classe abstraite `Animal`, deux filles
> `Chien` et `Chat`, une interface `Nageur`, et une classe **publique** `Demo` avec le
> `main`. On compile, puis on lance (voir en bas).

---

## 1. C'est quoi l'HÉRITAGE ?

L'**héritage**, c'est créer une nouvelle classe à partir d'une classe existante : la
nouvelle (**la fille**) **récupère automatiquement** tout ce que possède l'ancienne (**la
mère**), puis peut **ajouter** ses propres choses ou **modifier** certaines.

L'analogie clé : « **EST UN** ». Un **chien EST UN animal**. Donc tout ce qu'un animal sait
faire, un chien sait le faire aussi — plus ses spécificités à lui (aboyer).

```
   CLASSE MÈRE   Animal   (a un nom, sait decrire())
        │
        │  « un Chien EST UN Animal »
        ▼
   CLASSE FILLE  Chien    (hérite de nom + decrire(), et AJOUTE aboyer())
```

En Java, on écrit **`class Fille extends Mère`**. Le mot `extends` se lit « hérite de ».

```java
class Animal {
    String nom;
    void decrire() {
        System.out.println("Je m'appelle " + nom);
    }
}

class Chien extends Animal {   // « Chien hérite de Animal »
    void aboyer() {            // une action EN PLUS, propre au chien
        System.out.println(nom + " aboie.");   // 'nom' vient de la mère
    }
}
```

`aboyer()` utilise directement `nom`, **sans le redéclarer** : il a été **hérité**. La
fille profite gratuitement de tout ce que possède la mère.

> 💡 **`super(...)`** appelle le constructeur de la mère depuis celui de la fille (pour
> initialiser la partie héritée). **`protected`** est comme `private`, mais les **filles**
> y ont aussi accès.

---

## 2. La CLASSE ABSTRAITE : un modèle qu'on ne crée pas directement

Parfois, la mère est trop **générale** pour exister seule : un « animal tout court » n'a pas
de cri précis. On la déclare alors **`abstract`** : on ne pourra **jamais** faire
`new Animal(...)`, seulement créer des `Chien`, des `Chat`…

Une classe abstraite peut contenir :
- des méthodes **concrètes** (avec un corps), héritées telles quelles ;
- des méthodes **abstraites** (sans corps, juste un `;`) que **chaque fille DOIT redéfinir**.

```java
abstract class Animal {
    protected String nom;

    void decrire() {                  // méthode CONCRÈTE : héritée telle quelle
        System.out.println("Je m'appelle " + nom);
    }

    abstract void parler();           // méthode ABSTRAITE : pas de corps, juste ;
                                      // chaque fille DOIT la fournir
}
```

> 🆚 En C++, une méthode « à fournir » s'écrivait `virtual void parler() = 0;`. En Java,
> c'est le mot-clé `abstract`.

---

## 3. Le POLYMORPHISME : la même demande, des réponses différentes

**Poly-morphisme** veut dire « **plusieurs formes** ». L'idée : on demande la **même chose**
à des objets différents, et **chacun répond à sa façon**. Tu réunis plein d'animaux et tu
leur dis à tous « **parle !** » : le chien répond « Wouf », le chat « Miaou ».

Chaque fille **redéfinit** la méthode de la mère. On marque ça avec **`@Override`** : une
étiquette qui dit « je redéfinis une méthode héritée » (et fait vérifier au compilateur
qu'on ne s'est pas trompé de nom).

```java
class Chien extends Animal {
    Chien(String nom) { super(nom); }
    @Override void parler() { System.out.println(nom + " fait Wouf !"); }
}

class Chat extends Animal {
    Chat(String nom) { super(nom); }
    @Override void parler() { System.out.println(nom + " fait Miaou !"); }
}
```

Le vrai pouvoir : une **variable (ou un tableau) de type MÈRE** peut contenir n'importe
quelle fille. À l'appel de `parler()`, Java exécute **automatiquement la bonne version**
(celle de la vraie classe de l'objet) :

```java
Animal[] animaux = { new Chien("Rex"), new Chat("Felix") };
for (Animal a : animaux) {   // boucle for-each (voir module 04)
    a.parler();              // Rex fait Wouf, puis Felix fait Miaou
}
```

> 🆚 En C++, il fallait `virtual` + un **pointeur** `Animal*` pour ça. En Java, **toute**
> méthode est redéfinissable par défaut, et toute variable d'objet est déjà une « référence » :
> le polymorphisme marche tout seul, sans `*` ni `->`.

---

## 4. L'INTERFACE : un contrat de capacités

Une **interface** est un **contrat** : une liste de méthodes (sans corps) qu'une classe
**s'engage à fournir** si elle « signe » le contrat. Elle ne décrit pas ce qu'un objet **est**
(ça, c'est l'héritage), mais ce qu'il **sait faire**.

L'analogie : « est **capable de** ». Peu importe que tu sois un chien, un humain ou un
poisson — si tu implémentes `Nageur`, c'est que tu **sais nager**.

```java
interface Nageur {
    void nager();   // juste la signature : aucun corps
}

class Chien extends Animal implements Nageur {   // Chien HÉRITE d'Animal ET signe Nageur
    @Override public void nager() {
        System.out.println(nom + " nage.");
    }
}
```

- On hérite d'**une seule** classe (`extends`), mais on peut implémenter **plusieurs**
  interfaces (`implements A, B`).
- Une classe qui « signe » une interface **doit** fournir toutes ses méthodes, sinon le
  code ne compile pas.

> 🆚 C'est l'équivalent Java des `interface` du Go, ou des classes 100 % abstraites du C++.

---

## 5. 🆚 Récapitulatif des mots-clés

| Mot-clé | Où | Rôle |
|---------|-----|------|
| `extends` | en-tête de la fille | la fille **hérite** d'une classe mère (une seule) |
| `super(...)` | constructeur de la fille | appelle le **constructeur de la mère** |
| `abstract` | classe ou méthode | modèle non instanciable / méthode à fournir |
| `@Override` | méthode de la fille | indique qu'on **redéfinit** une méthode héritée |
| `interface` / `implements` | contrat / en-tête | liste de capacités à **fournir obligatoirement** |

---

## ▶️ À toi de jouer

```bash
# Héritage + classe abstraite + interface + polymorphisme, dans un seul fichier
javac -d /tmp/jb java/03_heritage_interfaces/Demo.java
java -cp /tmp/jb Demo
```

Lis le fichier, puis **modifie-le** et **recompile** : ajoute une classe `Vache` qui fait
« Meuh », ajoute-la au tableau `animaux`, ou fais aussi implémenter `Nageur` au `Chat` et
observe que tu **dois** alors écrire sa méthode `nager()`.

➡️ Module suivant : [`04_collections`](../04_collections/).
