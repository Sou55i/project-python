# Module 04 — Collections : listes et dictionnaires

Au module 01, tu connaissais déjà les **tableaux** (`int[]`). Leur défaut : leur taille est
**fixée à la création**. Or, très souvent, on ne sait pas à l'avance combien d'éléments on
va stocker (une liste de courses qui s'allonge, un annuaire qui grandit…). Java fournit des
**collections** : des « boîtes » qui **grandissent et rétrécissent toutes seules**.

> Fichier du module : `Collections.java`. On y voit les deux collections les plus utiles :
> la **liste** (`ArrayList`) et le **dictionnaire** (`HashMap`). On compile, puis on lance.

---

## 1. Les GÉNÉRIQUES `<>` : annoncer le type du contenu

Avant les collections, un détail essentiel : les **génériques**, ces chevrons `<>` que tu
vas voir partout. Ils servent à dire **quel type d'éléments** la boîte contient.

```java
List<String> courses;        // une liste qui ne contient QUE des String
Map<String, Integer> ages;   // une map dont les clés sont des String et les valeurs des Integer
```

Pourquoi c'est utile ? Le compilateur t'**empêche** de mettre un nombre dans une liste de
texte, et tu n'as pas à « deviner » ce que tu sors de la boîte. C'est plus sûr.

> ⚠️ Dans les génériques, on n'utilise **pas** `int` mais **`Integer`** (sa version
> « objet »). Pareil : `Double`, `Boolean`, `Character`. Pour `String`, rien ne change.

---

## 2. La LISTE : `List` / `ArrayList`

Une **liste** est une suite **ordonnée** d'éléments, dont la taille **varie**. On la déclare
de type `List<...>` et on la crée avec `new ArrayList<>()`.

```java
List<String> courses = new ArrayList<>();   // <> vide : Java devine le type à gauche
courses.add("pain");        // ajouter à la fin
courses.add("lait");
System.out.println(courses.size());   // 2  → le nombre d'éléments
System.out.println(courses.get(0));   // "pain"  → accès par INDICE (commence à 0)
```

> 💡 **Pourquoi `List` à gauche et `ArrayList` à droite ?** `List` est le **type général**
> (le contrat « c'est une liste »), `ArrayList` est **l'implémentation concrète**. Déclarer
> avec le type général est une bonne habitude : on peut changer d'implémentation plus tard
> sans tout réécrire.

Les méthodes les plus utiles : `add(x)`, `get(i)`, `size()`, `remove(i)`, `contains(x)`.

---

## 3. La boucle FOR-EACH : parcourir sans indice

Pour parcourir une collection, on utilise la boucle **for-each**, qui se lit « **pour chaque**
élément de la collection ». Plus simple et plus sûre qu'un `for (int i = …)` :

```java
for (String c : courses) {     // "pour chaque String c dans courses"
    System.out.println(c);
}
```

> 🆚 C'est l'équivalent du `for x in liste:` de Python, ou du `for _, v := range …` du Go.
> Les deux points `:` se lisent « dans ».

---

## 4. La MAP : `Map` / `HashMap`

Une **map** (dictionnaire) associe une **clé** à une **valeur**, comme un annuaire associe
un nom à un numéro. On la déclare `Map<TypeClé, TypeValeur>` et on la crée avec `new
HashMap<>()`.

```java
Map<String, Integer> ages = new HashMap<>();
ages.put("Lou", 30);                  // ranger une paire clé -> valeur
ages.put("Sam", 25);

System.out.println(ages.get("Lou"));          // 30  → lire par CLÉ
System.out.println(ages.containsKey("Sam"));  // true → la clé existe-t-elle ?
```

Les méthodes utiles : `put(clé, valeur)`, `get(clé)`, `containsKey(clé)`, `remove(clé)`,
`size()`.

> 🆚 C'est le `dict` de Python (`{"Lou": 30}`) ou la `map` du Go.

---

## 5. Parcourir une MAP

Deux façons, selon ce qu'on veut :

```java
// (a) juste les CLÉS
for (String nom : ages.keySet()) {
    System.out.println(nom);
}

// (b) les PAIRES clé/valeur ensemble
for (Map.Entry<String, Integer> e : ages.entrySet()) {
    System.out.println(e.getKey() + " a " + e.getValue() + " ans");
}
```

Chaque `e` est une **Entry** : `e.getKey()` donne la clé, `e.getValue()` donne la valeur.

> ⚠️ Une `HashMap` **ne garde pas l'ordre** d'insertion : ne compte pas sur un ordre précis
> en la parcourant. Si l'ordre importe, il existe `LinkedHashMap` (ordre d'insertion) ou
> `TreeMap` (ordre trié) — pour plus tard.

---

## 6. 🆚 Tableau vs collection : quand utiliser quoi ?

| | Tableau `int[]` | `ArrayList` / `HashMap` |
|--|-----------------|-------------------------|
| Taille | **fixe** dès la création | **variable** (grandit/rétrécit) |
| Ajout/retrait | manuel, pénible | `add` / `put` / `remove` |
| Contenu | types de base (`int`, …) | objets (`String`, `Integer`, …) via `<>` |
| Import nécessaire | non | oui (`java.util.*`) |

Retiens : **tableau** quand la taille est connue et fixe ; **collection** dès que ça bouge.

---

## ▶️ À toi de jouer

```bash
# Listes (ArrayList) + maps (HashMap) + for-each + génériques
javac -d /tmp/jb java/04_collections/Collections.java
java -cp /tmp/jb Collections
```

Lis le fichier, puis **modifie-le** et **recompile** : ajoute un article à la liste, retire
une personne de la map avec `ages.remove("Max")`, ou crée une `List<Integer>` de nombres et
affiche leur somme dans une boucle for-each.

➡️ Module suivant : [`05_exceptions`](../05_exceptions/).
