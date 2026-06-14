# 🧭 Anatomie d'un programme Go : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire quelques lignes de Go, mais ne savent pas **dans quel
ordre les ranger** pour former un programme complet et propre. Ce guide explique le
**squelette standard** d'un fichier Go, du `package` en haut jusqu'à `func main()`.

> 📌 À lire après les modules `00_demarrer` et `01_les_bases`, et à garder sous la main
> comme aide-mémoire. Garde aussi à portée l'[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) et le
> [GLOSSAIRE.md](./GLOSSAIRE.md).

---

## 1. LA règle d'or : on lit de HAUT en BAS… avec une nuance importante

Comme partout, on **lit** un fichier de haut en bas, comme une page. Garder ses blocs
**dans un ordre logique** (les outils en haut, le point d'entrée en bas) rend le code
beaucoup plus facile à comprendre.

> 🆚 **Mais attention, gros piège quand on vient de Python !** En Python, une chose doit
> exister **avant** qu'on l'utilise (Python exécute ligne par ligne, de haut en bas).
> **En Go, ce n'est PAS le cas pour les fonctions, types et constantes.**

En Go, tout ce qui est écrit dans le **même `package`** (souvent : le même dossier) **se
voit mutuellement**, peu importe l'ordre dans le fichier. Le compilateur lit **tout le
fichier d'abord**, puis range tout, et **ensuite seulement** il lance le programme.

```go
package main

import "fmt"

func main() {
    direBonjour()   // ✅ ça marche, MÊME SI direBonjour est définie PLUS BAS
}

func direBonjour() {
    fmt.Println("Bonjour !")
}
```

En Python, appeler une fonction définie **plus bas** planterait. En Go, **aucun
problème** : `main` peut appeler `direBonjour` même si elle est écrite après.

> 💡 **À retenir :** l'ordre des fonctions dans le fichier **n'a pas d'importance pour le
> compilateur**. Mais il a de l'importance **pour l'humain qui te lit** (et c'est souvent
> toi, plus tard !). On garde donc un ordre **propre et conventionnel** : c'est l'objet de
> ce guide.

---

## 2. Le squelette standard d'un fichier Go

Presque tous les programmes Go bien écrits suivent **ce même ordre**, de haut en bas :

```go
// ╔══════════════════════════════════════════════════════════════╗

package main                          // (1) DÉCLARATION DU PACKAGE
                                      //     "main" = programme lançable

import (                              // (2) LES IMPORTS
    "fmt"                             //     les caisses à outils qu'on
    "strings"                         //     va utiliser
)

const TauxTVA = 0.20                  // (3) LES CONSTANTES
const NomApp = "MaCalculette"         //     valeurs fixes, qui ne changent jamais

type Article struct {                 // (4) LES TYPES / STRUCTS
    Nom  string                       //     les "modèles de fiches" qu'on invente
    Prix float64
}

func prixTTC(prixHT float64) float64 { // (5) LES FONCTIONS (et méthodes)
    return prixHT * (1 + TauxTVA)      //     on les DÉFINIT ici
}

func main() {                         // (6) func main() : LE POINT D'ENTRÉE
    a := Article{Nom: "Stylo", Prix: 2.0}
    fmt.Println(a.Nom, "coûte", prixTTC(a.Prix), "TTC")
}

// ╚══════════════════════════════════════════════════════════════╝
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Rôle et pourquoi il est là |
|------|------|----------------------------|
| 1 | **`package main`** | La **toute 1re ligne** d'un fichier Go (obligatoire). Elle dit à quel **package** (= groupe de fichiers) ce fichier appartient. `main` est le package **spécial** : c'est le seul qui produit un **programme lançable**. |
| 2 | **`import`** | On **ouvre les caisses à outils** dont on a besoin (`fmt` pour afficher, `strings` pour le texte…) **avant** de s'en servir. On les met juste après le `package`, par convention. |
| 3 | **Constantes (`const`)** | Les **valeurs fixes** qui ne changeront jamais (un taux, un nom d'appli). Regroupées en haut pour les retrouver et les modifier facilement. |
| 4 | **Types / `struct`** | Les **modèles** qu'on invente (cf. module [`03_structs_methodes`](./03_structs_methodes/)). On les place avant les fonctions car les fonctions s'en servent souvent. |
| 5 | **Fonctions et méthodes** | On **définit** les actions réutilisables. ⚠️ Définir ≠ exécuter : le code d'une fonction ne tourne que lorsqu'on l'**appelle**. |
| 6 | **`func main()`** | Le **chef d'orchestre** : le point où le programme **démarre vraiment**. On le met tout en bas, c'est lui qui appelle les fonctions dans le bon ordre. |

> 💡 « Définir une fonction » = écrire la recette. « Appeler la fonction » = cuisiner le
> plat. On écrit toutes les recettes plus haut, puis le `main` les utilise.

> 📌 **Rappel honnête :** comme vu en partie 1, le compilateur **accepterait** un autre
> ordre. Cet ordre-là est une **convention de lisibilité**, pas une obligation technique.
> Suis-le quand même : tous les programmes Go se ressemblent ainsi, et ça aide tout le
> monde.

---

## 3. Go est COMPILÉ — et le compilateur est (gentiment) sévère

Rappel du [README](./README.md) : **Python est interprété**, **Go est compilé** (traduit
en langage machine avant de tourner). La commande `go run` fait les **deux d'un coup** :
elle **compile** ton fichier, puis le **lance** immédiatement.

```bash
go run go/00_demarrer/premier_programme.go   # compile PUIS exécute, en une commande
```

### Le compilateur REFUSE les imports et variables inutilisés

C'est une particularité qui surprend au début : si tu importes un outil **sans t'en
servir**, ou si tu crées une variable **que tu n'utilises jamais**, le programme
**refuse de compiler**.

```go
import "strings"   // ❌ erreur : "imported and not used: strings"
                   //    (si tu n'appelles jamais strings.quelquechose)

func main() {
    x := 42        // ❌ erreur : "declared and not used: x"
                   //    (si tu n'utilises jamais x ensuite)
}
```

> ✅ **Pourquoi c'est une BONNE chose ?** Ça t'oblige à garder un code **propre, sans
> déchets**. Pas d'import oublié qui traîne, pas de variable morte qui sème le doute.
> Beaucoup de bugs viennent de variables qu'on croyait utiliser : Go te les signale **tout
> de suite**, au lieu de te laisser deviner plus tard. Au début ça agace, vite ça rassure.

---

## 4. Le rôle de `func main()` dans le package `main`

`func main()` est le **point d'entrée** du programme : c'est **exactement** la ligne par
laquelle Go commence à exécuter ton code.

- Elle doit s'appeler **`main`**, sans paramètre ni valeur de retour : `func main() { … }`.
- Elle doit se trouver dans un fichier qui déclare **`package main`**.
- **Sans** `package main` **et** `func main()`, Go ne sait pas par où démarrer : il ne
  produit pas de programme lançable.

> 🐍 **Équivalent Python.** En Python, on écrivait le « démarrage » dans
> `if __name__ == "__main__":` tout en bas. En Go, ce rôle de point de départ est tenu par
> `func main()`. C'est **le** bloc qui « démarre tout ».

---

## 5. La logique INTERNE : entrée → traitement → sortie

À l'intérieur de `main` (ou d'une fonction), le code suit presque toujours **3 phases**,
dans cet ordre :

```
   1. ENTRÉE              2. TRAITEMENT             3. SORTIE
   (je récupère           (je calcule, je décide,   (j'affiche ou
    les données)           je transforme)            j'enregistre)
   ──────────             ───────────────          ──────────
   fmt.Scan(&x)           if / else, switch         fmt.Println(...)
   os.ReadFile(...)       for                       fmt.Printf(...)
   os.Args                calculs, appels de        os.WriteFile(...)
   bufio.Scanner          fonctions
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

> 🔧 La lecture clavier (`fmt.Scan`) et les fichiers (`os.ReadFile`, `os.WriteFile`,
> `bufio.Scanner`) sont détaillés dans le module [`05_fichiers`](./05_fichiers/).

---

## 6. Comment lire un programme Go complexe qu'on découvre

Quand un programme te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Trouve `func main()`.** C'est le **point de départ** réel du programme : il montre
   l'enchaînement principal. (En Go, peu importe où il est dans le fichier — souvent en bas
   par convention.)
2. **Suis les appels de fonctions** depuis `main`. Quand tu vois `prixTTC(a.Prix)`, va lire
   la fonction `func prixTTC` pour comprendre ce qu'elle fait — qu'elle soit écrite plus
   haut **ou** plus bas, ça n'a pas d'importance.
3. **Repère les `type … struct`** : ils te disent quelles **données** le programme
   manipule. Comprendre les structs, c'est souvent comprendre la moitié du programme.
4. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le `main`),
> puis tu ouvres les chapitres qui t'intéressent (les fonctions et les structs).

---

## 7. Récapitulatif visuel

```
┌─────────────────────────────────────────────┐
│ 1. package main     : programme lançable      │
│ 2. import (...)     : les outils              │  ← on prépare
│ 3. const ...        : les valeurs fixes       │
├─────────────────────────────────────────────┤
│ 4. type ... struct  : les modèles de données  │  ← on outille
│ 5. func ...         : on DÉFINIT les actions   │
├─────────────────────────────────────────────┤
│ 6. func main() {                              │
│        entrée  ->  traitement  ->  sortie     │  ← on EXÉCUTE
│    }                                          │     (point d'entrée)
└─────────────────────────────────────────────┘
   On LIT de haut en bas (pour l'humain),
   mais le compilateur voit TOUT le package :
   l'ordre des fonctions ne le gêne pas.
```

➡️ Garde ce squelette en tête pour démarrer tes propres programmes du bon pied, et
reviens-y dès qu'un fichier Go te semble désordonné.
