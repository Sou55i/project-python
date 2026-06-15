# Module 03 — Fonctions avancées : le cœur de JavaScript

Tu connais déjà les fonctions (module 01) : elles **emballent du code** pour le
réutiliser. En JavaScript, les fonctions sont **bien plus puissantes** que ça :
on peut les passer en argument, les renvoyer, et même leur faire « se souvenir »
de choses. C'est ce qui fait la force du langage. On y va doucement.

---

## 1. Les fonctions fléchées `=>` (rappel et détails)

Tu as croisé la **fonction fléchée** au module 01. C'est une écriture **plus
courte** d'une fonction. Comparons les deux écritures de la même fonction :

```javascript
// Écriture classique :
function doubler(x) {
  return x * 2;
}

// Écriture fléchée (équivalente) :
const doubler = (x) => x * 2;
```

Règles utiles :
- **Un seul paramètre** : les parenthèses sont optionnelles → `x => x * 2`.
- **Corps sur une ligne** : le `return` est **sous-entendu** (pas besoin de l'écrire).
- **Corps sur plusieurs lignes** : on remet des accolades **et** le `return`.

```javascript
const additionner = (a, b) => {
  const total = a + b; // on peut écrire plusieurs lignes
  return total;        // ici le return est obligatoire
};
```

---

## 2. Les callbacks : une fonction passée à une autre fonction

En JavaScript, **une fonction est une valeur** comme une autre. On peut donc la
**passer en argument** à une autre fonction. Cette fonction passée s'appelle un
**callback** (« fonction de rappel »).

Tu en as déjà utilisé sans le savoir : `map`, `filter`, `find` reçoivent un
callback ! Ici, `map` **rappelle** la fonction `(n => n + 1)` pour chaque élément.

```javascript
[1, 2, 3].map((n) => n + 1); // (n) => n + 1  est le callback
```

> 💡 Idée clé : on ne donne pas seulement des **données** à une fonction, on peut
> aussi lui donner un **comportement** (« voici quoi faire »).

---

## 3. Les fonctions d'ordre supérieur

Une **fonction d'ordre supérieur** (*higher-order function*) est simplement une
fonction qui **reçoit** une fonction en argument **ou** qui **renvoie** une
fonction. Pas de magie : c'est juste un nom pour ce qu'on vient de voir.

```javascript
// Reçoit une fonction (un callback) :
function repeter(n, action) {
  for (let i = 0; i < n; i++) {
    action(i); // on APPELLE le callback
  }
}
```

---

## 4. Les closures (fermetures) : une fonction qui se souvient

C'est la notion la plus subtile, alors prenons notre temps. Une **closure**
(« fermeture ») se produit quand une fonction **interne** continue d'avoir accès
aux variables de la fonction **externe**, même **après** que celle-ci a terminé.

```javascript
function creerCompteur() {
  let compte = 0;            // variable "privée"
  return () => {             // on RENVOIE une fonction...
    compte = compte + 1;     // ...qui se souvient de "compte"
    return compte;
  };
}

const compteur = creerCompteur();
compteur(); // 1
compteur(); // 2  -> "compte" a survécu entre les deux appels !
```

La fonction renvoyée « garde un fil » vers `compte`. Chaque compteur créé a **son
propre** `compte`, bien rangé et inaccessible de l'extérieur. C'est très pratique
pour **mémoriser un état** sans utiliser de variable globale.

---

## ▶️ À toi de jouer

```bash
node js-ts/03_fonctions_avancees/fonctions.js
```

Lis le fichier en entier (il est commenté) et suis le bloc
**🗺️ CHEMINEMENT DU SCRIPT** au début pour comprendre l'ordre des étapes.

➡️ Module suivant : [`04_async`](../04_async/) — l'asynchrone, le point fort de Node.
