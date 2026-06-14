/*
 * MODULE 02 - Les MAPS (dictionnaires clé -> valeur) en Go
 * ========================================================
 * Illustre, dans l'ordre, les notions du README : créer une map,
 * ajouter et lire une valeur, tester l'existence d'une clé avec
 * "valeur, ok := m[clé]", et parcourir avec for...range.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/02_collections/maps.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer une map "annuaire" : nom (string) -> age (int).
 *   2. Ajouter de nouvelles entrées avec annuaire["clé"] = valeur.
 *   3. Lire une valeur connue par sa clé.
 *   4. Tester une clé qui EXISTE puis une qui N'EXISTE PAS (forme "valeur, ok").
 *   5. Parcourir toute la map avec for...range (clé puis valeur).
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

func main() {

	// 1. CRÉER UNE MAP
	//    map[string]int = "clés string, valeurs int". On la remplit avec { }.
	ages := map[string]int{
		"Sam": 30,
		"Lou": 25,
	}
	fmt.Println("Annuaire de depart :", ages)

	// 2. AJOUTER (ou modifier) une entrée : on range une valeur sous une clé.
	ages["Max"] = 40 // nouvelle clé "Max"
	ages["Lou"] = 26 // la clé "Lou" existe déjà -> sa valeur est MODIFIÉE
	fmt.Println("Apres ajout/maj    :", ages)

	// 3. LIRE une valeur par sa clé.
	fmt.Println("Age de Sam :", ages["Sam"])

	// 4. TESTER L'EXISTENCE d'une clé avec la forme "valeur, ok".
	//    ok vaut true si la clé existe, false sinon.
	age, ok := ages["Max"]
	if ok {
		fmt.Println("Max est dans l'annuaire, il a", age, "ans")
	} else {
		fmt.Println("Max n'est pas dans l'annuaire")
	}

	//    Même test, mais sur une clé qui N'EXISTE PAS.
	age2, ok2 := ages["Inconnu"]
	if ok2 {
		fmt.Println("Trouve :", age2)
	} else {
		fmt.Println("La cle \"Inconnu\" n'existe pas (valeur par defaut :", age2, ")")
	}

	// 5. PARCOURIR avec for...range : range donne la clé puis la valeur.
	//    ⚠️ L'ordre d'affichage n'est PAS garanti, c'est normal pour une map.
	fmt.Println("--- Tout l'annuaire ---")
	for nom, age := range ages {
		fmt.Printf("%s a %d ans\n", nom, age)
	}
}
