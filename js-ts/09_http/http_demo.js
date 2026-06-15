// MODULE 09 - http_demo.js : une requête HTTP avec le fetch natif de Node 22
// =========================================================================
// Ce script tente d'aller chercher des données sur internet. L'accès réseau
// peut être BLOQUÉ : dans ce cas, on attrape l'erreur et on se termine
// proprement, SANS planter. Lance :
//   node js-ts/09_http/http_demo.js
//
//  🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
//     1. On prépare l'adresse (URL) à interroger.
//     2. Dans un try : on lance fetch (await), on vérifie le statut, on lit le JSON.
//     3. Dans un catch : si le réseau échoue, on affiche un message clair.
//     4. Quoi qu'il arrive, le script se termine normalement.

// On enveloppe tout dans une fonction async pour pouvoir utiliser "await".
async function recupererDonnees() {
  // 1. L'adresse à interroger. (Une API publique de test renvoyant du JSON.)
  const url = "https://jsonplaceholder.typicode.com/todos/1";
  console.log("Tentative de requête vers :", url);

  // 2. & 3. On ESSAIE la requête, et on PRÉVOIT l'échec réseau.
  try {
    // Premier await : on attend la RÉPONSE du serveur.
    const reponse = await fetch(url);

    // reponse.ok vaut true si le statut est un succès (200-299).
    if (!reponse.ok) {
      // Le serveur a répondu, mais avec une erreur (ex : 404, 500).
      console.error(`Le serveur a répondu avec le statut ${reponse.status}.`);
      return; // on s'arrête proprement, sans planter
    }

    // Second await : on attend la LECTURE du corps, transformé en objet JS.
    const data = await reponse.json();
    console.log("✅ Données reçues :");
    console.log(data);
  } catch (erreur) {
    // 3. On arrive ici si le réseau est COUPÉ ou BLOQUÉ, ou le serveur injoignable.
    //    On ne plante pas : on explique calmement ce qui s'est passé.
    console.error("⚠️  Impossible de joindre le serveur (réseau indisponible ?).");
    console.error("   Détail :", erreur.message);
    console.error("   Ce n'est pas grave : le script gère l'erreur et continue.");
  }
}

// 4. On lance la fonction. La promesse se termine seule, le script s'arrête ensuite.
recupererDonnees().then(() => {
  console.log("\n✅ Fin du script (avec ou sans réseau, sans plantage).");
});
