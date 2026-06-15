# Module 00 — Démarrer en Java : compiler et exécuter

Avant d'écrire du code, comprenons **ce qui se passe** quand on programme en Java. Ce
module est surtout théorique, avec un premier programme à compiler à la fin.

---

## 1. C'est quoi Java ?

Java est un langage **compilé**, mais pas tout à fait comme le C ou le C++. Quand tu
compiles ton fichier `.java`, tu n'obtiens **pas** directement du langage machine : tu
obtiens du **bytecode** (un fichier `.class`). Ce bytecode est ensuite exécuté par un
programme spécial appelé la **JVM** (*Java Virtual Machine*, la « machine virtuelle Java »).

```
   PremierProgramme.java  ──[ javac ]──►  PremierProgramme.class  ──[ java / JVM ]──►  exécution
   (TON code, lisible)     compilateur     (bytecode)                machine virtuelle      (ça tourne)
```

Pourquoi ce détour par le bytecode ? Parce que la JVM existe pour **tous** les systèmes
(Windows, macOS, Linux…). Du coup, le **même** fichier `.class` tourne partout sans être
recompilé. C'est la fameuse promesse de Java :

> ✍️ **« Écris une fois, exécute partout »** (*write once, run anywhere*).

Analogie : tu écris une recette une seule fois (`.java`), un traducteur (`javac`) la
transforme en une « langue universelle » (le bytecode), et **n'importe quel** cuisinier
équipé de la JVM peut la préparer, quel que soit son pays.

> 📌 Comme en C/C++, si ton code contient une faute, **le compilateur refuse de traduire**
> et t'affiche des erreurs. Rien ne s'exécute tant que ça ne compile pas.

---

## 2. 🆚 Java face à Python et au C++

Tu viens peut-être de Python ou du C++. Voici les grandes différences :

| | Python | C++ | **Java** |
|--|--------|-----|----------|
| Exécution | interprété | compilé en langage machine | **compilé en bytecode**, exécuté par la JVM |
| Typage | dynamique (`x = 5`) | statique (`int x = 5;`) | **statique** (`int x = 5;`) |
| Orienté objet | possible | possible | **obligatoire** : tout vit dans une `class` |
| Mémoire | automatique | **manuelle** (`new` / `delete`) | **automatique** (ramasse-miettes) |

Les points clés à retenir :

- **Compilé** : contrairement à Python, il y a une étape `javac` avant de lancer.
- **Typé** : comme en C++, tu dois annoncer le **type** de chaque variable (`int`,
  `double`, `String`…). Le compilateur attrape beaucoup d'erreurs à l'avance.
- **Très orienté objet** : en Java, **on ne peut rien écrire en dehors d'une classe**.
  Même un simple « bonjour » doit vivre à l'intérieur d'une `class`.
- **Mémoire automatique** : en C++, tu devais penser à libérer la mémoire (`delete`). En
  Java, un **ramasse-miettes** (*garbage collector*) s'en charge tout seul, comme en Python.

---

## 3. Installer Java

Il te faut le **JDK** (*Java Development Kit*), qui fournit `javac` (le compilateur) et
`java` (la JVM pour lancer).

- **Linux (Debian/Ubuntu)** : `sudo apt install default-jdk`
- **macOS** : `brew install openjdk` (avec Homebrew).
- **Windows** : installe **Temurin** (OpenJDK) depuis adoptium.net.

Vérifie l'installation :

```bash
javac --version   # le compilateur
java --version    # la machine virtuelle
```

---

## 4. La structure minimale d'un programme Java

Voici le plus petit programme Java utile, décortiqué :

```java
public class PremierProgramme {                 // (1) tout vit dans une CLASSE
    public static void main(String[] args) {    // (2) main : le POINT DE DÉPART
        System.out.println("Bonjour");          // (3) afficher du texte (avec retour à la ligne)
    }
}
```

1. **`public class PremierProgramme`** : en Java, **tout** le code vit à l'intérieur d'une
   **classe**. ⚠️ Une classe `public` **doit** être dans un fichier du **même nom** : la
   classe `PremierProgramme` va donc dans `PremierProgramme.java`.
2. **`public static void main(String[] args)`** : **tout programme Java démarre par la
   méthode `main`**. C'est l'équivalent du `main` du C/C++. On détaillera chaque mot plus
   tard ; pour l'instant, retiens que c'est le point d'entrée.
3. **`System.out.println(...)`** : affiche du texte, suivi d'un retour à la ligne. Chaque
   instruction se termine par un **`;`**.

> 💬 Les commentaires en Java s'écrivent `// sur une ligne` ou `/* sur plusieurs lignes */`.
> Le compilateur les ignore : ils sont là pour les humains.

---

## 5. Compiler et lancer

Une fois le fichier `PremierProgramme.java` écrit :

```bash
# Compiler : crée le fichier PremierProgramme.class (du bytecode)
javac java/00_demarrer/PremierProgramme.java

# Lancer : -cp ("classpath") dit à la JVM OÙ chercher le .class.
# On lui donne le DOSSIER, puis le NOM DE LA CLASSE (sans .class ni .java).
java -cp java/00_demarrer PremierProgramme
```

Le cycle de travail en Java est donc : **écrire → compiler (`javac`) → (corriger les
erreurs) → lancer (`java`)**.

---

## ▶️ À toi de jouer

Compile et lance le programme de ce module :

```bash
javac java/00_demarrer/PremierProgramme.java
java -cp java/00_demarrer PremierProgramme
```

Lis ensuite [`PremierProgramme.java`](./PremierProgramme.java) (tout est commenté), puis
**modifie le texte** et **recompile** pour voir le changement.

---

## 🗂️ Les modules du parcours Java

| Module | Contenu |
|--------|---------|
| [`00_demarrer`](.) | Compiler/lancer, bytecode et JVM, premier programme |
| [`01_les_bases`](../01_les_bases/) | Types, variables, conditions, boucles, méthodes, mini-calculatrice |

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
