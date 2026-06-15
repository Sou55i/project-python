# 🧭 Anatomie d'un script Node : dans quel ordre écrire son code ?

Beaucoup de débutants savent écrire des lignes de JavaScript, mais ne savent pas **dans quel
ordre les ranger** pour former un script complet et propre. Ce guide explique le
**cheminement logique** d'un script Node.js, du début à la fin.

> 📌 À lire après les modules `00_demarrer` et `01_les_bases`, et à garder sous la main
> comme aide-mémoire.

---

## 1. LA règle d'or : Node lit de HAUT en BAS

C'est le point le plus important, et la cause n°1 des bugs de débutant.

> Node.js exécute ton fichier **ligne par ligne, du haut vers le bas**, comme tu lis une
> page. **Une chose doit exister AVANT qu'on l'utilise.**

Tu ne peux pas verser le café dans une tasse que tu n'as pas encore sortie du placard.
En code, c'est pareil : tu ne peux pas utiliser une variable, une fonction ou un outil
**avant** de l'avoir créé/importé plus haut.

---

## 2. Le squelette standard d'un script complet

Presque tous les scripts Node bien écrits suivent **ce même ordre**, de haut en bas :

```javascript
// Description du script : à quoi il sert, comment le lancer.   ┐ (1) EN-TÊTE
//   Lance-le :  node mon_script.js                             ┘    (commentaire)

import fs from "node:fs";                                       ┐ (2) IMPORTS
// (ou en CommonJS :  const fs = require("node:fs");)           ┘    (les outils)

const DOSSIER_SORTIE = "resultats";                             ┐ (3) CONSTANTES
const TIMEOUT = 10;                                             ┘    (valeurs fixes, EN MAJUSCULES)

function telecharger(url) {                                     ┐
  // Fait une seule chose, bien.                                │ (4) FONCTIONS
  ...                                                           │    (on les DÉFINIT ici, elles
}                                                               │     ne s'exécutent PAS encore)
function sauvegarder(donnees) {                                 │
  ...                                                           │
}                                                               ┘

function main() {                                               ┐ (5) POINT D'ENTRÉE
  const page = telecharger("https://exemple.com");              │    (le code qui DÉMARRE tout
  sauvegarder(page);                                            │     et appelle les fonctions)
}                                                               │
main();                                                         ┘    on APPELLE main() tout en bas
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 1 | **En-tête** | La 1re chose qu'on lit : « ce script sert à… » et « voici comment le lancer ». |
| 2 | **Imports** | On **ouvre les caisses à outils** avant de s'en servir : `import` (moderne) ou `require` (CommonJS). (Cours détaillé : module [`06_modules_npm`](./06_modules_npm/).) |
| 3 | **Constantes** | Les réglages fixes, regroupés en haut pour les changer facilement. Déclarés avec `const`, nommés par convention `EN_MAJUSCULES`. |
| 4 | **Fonctions** | On **définit** les actions réutilisables. ⚠️ Définir ≠ exécuter : le code d'une fonction ne tourne que lorsqu'on l'**appelle**. |
| 5 | **Point d'entrée** | Le **chef d'orchestre** : souvent une fonction `main()` qui appelle les autres dans le bon ordre. On la définit, puis on l'**appelle** (`main();`) tout en bas. |

> 💡 « Définir une fonction » = écrire la recette. « Appeler la fonction » = cuisiner le
> plat. On écrit toutes les recettes en haut, puis on cuisine en bas.

> 💬 `import` (ES Modules) vs `require` (CommonJS) : deux façons d'importer. La première est
> moderne, la seconde historique mais toujours très répandue. Le module 06 explique les deux.

---

## 3. La logique INTERNE : entrée → traitement → sortie

À l'intérieur du point d'entrée (ou d'une fonction), le code suit presque toujours
**3 phases**, dans cet ordre :

```
   1. ENTRÉE              2. TRAITEMENT             3. SORTIE
   (je récupère           (je calcule, je décide,   (j'affiche ou
    les données)           je transforme)            j'enregistre)
   ──────────             ───────────────          ──────────
   process.argv           if / else                console.log()
   fs.readFileSync(...)   for / while / map        fs.writeFileSync(...)
   await fetch(...)       calculs, fonctions        envoyer un résultat
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

> 💬 Côté asynchrone : si une étape « prend du temps » (lecture réseau, gros fichier), tu
> verras un `await` devant. Pense alors à marquer ta fonction `async` (module 04).

---

## 4. Comment lire un script complexe qu'on découvre

Quand un script te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va tout en bas**, à l'appel `main();` (ou au code principal). C'est le **point de départ**
   réel du programme : il montre l'enchaînement principal.
2. **Suis les appels de fonctions** depuis ce bloc. Quand tu vois `telecharger(url)`,
   remonte lire la fonction `function telecharger` pour comprendre ce qu'elle fait.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le bloc
> principal), puis tu ouvres les chapitres qui t'intéressent (les fonctions).

---

## 5. Récapitulatif visuel

```
┌─────────────────────────────────────────────┐
│ 1. // En-tête      : à quoi sert le script    │
│ 2. import / require : les outils              │  ← on prépare
│ 3. CONSTANTES       : les réglages fixes      │
├─────────────────────────────────────────────┤
│ 4. function ...()   : on DÉFINIT les actions  │  ← on outille
├─────────────────────────────────────────────┤
│ 5. function main() { entrée -> traitement     │
│                       -> sortie }             │  ← on EXÉCUTE
│    main();          : on APPELLE le tout      │
└─────────────────────────────────────────────┘
              (Node lit de haut en bas)
```

➡️ Voir aussi : [AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe et [GLOSSAIRE.md](./GLOSSAIRE.md)
pour le sens des mots.
