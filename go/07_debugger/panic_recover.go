/*
 * MODULE 07 - PANIC & RECOVER (déclencher un bug grave, puis le rattraper)
 * =======================================================================
 * En Go, un PANIC est une erreur GRAVE qui ARRÊTE le programme et affiche
 * une "stack trace" (la pile d'appels). Mais on peut le RATTRAPER avec la
 * fonction recover(), à condition de l'appeler dans un defer (du code exécuté
 * juste avant de sortir d'une fonction, MÊME en cas de panic).
 *
 * Ici : la fonction diviser() PANIQUE volontairement (division par zéro), mais
 * un defer + recover() RATTRAPE la panique. Résultat : le programme NE PLANTE
 * PAS, il affiche un message clair et se termine NORMALEMENT.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/07_debugger/panic_recover.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce qui se passe, dans l'ordre)
 *   1. main affiche "Début du programme".
 *   2. main appelle diviser(10, 0) (diviser par 0 -> ça va paniquer).
 *   3. Dans diviser, on installe d'ABORD un defer avec recover() (le filet).
 *   4. La division par zéro déclenche un PANIC : diviser s'interrompt.
 *   5. Le defer s'exécute quand même : recover() RATTRAPE la panique.
 *   6. diviser revient calmement vers main (au lieu de tout faire planter).
 *   7. main affiche "Fin du programme" : preuve qu'on a survécu au panic.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// diviser fait a / b, mais b vaut 0 ici : ça va PANIQUER.
// Grâce au defer + recover() installé au début, le panic est RATTRAPÉ
// et la fonction revient proprement au lieu de planter le programme.
func diviser(a, b int) {

	// 3. ON INSTALLE LE FILET EN PREMIER.
	// defer = "exécute cette fonction juste avant de sortir de diviser",
	// et ce, MÊME si diviser panique entre-temps. C'est ce qui rend le
	// rattrapage possible.
	defer func() {
		// recover() ne fonctionne QUE dans un defer. Il ARRÊTE la panique
		// en cours et renvoie sa valeur (ou nil s'il n'y a pas eu de panic).
		if r := recover(); r != nil {
			// 5. On est arrivé ici : il Y A EU un panic, on l'a rattrapé.
			fmt.Println("⚠️  Panic rattrapé proprement :", r)
			fmt.Println("    -> on ne plante pas, on reprend la main.")
		}
	}()

	// 4. ICI ça PANIQUE : diviser par zéro est une erreur grave en Go.
	// Le code APRÈS cette ligne ne s'exécutera PAS ; on saute directement
	// au defer ci-dessus.
	resultat := a / b

	// (Jamais atteint : la ligne du dessus a déjà déclenché le panic.)
	fmt.Println("Résultat :", resultat)
}

func main() {

	// 1. Le programme démarre normalement.
	fmt.Println("Début du programme.")

	// 2. On appelle diviser avec b = 0 : ça VA paniquer...
	// ...mais diviser rattrape sa propre panique en interne, donc l'appel
	// nous rend la main sans tout faire exploser.
	diviser(10, 0)

	// 7. On arrive bien ICI : la preuve que le recover a fonctionné.
	// Si la panique n'avait PAS été rattrapée, ce message ne s'afficherait
	// jamais (le programme aurait planté avant).
	fmt.Println("Fin du programme : on a survécu au panic ! 🎉")
}
