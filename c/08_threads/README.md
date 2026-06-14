# Module 08 (AVANCÉ) — Threads & programmation concurrente (pthreads)

Bravo, tu as fini les fondations ! Ce module est **avancé** : on va apprendre à faire faire
**plusieurs choses EN MÊME TEMPS** à un programme grâce aux **threads**. C'est puissant…
et plein de pièges. On y va doucement, avec des analogies, comme d'habitude.

> Fichier du module : `threads.c` (plusieurs threads incrémentent un compteur partagé
> protégé par un verrou). On **compile** puis on **lance** (voir en bas).
>
> ⚠️ Nouveauté : il faudra compiler avec l'option **`-pthread`** (détails plus bas).

---

## 1. Un THREAD, c'est quoi ? Une « ligne d'exécution »

D'habitude, ton programme fait **une chose à la fois**, ligne après ligne : c'est **un seul
fil** d'exécution. Un **thread** (« fil » en anglais), c'est une **ligne d'exécution** qui
peut tourner **en parallèle** des autres, dans le **même** programme.

👨‍🍳 **Analogie : plusieurs cuisiniers dans la même cuisine.** Un seul cuisinier prépare
les plats l'un après l'autre. Mais si tu as **4 cuisiniers** (4 threads) qui travaillent
**en même temps** dans la même cuisine, le service va beaucoup plus vite. Ils partagent la
**même** cuisine (la même mémoire du programme) : les mêmes plans de travail, les mêmes
ingrédients…

> 💡 Sur une machine moderne (plusieurs cœurs de processeur), les threads tournent
> **vraiment** en parallèle. C'est comme ça qu'on exploite toute la puissance du CPU.

---

## 2. Lancer un thread : `pthread_create`

On utilise les **threads POSIX** (« pthreads »), disponibles via `<pthread.h>`.

Un thread, ça **exécute une fonction**. On dit à `pthread_create` : « lance un nouveau
cuisinier, et envoie-le faire **cette** tâche ».

```c
#include <pthread.h>

void *travailleur(void *arg) {   // la fonction que le thread va exécuter
    // ... le travail du thread ...
    return NULL;
}

pthread_t id;                                  // un "badge" pour identifier le thread
pthread_create(&id, NULL, travailleur, NULL);  // GO : un nouveau thread part travailler
```

- `&id` : où ranger l'identifiant du thread créé ;
- `NULL` (2ᵉ) : les options/attributs — `NULL` = celles par défaut, ça suffit ;
- `travailleur` : la **fonction** que le thread va exécuter ;
- `NULL` (4ᵉ) : l'**argument** passé à la fonction (rien ici).

> La fonction d'un thread a une **signature imposée** : elle prend un `void *` et renvoie un
> `void *`. C'est un format générique « passe-partout » (on verra plus tard comment y glisser
> de vraies données).

---

## 3. Attendre la fin d'un thread : `pthread_join`

Quand tu lances des threads, `main()` **continue** son chemin sans les attendre. Problème :
si `main()` se termine avant eux, le programme s'arrête et les threads sont coupés en plein
travail !

🍽️ **Analogie :** le chef (`main`) ne doit pas quitter la cuisine et fermer le restaurant
tant que **tous** les cuisiniers n'ont pas **fini** leur plat.

`pthread_join` veut dire « **attends** que ce thread ait fini avant de continuer » :

```c
pthread_join(id, NULL);   // bloque ici jusqu'à ce que le thread 'id' soit terminé
```

On fait un `join` pour **chaque** thread lancé. Après, on est sûr que tout le travail est
fait.

---

## 4. ⚠️ LE DANGER : la « course aux données » (race condition)

Voici le grand piège du parallélisme. Si plusieurs threads **modifient la même variable en
même temps**, le résultat peut être… **faux**.

Pourquoi ? Une simple ligne comme `compteur = compteur + 1` n'est PAS une seule opération
pour la machine. C'est en réalité **trois étapes** :

1. **lire** la valeur actuelle du compteur ;
2. **ajouter** 1 ;
3. **réécrire** le résultat dans le compteur.

🛒 **Analogie : deux cuisiniers, une seule ardoise « nombre de plats servis ».** Le
cuisinier A lit « 41 ». Au même instant, le cuisinier B lit aussi « 41 ». A écrit « 42 ».
B écrit « 42 » lui aussi. Deux plats ont été servis… mais l'ardoise n'affiche que **+1** !
Un incrément a été **perdu**.

C'est ça, une **course aux données** (*race condition*) : le résultat dépend de **qui passe
quand**, et certains incréments **disparaissent**. Avec des centaines de milliers
d'incréments répartis sur plusieurs threads, on obtient un total **trop petit**, et
**différent à chaque exécution**.

> ❗ Sans protection, notre programme afficherait un total **FAUX** (ex : 380000 au lieu de
> 400000) — et un nombre **différent** à chaque fois que tu le relances. C'est le symptôme
> typique d'une course aux données.

---

## 5. La SOLUTION : le MUTEX (un verrou)

Pour empêcher deux threads de toucher la variable **en même temps**, on utilise un **mutex**
(de « **mut**ual **ex**clusion », exclusion mutuelle). C'est un **verrou** : un seul thread à
la fois peut le « tenir ».

🔑 **Analogie : la clé unique des toilettes du restaurant.** Pour entrer (modifier la
variable), il faut **prendre la clé**. Tant que tu l'as, personne d'autre ne peut entrer :
les autres **attendent** devant la porte. Quand tu sors, tu **rends la clé** et le suivant
peut entrer. Résultat : **un seul** à la fois dans la zone sensible.

```c
pthread_mutex_t verrou = PTHREAD_MUTEX_INITIALIZER;  // création du verrou

pthread_mutex_lock(&verrou);     // 🔒 je prends le verrou (j'attends s'il est pris)
compteur = compteur + 1;         //    zone PROTÉGÉE : moi seul ici
pthread_mutex_unlock(&verrou);   // 🔓 je rends le verrou : au suivant
```

La portion entre `lock` et `unlock` s'appelle la **section critique** : on la veut la plus
**courte** possible (sinon les threads passent leur temps à s'attendre). Grâce au verrou, les
trois étapes lire/ajouter/réécrire ne peuvent **plus** s'entremêler : plus aucun incrément
n'est perdu, et le total devient **DÉTERMINISTE** (le même à chaque fois).

> 🛡️ **Règle d'or :** à chaque `lock` doit correspondre **un** `unlock`. Si tu oublies le
> `unlock`, les autres threads attendent **pour toujours** (c'est un *interblocage*, ou
> *deadlock*).

---

## 6. Ce que fait `threads.c`

- on crée **4 threads** (`NB_THREADS`) ;
- chacun incrémente **100 000 fois** (`NB_INCREMENTS`) le **même** compteur partagé, en le
  protégeant par le mutex ;
- `main()` attend tout le monde avec `pthread_join`, puis affiche le total.

Le total attendu est donc `4 × 100 000 = 400 000`, et grâce au mutex on l'obtient **à tous
les coups**. Le programme le vérifie et te le confirme.

---

## ▶️ À toi de jouer

⚠️ Avec les threads, **on doit ajouter l'option `-pthread`** à la compilation (elle relie la
bibliothèque des threads). Sans elle, ça ne se compile pas correctement.

```bash
# Compiler AVEC -pthread, puis lancer
gcc -Wall -pthread c/08_threads/threads.c -o threads && ./threads
```

Tu dois voir un **total obtenu = 400000** (égal au total attendu), à **chaque** exécution.

**Expériences** pour bien comprendre :
- relance plusieurs fois : le total reste **toujours** le même (déterministe) ;
- change `NB_THREADS` ou `NB_INCREMENTS` : le total attendu suit la formule
  `NB_THREADS × NB_INCREMENTS` ;
- pour **voir** la course aux données : mets en commentaire les lignes `pthread_mutex_lock`
  et `pthread_mutex_unlock`, recompile, relance plusieurs fois → le total devient **faux**
  et **change** à chaque exécution. Remets ensuite le verrou : tout redevient correct.

➡️ Tu viens de toucher à la **programmation concurrente** : très utile (serveurs, calculs,
interfaces réactives…) et exigeante (toujours se demander « quelle donnée est partagée, et
comment je la protège ? »).
Garde sous la main l'[`AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) et le
[`GLOSSAIRE.md`](../GLOSSAIRE.md).
