// ===========================================================
//  MODULE 04 - L'asynchrone : callbacks -> Promesses -> async/await
//  ==========================================================
//  On illustre les 3 façons de gérer une tâche "qui prend du temps".
//  Pour simuler une attente, on utilise setTimeout (un "minuteur").
//
//  Lance-le :  node js-ts/04_async/async_demo.js
//  (Le script attend de courts délais puis se termine TOUT SEUL.)
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. Un exemple avec un CALLBACK (l'ancienne façon).
//     2. Une PROMESSE manipulée avec .then() / .catch().
//     3. La même idée en async / await (la façon moderne), étape par étape.
//     4. Le tout est orchestré pour s'exécuter dans l'ordre et se terminer.

// ─────────────────────────────────────────────
// OUTIL : une "tâche longue" simulée
// ─────────────────────────────────────────────
// attendre(ms) renvoie une PROMESSE qui se résout après "ms" millisecondes.
// "resolve" est la fonction à appeler quand la promesse est tenue (réussie).
function attendre(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms); // après ms, on appelle resolve -> la promesse réussit
  });
}

// ─────────────────────────────────────────────
// 1. CALLBACK : on passe une fonction appelée "quand c'est prêt"
// ─────────────────────────────────────────────
function exempleCallback(quandFini) {
  console.log("[1] Callback : je lance une tâche...");
  setTimeout(() => {
    console.log("[1] Callback : tâche terminée !");
    quandFini(); // on PRÉVIENT l'appelant que c'est fini
  }, 50); // 50 ms d'attente simulée
}

// ─────────────────────────────────────────────
// 2. PROMESSE avec .then() / .catch()
// ─────────────────────────────────────────────
function exemplePromesse() {
  console.log("[2] Promesse : je lance une tâche...");
  // On RENVOIE une promesse pour que l'appelant puisse l'attendre.
  return attendre(50).then(() => {
    console.log("[2] Promesse : résolue (.then) !");
    return "valeur-de-la-promesse"; // ce que la promesse "fournit" au final
  });
}

// ─────────────────────────────────────────────
// 3. ASYNC / AWAIT : on écrit comme du code "normal", ligne par ligne
// ─────────────────────────────────────────────
// Le mot-clé "async" autorise l'usage de "await" dans cette fonction.
async function exempleAsyncAwait() {
  console.log("[3] async/await : étape A");
  await attendre(50); // PAUSE ici jusqu'à la fin du délai (sans bloquer Node)
  console.log("[3] async/await : étape B (après l'attente)");

  // try/catch : on "essaie" et on "attrape" une éventuelle erreur.
  try {
    await attendre(50);
    console.log("[3] async/await : étape C terminée sans erreur");
  } catch (erreur) {
    console.log("[3] async/await : une erreur est survenue :", erreur);
  }
}

// ─────────────────────────────────────────────
// 4. ORCHESTRATION : tout exécuter DANS L'ORDRE, puis terminer
// ─────────────────────────────────────────────
// On enveloppe le tout dans une fonction async pour pouvoir "await" chaque étape.
async function main() {
  // On transforme l'exemple à callback en promesse pour pouvoir l'attendre.
  await new Promise((resolve) => exempleCallback(resolve));

  // .then renvoie une promesse : on l'attend aussi avec await.
  const valeur = await exemplePromesse();
  console.log(`[2] Promesse : valeur reçue = ${valeur}`);

  // Enfin, l'exemple async/await.
  await exempleAsyncAwait();

  console.log("✅ Terminé : le script se ferme proprement.");
}

// On lance main(). Le .catch attrape toute erreur imprévue (bonne habitude).
main().catch((erreur) => console.log("Erreur inattendue :", erreur));
