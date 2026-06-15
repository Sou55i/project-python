# Module 05 — Introduction à TypeScript : ajouter les types

On revient sur le mot croisé au tout début du parcours (module 00) : **TypeScript**,
c'est **JavaScript + les types**. Maintenant que tes bases JS sont solides, on
peut découvrir ce que les types apportent. Bonne nouvelle : **tout ce que tu sais
déjà en JavaScript reste vrai** ; on ne fait qu'**ajouter des étiquettes**.

---

## 1. Pourquoi des types ?

Un **type** précise la **nature** d'une valeur : un nombre ? du texte ? un booléen ?
En JavaScript, rien ne t'empêche d'écrire une bêtise comme additionner un texte et
un nombre, et le bug n'apparaît qu'**à l'exécution**. TypeScript repère ces erreurs
**avant** même de lancer le programme, en lisant ton code.

```typescript
let age: number = 30;
age = "trente"; // ❌ TypeScript refuse : "trente" est un texte, pas un nombre
```

> 💡 Les types sont des **garde-fous** : ils t'évitent des erreurs et **documentent**
> ton code (on voit tout de suite ce qu'une fonction attend et renvoie).

---

## 2. Les types de base et les annotations

Une **annotation** s'écrit avec **deux-points** après le nom : `nom: type`.

```typescript
let prenom: string = "Alice"; // string  : du texte
let age: number = 30;         // number  : un nombre (entier ou à virgule)
let majeur: boolean = true;   // boolean : true ou false
```

> 📌 Souvent, TypeScript **devine** le type tout seul (on dit qu'il l'« infère ») :
> `let age = 30;` est déjà compris comme un `number`. On annote surtout là où c'est
> utile : les **paramètres de fonctions** et les **structures de données**.

---

## 3. Typer une fonction

On annote **chaque paramètre** et, après les parenthèses, le type de **retour**.

```typescript
// (a: number, b: number) -> les paramètres ; ": number" -> le type renvoyé
function additionner(a: number, b: number): number {
  return a + b;
}
```

Une fonction qui ne renvoie rien a le type de retour spécial **`void`** (« vide ») :

```typescript
function direBonjour(nom: string): void {
  console.log(`Bonjour ${nom}`); // pas de "return" : void
}
```

---

## 4. Les interfaces : décrire la forme d'un objet

Une **interface** est un **modèle** qui décrit les clés et les types d'un objet.
C'est très pratique pour les objets qu'on a vus au module 02.

```typescript
interface Personne {
  prenom: string;
  age: number;
  ville?: string; // le "?" rend la clé OPTIONNELLE
}

const alice: Personne = { prenom: "Alice", age: 30 }; // ✅ ville est facultative
```

Si tu oublies une clé obligatoire ou que tu mets le mauvais type, TypeScript te
prévient immédiatement.

---

## 5. Compiler et lancer

Rappel : Node.js exécute du **`.js`**, pas du `.ts`. On passe donc par une étape
de **compilation** (on dit aussi *transpilation*) avec l'outil **`tsc`** (le
*TypeScript Compiler*). Il **vérifie les types** puis **produit un `.js`**.

```bash
# 1) Compiler : vérifie les types ET génère exemple.js à côté du .ts
tsc js-ts/05_typescript/exemple.ts

# 2) Lancer le JavaScript produit avec Node, comme d'habitude
node js-ts/05_typescript/exemple.js
```

> 💡 Pour **seulement vérifier les types** sans générer de fichier, on ajoute
> `--noEmit` : `tsc --noEmit js-ts/05_typescript/exemple.ts`. Pratique pour
> contrôler son code sans rien produire.

---

## ▶️ À toi de jouer

Lis les deux fichiers (chaque ligne est commentée), puis compile et lance :

```bash
tsc js-ts/05_typescript/exemple.ts && node js-ts/05_typescript/exemple.js
tsc js-ts/05_typescript/mini_exemple.ts && node js-ts/05_typescript/mini_exemple.js
```

Essaie ensuite d'**introduire volontairement une erreur de type** (mettre du texte
dans un `number`) et relance `tsc` : observe comment il t'avertit **avant**
l'exécution. C'est tout l'intérêt de TypeScript.

🎉 Bravo, tu as parcouru les bases de JavaScript **et** de TypeScript !
