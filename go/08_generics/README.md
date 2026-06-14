# Module avancé 08 — Les génériques (type parameters)

Bienvenue dans ton **premier module avancé** ! Tu as déjà vu les fonctions, les slices, les
interfaces… Ici on franchit une marche : on va apprendre à écrire **une seule fonction qui
marche pour PLUSIEURS types** à la fois. En Go, ça s'appelle les **génériques** (apparus dans
**Go 1.18** ; tu es en **Go 1.24**, donc tout fonctionne).

> Fichiers du module : `generics.go` (une fonction générique toute simple) et
> `contraintes.go` (une contrainte personnalisée pour additionner des nombres).
> ⚠️ Chaque fichier a son propre `package main` et son propre `func main`, dans le **même
> dossier** : on les lance **séparément** avec `go run` (pas de `go.mod` ici, c'est voulu).

---

## 1. Le problème : on réécrit toujours la même fonction

Imagine une fonction qui renvoie le **premier élément** d'une liste. Tu l'écris pour des
entiers :

```go
func PremierInt(s []int) int { return s[0] }
```

Puis tu en as besoin pour des `float64`… et pour des `string`… À chaque fois, **le même code**,
juste le type qui change :

```go
func PremierFloat(s []float64) float64 { return s[0] }
func PremierString(s []string) string { return s[0] }
```

C'est **pénible** et **répétitif**. On aimerait écrire la logique **une seule fois**.

> 🍪 **Analogie : l'emporte-pièce.** Un emporte-pièce en forme d'étoile découpe des étoiles,
> peu importe la **pâte** (chocolat, vanille, citron). La **forme** (la logique) est la même ;
> seul l'**ingrédient** (le type) change. Un générique, c'est cet emporte-pièce : une logique,
> plusieurs types.

---

## 2. La solution : un « paramètre de type » `[T ...]`

Un **générique** ajoute, entre crochets, un **paramètre de type** : un nom (souvent `T`, pour
*Type*) qui **représente n'importe quel type**, décidé au moment de l'appel.

```go
func Premier[T any](s []T) T {
    return s[0]
}
```

Décortiquons :

- **`[T any]`** : on déclare un paramètre de type nommé `T`. Le mot `any` est sa **contrainte**
  (voir plus bas) : ici, « `T` peut être **n'importe quel** type ».
- **`s []T`** : le paramètre `s` est une liste **du** type `T`.
- **`T`** (avant `{`) : la fonction **renvoie** une valeur de ce même type `T`.

À l'appel, Go **devine `T` tout seul** d'après ce que tu lui passes :

```go
Premier([]int{10, 20, 30})       // T devient int    -> renvoie 10
Premier([]string{"a", "b"})       // T devient string -> renvoie "a"
```

> 🧠 `T` n'est **pas** un vrai type : c'est un **emplacement** que Go remplit par le bon type à
> chaque appel. Comme une case « ____ » qu'on remplit au dernier moment.

---

## 3. Les contraintes : limiter les types acceptés

`any` veut dire « tout type ». Mais parfois c'est **trop large**. Si ta fonction fait `a + b`,
elle ne peut PAS accepter `bool` (on n'additionne pas des `true`/`false` !). Il faut donc
**restreindre** les types autorisés : c'est le rôle d'une **contrainte**.

Une contrainte répond à la question : **« quels types ai-je le droit de mettre dans `T` ? »**

Trois contraintes utiles à connaître :

- **`any`** : absolument tous les types (c'est le cas le plus permissif).
- **`comparable`** : les types qu'on peut comparer avec `==` et `!=` (utile pour les clés de map,
  par exemple).
- **une contrainte personnalisée** : tu la fabriques toi-même avec une **interface** qui liste
  des types, séparés par `|` (« ou ») :

```go
type Nombre interface {
    ~int | ~int64 | ~float64
}
```

Ça se lit : « est un `Nombre` tout type qui est un `int`, un `int64` **ou** un `float64` ».

> 🔵 **Le `~` (tilde), à quoi ça sert ?** Il veut dire « ce type **OU tout type construit à
> partir de lui** ». Si tu écris `type Age int`, alors `Age` est « basé sur `int` » : grâce au
> `~int`, il est **lui aussi** accepté. Sans le `~`, seul `int` pile-poil passerait.

---

## 4. Mettre une contrainte au travail

Une fois la contrainte définie, on l'utilise **à la place de `any`** :

```go
func Somme[T Nombre](s []T) T {
    var total T          // total démarre à la "valeur zéro" du type T (0, 0.0...)
    for _, v := range s {
        total += v       // autorisé : la contrainte Nombre garantit que + existe
    }
    return total
}
```

Comme `T` est contraint à des `Nombre`, le compilateur **sait** que `+=` est permis. Si tu
tentais `Somme([]string{...})`, Go **refuserait de compiler** : `string` n'est pas un `Nombre`.
C'est tout l'intérêt : la contrainte **protège** ta fonction des types qui n'ont pas de sens.

---

## 5. Génériques vs interfaces : quelle différence ?

Tu te souviens des **interfaces** (module 04) ? Elles aussi permettent un « même code pour
plusieurs types ». La différence :

- une **interface** dit « ce type sait faire telle **méthode** » (un *comportement*) ;
- un **générique** dit « ce code marche pour ce **type** lui-même » (et garde le type **exact**,
  pas une boîte abstraite).

En pratique : interface quand tu veux des **comportements** partagés ; générique quand tu veux
**la même logique** appliquée à des types variés (souvent des conteneurs : listes, paires…).

---

## ▶️ À toi de jouer

⚠️ Les deux fichiers ont **chacun** leur `package main` et leur `func main`, dans le **même
dossier**. On ne peut donc **pas** lancer le dossier entier : on les lance **séparément**, en
nommant le fichier. (Pas de `go.mod` ici, c'est volontaire : on reste sur de simples fichiers.)

Lance les commandes **DEPUIS LA RACINE** du dépôt (le dossier qui contient `go/`) :

```bash
# Une fonction générique simple, appelée sur des int PUIS des string :
go run go/08_generics/generics.go

# Une contrainte personnalisée Nombre + une fonction Somme générique :
go run go/08_generics/contraintes.go
```

Lis les deux fichiers, puis **modifie-les** : ajoute un appel de `Premier` sur une liste de
`float64`, ou écris ta propre fonction générique `Dernier[T any](s []T) T`. Tu peux aussi
ajouter `~float32` à la contrainte `Nombre` et faire une somme de `float32`.

➡️ D'autres modules avancés arriveront dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe Go en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots de Go expliqués simplement.
