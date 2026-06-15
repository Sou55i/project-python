# Module 02 — Objets et tableaux : ranger les données

Jusqu'ici, une variable contenait **une seule** valeur (un nombre, un texte…).
Mais dans la vraie vie, on manipule des **paquets** de données : une fiche client,
une liste de courses, une collection de notes… Pour ça, JavaScript nous donne
deux outils essentiels : les **objets** et les **tableaux**.

---

## 1. Les tableaux `[ ]` : une liste ordonnée

Un **tableau** (en anglais *array*) est une **suite ordonnée** de valeurs, écrite
entre **crochets** `[ ]`, séparées par des virgules.

```javascript
const fruits = ["pomme", "banane", "cerise"];
```

Chaque valeur a une **position**, appelée **indice** (*index*). Attention :
**on compte à partir de 0**, pas de 1 !

```
   indice :     0          1          2
   valeur : "pomme"   "banane"   "cerise"
```

On accède à une valeur avec son indice entre crochets :

```javascript
fruits[0];   // "pomme"  (le PREMIER)
fruits[2];   // "cerise" (le TROISIÈME)
fruits.length; // 3  (le NOMBRE d'éléments)
```

---

## 2. Les objets `{ }` : des étiquettes clé → valeur

Un **objet** regroupe des informations sous forme de **paires** `clé: valeur`,
entre **accolades** `{ }`. Pense à une fiche d'identité :

```javascript
const personne = {
  prenom: "Alice",   // la clé "prenom" a pour valeur "Alice"
  age: 30,           // la clé "age" a pour valeur 30
  majeur: true,
};
```

On accède à une valeur par sa **clé** (et non par une position) :

```javascript
personne.prenom;      // "Alice"  (notation avec un point, la plus courante)
personne["age"];      // 30       (notation avec des crochets, équivalente)
```

> 💡 **Tableau ou objet ?** Un tableau, c'est *plusieurs choses du même genre*
> dans un ordre (une liste de fruits). Un objet, c'est *une seule chose décrite
> par plusieurs propriétés* (une personne avec un prénom, un âge…).

On peut combiner les deux : un **tableau d'objets** est extrêmement courant.

```javascript
const equipe = [
  { prenom: "Alice", age: 30 },
  { prenom: "Bob", age: 25 },
];
```

---

## 3. Les méthodes utiles des tableaux

Une **méthode** est une fonction « attachée » à une valeur, qu'on appelle avec
un point : `monTableau.maMethode(...)`. Voici les indispensables.

| Méthode | À quoi ça sert |
|---------|----------------|
| `push(x)` | **Ajoute** `x` à la fin du tableau |
| `map(fn)` | **Transforme** chaque élément → renvoie un **nouveau** tableau |
| `filter(fn)` | **Garde** les éléments qui passent un test → nouveau tableau |
| `reduce(fn, init)` | **Combine** tous les éléments en **une seule** valeur (somme…) |
| `find(fn)` | Renvoie le **premier** élément qui passe un test |

> 📌 `map`, `filter`, `reduce` et `find` ne **modifient pas** le tableau de départ :
> elles renvoient un nouveau résultat. C'est une bonne habitude (moins de bugs).

---

## 4. JSON : convertir un objet en texte (et l'inverse)

**JSON** (*JavaScript Object Notation*) est un format **texte** pour représenter
des objets et tableaux. C'est le langage universel pour **échanger des données**
(entre un serveur et une appli, dans un fichier de configuration…).

- `JSON.stringify(valeur)` → transforme un objet/tableau en **texte**.
- `JSON.parse(texte)` → transforme un **texte** JSON en objet/tableau.

```javascript
const texte = JSON.stringify({ prenom: "Alice" }); // '{"prenom":"Alice"}'
const obj   = JSON.parse('{"age":30}');            // { age: 30 }
```

> 💬 Pratique : `JSON.stringify(valeur, null, 2)` ajoute des retours à la ligne et
> une indentation de 2 espaces → c'est plus **lisible** pour un humain.

---

## ▶️ À toi de jouer

Lis puis lance les deux fichiers (chaque ligne est commentée) :

```bash
node js-ts/02_objets_tableaux/objets.js
node js-ts/02_objets_tableaux/tableaux.js
```

Essaie ensuite d'ajouter un fruit, une personne, ou de modifier un filtre, puis
relance pour observer le changement.

➡️ Module suivant : [`03_fonctions_avancees`](../03_fonctions_avancees/).
