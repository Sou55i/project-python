# Module 02 — Les collections : slices et maps

Jusqu'ici nos variables ne retenaient **qu'une seule valeur** (un âge, un nom). Mais souvent
on veut ranger **plusieurs valeurs ensemble** : une liste de courses, les notes d'une classe,
un annuaire nom → numéro. C'est le rôle des **collections**. En Go, les deux plus utilisées
sont les **slices** (des listes) et les **maps** (des dictionnaires).

> Fichiers du module : `slices.go` (les listes dynamiques) et `maps.go` (les dictionnaires).

> ⚠️ **Important — deux fichiers, deux `func main`.** `slices.go` et `maps.go` sont dans le
> **même dossier** et déclarent **chacun** `package main` et `func main`. C'est OK **à
> condition de les lancer SÉPARÉMENT**, un seul fichier à la fois :
> ```bash
> go run go/02_collections/slices.go   # lance UNIQUEMENT slices.go
> go run go/02_collections/maps.go     # lance UNIQUEMENT maps.go
> ```
> (On ne crée pas de fichier `go.mod` : inutile pour lancer un seul fichier avec `go run`.)

---

## 1. Les SLICES : des listes qui grandissent

Un **slice** est une **suite ordonnée** de valeurs **du même type**. C'est l'équivalent Go
de la **liste** Python. On le note avec des **crochets** devant le type :

```go
var notes []int          // un slice (vide) d'entiers
notes := []int{12, 8, 15} // un slice déjà rempli (forme courte)
prenoms := []string{"Sam", "Lou"} // un slice de chaînes de caractères
```

> 💡 **Slice vs Python.** En Python tu écris `notes = [12, 8, 15]`. En Go, c'est presque
> pareil, sauf qu'il faut **annoncer le type** des éléments : `[]int` = « slice d'entiers ».
> Un slice ne mélange pas les types (que des `int`, ou que des `string`…).

### Ajouter avec `append`

Un slice peut **grandir**. Pour ajouter un élément **à la fin**, on utilise la fonction
intégrée **`append`**. Petit piège à retenir : `append` **renvoie** le nouveau slice, il faut
donc **réaffecter** le résultat dans la variable :

```go
notes = append(notes, 20)   // ajoute 20 à la fin ; on RANGE le résultat dans notes
```

> 💡 En Python tu fais `notes.append(20)` (ça modifie la liste directement). En Go,
> `append` te **rend** la liste agrandie : pense bien à écrire `notes = append(notes, 20)`.

### Connaître la taille avec `len`

```go
len(notes)   // renvoie le nombre d'éléments du slice (comme len() en Python)
notes[0]     // le PREMIER élément (on compte à partir de 0, comme en Python)
```

### Parcourir avec `for ... range`

Pour passer en revue **chaque élément**, on utilise `for` avec le mot-clé **`range`**. Il
donne **deux choses** à chaque tour : l'**indice** (la position) et la **valeur** :

```go
for i, note := range notes {     // i = position (0, 1, 2…), note = la valeur
    fmt.Println(i, note)
}
```

Si l'indice ne t'intéresse pas, remplace-le par un **`_`** (le « tiret du vide ») — sinon Go
râle, car une variable déclarée et non utilisée est **interdite** :

```go
for _, note := range notes {     // on ignore la position, on ne veut que la valeur
    fmt.Println(note)
}
```

> 💡 **Range vs Python.** `for i, note := range notes` ressemble beaucoup au
> `for i, note in enumerate(notes)` de Python.

---

## 2. Les MAPS : des dictionnaires clé → valeur

Une **map** range des paires **clé → valeur**. C'est l'équivalent Go du **dictionnaire**
Python. On déclare le **type de la clé** et le **type de la valeur** :

```go
ages := map[string]int{}          // map vide : clés string, valeurs int
ages := map[string]int{           // map déjà remplie
    "Sam": 30,
    "Lou": 25,
}
```

`map[string]int` se lit : « une map dont les **clés** sont des `string` et les **valeurs**
des `int` ».

### Ajouter et lire

```go
ages["Max"] = 40        // AJOUTER (ou modifier) : on range 40 sous la clé "Max"
age := ages["Sam"]      // LIRE : on récupère la valeur rangée sous "Sam"
```

> 💡 **Map vs Python.** C'est quasi identique au dictionnaire Python :
> `ages = {"Sam": 30}`, puis `ages["Max"] = 40`. La seule nouveauté est d'**annoncer les
> types** : `map[string]int`.

### Tester l'existence avec `valeur, ok := m[clé]`

Attention : si tu lis une clé **qui n'existe pas**, Go ne plante PAS — il renvoie la **valeur
par défaut** du type (0 pour un `int`). Pour savoir si la clé existe **vraiment**, Go offre
une forme spéciale à **deux résultats** :

```go
age, ok := ages["Inconnu"]   // ok = true si la clé existe, false sinon
if ok {
    fmt.Println("Trouve :", age)
} else {
    fmt.Println("Cette cle n'existe pas")
}
```

> 💡 En Python, l'équivalent prudent serait `ages.get("Inconnu")` (qui renvoie `None`) ou
> `"Inconnu" in ages`. En Go, c'est le fameux **« valeur, ok »**.

### Parcourir avec `for ... range`

Sur une map, `range` donne la **clé** puis la **valeur** :

```go
for nom, age := range ages {     // nom = la clé, age = la valeur
    fmt.Println(nom, "a", age, "ans")
}
```

> ⚠️ L'ordre de parcours d'une map n'est **pas garanti** : Go peut te les sortir dans un
> ordre différent à chaque exécution. C'est normal.

---

## 3. Bonus : le package `strings`

Pour manipuler du **texte**, Go fournit une boîte à outils : le package **`strings`** (à
importer avec `import "strings"`). Quelques outils utiles :

```go
strings.ToUpper("salut")          // "SALUT"  (mettre en majuscules)
strings.Contains("chat", "ha")    // true     (contient ?)
strings.Split("a,b,c", ",")       // []string{"a", "b", "c"}  (découper -> slice !)
strings.Join([]string{"a", "b"}, "-") // "a-b"  (recoller un slice en texte)
```

> 💡 Ça rappelle les méthodes de texte de Python (`.upper()`, `.split()`, `"-".join(...)`),
> sauf qu'en Go ce sont des **fonctions** du package `strings`, pas des méthodes du texte.

---

## ▶️ À toi de jouer

⚠️ On lance les fichiers **un par un** (chacun a son propre `func main`) :

```bash
# Le fichier sur les slices (listes dynamiques)
go run go/02_collections/slices.go

# Le fichier sur les maps (dictionnaires)
go run go/02_collections/maps.go
```

Lis les deux fichiers, puis **modifie-les** et **relance** : ajoute des éléments, change les
clés, calcule un total, teste une clé qui n'existe pas.

➡️ La suite du parcours (structures, gestion des erreurs, projets…) arrivera dans le même
style. En attendant, garde sous la main l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
