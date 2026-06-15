# Module 02 — Programmation Orientée Objet : classes & objets

Jusqu'ici (module 01), tes données et tes actions vivaient un peu **séparées** : des
variables d'un côté (`int age`, `double taille`…), des méthodes de l'autre. La
**programmation orientée objet** (POO) propose de **regrouper** ce qui va ensemble : les
**données** ET les **actions** qui s'appliquent à ces données, dans un même paquet bien
rangé : une **classe**.

> En Java, tu fais déjà de la POO sans le savoir : `String`, `System`… sont des classes.
> Ici, tu vas créer **les tiennes**. Fichier du module : `CompteBancaire.java`.

---

## 1. C'est quoi une CLASSE ? Et un OBJET ?

Imagine le **plan d'une maison** dessiné par un architecte. Le plan décrit ce qu'aura
**toute** maison construite à partir de lui : un nombre de pièces, une surface… Mais le
plan **n'est pas** une maison : tu ne peux pas dormir dedans !

- Une **classe**, c'est le **plan/modèle**. Elle décrit ce que **contient** un objet
  (ses **données**, qu'on appelle **attributs**) et ce qu'il **sait faire** (ses
  **actions**, qu'on appelle **méthodes**).
- Un **objet**, c'est un **exemplaire concret** construit à partir du plan : une **maison
  réelle**. À partir d'un seul plan, on peut bâtir **autant d'objets que l'on veut**, et
  chacun a ses propres valeurs.

```
   CLASSE  CompteBancaire   ──►  plan / modèle  (décrit titulaire, solde, deposer()…)
                  │
                  ├──►  OBJET compte  (titulaire "Lou",  solde 100)   ← un compte réel
                  └──►  OBJET autre   (titulaire "Sam",  solde 0)     ← un autre compte réel
```

Autres analogies : la classe = le **moule à gâteaux**, les objets = les **gâteaux** ; la
classe = la **fiche modèle** d'un personnage de jeu, les objets = les **personnages**
réellement créés, chacun avec ses points de vie.

---

## 2. Attributs (les données) et méthodes (les actions)

Une classe rassemble deux choses :

- les **attributs** : des **variables** qui appartiennent à l'objet (son titulaire, son
  solde…). Ce sont **les données** de l'objet.
- les **méthodes** : des **fonctions** rangées dans la classe (déposer, retirer…). Ce sont
  **les actions** que l'objet sait faire, souvent **sur ses propres attributs**.

```java
public class CompteBancaire {
    String titulaire;   // ATTRIBUT (une donnée de l'objet)
    double solde;       // ATTRIBUT

    void deposer(double montant) {   // MÉTHODE (une action de l'objet)
        solde += montant;            // elle utilise un attribut de l'objet
    }
}
```

> 💡 Une **méthode** d'objet n'a PAS le mot `static` (contrairement au `main` ou aux
> méthodes du module 01). Pourquoi ? Parce qu'elle agit sur **un objet précis** : il faut
> d'abord créer l'objet, puis l'appeler dessus.

---

## 3. Créer un objet avec `new` et utiliser ses méthodes

Le **type** d'un objet, c'est le **nom de la classe**. On le crée avec le mot-clé **`new`**,
puis on accède à ses méthodes avec le point **`.`** (le même `.` que `System.out`).

```java
CompteBancaire compte = new CompteBancaire(...);   // on CRÉE un objet avec new
compte.deposer(50.0);                              // on appelle une méthode avec  .
```

> 🆚 En C++, on écrivait `Rectangle r(4, 3);`. En Java, **toujours** `new` :
> `new CompteBancaire(...)`. La mémoire sera libérée automatiquement (ramasse-miettes).

---

## 4. Le CONSTRUCTEUR : initialiser un objet dès sa création

Régler les attributs un par un après coup est fastidieux et on risque d'en **oublier**. Le
**constructeur** est une **méthode spéciale** appelée **automatiquement** au moment où
l'objet naît (avec `new`) : il donne ses valeurs de départ.

Particularités du constructeur :
- il porte **exactement le même nom que la classe** ;
- il **n'a aucun type de retour** (même pas `void`).

```java
public class CompteBancaire {
    String titulaire;
    double solde;

    // CONSTRUCTEUR : même nom que la classe, aucun type de retour.
    public CompteBancaire(String titulaire, double soldeInitial) {
        this.titulaire = titulaire;   // 'this.titulaire' = l'attribut de l'objet
        this.solde = soldeInitial;    // 'titulaire' (à droite) = le paramètre reçu
    }
}
```

> 💡 **`this`** désigne « l'objet courant ». On l'utilise pour lever l'ambiguïté quand un
> paramètre porte le même nom qu'un attribut (`this.titulaire = titulaire;`).

Du coup, on crée un objet **déjà prêt**, en passant les valeurs entre parenthèses :

```java
CompteBancaire compte = new CompteBancaire("Lou", 100.0);   // titulaire="Lou", solde=100
```

> 🆚 En Python, le constructeur s'appelait `__init__`. En Java (comme en C++), il porte le
> **nom de la classe**.

---

## 5. L'ENCAPSULATION : `private` + getters

**Encapsuler**, c'est **cacher les détails internes** d'un objet et n'exposer que ce qui
est utile. Pense à une **voiture** : tu utilises le volant et les pédales (la partie
*publique*), sans toucher au moteur (la partie *privée*, sous le capot).

| Mot-clé | Signifie | Accessible depuis… |
|---------|----------|--------------------|
| `public` | la partie « visible », l'interface | n'importe où (depuis `main`, etc.) |
| `private` | les détails internes, protégés | uniquement **depuis l'intérieur de la classe** |

On met les **attributs sensibles en `private`** (pour qu'on ne puisse pas les modifier
n'importe comment de l'extérieur), et on offre des **méthodes `public`** contrôlées :

```java
public class CompteBancaire {
    private double solde;   // PRIVÉ : intouchable directement depuis l'extérieur

    public void deposer(double montant) {   // PUBLIC : une porte d'entrée contrôlée
        if (montant > 0) {
            solde += montant;               // l'intérieur de la classe, LUI, a le droit
        }
    }
}
```

Avec ça, `compte.solde = -1000000;` depuis `main` est **interdit** (erreur de
compilation !). On est **obligé** de passer par `deposer()` / `retirer()`, qui **vérifient**
que l'opération est valide.

Et pour **lire** un attribut privé de l'extérieur, on écrit un **getter** : une petite
méthode publique qui renvoie la valeur, sans permettre de l'écrire.

```java
public double getSolde() {   // GETTER : permet de LIRE le solde, pas de le modifier
    return this.solde;
}
```

> 💬 Convention Java : un getter se nomme `getNomAttribut()`. C'est juste une habitude
> universelle qui rend ton code immédiatement lisible par les autres.

---

## 6. 🆚 Une classe, c'est mieux que des variables nues

On *pourrait* juste se balader avec une variable `double solde;` toute nue. Le problème :
elle est **exposée** et **sans protection**. N'importe qui peut la mettre à un million,
oublier une règle… La **classe** corrige ça en **mariant les données et les règles qui les
gardent** :

| | Variable « nue » | `class` (POO) |
|--|------------------|---------------|
| Données | exposées, modifiables librement | peuvent être **`private`** (protégées) |
| Règles / vérifications | nulle part | dans les **méthodes** de la classe |
| Données + actions | séparées | **regroupées** au même endroit |

---

## ▶️ À toi de jouer

```bash
# La classe CompteBancaire : attributs privés, constructeur, deposer/retirer, getters
javac -d /tmp/jb java/02_poo/CompteBancaire.java
java -cp /tmp/jb CompteBancaire
```

Lis le fichier, puis **modifie-le** et **recompile** : ajoute un attribut `private String
numero;`, crée d'autres comptes, ou **décommente** la ligne `compte.solde = 1000000;` dans
`main` et observe l'**erreur** du compilateur (c'est l'encapsulation qui te protège).

➡️ Module suivant : [`03_heritage_interfaces`](../03_heritage_interfaces/).
