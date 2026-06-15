# 🟨 Apprendre le JavaScript & TypeScript (avec Node.js) — pour grands débutants

**JavaScript** (souvent abrégé **JS**) est le langage **du web** : au départ, il rendait les
pages internet *vivantes* (boutons, animations, formulaires). Mais grâce à **Node.js** (un
programme qui sait exécuter du JavaScript *en dehors* du navigateur), on peut aussi écrire
des **scripts** d'automatisation et des **serveurs**, directement dans le terminal — comme on
le ferait en Python. **TypeScript** (abrégé **TS**), lui, c'est **JavaScript + les types** :
des étiquettes qui précisent la nature d'une valeur et attrapent des erreurs **avant** même
de lancer le programme.

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par
> ligne**. Lis, lance, modifie.

---

## 🆚 Différences avec Python

Si tu viens de Python, voici les principaux changements de décor :

| | Python | JavaScript (Node.js) |
|--|--------|----------------------|
| Exécution | interprété (`python script.py`) | interprété (`node script.js`) |
| Types | dynamiques (`x = 5`) | dynamiques (`let x = 5`) ; **TypeScript** ajoute des types statiques |
| Blocs | **indentation** obligatoire | des **accolades `{ }`** |
| Fin d'instruction | retour à la ligne | un **point-virgule `;`** (conseillé) |
| Déclarer | `x = 5` | `const x = 5` (fixe) ou `let x = 5` (modifiable) |
| Afficher | `print(...)` | `console.log(...)` |
| Insérer une variable | f-string `f"{nom}"` | *template literal* `` `${nom}` `` (accents graves) |
| Absence de valeur | `None` | `null` **et** `undefined` |
| Listes / dictionnaires | `list` / `dict` | *tableau* `[ ]` / *objet* `{ }` |
| Boîtes à outils | `pip` + `import` | `npm` + `import`/`require` |

> 💬 Bonne nouvelle : comme Python, JavaScript est **interprété**. Tu écris du texte, Node.js
> le lit et l'exécute **directement**, sans étape de compilation manuelle à gérer.

---

## 📚 Le parcours (fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Comprendre JavaScript, Node.js, le terminal, `console.log`, les commentaires |
| 1 | [`01_les_bases`](./01_les_bases/) | Variables (`const`/`let`), types, *template literals*, conditions, boucles, fonctions |
| 2 | [`02_objets_tableaux`](./02_objets_tableaux/) | Ranger les données : objets `{ }` (clé → valeur) et tableaux `[ ]` (suite ordonnée) |
| 3 | [`03_fonctions_avancees`](./03_fonctions_avancees/) | Fonctions fléchées, callbacks, closures, `map`/`filter`/`reduce` |
| 4 | [`04_async`](./04_async/) | L'asynchrone : `Promise`, `async`/`await`, le point fort de Node.js |
| 5 | [`05_typescript`](./05_typescript/) | Ajouter les types : annotations, `interface`, attraper les erreurs avant l'exécution |
| 6 | [`06_modules_npm`](./06_modules_npm/) | Découper son code en modules (`import`/`require`), installer des paquets avec **npm** |
| 7 | [`07_debugger`](./07_debugger/) | Déboguer : lire une *stack trace*, bugs fréquents, garder son calme |

### 🚀 Modules avancés

Une fois les fondations solides, va plus loin :

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 8 | [`08_classes`](./08_classes/) | Les classes : créer ses propres « moules » d'objets (`class`, `constructor`, méthodes) |
| 9 | [`09_http`](./09_http/) | Une requête réseau avec `fetch` : aller chercher des données sur un serveur (HTTP) |

> 🛠️ **Prêt à assembler ?** Une fois les fondations digérées, passe au dossier
> [`projets/`](./projets/) : un mini-projet **capstone** qui COMBINE plusieurs modules
> (objets + tableaux + fonctions + classes + fichiers) pour fabriquer un vrai petit outil.

> 📎 **Ressources** (à garder sous la main) : l'[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md)
> (cheat-sheet de syntaxe JS/TS), le [GLOSSAIRE.md](./GLOSSAIRE.md) (le sens des mots du
> langage) et l'[ANATOMIE_D_UN_SCRIPT.md](./ANATOMIE_D_UN_SCRIPT.md) (dans quel ordre ranger
> le code d'un fichier Node : imports, constantes, fonctions, point d'entrée…).

---

## ⚙️ Pré-requis : installer Node.js (et npm)

Vérifie si c'est déjà là :

```bash
node --version    # Node.js : l'exécuteur de JavaScript
npm --version     # npm : le gestionnaire de paquets (livré AVEC Node.js)
```

Sinon, télécharge Node.js sur **<https://nodejs.org/>** (choisis la version **LTS**, la plus
stable). L'installation ajoute **les deux** commandes `node` et `npm` à ton terminal.

---

## ▶️ Comment lancer un programme

```bash
node js-ts/00_demarrer/premier_script.js   # exécute un fichier JavaScript
node --check js-ts/01_les_bases/bases.js   # vérifie la SYNTAXE sans exécuter
```

Pour le **TypeScript** (module 05), il faut un outil supplémentaire qui le traduit en
JavaScript ; les explications sont dans le README du module.

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).

---

## 🔐 Module sécurité (pentest)

Pour découvrir le rôle de ce langage en **sécurité informatique** — à usage
**strictement éducatif et autorisé** (tes propres machines, CTF, labs) — voir le
dossier [`pentest/`](./pentest/).
