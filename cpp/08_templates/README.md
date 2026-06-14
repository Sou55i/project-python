# Module 08 (avancé) — Les TEMPLATES : écrire du code générique

Bravo, tu arrives dans les **modules avancés** ! Jusqu'ici, quand tu écrivais une fonction,
tu devais choisir **un type précis** : `int maximum(int a, int b)` ne marche qu'avec des
`int`. Si tu voulais la même chose pour des `double`, tu devais **réécrire** une deuxième
fonction quasi identique… puis une troisième pour les `std::string`… Quelle corvée !

Les **templates** (en français : « modèles » ou « patrons ») résolvent exactement ce
problème : tu écris ton code **une seule fois**, de façon **générique**, et il marche
**pour n'importe quel type**.

> Fichiers du module : `fonctions_templates.cpp` (une fonction générique `maximum<T>` qui
> marche avec `int`, `double` et `std::string`) et `classe_template.cpp` (une petite classe
> générique `Boite<T>` qui range une valeur de n'importe quel type). Lis ce README, puis
> compile et lance (voir en bas).

---

## 1. C'est quoi un TEMPLATE ? Un MOULE à code

Pense à un **moule à gâteau**. Le moule a une **forme** (un cœur, un rond, une étoile…),
mais il **ne décide pas** de la pâte que tu verses dedans : pâte au chocolat, à la vanille,
aux amandes… **Le même moule** produit un gâteau quelle que soit la pâte. La forme est
**fixe**, l'ingrédient est **libre**.

Un **template**, c'est pareil pour le code :

- la **logique** est fixe (par exemple : « renvoyer le plus grand des deux ») ;
- le **type** des données est **libre** (`int`, `double`, `std::string`…).

```
   TEMPLATE  maximum<T>      ──►  un MOULE : "renvoie le plus grand de a et b"
                  │                          (T = un type, encore inconnu)
                  │
                  ├──►  maximum<int>     ← le compilateur "coule" la version int
                  ├──►  maximum<double>  ← … la version double
                  └──►  maximum<std::string>  ← … la version texte
```

Le mot-clé magique, c'est **`template<typename T>`** :

- `template` annonce « attention, ce qui suit est un **moule**, pas du code définitif » ;
- `typename T` veut dire « **T** est un **type au choix**, on décidera plus tard lequel ».
  `T` est juste un **nom** (on aurait pu écrire `U`, `Type`…), mais `T` est la tradition.

> 💡 C'est le **compilateur** qui, en voyant `maximum(3, 5)`, fabrique tout seul la version
> `int` du moule. On appelle ça **l'instanciation** du template. Tu écris le moule **une
> fois**, lui génère **autant de versions** que de types utilisés.

---

## 2. Une FONCTION template (généricité côté fonctions)

Voici le moule d'une fonction qui renvoie le plus grand de deux valeurs :

```cpp
template<typename T>          // "T = un type au choix"
T maximum(T a, T b) {         // a et b sont de ce type T, et on renvoie un T
    if (a > b) {
        return a;
    }
    return b;
}
```

On l'appelle ensuite comme une fonction normale — le compilateur **devine** `T` tout seul
à partir des arguments :

```cpp
std::cout << maximum(3, 9) << std::endl;          // T = int    -> 9
std::cout << maximum(2.5, 1.5) << std::endl;      // T = double -> 2.5
std::string a = "abricot", b = "banane";
std::cout << maximum(a, b) << std::endl;          // T = std::string -> banane
```

Une **seule** définition, et elle marche pour les trois types ! (Pour `std::string`, le
`>` compare dans l'**ordre alphabétique** : c'est pour ça que `"banane"` « gagne ».)

> 💬 En Python, tu n'avais pas ce souci : `def maximum(a, b)` acceptait déjà n'importe quoi,
> car les types sont dynamiques. En C++, les types sont **statiques** (fixés à la
> compilation) : le template est la façon propre de retrouver cette **souplesse**, sans
> perdre la **vérification des types** par le compilateur.

---

## 3. Une CLASSE template (généricité côté classes)

On peut aussi rendre **une classe entière** générique. Exemple : une `Boite<T>` qui **range
une valeur** de n'importe quel type.

```cpp
template<typename T>     // la classe tout entière dépend d'un type T
class Boite {
private:
    T contenu;           // l'attribut est de type T (int, double, std::string…)

public:
    Boite(T valeur) {    // le constructeur reçoit une valeur de type T
        contenu = valeur;
    }
    T lire() {           // une méthode qui renvoie le contenu (de type T)
        return contenu;
    }
};
```

À l'usage, on **précise le type entre `< >`** au moment de créer l'objet :

```cpp
Boite<int> b1(42);                 // une boîte qui range un int
Boite<std::string> b2("coucou");   // une boîte qui range du texte
std::cout << b1.lire() << std::endl;   // 42
std::cout << b2.lire() << std::endl;   // coucou
```

> 💡 Tu as **déjà** utilisé des classes templates sans le savoir ! `std::vector<int>`,
> `std::map<std::string, int>`… ce sont des **classes templates** : les `< >` servent
> justement à dire **quel type** ranger.

---

## 4. Pourquoi c'est utile ? (et le lien avec la STL)

Sans template, pour couvrir 3 types, tu écrirais 3 fonctions quasi identiques — donc 3 fois
plus de code à écrire, à relire et à **corriger** en cas de bug. Avec un template : **un
seul** endroit.

| Tu veux… | Sans template | Avec template |
|----------|---------------|---------------|
| `maximum` pour `int`, `double`, `string` | 3 fonctions copiées-collées | **1** fonction `maximum<T>` |
| Une boîte pour ranger n'importe quoi | une classe par type | **1** classe `Boite<T>` |
| Corriger un bug dans la logique | le corriger 3 fois | le corriger **1 fois** |

Et surtout : **toute la STL du module 06 est faite de templates !** Quand tu écris
`std::vector<int>` ou `std::map<std::string, int>`, tu **utilises** des moules génériques
que les créateurs du C++ ont écrits **une seule fois** pour qu'ils marchent avec **tous**
les types. Le `T` que tu apprends ici, c'est exactement ce qui se cache derrière les `< >`
de la STL.

> 💬 Rappelle-toi : **STL** = **S**tandard **T**emplate **L**ibrary. Le mot « Template »
> est même dans son nom ! Tu sais maintenant ce qu'il veut dire.

---

## ▶️ À toi de jouer

Depuis la **racine du dépôt** (le dossier qui contient `cpp/`) :

```bash
# 1. Une fonction générique maximum<T> appelée avec int, double et std::string
g++ -std=c++17 -Wall cpp/08_templates/fonctions_templates.cpp -o fonctions_templates && ./fonctions_templates

# 2. Une classe générique Boite<T> qui range une valeur de n'importe quel type
g++ -std=c++17 -Wall cpp/08_templates/classe_template.cpp -o classe_template && ./classe_template
```

Ensuite, **modifie** : ajoute un appel `maximum(...)` avec deux `char` (`'a'` et `'z'`),
crée une `Boite<double>`, ou ajoute une méthode `remplacer(T nouvelle)` à la `Boite`. Tu
verras : le moule s'adapte tout seul.

➡️ D'autres modules avancés viendront dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
