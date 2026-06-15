# ☕ Apprendre le Java — pour grands débutants

**Java** est un langage **compilé en bytecode** et exécuté par la **JVM** (*Java Virtual
Machine*). Au lieu de produire directement du langage machine (comme le C/C++), `javac`
traduit ton code en un fichier intermédiaire `.class` que la JVM sait lire **partout** :
c'est la fameuse promesse **« écris une fois, exécute partout »** (*write once, run
anywhere*). Java est aussi **très orienté objet** : tout, sans exception, vit à l'intérieur
d'une `class`. On l'utilise pour les applications d'entreprise, Android, les gros services
serveur…

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, compile, lance, modifie.

---

## 🆚 Différences avec Python et avec C++

Tu viens peut-être de Python ou du C++. Voici les grandes différences :

| | Python | C++ | **Java** |
|--|--------|-----|----------|
| Exécution | interprété | compilé en **langage machine** | **compilé en bytecode**, exécuté par la JVM |
| Typage | dynamique (`x = 5`) | statique (`int x = 5;`) | **statique** (`int x = 5;`) |
| Orienté objet | possible | possible | **obligatoire** : tout vit dans une `class` |
| Mémoire | automatique | **manuelle** (`new` / `delete`) | **automatique** (ramasse-miettes) |
| Fin d'instruction | retour à la ligne | un **`;`** | un **`;`** |
| Blocs | indentation | des **accolades `{ }`** | des **accolades `{ }`** |
| Afficher | `print("Bonjour")` | `std::cout << "Bonjour";` | `System.out.println("Bonjour");` |

Les points clés à retenir :

- **Compilé** : contrairement à Python, il y a une étape `javac` avant de lancer. Si ton
  code contient une faute, le compilateur **refuse de traduire** : rien ne s'exécute.
- **Typé** : comme en C++, tu dois annoncer le **type** de chaque variable (`int`, `double`,
  `String`…). Le compilateur attrape beaucoup d'erreurs à l'avance.
- **Très orienté objet** : on **ne peut rien écrire en dehors d'une classe**. Même un simple
  « bonjour » doit vivre à l'intérieur d'une `class`.
- **Mémoire automatique** : en C++, tu pensais à libérer la mémoire (`delete`). En Java, un
  **ramasse-miettes** (*garbage collector*) s'en charge tout seul, comme en Python.

---

## 📚 Le parcours

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Compiler/lancer, **bytecode** et **JVM**, premier programme, `System.out.println` |
| 1 | [`01_les_bases`](./01_les_bases/) | Types, variables, conditions, boucles, **méthodes**, mini-calculatrice |
| 2 | [`02_poo`](./02_poo/) | Programmation objet : **classes & objets**, attributs/méthodes, constructeur, `public`/`private` (encapsulation) |
| 3 | [`03_heritage_interfaces`](./03_heritage_interfaces/) | **Héritage** (`extends`), **interfaces** (`implements`), `@Override`, **polymorphisme** |
| 4 | [`04_collections`](./04_collections/) | **`ArrayList`** (liste qui grandit) et **`HashMap`** (dictionnaire clé→valeur), boucle for-each |
| 5 | [`05_exceptions`](./05_exceptions/) | Gérer les erreurs sans planter : `try`/`catch`/`finally`, exceptions **checked**/**unchecked**, lire une stack trace |
| 6 | [`06_generics`](./06_generics/) | Les **génériques `<T>`** : écrire un code qui marche pour plusieurs types (c'est ce qui se cache derrière les `< >` des collections) |
| 7 | [`07_debugger`](./07_debugger/) | Trouver et corriger les bugs : lire une **stack trace**, reconnaître les erreurs fréquentes (`NullPointerException`, hors limites…) |

> ✅ **Parcours complet** : fondations (00→07), modules avancés (08–09), projet capstone et
> module sécurité (voir plus bas).

## 🚀 Modules avancés

Une fois les fondations digérées, ces modules vont plus loin — toujours dans le même style
(théorie d'abord, code commenté ensuite).

| Module | Ce que tu apprends |
|--------|--------------------|
| [`08_streams_lambdas`](./08_streams_lambdas/) | Les **lambdas** (`->`, de mini-fonctions anonymes) et l'**API Stream** : filtrer, transformer et résumer une collection de façon **courte et lisible** (`filter`, `map`, `collect`, `count`) plutôt qu'avec de longues boucles `for`. |
| [`09_threads`](./09_threads/) | La **concurrence** : faire **plusieurs choses « en même temps »**. Créer un **thread** (« fil d'exécution »), le lancer, l'attendre (`join`), et comprendre pourquoi partager des données entre threads demande de la **synchronisation**. |

### 🛠️ Et pour mettre tout ça en pratique : [`projets/`](./projets/)

Une fois les fondations en place, le dossier [`projets/`](./projets/) propose un mini-projet
**« capstone »** qui **combine plusieurs modules** (classe + `ArrayList` + génériques +
`try`/`catch` + streams) pour construire un vrai petit outil : un **gestionnaire de tâches**
qui sauvegarde et recharge ses données dans un fichier.

---

## 📎 Ressources

- [`ANATOMIE_D_UN_PROGRAMME.md`](./ANATOMIE_D_UN_PROGRAMME.md) — dans quel ordre écrire son code (squelette d'un programme Java).
- [`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md) — la syntaxe Java essentielle en une page.
- [`GLOSSAIRE.md`](./GLOSSAIRE.md) — les mots du Java expliqués simplement.

---

## ⚙️ Pré-requis : le JDK (`javac` + `java`)

Tu as besoin du **JDK** (*Java Development Kit*), qui fournit **`javac`** (le compilateur) et
**`java`** (la JVM pour lancer). Vérifie s'il est déjà là :

```bash
javac --version   # le compilateur
java --version    # la machine virtuelle
```

Sinon, voir les instructions d'installation dans [`00_demarrer`](./00_demarrer/).

## ▶️ Compiler et lancer un programme

> ⚠️ **Règle Java :** une classe `public` doit être dans un fichier du **même nom**. La
> classe `PremierProgramme` va donc dans `PremierProgramme.java`.

```bash
# 1. Compiler : crée le fichier .class (du bytecode)
javac java/00_demarrer/PremierProgramme.java

# 2. Lancer : -cp ("classpath") dit à la JVM OÙ chercher le .class.
#    On lui donne le DOSSIER, puis le NOM DE LA CLASSE (sans .class ni .java).
java -cp java/00_demarrer PremierProgramme
```

Le cycle de travail en Java est donc : **écrire → compiler (`javac`) → corriger les
erreurs → lancer (`java`)**.

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).

## 🔐 Module sécurité (pentest)

Pour découvrir le rôle de ce langage en **sécurité informatique** — à usage
**strictement éducatif et autorisé** (tes propres systèmes, CTF, labs) — voir le
dossier [`pentest/`](./pentest/).
