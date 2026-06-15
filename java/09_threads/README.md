# Module 09 — La concurrence : faire plusieurs choses « en même temps »

Jusqu'ici, ton programme faisait **une chose à la fois**, dans l'ordre. Mais un ordinateur
moderne a plusieurs cœurs et peut faire **plusieurs tâches en parallèle**. En Java, chaque
tâche parallèle s'appelle un **thread** (« fil d'exécution »). C'est puissant… mais il faut
faire attention quand plusieurs threads touchent à la **même donnée**.

> Fichier du module : `Threads.java`. On compile, puis on lance (voir en bas).

---

## 1. Un THREAD, c'est quoi ?

Un **thread** est une suite d'instructions qui s'exécute **en même temps** que les autres.
Pour créer un thread, on lui donne un **`Runnable`** : un bout de code à exécuter (souvent
écrit en lambda, vu au module 08).

```java
Runnable tache = () -> System.out.println("Bonjour depuis un thread !");
Thread t = new Thread(tache);
t.start();   // start() lance l'exécution EN PARALLÈLE
```

> ⚠️ `start()` lance le thread **en parallèle**. `run()` (sans `start`) exécuterait juste le
> code normalement, **sans** parallélisme. On utilise presque toujours `start()`.

---

## 2. `join()` : attendre la fin d'un thread

Après `start()`, ton `main` **continue sans attendre**. Si tu veux lire un résultat produit
par les threads, tu dois d'abord les **attendre** avec **`join()`** :

```java
t.start();
t.join();   // "j'attends que t ait fini avant de continuer"
```

Sans `join`, `main` pourrait lire la donnée **avant** que les threads aient terminé → résultat
partiel et faux.

---

## 3. Le piège : la donnée PARTAGÉE

Quand plusieurs threads modifient la **même** variable, ils peuvent se **marcher dessus**.
Un simple `compteur++` n'est pas une opération unique : c'est « lire, ajouter 1, réécrire ».
Deux threads peuvent lire la même valeur en même temps et écraser le travail de l'autre → le
total final est **faux et imprévisible**.

Deux solutions :

- **`AtomicInteger`** : un compteur spécial dont les additions sont **atomiques**
  (indivisibles). `compteur.incrementAndGet()` ne peut **pas** être interrompu au milieu.
- **`synchronized`** : un mot-clé qui met une « porte à un seul passage » autour d'un bloc,
  pour qu'**un seul thread à la fois** y entre.

```java
AtomicInteger compteur = new AtomicInteger(0);
compteur.incrementAndGet();   // +1, garanti correct même en parallèle
```

Dans ce module, on utilise `AtomicInteger`. Résultat : **4 threads × 1000 = 4000**,
**toujours** (sortie déterministe).

> 🆚 Python a aussi des threads, mais son fameux *GIL* limite le vrai parallélisme de calcul.
> En Java, les threads tournent réellement en parallèle — d'où l'importance de protéger les
> données partagées.

---

## 🗺️ CHEMINEMENT du programme

1. Créer un compteur **partagé et sûr** (`AtomicInteger`), commun à tous les threads.
2. Créer plusieurs threads ; chacun ajoute 1000 fois au compteur (via un `Runnable`).
3. **Démarrer** tous les threads (`start`) : ils tournent en parallèle.
4. **Attendre** qu'ils finissent tous (`join`) avant de lire le résultat.
5. Afficher la somme finale : **déterministe** (toujours 4000) grâce à `AtomicInteger`.

---

## ▶️ À toi de jouer

```bash
# threads + Runnable + join + AtomicInteger (somme finale = 4000, déterministe)
javac -d /tmp/jb java/09_threads/Threads.java
java -cp /tmp/jb Threads
```

Lis le fichier, puis **expérimente** : change `NB_THREADS` ou `INCREMENTS_PAR_THREAD` et
vérifie que la somme reste correcte. Pour voir le **bug**, remplace `AtomicInteger` par un
simple `int` partagé : la somme deviendra parfois inférieure à l'attendu !

➡️ Prochaine étape : le **projet capstone** dans `java/projets/`, qui rassemble tout ce que
tu as appris.
