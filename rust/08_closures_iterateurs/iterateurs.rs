/*
 * MODULE 08 - Closures et itérateurs
 * ==================================
 * Une CLOSURE est une mini-fonction sans nom qu'on écrit "sur place" : |x| x + 1.
 * Un ITÉRATEUR parcourt une collection ; on lui enchaîne des opérations
 * (map, filter...) puis on RÉCOLTE le résultat (collect, sum...).
 * Ensemble, ils permettent de transformer des listes en quelques lignes lisibles.
 *
 * Compiler puis lancer :
 *     rustc --edition 2021 rust/08_closures_iterateurs/iterateurs.rs -o /tmp/r && /tmp/r
 */

fn main() {
    println!("=== 1. Une closure, c'est une fonction-eclair ===");
    // |x| x * 2  se lit : "prends x, renvoie x * 2". Les |...| remplacent les () des params.
    let doubler = |x: i32| x * 2;
    println!("doubler(5) = {}", doubler(5));

    // Une closure peut CAPTURER une variable de l'extérieur (ici 'tva').
    let tva = 20;
    let avec_tva = |prix: i32| prix + prix * tva / 100;
    println!("avec_tva(100) = {}", avec_tva(100));

    println!();
    println!("=== 2. map : transformer chaque element ===");
    let nombres = vec![1, 2, 3, 4, 5];
    // .iter()      : on commence à parcourir la liste
    // .map(|n| ...) : pour CHAQUE élément n, on calcule une nouvelle valeur
    // .collect()   : on RANGE les résultats dans une nouvelle liste (Vec)
    let carres: Vec<i32> = nombres.iter().map(|n| n * n).collect();
    println!("nombres = {:?}", nombres);
    println!("carres  = {:?}", carres);

    println!();
    println!("=== 3. filter : ne garder que certains elements ===");
    // .filter(|n| ...) garde l'élément seulement si la closure renvoie 'true'.
    // n % 2 == 0  => le nombre est pair.
    let pairs: Vec<i32> = nombres.iter().filter(|n| *n % 2 == 0).cloned().collect();
    println!("pairs (de nombres) = {:?}", pairs);

    println!();
    println!("=== 4. sum : tout additionner ===");
    // .sum() additionne tous les éléments parcourus. Ici la somme totale.
    let total: i32 = nombres.iter().sum();
    println!("somme de nombres = {}", total);

    println!();
    println!("=== 5. Tout enchainer (la vraie force) ===");
    // On peut CHAÎNER : prendre les nombres, ne garder que les pairs, les doubler,
    // puis tout additionner — le tout en une seule expression lisible.
    let resultat: i32 = nombres
        .iter()                     // parcourir
        .filter(|n| *n % 2 == 0)    // garder les pairs : 2 et 4
        .map(|n| n * 10)            // les multiplier par 10 : 20 et 40
        .sum();                     // additionner : 60
    println!("pairs * 10 puis somme = {}", resultat);
}
