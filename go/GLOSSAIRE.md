# 📖 Glossaire — les mots du Go expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours de Go ? Cherche-le ici. Les
termes sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**`:=` (déclaration courte)** — La façon courte de créer une variable **et** lui donner une
valeur : `age := 30`. Go **devine** le type tout seul. Ne marche qu'**à l'intérieur** d'une
fonction. (Voir aussi `var`.)

**append** — La fonction intégrée qui **ajoute** un élément à la fin d'un slice. Elle
**renvoie** le slice agrandi, d'où le réflexe : `notes = append(notes, 20)`. Équivalent du
`.append()` de Python, en plus explicite.

**Booléen** (`bool`) — Un type qui ne vaut que `true` (vrai) ou `false` (faux). Sert aux
conditions.

**Compiler** — Traduire ton code en langage machine **avant** de l'exécuter. En Go, `go run`
le fait automatiquement juste avant de lancer.

**Fonction** — Un bloc de code nommé et réutilisable. On la **définit** avec `func`, on
l'**appelle** par son nom. Comme une recette qu'on peut refaire à volonté.

**Float** (`float64`) — Un nombre à virgule : `3.14`. En Go on écrit le plus souvent
`float64`.

**fmt** — Le package (la boîte à outils) d'**affichage** de Go. `fmt.Println` affiche
simplement ; `fmt.Printf` affiche avec un format précis (`%d`, `%s`…).

**Garbage collector** (*ramasse-miettes*) — Le mécanisme **automatique** qui libère la
mémoire dont le programme ne se sert plus. Grâce à lui, tu n'as pas à gérer la mémoire à la
main (contrairement au C).

**`go build`** — La commande qui **fabrique un exécutable** à garder (un vrai fichier qu'on
peut relancer sans Go). À utiliser quand le programme est prêt à être distribué.

**`go run`** — La commande qui **compile en mémoire ET lance** le programme d'un coup, sans
créer de fichier. C'est la plus pratique pour apprendre.

**import** — L'action d'ouvrir une boîte à outils (un package) pour s'en servir :
`import "fmt"`. ⚠️ Un import **inutilisé** provoque une **erreur de compilation**.

**Int** — Un nombre entier (sans virgule) : `42`.

**main** — Deux choses portent ce nom : le **package** `main` (celui d'un programme
exécutable) et la **fonction** `func main()`, qui est le **point de départ** lancé
automatiquement.

**Map** — Un rangement de paires **clé → valeur**, noté `map[string]int`. C'est le
**dictionnaire** de Go. La clé sert d'étiquette pour retrouver la valeur. Pour savoir si une
clé existe, on utilise la forme `valeur, ok := m[clé]`.

**ok (idiome « valeur, ok »)** — Quand tu lis une clé de map, Go peut renvoyer **deux**
résultats : la valeur **et** un booléen `ok` qui dit si la clé existait vraiment.
Ex : `age, ok := ages["Max"]`.

**Package** — Un regroupement de code Go. Ton programme exécutable est dans le package
`main`. Les outils tout faits (comme `fmt` ou `strings`) sont aussi des packages.

**range** — Le mot-clé qui, avec `for`, **parcourt** une collection. Sur un slice il donne
`(indice, valeur)` ; sur une map il donne `(clé, valeur)`. Proche du `enumerate()` /
`.items()` de Python.

**return** — Le mot-clé qui fait **renvoyer** un résultat par une fonction à celui qui
l'a appelée.

**Slice** — Une **liste dynamique** de valeurs du même type, notée `[]int`, `[]string`…
C'est l'équivalent de la **liste** Python. Elle peut grandir avec `append`.

**string** — Du texte, écrit entre guillemets : `"bonjour"`.

**strings (package)** — La boîte à outils pour manipuler le texte : `strings.ToUpper`,
`strings.Split`, `strings.Contains`, `strings.Join`… (À ne pas confondre avec le type
`string`.)

**Typage statique** — En Go, chaque variable a un **type fixé** (un entier reste un entier).
Go peut souvent le **deviner** (avec `:=`), mais il ne change jamais ensuite. C'est l'opposé
du typage **dynamique** de Python.

**`var`** — La forme **longue** pour créer une variable, en précisant le type :
`var age int = 30`. Utile hors d'une fonction, ou pour créer une variable vide. (Voir aussi
`:=`.)

**Variable** — Une boîte étiquetée qui retient une valeur : `age := 30`. Le `=` (ou `:=`)
**range** la valeur de droite dans la boîte de gauche. ⚠️ Une variable déclarée mais jamais
utilisée provoque une **erreur de compilation** en Go.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
