# Module 03 — Classes & objets : la programmation orientée objet

Jusqu'ici, tes données et tes actions vivaient un peu **séparées** : des variables d'un
côté (`int largeur`, `double solde`…), des fonctions de l'autre. La **programmation
orientée objet** (POO) propose de **regrouper** ce qui va ensemble : les **données** ET
les **actions** qui s'appliquent à ces données, dans un même paquet bien rangé : une
**classe**.

> Fichiers du module : `classe.cpp` (une classe `Rectangle` toute simple) et `objets.cpp`
> (une classe `CompteBancaire`, plus parlante). Pour chacun : on **compile** puis on
> **lance** (voir en bas).

---

## 1. C'est quoi une CLASSE ? Et un OBJET ?

Imagine le **plan d'une maison** dessiné par un architecte. Le plan décrit ce qu'aura
**toute** maison construite à partir de lui : un nombre de pièces, une surface, une porte
d'entrée… Mais le plan **n'est pas** une maison : tu ne peux pas dormir dedans !

- Une **classe**, c'est le **plan/modèle**. Elle décrit ce que **contient** un objet
  (ses **données**, qu'on appelle **attributs**) et ce qu'il **sait faire** (ses
  **actions**, qu'on appelle **méthodes**).
- Un **objet**, c'est un **exemplaire concret** construit à partir du plan : une **maison
  réelle**. À partir d'un seul plan, on peut bâtir **autant de maisons que l'on veut**, et
  chacune a ses propres valeurs (l'une est bleue, l'autre rouge…).

```
   CLASSE  Rectangle   ──►  plan / modèle  (décrit largeur, hauteur, aire()…)
                  │
                  ├──►  OBJET r1  (largeur 4, hauteur 3)   ← un rectangle réel
                  └──►  OBJET r2  (largeur 10, hauteur 2)  ← un autre rectangle réel
```

Autres analogies qui marchent bien :
- La classe = le **moule à gâteaux** ; les objets = les **gâteaux** qu'il produit.
- La classe = la **fiche modèle** d'un personnage de jeu ; les objets = les **personnages**
  réellement créés, chacun avec ses points de vie.

---

## 2. Attributs (les données) et méthodes (les actions)

Une classe rassemble deux choses :

- les **attributs** : des **variables** qui appartiennent à l'objet (sa largeur, son
  solde…). Ce sont **les données** de l'objet.
- les **méthodes** : des **fonctions** qui appartiennent à l'objet (calculer son aire,
  déposer de l'argent…). Ce sont **les actions** que l'objet sait faire, souvent **sur ses
  propres attributs**.

```cpp
class Rectangle {
public:
    int largeur;   // ATTRIBUT (une donnée de l'objet)
    int hauteur;   // ATTRIBUT

    int aire() {                    // MÉTHODE (une action de l'objet)
        return largeur * hauteur;   // elle utilise les attributs de l'objet
    }
};   // ⚠️ point-virgule OBLIGATOIRE après l'accolade qui ferme une classe
```

> 💡 Une **méthode** est juste une **fonction rangée à l'intérieur d'une classe**. Elle a
> le droit d'utiliser directement les attributs de l'objet (ici `largeur` et `hauteur`)
> sans qu'on les lui passe en paramètres.

---

## 3. Créer un objet et utiliser ses méthodes

On crée un objet comme on déclarerait une variable : **le type, c'est le nom de la
classe**. Puis on accède à ses attributs et ses méthodes avec le point **`.`** (le même
`.` que `mot.size()` du module 02 — ce n'était d'ailleurs pas un hasard : `std::string`
est une classe !).

```cpp
Rectangle r;        // on CRÉE un objet 'r' de type Rectangle
r.largeur = 4;      // on accède à un attribut avec le point  .
r.hauteur = 3;
std::cout << r.aire() << std::endl;   // on appelle une méthode : 12
```

---

## 4. Le CONSTRUCTEUR : initialiser un objet dès sa création

Régler les attributs un par un après coup (`r.largeur = 4; r.hauteur = 3;`) est fastidieux
et on risque d'en **oublier**. Le **constructeur** est une **méthode spéciale** appelée
**automatiquement** au moment où l'objet naît : il sert à lui donner ses valeurs de départ.

Particularités du constructeur :
- il porte **exactement le même nom que la classe** ;
- il **n'a aucun type de retour** (même pas `void`).

```cpp
class Rectangle {
public:
    int largeur;
    int hauteur;

    // CONSTRUCTEUR : même nom que la classe, aucun type de retour.
    Rectangle(int l, int h) {
        largeur = l;   // on range les valeurs reçues dans les attributs
        hauteur = h;
    }

    int aire() { return largeur * hauteur; }
};
```

Du coup, on crée un objet **déjà prêt**, en passant les valeurs entre parenthèses :

```cpp
Rectangle r(4, 3);   // le constructeur s'exécute : largeur=4, hauteur=3
std::cout << r.aire() << std::endl;   // 12
```

> 🆚 En Python, le constructeur s'appelait `__init__`. En C++, il porte le **nom de la
> classe**.

---

## 5. L'ENCAPSULATION : `public` et `private`

**Encapsuler**, c'est **cacher les détails internes** d'un objet et n'exposer que ce qui
est utile à l'extérieur. Pense à une **voiture** : tu utilises le volant et les pédales
(la partie *publique*), sans toucher au moteur (la partie *privée*, protégée sous le capot).

En C++, on classe les membres d'une classe en deux zones :

| Mot-clé | Signifie | Accessible depuis…
|---------|----------|-------------------|
| `public` | la partie « visible », l'interface | n'importe où (depuis `main`, etc.) |
| `private` | les détails internes, protégés | uniquement **depuis l'intérieur de la classe** |

L'idée : on met les **attributs sensibles en `private`** (pour qu'on ne puisse pas les
modifier n'importe comment de l'extérieur), et on offre des **méthodes `public`**
contrôlées pour agir dessus.

```cpp
class CompteBancaire {
private:
    double solde;   // PRIVÉ : impossible d'y toucher directement depuis l'extérieur

public:
    void deposer(double montant) {   // PUBLIC : une porte d'entrée contrôlée
        if (montant > 0) {
            solde += montant;        // l'intérieur de la classe, LUI, a le droit
        }
    }
};
```

Avec ça, `compte.solde = -1000000;` depuis `main` est **interdit** (erreur de
compilation !). On est **obligé** de passer par `deposer()` / `retirer()`, qui peuvent
**vérifier** que l'opération est valide. C'est ça, protéger ses données.

> 💡 Par défaut, dans une `class`, tout est `private` tant qu'on n'a pas écrit `public:`.
> C'est pourquoi nos exemples mettent `public:` explicitement.

---

## 6. 🆚 Une classe, c'est mieux qu'une simple structure de données

On *pourrait* juste regrouper des données dans une **structure** (`struct`), comme une
fiche :

```cpp
struct CompteSimple {
    double solde;   // juste une donnée, toute nue
};

CompteSimple c;
c.solde = -999999;   // ✋ RIEN ne l'empêche : on peut écrire n'importe quoi
```

Le problème : la donnée est **exposée** et **sans protection**. N'importe qui peut mettre
un solde négatif, oublier une règle… La **classe** corrige ça en **mariant les données et
les règles qui les gardent** :

| | `struct` « données nues » | `class` (POO) |
|--|---------------------------|---------------|
| Données | exposées, modifiables librement | peuvent être **`private`** (protégées) |
| Règles / vérifications | nulle part | dans les **méthodes** de la classe |
| Données + actions | séparées | **regroupées** au même endroit |

> ℹ️ En C++, `struct` et `class` sont presque identiques techniquement (seule la
> visibilité par défaut change : `public` pour `struct`, `private` pour `class`). Mais par
> **convention**, on réserve `struct` aux simples paquets de données, et `class` dès qu'il
> y a des règles et des comportements à encapsuler.

---

## ▶️ À toi de jouer

```bash
# Une première classe : Rectangle (constructeur, aire(), perimetre())
g++ -Wall cpp/03_classes_objets/classe.cpp -o classe && ./classe

# Une classe plus parlante : CompteBancaire (solde privé, deposer/retirer/afficher)
g++ -Wall cpp/03_classes_objets/objets.cpp -o objets && ./objets
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : ajoute une méthode
(ex : `doubler()` au Rectangle), crée d'autres objets, essaie de toucher à un attribut
`private` depuis `main` et observe l'**erreur** du compilateur.

➡️ La suite du parcours (fichiers, projets…) arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
