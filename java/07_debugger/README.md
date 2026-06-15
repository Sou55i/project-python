# Module 07 — Déboguer : lire une stack trace et reconnaître les erreurs

Ton programme plante avec un gros pavé rouge incompréhensible ? Pas de panique. Ce pavé,
c'est une **stack trace** (la « pile d'appels »), et c'est ton **meilleur ami** : il te dit
**quelle** erreur s'est produite et **où** EXACTEMENT. Apprendre à le lire, c'est la
compétence n°1 pour réparer un bug.

> Fichier du module : `DemoDebug.java`. On compile, puis on lance (voir en bas).

---

## 1. Lire une STACK TRACE

Quand une exception n'est pas attrapée, Java affiche quelque chose comme :

```
Exception in thread "main" java.lang.NullPointerException: ...
    at DemoDebug.niveau2(DemoDebug.java:38)
    at DemoDebug.niveau1(DemoDebug.java:31)
    at DemoDebug.main(DemoDebug.java:52)
```

On lit **du HAUT vers le BAS** :

- **1re ligne** : le **type** de l'exception (`NullPointerException`) et son message.
- **Ligne suivante** (`at ...niveau2(...:38)`) : l'endroit **EXACT** où ça a cassé —
  méthode `niveau2`, fichier `DemoDebug.java`, **ligne 38**. C'est là qu'il faut regarder !
- **Lignes du dessous** : **qui a appelé qui**. `niveau2` a été appelée par `niveau1`,
  elle-même appelée par `main`. C'est le « chemin » qu'a suivi le programme.

> 💡 Réflexe : regarde la **première ligne `at ...` qui concerne TON code** (le numéro de
> ligne), va voir cette ligne, et demande-toi quelle valeur pose problème.

---

## 2. Les 3 erreurs les plus fréquentes

| Exception | Cause typique | Comment l'éviter |
|-----------|---------------|------------------|
| `NullPointerException` | utiliser un objet qui vaut `null` (`texte.length()` alors que `texte` est `null`) | vérifier `if (x != null)` avant d'utiliser |
| `ArrayIndexOutOfBoundsException` | indice hors du tableau (`notes[5]` sur 3 cases : 0,1,2) | vérifier `indice >= 0 && indice < tableau.length` |
| `ClassCastException` | conversion impossible (`(Integer) unString`) | s'assurer du vrai type, ou utiliser `instanceof` |

```java
// NullPointerException : la plus fréquente !
String texte = null;
texte.length();         // 💥 on appelle une méthode sur "rien"
```

---

## 3. Le `println` de debug

La technique la plus simple et la plus efficace : quand un résultat est bizarre, **affiche
les valeurs intermédiaires** pour voir où ça dérape.

```java
System.out.println("[debug] a = " + a + ", b = " + b);
int somme = a + b;
System.out.println("[debug] somme = " + somme);
```

On préfixe souvent par `[debug]` pour les repérer (et les **enlever** ensuite).

> 🆚 C'est le `print()` de débogage de Python, exactement la même idée.

---

## 4. Aller plus loin : le débogueur `jdb`

Mettre des `println` partout, c'est vite fastidieux. Un **débogueur** permet de **mettre en
pause** le programme et d'inspecter les variables **ligne par ligne**. Le JDK fournit `jdb` :

```bash
javac -g -d /tmp/jb java/07_debugger/DemoDebug.java   # -g : garde les infos de debug
jdb -classpath /tmp/jb DemoDebug
```

Puis, dans `jdb` :

```
stop in DemoDebug.niveau2   # poser un point d'arrêt
run                          # lancer jusqu'au point d'arrêt
print texte                  # afficher la valeur d'une variable
cont                         # continuer
```

Les **IDE** (IntelliJ, VS Code, Eclipse) offrent la même chose en cliquant dans la marge.

---

## ▶️ À toi de jouer

```bash
# stack traces des 3 erreurs fréquentes + println de debug (sortie déterministe)
javac -d /tmp/jb java/07_debugger/DemoDebug.java
java -cp /tmp/jb DemoDebug
```

Lis le fichier : chaque erreur est **provoquée volontairement** dans un `try/catch`, donc
le programme **ne plante pas** — il te MONTRE les erreurs. Entraîne-toi à **enlever un
`try/catch`** : le programme plantera, et tu pourras t'exercer à lire la vraie stack trace.

➡️ Prochaine étape : le module **08_streams_lambdas**, pour manipuler des données de façon
élégante.
