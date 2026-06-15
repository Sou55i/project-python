# Projet capstone — Un gestionnaire de tâches persisté en JSON

Bravo d'être arrivé jusqu'ici ! Ce **projet final** (on dit *capstone*, la « pierre
de couronnement ») rassemble tout ce que tu as appris : variables, tableaux, objets,
fonctions, classes, et même l'écriture de fichiers. On construit une **petite
application** utile : un **gestionnaire de tâches** (une *todo list*) qui **se
souvient** des tâches d'une exécution à l'autre.

---

## 1. Ce que fait l'application

Une *todo list* classique : on **ajoute** des tâches, on les **marque comme faites**,
on les **affiche**. La nouveauté ici, c'est la **persistance** : les tâches sont
**sauvegardées dans un fichier**, donc elles ne disparaissent pas quand le programme
se termine.

> 📌 Ce projet est **non interactif** : il ne te pose pas de questions. Il ajoute des
> tâches de démonstration, les sauvegarde, **recharge** le fichier, puis affiche le
> résultat. Tu peux le relancer autant de fois que tu veux.

---

## 2. La pièce nouvelle : le module `fs` (file system)

`fs` est un module **intégré** à Node (pas besoin de l'installer) qui sert à **lire**
et **écrire** des fichiers sur le disque. On utilise sa version moderne, à base de
Promesses (`await`).

```javascript
const fs = require("node:fs/promises"); // la boîte à outils "fichiers"

await fs.writeFile("data.json", "...");      // ÉCRIRE dans un fichier
const contenu = await fs.readFile("data.json", "utf-8"); // LIRE un fichier
```

---

## 3. Le format JSON pour ranger les données

Pour sauvegarder nos tâches (qui sont des **objets** dans un **tableau**), on les
transforme en **texte** au format **JSON** :

- `JSON.stringify(donnees, null, 2)` : transforme un objet/tableau JS en **texte**
  (le `2` met une jolie indentation lisible) ;
- `JSON.parse(texte)` : fait l'inverse, retransforme le **texte** en objet/tableau JS.

C'est ainsi qu'on **sauvegarde** (objet → texte → fichier) et qu'on **recharge**
(fichier → texte → objet).

---

## 4. Où sont rangées les données ?

Le fichier de sauvegarde est créé dans un sous-dossier **`exemples/`**, à côté du
script. Le programme crée ce dossier tout seul s'il n'existe pas. Tu peux ensuite
ouvrir `exemples/taches.json` pour voir tes tâches en texte brut.

---

## ▶️ À toi de jouer

```bash
node --check js-ts/projets/gestionnaire_taches.js   # vérifier la syntaxe
node js-ts/projets/gestionnaire_taches.js           # lancer le projet
```

Le script :
1. crée le dossier `exemples/` si besoin ;
2. ajoute quelques tâches de démonstration et en marque une comme faite ;
3. **sauvegarde** le tout dans `exemples/taches.json` ;
4. **recharge** ce fichier depuis le disque (pour prouver la persistance) ;
5. **affiche** les tâches rechargées.

🎉 Si tu comprends ce projet en entier, tu maîtrises les fondations du développement
Node.js. Félicitations pour tout le parcours !
