# Module 09 — Une requête HTTP avec `fetch` (réseau)

Jusqu'ici, ton programme travaillait **tout seul**, sur ta machine. Mais le vrai
intérêt de Node.js, c'est souvent d'aller **chercher des données ailleurs** : la
météo, un taux de change, une liste d'articles… Ces données vivent sur des
**serveurs** qu'on interroge via le réseau, avec le protocole **HTTP**.

---

## 1. Le vocabulaire en deux mots

- **HTTP** : le « langage » que parlent les navigateurs et les serveurs pour
  s'échanger des informations sur internet.
- Une **requête** : ta question (« donne-moi cette page / ces données »).
- Une **réponse** : ce que le serveur te renvoie (les données, + un **code** qui dit
  si tout s'est bien passé).

Quelques **codes de statut** courants : `200` = OK, `404` = pas trouvé, `500` =
erreur du serveur.

---

## 2. `fetch` est intégré à Node 22

Bonne nouvelle : depuis les versions récentes, Node **inclut** une fonction
**`fetch`** (la même que dans le navigateur). Rien à installer. `fetch` est
**asynchrone** (le réseau prend du temps) : on l'utilise donc avec `await`, comme au
module 04.

```javascript
const reponse = await fetch("https://exemple.com/donnees"); // on ATTEND la réponse
const data = await reponse.json(); // on lit le corps et on le transforme en objet
console.log(data);
```

> 📌 Deux `await` ! Le premier attend la **réponse** ; le second attend la **lecture**
> du corps (souvent du **JSON**, le format texte des données structurées).

---

## 3. Le réseau peut échouer : on PRÉVOIT le pire

Contrairement au reste de ton code, une requête réseau peut **rater** pour des
raisons qui ne dépendent pas de toi : pas de connexion, serveur en panne, accès
bloqué… Un programme sérieux **ne plante pas** dans ce cas : il **attrape** l'erreur
avec `try / catch` et affiche un message clair.

```javascript
try {
  const reponse = await fetch("https://exemple.com/donnees");
  const data = await reponse.json();
  console.log("Reçu :", data);
} catch (erreur) {
  // Pas de réseau ? Serveur injoignable ? On gère proprement, on ne plante pas.
  console.error("Impossible de joindre le serveur :", erreur.message);
}
```

> 💡 C'est exactement ce que fait le script de ce module. **Si l'accès réseau est
> bloqué dans ton environnement, le script ne plantera pas** : il affichera un
> message d'erreur propre et se terminera normalement. C'est le comportement attendu.

---

## ▶️ À toi de jouer

Le fichier `http_demo.js` tente une vraie requête `fetch`. Selon que le réseau est
disponible ou non, tu verras soit les données reçues, soit un message d'erreur
maîtrisé — mais **dans tous les cas, le script se termine sans planter**.

```bash
node --check js-ts/09_http/http_demo.js   # vérifier la syntaxe
node js-ts/09_http/http_demo.js           # lancer la démo (réseau ou pas)
```

➡️ Suite : le [projet capstone](../projets/) — assembler tout ce que tu as appris.
