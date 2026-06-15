# 📖 Glossaire — les mots du Java expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**Attribut** (ou *champ*) — Une **donnée** que possède un objet, déclarée dans la classe
(ex : `private String nom;`). C'est ce que l'objet *a*. On les met souvent en `private`
pour les protéger (voir **encapsulation**).

**Bytecode** — Le résultat de la compilation Java : un fichier `.class` dans une « langue
intermédiaire » que la **JVM** sait lire. Ce n'est pas du langage machine ; c'est ce qui
permet au même `.class` de tourner partout (« écris une fois, exécute partout »).

**Classe** — Le **modèle** (le plan, le moule) à partir duquel on fabrique des objets. Elle
regroupe des **attributs** (les données) et des **méthodes** (les actions). Comme un plan
d'architecte : à partir d'un plan, on peut bâtir plusieurs maisons.

**Compilateur (`javac`)** — Le programme qui **traduit** ton fichier `.java` (lisible par
les humains) en **bytecode** (`.class`). Tant qu'il y a une erreur, rien n'est produit.

**Constructeur** — Une **méthode spéciale** appelée automatiquement à la création d'un objet
(avec `new`). Elle porte le **même nom que la classe**, n'a **aucun type de retour**, et sert
à **initialiser** les attributs. Comme la mise en route d'un appareil neuf.

**Encapsulation** — Le principe de **protéger les données** d'un objet en les rendant
`private`, et de n'autoriser l'accès qu'à travers des méthodes contrôlées (**getters** /
**setters**). Comme un distributeur : tu n'attrapes pas l'argent à la main, tu passes par
les boutons prévus.

**Exception** — Un **accident** pendant l'exécution (division par zéro, fichier introuvable,
texte non convertible en nombre…). Sans rien faire, elle **arrête** le programme. On les
attrape avec `try` / `catch` pour réagir proprement.

**Exception *checked* (vérifiée)** — Une exception que le compilateur **t'oblige** à gérer
(`try`/`catch`) ou à déclarer (`throws`), sinon le code ne compile pas. Typique des
opérations risquées « prévisibles » comme l'accès aux fichiers (`IOException`).

**Exception *unchecked* (non vérifiée)** — Une exception que le compilateur **n'oblige pas**
à gérer ; elle signale souvent un bug de programmation (`NullPointerException`,
`ArrayIndexOutOfBoundsException`). À toi de l'éviter en écrivant du code correct.

**Generics** (génériques, `<T>`) — Une façon d'écrire **une seule** classe ou méthode qui
marche pour **plusieurs types**. Le `T` est un « type à remplir plus tard » : `Boite<String>`
range du texte, `Boite<Integer>` range des entiers, à partir du même code. C'est ce qui se
cache derrière les `< >` de `List<...>` et `Map<...>`.

**Getter / Setter** — Des **méthodes publiques** pour **lire** (`getNom()`) ou **modifier**
(`setNom(...)`) un attribut privé de façon contrôlée. Les portes d'entrée officielles vers
l'intérieur d'un objet.

**Héritage** (`extends`) — Le mécanisme par lequel une classe **récupère** les attributs et
méthodes d'une autre, pour les réutiliser et les **spécialiser**. `class Chat extends Animal`
se lit « un Chat **est un** Animal ». Évite de réécrire le code commun.

**Interface** (`implements`) — Un **contrat** : une liste de méthodes qu'une classe **promet**
de fournir, sans dire comment. `class Oiseau implements Volant` signifie « Oiseau s'engage à
savoir `voler()` ». Une classe peut implémenter **plusieurs** interfaces.

**`import`** — Une ligne en haut du fichier qui **ouvre une boîte à outils** de la
bibliothèque standard (ex : `import java.util.ArrayList;` pour les listes). Sans elle,
l'outil est inconnu.

**JVM** (*Java Virtual Machine*) — La **machine virtuelle Java** : le programme qui **exécute**
le **bytecode** (`.class`). Comme elle existe sur tous les systèmes (Windows, macOS, Linux),
le même `.class` tourne partout. On la lance avec la commande `java`.

**Lambda** (`->`) — Une **mini-fonction anonyme** (sans nom) qu'on écrit en une ligne :
`n -> n >= 10` se lit « donne `n`, renvoie `n >= 10` ». Très pratique avec les **streams**
pour dire « voici l'action à appliquer ».

**main** — La méthode de **départ** : `public static void main(String[] args)`. Quand on
lance le programme, l'exécution commence par là. **Tout part de `main`.**

**Méthode** — Une **action** que sait faire un objet (ou une classe), un bloc de code nommé
et réutilisable (`int additionner(int a, int b) { ... }`). C'est ce que l'objet *fait*.
L'équivalent d'une fonction, mais rattachée à une classe.

**Objet** — Un **exemplaire concret** fabriqué à partir d'une classe (avec `new`). Si la
classe `Chien` est le plan, alors `new Chien("Rex")` est un chien réel. Chaque objet a ses
**propres** valeurs d'attributs.

**`@Override`** — Une **annotation** qu'on met au-dessus d'une méthode pour dire « je
**redéfinis** la méthode du parent ». Le compilateur vérifie alors que tu redéfinis bien une
méthode existante (et te signale les fautes de frappe).

**Polymorphisme** — Le fait qu'un même appel (`animal.crier()`) produise un **comportement
différent** selon le vrai type de l'objet (un `Chat` miaule, un `Chien` aboie), même quand on
les manipule via leur type parent `Animal`. Un seul ordre, plusieurs réponses.

**Ramasse-miettes** (*garbage collector*) — Le mécanisme qui **libère automatiquement** la
mémoire des objets dont plus personne ne se sert. Contrairement au C++ (`delete` manuel), tu
n'as rien à libérer toi-même en Java.

**Stack trace** (pile d'appels) — Le « pavé rouge » affiché quand une exception n'est pas
attrapée. Loin d'être ton ennemi, il t'indique **quelle** erreur s'est produite et **où
exactement** (le fichier et la ligne). À lire **de haut en bas**.

**Stream** (flux) — Un **tapis roulant** sur lequel passent les éléments d'une collection.
On y enchaîne des opérations lisibles : `.filter(...)` (garder), `.map(...)` (transformer),
`.count()` / `.collect(...)` (résumer). Plus court et clair qu'une boucle `for`.

**`String`** — Le type **texte** en Java (avec un grand `S`), entre guillemets `"..."`. On
colle deux textes avec `+`. ⚠️ Pour comparer deux `String`, on utilise `.equals()` et **non**
`==`.

**Thread** (fil d'exécution) — Une tâche qui s'exécute **en parallèle** des autres. On le
crée, on le lance avec `.start()`, et on l'attend avec `.join()`. Permet de faire plusieurs
choses « en même temps », mais partager des données entre threads demande de la prudence.

**`this`** — Un mot qui désigne **l'objet courant**, celui sur lequel la méthode est appelée.
On l'utilise surtout pour distinguer l'attribut du paramètre : `this.nom = nom;`.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
