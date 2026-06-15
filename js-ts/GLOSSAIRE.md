# 📖 Glossaire — les mots de JavaScript & TypeScript expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**Argument** — La valeur concrète que tu donnes à une fonction quand tu l'appelles.
Dans `saluer("Alice")`, `"Alice"` est l'argument. (Côté définition, on parle de *paramètre*.)

**Asynchrone** — Une façon de travailler où l'on **lance une tâche longue** (lire un fichier,
interroger le réseau) et où l'on **continue autre chose** en attendant le résultat, au lieu
de rester bloqué. C'est le point fort de Node.js (module 04).

**async / await** — Deux mots-clés qui rendent le code asynchrone **lisible comme du code
normal**. `await` veut dire « attends ici que la promesse soit prête » ; il ne s'utilise qu'à
l'intérieur d'une fonction marquée `async`.

**Booléen** (`boolean`) — Un type qui ne vaut que `true` (vrai) ou `false` (faux). Sert aux
conditions.

**Boucle** — Une instruction qui répète des actions : `for`, `for...of` (« pour chaque… ») ou
`while` (« tant que… »).

**Callback** (*fonction de rappel*) — Une fonction qu'on **passe en argument** à une autre,
pour qu'elle soit appelée plus tard. Ex : `tableau.map(n => n * 2)` — le `n => n * 2` est un
callback. (Module 03.)

**Chaîne de caractères** (`string`) — Du texte, écrit entre guillemets `"..."`, apostrophes
`'...'` ou accents graves `` `...` ``.

**Classe** (`class`) — Un **moule** pour fabriquer plein d'objets qui se ressemblent. On crée
un objet à partir d'une classe avec `new` (module 08).

**Closure** (*fermeture*) — Une fonction qui **se souvient** des variables de l'endroit où elle
a été créée, même après que cet endroit a « fini ». Comme un sac à dos qu'elle emporte avec
elle. (Module 03.)

**CommonJS** — L'ancienne façon (toujours courante) de gérer les modules en Node.js, avec
`require(...)` pour importer et `module.exports` pour exporter.

**Commentaire** — Une note écrite pour les humains, ignorée par Node.js. Sur une ligne avec
`//`, ou sur plusieurs lignes entre `/*` et `*/`.

**console.log()** — L'instruction qui **affiche** quelque chose à l'écran (l'équivalent du
`print()` de Python).

**const** — Mot-clé pour déclarer une variable dont la valeur **ne sera pas réaffectée**.
À utiliser par défaut, c'est le plus sûr.

**Constante** — Une valeur fixe, qu'on déclare souvent avec `const` et qu'on nomme par
convention `EN_MAJUSCULES` quand c'est un réglage.

**ES Modules** (*ESM*) — La façon moderne de gérer les modules, avec `import` et `export`.
On l'active avec l'extension `.mjs` ou `"type": "module"` dans `package.json`.

**fetch** — La fonction intégrée pour faire une **requête réseau** (HTTP) et aller chercher des
données sur un serveur. Elle renvoie une promesse (module 09).

**Fonction** — Un bloc de code nommé et réutilisable. On la *définit* (avec `function` ou une
flèche `=>`), on l'*appelle* par son nom. Comme une recette qu'on peut refaire à volonté.

**Fonction fléchée** (*arrow function*) — Une écriture courte des fonctions avec `=>` :
`const doubler = (x) => x * 2;`. Très utilisée avec `map`, `filter`, etc.

**Import** — L'action d'ouvrir une boîte à outils (un module) pour s'en servir : `import` (ESM)
ou `require` (CommonJS).

**Index (indice)** — La position d'un élément dans un tableau. ⚠️ On compte **à partir de 0** :
`tableau[0]` est le premier élément.

**Interface** (TypeScript) — La **forme attendue** d'un objet : quels champs il doit avoir et
de quel type. Un contrat que l'objet doit respecter (module 05).

**JSON** (*JavaScript Object Notation*) — Un format texte pour stocker et échanger des données,
très proche des objets JavaScript. `JSON.stringify(obj)` transforme un objet en texte,
`JSON.parse(texte)` fait l'inverse.

**let** — Mot-clé pour déclarer une variable dont la valeur **pourra changer** plus tard.

**map / filter / reduce** — Trois méthodes de tableau très utiles : `map` **transforme** chaque
élément, `filter` **garde** ceux qui passent un test, `reduce` **combine** tout en une seule
valeur. (Module 03.)

**Module** — Un fichier de code regroupant des fonctions réutilisables, qu'on peut importer
ailleurs. (Module 06.)

**npm** (*Node Package Manager*) — L'outil, livré avec Node.js, qui installe les paquets
(bibliothèques) écrits par d'autres : `npm install ...`. L'équivalent de `pip` en Python.

**Node.js** — Le programme qui sait **exécuter du JavaScript en dehors du navigateur**, dans
le terminal. C'est ce qui nous permet d'écrire des scripts et des serveurs.

**null** — Une valeur qui signifie « **volontairement** vide » (j'ai mis rien, exprès).

**number** — Le type des nombres en JavaScript : entiers ET décimaux, c'est le même type
(`42`, `3.14`).

**Objet** — Un rangement de paires `clé: valeur`, entre `{ }`. Parfait pour décrire une chose :
`{ nom: "Alice", age: 30 }`. La clé sert d'étiquette pour retrouver la valeur.

**Paramètre** — Le nom d'une entrée dans la *définition* d'une fonction : `function saluer(nom)`
→ `nom` est un paramètre. (La valeur fournie à l'appel est l'*argument*.)

**Paquet** (*package*) — Une bibliothèque réutilisable installée avec npm. La liste des paquets
d'un projet est notée dans `package.json`.

**Promise** (*promesse*) — Un objet qui représente un **résultat à venir** (pas encore là). On
attend qu'elle soit *résolue* (succès) ou *rejetée* (échec), avec `.then()`/`.catch()` ou avec
`await`. (Module 04.)

**Prototype** — Le mécanisme **historique** par lequel les objets JavaScript partagent des
méthodes. Les `class` modernes reposent dessus, mais sont plus simples à lire. (Module 08.)

**require** — La fonction qui importe un module en style CommonJS : `const x = require("./x.js")`.

**return** — Le mot-clé qui fait *renvoyer* un résultat par une fonction à celui qui l'a appelée.

**Stack trace** (*pile d'appels*) — Le message d'erreur complet affiché quand le programme
plante. Il indique le type d'erreur et la ligne fautive. (Voir le module `07_debugger`.)

**Template literal** (*littéral de gabarit*) — Une chaîne entre **accents graves** `` ` `` où
l'on insère des variables avec `${ }` : `` `Bonjour ${nom}` ``. L'équivalent de la f-string.

**this** — Mot-clé qui, à l'intérieur d'une méthode de classe, désigne **l'objet courant**
(celui sur lequel la méthode a été appelée).

**Type** — La nature d'une valeur : `number`, `string`, `boolean`, `object`… On la révèle avec
`typeof`. En **TypeScript**, on peut les **écrire explicitement** pour attraper des erreurs tôt.

**TypeScript** — **JavaScript + les types**. On ajoute des étiquettes (`: number`, `: string`…)
qui aident à éviter les erreurs **avant** de lancer le programme (module 05).

**undefined** — Une valeur qui signifie « pas (encore) de valeur » : une variable déclarée mais
jamais remplie, ou une propriété qui n'existe pas.

**var** — L'ancienne façon de déclarer une variable, pleine de pièges. On ne l'utilise **plus** :
on préfère `const` et `let`.

**Variable** — Une boîte étiquetée qui retient une valeur : `const age = 30;`. Le `=` *range* la
valeur de droite dans la boîte de gauche.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
