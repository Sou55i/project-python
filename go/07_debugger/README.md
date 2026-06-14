# Module 07 — Débugger : trouver et corriger les bugs en Go

Un bug, ce n'est **pas un échec** : c'est ton programme qui te dit « là, quelque chose ne
colle pas ». En Go, deux mondes cohabitent : les **erreurs renvoyées** (qu'on gère
calmement) et le **panic** (l'erreur grave qui arrête tout). Apprendre à **lire** ce que Go
t'affiche est la compétence qui fait le plus progresser un débutant.

> Fichier du module : `panic_recover.go` (déclenche un panic volontairement, puis le
> **rattrape** proprement avec `defer` + `recover()` pour que le programme finisse bien).

---

## 1. D'abord : Go préfère les erreurs RENVOYÉES (rappel du module 04)

En Go, la façon **normale** de signaler un problème, c'est de **renvoyer une `error`** en
plus du résultat. On a vu ça au module 04. L'appelant **vérifie** cette erreur :

```go
contenu, err := os.ReadFile("config.txt")
if err != nil {            // y a-t-il eu un souci ?
    fmt.Println("Souci :", err)
    return                 // on réagit proprement, on ne plante pas
}
// ... ici, on sait que tout s'est bien passé
```

> 🔑 **La règle d'or du Go : `if err != nil`.** Une fonction qui peut échouer te renvoie une
> erreur. Tu la regardes **tout de suite**. C'est la voie « calme » : pas de plantage.

---

## 2. Le `panic` : l'erreur GRAVE qui arrête le programme

Parfois, le programme rencontre un problème si grave qu'il ne peut **pas** continuer : il
**panique** (`panic`). Il s'arrête net et affiche un gros pavé appelé **stack trace** (la
**pile d'appels** : la liste des fonctions qui étaient en cours, l'une dans l'autre).

Exemple de pavé quand on lit une case qui n'existe pas dans un slice :

```
panic: runtime error: index out of range [5] with length 3

goroutine 1 [running]:
main.lireCase(...)
	/chemin/mon_prog.go:12
main.main()
	/chemin/mon_prog.go:7 +0x1d
exit status 2
```

### Comment LIRE cette trace

- **La première ligne (tout en HAUT)** est la plus importante : c'est **le message**.
  Ici `index out of range [5] with length 3` → « tu as demandé la case 5 d'un slice qui n'a
  que 3 cases ».
- **En DESSOUS**, la pile d'appels te montre **où** ça s'est produit, de la fonction la plus
  « profonde » vers `main`. Chaque ligne `…/mon_prog.go:12` te donne le **fichier** et le
  **numéro de ligne**. Tu sais donc exactement où regarder.

> 🔑 En résumé : **le message en HAUT te dit QUOI ; les lignes en dessous te disent OÙ.**

---

## 3. Les bugs FRÉQUENTS en Go (cause → solution)

| Bug | Message typique | Cause | Solution |
|-----|-----------------|-------|----------|
| **Index hors limites** | `index out of range [i] with length n` | tu lis/écris `slice[i]` alors que `i >= len(slice)` | on compte **à partir de 0** ; vérifie avec `len(slice)` avant |
| **Map nil en écriture** | `assignment to entry in nil map` | tu écris dans une map jamais initialisée | crée-la d'abord : `m := make(map[string]int)` |
| **Pointeur nil déréférencé** | `invalid memory address or nil pointer dereference` | tu fais `*p` ou `p.Champ` alors que `p == nil` | vérifie `if p != nil` avant d'utiliser le pointeur |
| **`error` non gérée** | (pas de plantage… mais comportement faux) | tu ignores le `err` renvoyé | écris **toujours** `if err != nil { ... }` |

> 🍞 Le dernier est sournois : il **ne** fait **pas** planter le programme, mais celui-ci
> continue avec des données fausses. C'est souvent le plus difficile à débusquer.

---

## 4. `recover()` : rattraper un panic pour ne pas planter

Un panic n'est pas toujours fatal : on peut le **rattraper** avec la fonction `recover()`,
**à condition** de l'appeler dans une fonction `defer` (une fonction exécutée **juste avant
de sortir**, même quand ça panique).

```go
func tache() {
    defer func() {                       // s'exécute en sortant, même en cas de panic
        if r := recover(); r != nil {    // y a-t-il eu un panic à rattraper ?
            fmt.Println("Rattrapé :", r) // oui -> on l'affiche et on REPREND la main
        }
    }()

    panic("ça a mal tourné")             // ICI ça panique...
    // ...le defer ci-dessus est quand même exécuté, recover() arrête la panique
}
```

- `defer` : « fais ça **en dernier**, en sortant de la fonction » (toujours, même en panic).
- `recover()` : à l'intérieur du `defer`, **arrête** la panique en cours et renvoie sa valeur
  (`nil` s'il n'y a pas eu de panic).

> ⚠️ N'abuse pas de `recover` pour **masquer** les bugs. La bonne pratique reste `if err !=
> nil`. Le `recover` sert surtout à éviter qu'un imprévu fasse **tout** s'effondrer (ex : un
> serveur qui doit rester debout même si une requête plante).

---

## 5. Les outils pour débugger en Go

1. **Afficher avec `fmt.Println`** — la technique la plus simple et la plus utilisée : on
   place des affichages juste avant la ligne suspecte pour **voir les valeurs**.
   ```go
   fmt.Println("DEBUG i =", i, "len =", len(slice)) // que vaut i ? le slice est grand comment ?
   ```
2. **`go vet`** — un outil **inclus avec Go** qui **inspecte** ton code et signale des erreurs
   courantes (sans le lancer). À réflexe avant de lancer :
   ```bash
   go vet go/07_debugger/panic_recover.go
   ```
3. **`delve` (commande `dlv`)** — le **débogueur** de Go. Il permet de **mettre en pause** le
   programme, d'avancer **ligne par ligne** et d'**inspecter** les variables en direct. Plus
   avancé ; à découvrir quand `fmt.Println` ne suffit plus :
   ```bash
   dlv debug go/07_debugger/panic_recover.go
   ```

---

## ▶️ À toi de jouer

Lance **DEPUIS LA RACINE** du dépôt (le dossier qui contient `go/`) :

```bash
go run go/07_debugger/panic_recover.go
```

Le programme **déclenche** un panic exprès, le **rattrape** avec `defer` + `recover()`, et se
**termine normalement** avec un message clair (il ne plante pas). Lis le code commenté : tu
verras exactement où ça panique et comment on reprend la main.

> 🧪 **Expérience.** Dans `panic_recover.go`, mets en commentaire tout le bloc `defer` qui
> contient `recover()` et relance : cette fois le programme **plante** et affiche la stack
> trace du point 2. Compare-la avec ce qu'on a expliqué (message en haut, où en dessous) !

➡️ Avec ça, ni un pavé de panic ni un `if err != nil` ne devraient te faire peur. 💪

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe Go en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots de Go expliqués simplement.
