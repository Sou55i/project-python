# Module 06 — Organiser son code en modules + découvrir npm

Jusqu'ici, tout ton code tenait dans **un seul fichier**. Ça va très bien pour
s'entraîner… mais un vrai programme se découpe en **plusieurs fichiers** qui se
passent des outils. Chaque fichier est un **module** : une petite boîte de code
qu'on peut **réutiliser** ailleurs. C'est l'objet de ce module.

---

## 1. Pourquoi découper en modules ?

Imagine une cuisine : tu ne ranges pas les couteaux, les épices et les casseroles
dans le **même tiroir**. Tu sépares, tu étiquettes, tu retrouves vite. Le code,
c'est pareil :

- chaque fichier a **un rôle clair** (les outils mathématiques d'un côté, l'affichage
  de l'autre…) ;
- on **réutilise** un module dans plusieurs endroits sans recopier le code ;
- on **lit** et on **corrige** plus facilement un petit fichier qu'un énorme.

L'idée centrale : un module **exporte** (met à disposition) certaines choses, et un
autre fichier les **importe** (les récupère pour s'en servir).

---

## 2. Deux systèmes de modules en JavaScript

Il existe **deux façons** d'exporter/importer. C'est important de connaître les
deux, car tu croiseras les deux dans la vraie vie.

### a) CommonJS — `module.exports` / `require` (l'historique de Node.js)

C'est le système **d'origine** de Node.js. Il fonctionne **partout** en Node, sans
réglage particulier.

```javascript
// Dans outils.js : on MET À DISPOSITION des fonctions
function additionner(a, b) {
  return a + b;
}
module.exports = { additionner }; // on exporte un objet contenant nos outils

// Dans utiliser.js : on RÉCUPÈRE ce que outils.js a exporté
const outils = require("./outils.js"); // require = "va chercher ce module"
console.log(outils.additionner(2, 3)); // 5
```

> 📌 Le `./` dans `require("./outils.js")` veut dire « le fichier **à côté de moi**,
> dans le même dossier ». Sans `./`, Node chercherait un **paquet installé** (voir
> plus bas).

### b) ES Modules — `export` / `import` (le standard moderne)

C'est la syntaxe **moderne**, la même que dans le navigateur. En Node, pour l'activer
le plus simplement, on nomme ses fichiers en **`.mjs`** (ou on met `"type": "module"`
dans le `package.json`).

```javascript
// Dans outils.mjs
export function additionner(a, b) {
  return a + b;
}

// Dans utiliser.mjs
import { additionner } from "./outils.mjs";
console.log(additionner(2, 3)); // 5
```

> 💡 Même idée des deux côtés : un fichier **donne** (`export` / `module.exports`),
> l'autre **prend** (`import` / `require`). Seule la **syntaxe** change.

---

## 3. À quoi sert npm et le `package.json` ?

**npm** (*Node Package Manager*) est l'**outil livré avec Node** qui sert à :

1. **installer du code écrit par d'autres** (des « paquets ») pour ne pas tout
   réécrire soi-même — par exemple une bibliothèque pour faire des dates, des
   couleurs dans le terminal, etc. ;
2. **décrire ton projet** dans un fichier spécial : le **`package.json`**.

Le `package.json` est la **carte d'identité** de ton projet. Il contient son nom,
sa version, des **scripts** raccourcis, et la **liste des paquets** dont il dépend.

```jsonc
{
  "name": "mon-projet",
  "version": "1.0.0",
  "scripts": {
    "start": "node utiliser.js"   // "npm start" lancera cette commande
  },
  "dependencies": {}              // ici se rangeraient les paquets installés
}
```

Quelques commandes utiles (à connaître, pas besoin de les lancer ici) :

```bash
npm init -y                # crée un package.json avec des valeurs par défaut
npm install nom-du-paquet  # télécharge un paquet et l'ajoute aux dependencies
npm start                  # exécute le script "start" défini ci-dessus
```

> 📌 Quand tu fais `npm install`, les paquets atterrissent dans un dossier
> **`node_modules/`** (qu'on ne lit jamais à la main, et qu'on ne met pas sur Git).

---

## ▶️ À toi de jouer

Dans ce dossier, deux fichiers travaillent ensemble :

- **`outils.js`** : exporte deux petites fonctions (avec `module.exports`) ;
- **`utiliser.js`** : les importe (avec `require`) et s'en sert.

Lance le fichier qui **utilise** l'autre :

```bash
node js-ts/06_modules_npm/utiliser.js
```

Tu verras que `utiliser.js` se sert de fonctions qui sont **écrites ailleurs**.
C'est tout le principe des modules ! Un exemple jumeau en syntaxe moderne est
fourni dans `outils.mjs` / `utiliser.mjs` :

```bash
node js-ts/06_modules_npm/utiliser.mjs
```

➡️ Module suivant : [`07_debugger`](../07_debugger/) — trouver et corriger les bugs.
