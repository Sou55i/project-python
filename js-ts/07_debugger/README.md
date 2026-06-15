# Module 07 — Déboguer : trouver et corriger les bugs

Un **bug**, c'est un comportement du programme qui n'est pas celui qu'on voulait.
**Tout le monde** en fait, tout le temps. La vraie compétence n'est pas d'éviter les
bugs (impossible), mais de savoir les **traquer** calmement. Voici ta boîte à outils.

---

## 1. Le réflexe n°1 : `console.log`

Quand quelque chose ne marche pas, la première question est : *« qu'est-ce que mon
programme a VRAIMENT dans les mains à ce moment ? »*. Pour le savoir, on **affiche**
la valeur. C'est l'outil le plus simple et le plus utilisé au monde.

```javascript
const total = prix * quantite;
console.log("total =", total); // on REGARDE ce que vaut total
```

> 💡 Astuce : donne un **libellé** à ce que tu affiches (`"total ="`). Quand tu en
> as dix, tu t'y retrouves tout de suite.

Deux variantes très utiles :

- **`console.error("...")`** : affiche un message d'**erreur** (sur la sortie d'erreur,
  souvent en rouge). À utiliser pour signaler un problème.
- **`console.table(tableau)`** : affiche un **tableau** ou une liste d'objets sous
  forme de **grille** lisible. Parfait pour inspecter des données.

---

## 2. Vérifier la SYNTAXE sans exécuter : `node --check`

Parfois le bug est une simple **faute de frappe** (une accolade oubliée, une virgule
en trop). Pas besoin de lancer le programme pour la repérer :

```bash
node --check js-ts/07_debugger/demo_debug.js
```

`--check` lit le fichier et te dit **juste** si la syntaxe est correcte, sans rien
exécuter. S'il ne dit rien, c'est que la syntaxe est bonne.

---

## 3. Le vrai débogueur : `node --inspect` (pour info)

Pour les cas difficiles, Node a un **débogueur** qui permet de **mettre le programme
en pause** ligne par ligne et d'inspecter toutes les variables :

```bash
node --inspect-brk js-ts/07_debugger/demo_debug.js
```

Tu ouvres ensuite `chrome://inspect` dans le navigateur Chrome (ou les outils de ton
éditeur) pour piloter l'exécution. C'est puissant, mais **`console.log` suffit dans
90 % des cas** quand on débute : on te le mentionne pour que tu saches que ça existe.

---

## 4. Les erreurs les plus fréquentes (et leur cause)

### `undefined` — « il n'y a rien ici »
Tu lis une variable ou une clé d'objet qui **n'existe pas**.

```javascript
const personne = { nom: "Alice" };
console.log(personne.age); // undefined : la clé "age" n'existe pas
```

### `NaN` — *Not a Number*, « pas un nombre »
Apparaît quand un calcul mélange un **nombre** et quelque chose **qui n'en est pas un**.

```javascript
console.log(10 * "abc"); // NaN : on ne peut pas multiplier par du texte
```

### Oublier `await` (asynchrone non attendu)
Si tu oublies `await` devant une fonction asynchrone, tu récupères la **Promesse**
elle-même (un objet « résultat à venir »), pas la valeur attendue.

```javascript
const data = lireFichier(); // ❌ oublié await -> "data" est une Promise, pas le contenu
```

---

## 5. Le filet de sécurité : `try / catch`

Certaines opérations peuvent **échouer** (un fichier absent, un réseau coupé, des
données invalides). Sans protection, l'erreur fait **planter** tout le programme.
`try / catch` permet de **l'attraper** et de réagir proprement.

```javascript
try {
  // "essaie" d'exécuter ce bloc
  const data = JSON.parse(texteAbime); // peut casser si le texte n'est pas du JSON
} catch (erreur) {
  // "attrape" l'erreur si ça casse, et continue sans planter
  console.error("Données illisibles :", erreur.message);
}
```

> 📌 `erreur.message` contient l'explication courte du problème. C'est souvent
> la première chose à lire pour comprendre.

---

## ▶️ À toi de jouer

Le fichier `demo_debug.js` illustre chaque outil ci-dessus, **sans planter** : il
provoque volontairement des situations (undefined, NaN, erreur attrapée) et les
affiche pour que tu **voies** ce qui se passe.

```bash
node --check js-ts/07_debugger/demo_debug.js   # 1) vérifier la syntaxe
node js-ts/07_debugger/demo_debug.js           # 2) lancer la démo
```

➡️ Module suivant : [`08_classes`](../08_classes/) — créer ses propres « moules » d'objets.
