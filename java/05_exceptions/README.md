# Module 05 — Les exceptions : gérer les erreurs sans planter

Jusqu'ici, on a supposé que tout se passait bien. Mais dans la vraie vie, **ça casse** : une
division par zéro, un texte qu'on essaie de convertir en nombre, un fichier qui n'existe
pas… En Java, ces accidents s'appellent des **exceptions**. Sans rien faire, une exception
**fait planter** le programme. Ce module montre comment les **attraper** et réagir
proprement, pour que ton programme **continue** au lieu de mourir.

> Fichier du module : `Exceptions.java`. On compile, puis on lance (voir en bas).

---

## 1. C'est quoi une EXCEPTION ?

Une **exception**, c'est un **objet** qui représente un problème survenu **pendant
l'exécution**. Quand le problème arrive, Java « **lance** » (*throw*) cette exception : si
personne ne l'attrape, le programme s'arrête avec un message d'erreur.

Exemples très courants :

| Exception | Quand ça arrive |
|-----------|-----------------|
| `ArithmeticException` | division par zéro (`10 / 0`) |
| `NumberFormatException` | `Integer.parseInt("douze")` (texte non numérique) |
| `ArrayIndexOutOfBoundsException` | accès `tableau[5]` sur un tableau de taille 2 |
| `NullPointerException` | utiliser un objet qui vaut `null` |

---

## 2. `try` / `catch` : tenter, puis rattraper

L'idée : on met le code risqué dans un bloc **`try`** (« j'essaie »). Si une exception
survient, Java **saute immédiatement** dans le bloc **`catch`** (« j'attrape »), au lieu de
planter.

```java
try {
    int x = 10 / 0;                 // ça va lever une ArithmeticException
    System.out.println(x);          // jamais atteint
} catch (ArithmeticException e) {
    System.out.println("Erreur : " + e.getMessage());   // on réagit ici
}
```

- Entre les parenthèses du `catch`, on précise **le type** d'exception qu'on attrape.
- La variable `e` est l'objet exception ; `e.getMessage()` donne la description du problème.

> 🆚 C'est le `try / except` de Python. Le mot change (`catch` au lieu de `except`), mais
> l'idée est identique.

---

## 3. `finally` : ranger après soi, quoi qu'il arrive

Le bloc **`finally`** (facultatif) s'exécute **TOUJOURS** : qu'il y ait eu une erreur ou
non, qu'on soit passé par `catch` ou pas. On y met le **nettoyage** (fermer un fichier, une
connexion…).

```java
try {
    // ... code risqué ...
} catch (Exception e) {
    // ... en cas d'erreur ...
} finally {
    System.out.println("Je m'exécute dans tous les cas.");
}
```

---

## 4. `throw` : déclencher sa propre exception

On peut **soi-même** lever une exception avec **`throw`**, par exemple pour refuser une
valeur invalide. La méthode s'**arrête net** à ce moment-là.

```java
static int racineDePositif(int n) {
    if (n < 0) {
        throw new IllegalArgumentException("nombre negatif interdit : " + n);
    }
    return (int) Math.sqrt(n);
}
```

> ⚠️ Ne confonds pas : **`throw`** (sans `s`) **lance** une exception ; **`throws`** (avec
> `s`, voir ci-dessous) **annonce** dans la signature qu'une méthode *peut* en lancer.

---

## 5. Exceptions VÉRIFIÉES vs NON VÉRIFIÉES

C'est la grande spécificité de Java. Il existe **deux familles** d'exceptions :

- **Non vérifiées** (*unchecked*) : erreurs de **programmation** (division par zéro, indice
  hors limites, `null`…). Le compilateur ne t'oblige à **rien** : tu peux les attraper, ou
  non. Exemples : `ArithmeticException`, `NumberFormatException`, `IllegalArgumentException`,
  `NullPointerException`.

- **Vérifiées** (*checked*) : problèmes **prévisibles venant de l'extérieur** (fichier
  absent, réseau coupé…). Le compilateur t'**OBLIGE** à les gérer. Une méthode qui peut en
  lancer doit l'**annoncer** avec **`throws`**, et l'appelant doit alors soit l'entourer
  d'un `try/catch`, soit la re-déclarer avec `throws`.

```java
static void verifierAge(int age) throws Exception {   // 'throws' : "j'avertis que je peux échouer"
    if (age < 0) {
        throw new Exception("age impossible : " + age);
    }
}

// À l'appel, le compilateur EXIGE de gérer l'exception vérifiée :
try {
    verifierAge(-3);
} catch (Exception e) {
    System.out.println(e.getMessage());
}
```

| | Non vérifiée (*unchecked*) | Vérifiée (*checked*) |
|--|----------------------------|----------------------|
| Origine typique | bug de code | événement externe prévisible |
| Le compilateur force la gestion ? | **non** | **oui** (`throws` + try/catch obligatoire) |
| Exemples | `ArithmeticException`, `NullPointerException` | `IOException`, `Exception` |

> 🆚 Python et C++ n'ont **pas** cette distinction « vérifiée » : c'est propre à Java. Au
> début, ça semble pénible, mais ça force à ne pas **oublier** de gérer les erreurs externes.

---

## ▶️ À toi de jouer

```bash
# try/catch/finally + throw + exceptions vérifiées vs non vérifiées
javac -d /tmp/jb java/05_exceptions/Exceptions.java
java -cp /tmp/jb Exceptions
```

Lis le fichier, puis **modifie-le** et **recompile** : ajoute un `catch` pour une autre
exception, **enlève** le `try/catch` autour de `verifierAge(...)` et observe que le
compilateur **refuse** de compiler (parce qu'elle est vérifiée), ou ajoute tes propres
vérifications avec `throw`.

➡️ Tu as terminé les bases de la POO et de la robustesse en Java. Bravo !
