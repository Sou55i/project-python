# Module 04 — Erreurs & interfaces

Deux notions très « Go » qui changent des autres langages : la façon de **gérer les
erreurs** (sans exceptions) et les **interfaces** (un système de « contrats » très souple).

> Fichiers du module : `erreurs.go` (une fonction qui peut échouer) et `interfaces.go`
> (plusieurs types traités via un même contrat).
> ⚠️ Chaque fichier a son propre `func main` : on les lance **séparément** avec `go run`.

---

## 1. La gestion des erreurs : pas d'exceptions, mais une valeur `error`

Dans beaucoup de langages (Python, C++…), quand quelque chose échoue, le programme « lève
une exception ». **Go fait autrement** : une fonction qui peut échouer **renvoie deux
choses** — son résultat **et** une valeur de type `error`.

```go
func diviser(a float64, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division par zero impossible")  // échec
    }
    return a / b, nil   // succès : nil = "aucune erreur"
}
```

- `error` vaut **`nil`** quand tout va bien.
- Sinon, elle contient le **détail** du problème.

Côté appelant, on **teste toujours** l'erreur **avant** d'utiliser le résultat :

```go
resultat, err := diviser(10, 0)
if err != nil {                 // LA ligne réflexe en Go
    fmt.Println("Erreur :", err)
} else {
    fmt.Println(resultat)
}
```

> 🧠 Le motif `if err != nil { ... }` est **partout** en Go. C'est explicite : on voit
> dans le code, à chaque appel risqué, comment l'échec est traité.

Pour **créer** une erreur :
- `errors.New("message")` — un message fixe.
- `fmt.Errorf("... %q ...", valeur)` — un message qui **contient une valeur** (comme
  `Printf`, mais il fabrique une erreur au lieu d'afficher).

---

## 2. Les interfaces : un « contrat » de comportement

Une **interface** liste des **méthodes** (un contrat). **Tout type qui possède ces
méthodes satisfait l'interface — automatiquement**, sans rien déclarer de spécial.

🔌 **Analogie : la prise électrique.** La prise se moque de l'appareil branché (lampe,
chargeur, grille-pain). Tout ce qui compte, c'est qu'il ait **la bonne fiche**. L'interface,
c'est la forme de la fiche ; le type, c'est l'appareil.

```go
// Le contrat : "est une Forme tout ce qui sait calculer son Aire()".
type Forme interface {
    Aire() float64
}

type Rectangle struct{ largeur, hauteur float64 }
type Cercle struct{ rayon float64 }

// Rectangle satisfait Forme car il a une méthode Aire()...
func (r Rectangle) Aire() float64 { return r.largeur * r.hauteur }
// ...et Cercle aussi.
func (c Cercle) Aire() float64 { return 3.14159 * c.rayon * c.rayon }
```

On peut alors écrire **une seule fonction** qui marche pour **tous** les types respectant le
contrat :

```go
func decrire(f Forme) {
    fmt.Printf("aire = %.2f\n", f.Aire())
}

decrire(Rectangle{3, 4})   // marche
decrire(Cercle{2})          // marche aussi
```

> 💡 Différence clé avec d'autres langages : en Go, un type n'a **pas besoin de dire**
> « j'implémente Forme ». S'il a la méthode `Aire()`, **il satisfait le contrat, point.**
> C'est ce qu'on appelle le *duck typing* statique : « si ça fait coin-coin comme un
> canard, c'est un canard ».

---

## ▶️ À toi de jouer

```bash
# La gestion des erreurs (cas qui réussit, cas qui échoue, fmt.Errorf)
go run go/04_erreurs_interfaces/erreurs.go

# Les interfaces (Rectangle et Cercle traités via le contrat Forme)
go run go/04_erreurs_interfaces/interfaces.go
```

Lis les deux fichiers, puis **modifie-les** : ajoute un type `Triangle` qui satisfait
`Forme`, ou une fonction qui peut échouer (ex. une racine carrée d'un nombre négatif) et
gère son erreur avec `if err != nil`.

➡️ La suite du parcours arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe Go en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots de Go expliqués simplement.
