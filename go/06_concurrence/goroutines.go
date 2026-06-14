/*
 * MODULE 06 - GOROUTINES + sync.WaitGroup
 * =======================================
 * Une GOROUTINE = une tâche lancée "à côté" du programme principal avec le
 * mot-clé `go`. Le PIÈGE : main peut finir AVANT que les goroutines aient fini
 * -> le programme s'arrête trop tôt. La SOLUTION montrée ici : sync.WaitGroup,
 * un compteur de tâches qui fait ATTENDRE main jusqu'à ce que tout soit fini.
 *
 * Pour rester PÉDAGOGIQUE, la sortie est DÉTERMINISTE : chaque tâche ajoute un
 * nombre à un total protégé, et on n'affiche que le TOTAL final (qui ne dépend
 * pas de l'ordre dans lequel les goroutines se terminent). Résultat toujours
 * identique, même en relançant plusieurs fois.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/06_concurrence/goroutines.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer un WaitGroup (le compteur de tâches à attendre).
 *   2. Pour chaque tâche : Add(1), puis lancer la goroutine avec `go`.
 *   3. Chaque goroutine fait son travail, protège le total, puis Done().
 *   4. main appelle Wait() : il attend que TOUTES les goroutines aient fini.
 *   5. Afficher le total final (toujours le même).
 */

package main

import (
	"fmt"  // boîte à outils d'affichage (Println, Printf)
	"sync" // boîte à outils de synchronisation : WaitGroup, Mutex...
)

func main() {

	// 1. Le WaitGroup : un compteur de "tâches en cours", à zéro au départ.
	var wg sync.WaitGroup

	// Un Mutex (= "verrou") : comme PLUSIEURS goroutines vont toucher la même
	// variable `total`, on les empêche d'écrire EN MÊME TEMPS (sinon bug).
	// Une seule goroutine à la fois entre entre Lock() et Unlock().
	var verrou sync.Mutex

	// La variable partagée que les goroutines vont faire grandir ensemble.
	total := 0

	// On va lancer 5 tâches : la tâche n°i ajoutera i au total.
	// 1 + 2 + 3 + 4 + 5 = 15  (toujours, peu importe l'ordre d'exécution).
	nombreDeTaches := 5

	// 2. Lancer les goroutines.
	for i := 1; i <= nombreDeTaches; i++ {

		// "+1 tâche à attendre" : À FAIRE AVANT de lancer la goroutine.
		wg.Add(1)

		// `go func(...) {...}(i)` lance une fonction "à côté".
		// On passe i en paramètre (n) pour figer sa valeur pour cette tâche.
		go func(n int) {

			// defer = "fais-le juste avant de sortir de cette fonction".
			// Done() enlève 1 au compteur du WaitGroup : "moi, j'ai fini".
			defer wg.Done()

			// On verrouille AVANT de toucher total, on déverrouille APRÈS.
			verrou.Lock()
			total += n // la seule ligne "sensible" : on la protège.
			verrou.Unlock()

		}(i) // <- on appelle la fonction TOUT DE SUITE en lui donnant i.
	}

	// 4. main ATTEND ici, sans rien faire, que le compteur revienne à zéro
	//    (c'est-à-dire que les 5 goroutines aient toutes appelé Done()).
	wg.Wait()

	// 5. Une fois TOUT fini, on affiche le total. Sortie déterministe.
	fmt.Printf("%d tâches terminées. Total = %d\n", nombreDeTaches, total)
	fmt.Println("Toutes les goroutines sont finies : main peut s'arrêter tranquillement.")
}
