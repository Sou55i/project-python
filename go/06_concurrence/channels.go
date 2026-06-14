/*
 * MODULE 06 - CHANNELS (les "tuyaux" entre goroutines)
 * ====================================================
 * Un CHANNEL (`chan`) est un TUYAU qui transporte des valeurs d'une goroutine
 * à une autre. Il sert À LA FOIS à communiquer ET à synchroniser : sur un
 * channel simple, un envoi `ch <- v` attend un receveur, et une réception
 * `v := <-ch` attend un envoyeur. Les deux se donnent rendez-vous au tuyau.
 *
 * Ici : une goroutine ENVOIE des nombres dans le tuyau, puis le FERME ; main
 * les REÇOIT un par un avec `for ... range` (qui s'arrête seul à la fermeture)
 * et calcule leur somme. Sortie déterministe : toujours le même résultat.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer DEPUIS LA RACINE du dépôt :
 *     go run go/06_concurrence/channels.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer un channel d'entiers avec make(chan int).
 *   2. Lancer une goroutine qui ENVOIE 1, 2, 3 dans le tuyau, puis le FERME.
 *   3. main REÇOIT les valeurs une par une avec `for v := range ch`.
 *   4. À chaque réception : afficher la valeur et l'ajouter à la somme.
 *   5. Quand le tuyau est fermé, la boucle s'arrête : afficher la somme finale.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

func main() {

	// 1. CRÉER le tuyau : un channel qui transporte des entiers (int).
	ch := make(chan int)

	// 2. LANCER une goroutine "à côté" : c'est elle qui REMPLIT le tuyau.
	go func() {
		// On envoie trois valeurs, l'une après l'autre.
		// `ch <- n` : la flèche pointe VERS ch -> on ENVOIE n dans le tuyau.
		// Chaque envoi attend que main soit prêt à recevoir (rendez-vous).
		for n := 1; n <= 3; n++ {
			ch <- n
		}

		// FERMER le tuyau : "je n'enverrai plus rien". Indispensable pour que
		// le `for ... range` côté main sache qu'il peut s'arrêter.
		close(ch)
	}()

	// La somme qu'on construit au fil des réceptions.
	somme := 0

	// 3 + 4. RECEVOIR : `for v := range ch` sort une valeur du tuyau à chaque
	// tour, et s'arrête TOUT SEUL quand le tuyau est fermé.
	// (`range` sur un channel = "tant qu'il arrive des valeurs".)
	for v := range ch {
		fmt.Printf("Reçu du tuyau : %d\n", v)
		somme += v
	}

	// 5. Le tuyau est fermé, la boucle est finie : on affiche le bilan.
	// 1 + 2 + 3 = 6  (toujours).
	fmt.Printf("Tuyau fermé. Somme des valeurs reçues = %d\n", somme)
}
