# 🃏 Aide-mémoire Go (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle du Go. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `01_les_bases`, `02_collections`…

---

## Lancer un programme

```bash
go run fichier.go      # compile EN MÉMOIRE puis exécute (le plus simple)
go build fichier.go    # fabrique un exécutable à garder (./fichier)
go version             # vérifier que Go est installé
```

## Structure minimale d'un programme

```go
package main           // tout programme exécutable est dans le package "main"

import "fmt"           // on ouvre la boîte à outils "fmt" (affichage)

func main() {          // main = le point de départ, lancé automatiquement
    fmt.Println("Bonjour")
}
```

> ⚠️ Go REFUSE de compiler s'il y a un `import` inutilisé OU une variable déclarée et
> jamais utilisée. Ça garde le code propre.

## Variables et types

```go
var age int = 30   // forme LONGUE : var, nom, type, valeur
age := 30          // forme COURTE : Go DEVINE le type (uniquement dans une fonction)

// Types de base
int        // entier            42
float64    // décimal           3.14
string     // texte             "salut"
bool       // vrai / faux       true, false

float64(x) // CONVERSION : transforme x en float64 (Go ne convertit pas tout seul)
```

## Afficher avec `fmt`

```go
fmt.Println("Age :", age)          // simple, ajoute un saut de ligne, sépare par espaces
fmt.Printf("Age : %d ans\n", age)  // précis ; \n = saut de ligne (Printf n'en ajoute pas)
```

| Verbe | Type affiché |
|-------|--------------|
| `%d`  | entier (`int`) |
| `%f`  | décimal (`%.2f` = 2 décimales) |
| `%s`  | texte (`string`) |
| `%t`  | booléen (`bool`) |
| `%v`  | n'importe quelle valeur (format par défaut) |

## Conditions

```go
if note >= 16 {              // PAS de parenthèses autour de la condition…
    fmt.Println("Tres bien")
} else if note >= 10 {       // …mais accolades { } OBLIGATOIRES
    fmt.Println("Recu")
} else {
    fmt.Println("A revoir")
}
// Comparaisons : ==  !=  <  >  <=  >=    Logique : && (ET)  || (OU)  ! (NON)
```

## Boucles : Go n'a QUE `for` (3 formes)

```go
for i := 0; i < 3; i++ {     // 1. classique : début ; condition ; pas
    fmt.Println(i)
}

for x < 10 {                 // 2. une seule condition = le "while" des autres langages
    x++
}

for {                        // 3. sans condition = infinie, arrêtée par break
    break
}
```

## Fonctions

```go
func additionner(a int, b int) int {  // (params) puis le type de RETOUR
    return a + b
}

func saluer() {              // pas de type après () = ne renvoie rien
    fmt.Println("Bonjour !")
}
```

## Slices (listes dynamiques)

```go
notes := []int{12, 8, 15}        // créer (rempli)
var noms []string                // créer (vide)
notes = append(notes, 20)        // AJOUTER à la fin (réaffecter le résultat !)
len(notes)                       // nombre d'éléments
notes[0]                         // premier élément (on compte à partir de 0)

for i, note := range notes {     // parcourir : i = position, note = valeur
    fmt.Println(i, note)
}
for _, note := range notes {     // "_" = on ignore la position
    fmt.Println(note)
}
```

## Maps (dictionnaires clé → valeur)

```go
ages := map[string]int{"Sam": 30}   // créer ; clés string, valeurs int
ages["Max"] = 40                     // AJOUTER / modifier
age := ages["Sam"]                   // LIRE

age, ok := ages["Inconnu"]           // TESTER : ok = true si la clé existe
if ok { fmt.Println(age) }

for cle, valeur := range ages {      // parcourir (ordre NON garanti)
    fmt.Println(cle, valeur)
}
```

## Texte : le package `strings`

```go
import "strings"
strings.ToUpper("salut")               // "SALUT"
strings.Contains("chat", "ha")         // true
strings.Split("a,b,c", ",")            // []string{"a","b","c"}
strings.Join([]string{"a", "b"}, "-")  // "a-b"
```

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) pour le sens des mots.
