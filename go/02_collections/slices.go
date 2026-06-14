/*
 * MODULE 02 - Les SLICES (listes dynamiques) en Go
 * ================================================
 * Illustre, dans l'ordre, les notions du README : créer un slice,
 * ajouter avec append, parcourir avec for...range, calculer une somme
 * et une moyenne.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/02_collections/slices.go
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

func main() {

	// 1. CRÉER UN SLICE
	//    []int = "slice d'entiers". On le remplit directement avec { }.
	notes := []int{12, 8, 15} // un slice de 3 entiers
	fmt.Println("Notes de depart :", notes)
	fmt.Println("Nombre de notes :", len(notes)) // len = la taille du slice

	// 2. AJOUTER avec append
	//    append RENVOIE le slice agrandi : on RANGE le résultat dans 'notes'.
	notes = append(notes, 20) // ajoute 20 à la fin
	notes = append(notes, 5)  // ajoute 5 à la fin
	fmt.Println("Apres ajout   :", notes)
	fmt.Println("Nouvelle taille :", len(notes))

	// 3. ACCÉDER À UN ÉLÉMENT par sa position (on compte à partir de 0).
	fmt.Println("Premiere note :", notes[0])         // le 1er élément
	fmt.Println("Derniere note :", notes[len(notes)-1]) // le dernier

	// 4. PARCOURIR avec for...range
	//    range donne deux choses : i = la position, note = la valeur.
	fmt.Println("--- Toutes les notes ---")
	for i, note := range notes {
		fmt.Printf("Note numero %d : %d\n", i, note)
	}

	// 5. SOMME et MOYENNE
	//    On part de 0 et on additionne chaque note au fil du parcours.
	//    Ici la position ne nous sert pas : on l'ignore avec "_".
	somme := 0
	for _, note := range notes {
		somme = somme + note // on ajoute la note au total
	}
	fmt.Printf("Somme des notes : %d\n", somme)

	//    Moyenne = somme / nombre. On convertit en float64 pour avoir des décimales.
	moyenne := float64(somme) / float64(len(notes))
	fmt.Printf("Moyenne         : %.2f\n", moyenne) // %.2f = 2 chiffres après la virgule
}
