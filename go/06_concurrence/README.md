# Module 06 — La concurrence : goroutines & channels

Jusqu'ici, nos programmes faisaient **une seule chose à la fois**, dans l'ordre, de haut en
bas. Mais parfois, on aimerait lancer **plusieurs tâches « en même temps »** : par exemple
télécharger trois fichiers sans attendre que le premier finisse avant de commencer le
deuxième. C'est l'un des **grands atouts du Go** : faire ça est très simple.

> Fichiers du module : `goroutines.go` (lance plusieurs tâches et attend qu'elles finissent)
> et `channels.go` (deux tâches qui se parlent par un « tuyau »).
> ⚠️ Chaque fichier a son propre `func main` : on les lance **séparément** avec `go run`.

---

## 1. Une goroutine = une tâche lancée « en parallèle »

Une **goroutine**, c'est une tâche que Go fait tourner **« à côté »** du programme principal,
sans bloquer la suite. Pour en lancer une, il suffit d'écrire le mot-clé **`go`** devant un
appel de fonction :

```go
go direBonjour()   // lance direBonjour() "à côté" et CONTINUE tout de suite
```

> 🍞 **Analogie.** Tu fais les courses. Plutôt que de tout faire toi-même, tu **délègues** une
> course à un ami (« va chercher le pain ») pendant que **toi tu continues** à remplir le
> panier. La goroutine, c'est l'ami : il travaille **pendant que tu avances**.

Une goroutine est **très légère** : Go peut en lancer des **milliers** sans problème, là où
d'autres langages s'essouffleraient. C'est ce qui rend Go si apprécié pour les serveurs.

---

## 2. Le piège : le programme principal peut finir trop tôt

Il y a un **problème** avec l'analogie de l'ami : si tu rentres à la maison **avant** qu'il ait
rapporté le pain, tu n'auras jamais le pain ! En Go, c'est pareil : **quand `main` se termine,
le programme s'arrête**, même si des goroutines n'ont pas fini.

```go
go direBonjour()   // lancée "à côté"...
// ...mais main finit ICI, tout de suite -> direBonjour n'a peut-être jamais eu le temps !
```

Conclusion : il faut **SYNCHRONISER**, c'est-à-dire **attendre** que les goroutines aient
terminé. Go nous donne deux outils pour ça.

---

## 3. Outil n°1 : `sync.WaitGroup` (« attendre que tout soit fini »)

Un **`sync.WaitGroup`** est un **compteur de tâches en cours**. On l'utilise en 3 gestes :

```go
var wg sync.WaitGroup   // le compteur, à zéro au départ

wg.Add(1)               // "+1 tâche à attendre" (à faire AVANT de lancer la goroutine)
go func() {
    defer wg.Done()     // "-1" quand la goroutine a fini (defer = juste avant de sortir)
    // ... le travail ...
}()

wg.Wait()               // BLOQUE main tant que le compteur n'est pas revenu à zéro
```

- **`Add(n)`** : on prévient « il y a `n` tâches de plus à attendre ».
- **`Done()`** : la goroutine signale « moi, j'ai fini » (elle enlève 1 au compteur). On le met
  dans un `defer` pour ne **jamais oublier** de le faire.
- **`Wait()`** : `main` **attend** ici, sans rien faire, jusqu'à ce que le compteur soit à zéro.

> 🍞 Reprends l'analogie : `Add(1)` = « j'ai envoyé un ami chercher le pain » ; `Done()` = « il
> est revenu » ; `Wait()` = « je reste sur le pas de la porte tant que tout le monde n'est pas
> rentré ».

C'est ce que montre **`goroutines.go`**.

---

## 4. Outil n°2 : les channels (`chan`, des tuyaux pour communiquer)

Un **channel** (un *canal*, un *tuyau*) sert à **faire passer des valeurs d'une goroutine à une
autre**. C'est à la fois un moyen de **communiquer** ET de **synchroniser**.

```go
ch := make(chan int)   // crée un tuyau qui transporte des entiers (int)

ch <- 42               // ENVOYER : "je mets 42 dans le tuyau" (la flèche pointe vers ch)
v := <-ch              // RECEVOIR : "je sors une valeur du tuyau" (la flèche sort de ch)
```

Comment lire la flèche `<-` ? **Elle indique le sens du voyage.**

- `ch <- 42` : la valeur **entre dans** `ch` (on **envoie**).
- `v := <-ch` : la valeur **sort de** `ch` et va dans `v` (on **reçoit**).

Point clé qui synchronise tout : sur un channel simple, **l'envoi attend qu'il y ait un
receveur**, et **la réception attend qu'il y ait un envoyeur**. Les deux goroutines se
**rendez-vous** au tuyau. Pas besoin de `WaitGroup` : le tuyau lui-même fait patienter.

> 🚰 **Analogie.** Un tuyau étroit entre deux personnes : celle qui pousse une balle dedans
> attend que l'autre la prenne de l'autre côté. Le passage de la balle, c'est le rendez-vous.

### Fermer le tuyau et tout recevoir avec `range`

Quand l'envoyeur n'a plus rien à transmettre, il **ferme** le tuyau avec `close(ch)`. Côté
réception, on peut alors parcourir **toutes** les valeurs reçues avec un `for ... range`, qui
s'arrête **tout seul** quand le tuyau est fermé :

```go
for v := range ch {    // reçoit tant que le tuyau n'est pas fermé
    fmt.Println(v)
}
```

C'est ce que montre **`channels.go`**.

---

## 🆚 Comparaison avec Python

En Python, faire « plusieurs choses à la fois » est possible (`threading`, `asyncio`…) mais
c'est souvent **plus compliqué** à mettre en place. En Go, le mot-clé **`go`** suffit pour
lancer une tâche, et les **channels** offrent une façon **propre** de faire communiquer ces
tâches sans se prendre la tête avec des verrous compliqués.

La philosophie de Go tient en une phrase :

> « Ne communique pas en partageant la mémoire ; partage la mémoire en communiquant. »

Traduction simple : **fais passer les données par un channel** plutôt que de laisser plusieurs
tâches toucher la même variable en même temps (source de bugs).

---

## ▶️ À toi de jouer

⚠️ Les deux fichiers ont **chacun** leur `package main` et leur `func main`, dans le **même
dossier**. On ne peut donc **pas** lancer le dossier entier : on les lance **séparément**, en
nommant le fichier. (Pas de `go.mod` ici, c'est volontaire : on reste sur de simples fichiers.)

Lance les commandes **DEPUIS LA RACINE** du dépôt (le dossier qui contient `go/`) :

```bash
# Plusieurs tâches lancées en parallèle, attendues avec un WaitGroup :
go run go/06_concurrence/goroutines.go

# Deux tâches qui communiquent par un channel :
go run go/06_concurrence/channels.go
```

Bonne nouvelle pour apprendre : **la sortie est toujours la même** (déterministe). On a
synchronisé correctement, donc pas de surprise ni d'ordre qui change d'une fois à l'autre.
Relance-les plusieurs fois : tu obtiendras **exactement** le même résultat.

> 🧪 **Expérience.** Dans `goroutines.go`, mets en commentaire la ligne `wg.Wait()` et relance :
> tu verras que `main` finit **avant** les goroutines (le message final sort, mais le travail
> n'a pas eu le temps de s'afficher). C'est exactement le piège du point 2 !

➡️ La suite du parcours arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe Go en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots de Go expliqués simplement.
