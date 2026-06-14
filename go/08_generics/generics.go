/*
 * MODULE AVANCÉ 08 - Les GÉNÉRIQUES : une fonction pour PLUSIEURS types
 * ====================================================================
 * Illustre la notion clé du README : un PARAMÈTRE DE TYPE [T ...] permet
 * d'écrire UNE SEULE fonction qui marche pour des types DIFFÉRENTS (int,
 * string...). Go devine TOUT SEUL le type au moment de l'appel.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer (depuis la racine du dépôt) :
 *     go run go/08_generics/generics.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Appeler Premier() sur une liste d'ENTIERS : T devient int.
 *   2. Appeler la MÊME Premier() sur une liste de TEXTES : T devient string.
 *   3. Appeler Inverser() sur des entiers, puis sur des textes.
 *   4. Constater qu'UNE SEULE fonction a servi pour des types différents.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// FONCTION GÉNÉRIQUE n°1 : renvoie le PREMIER élément d'une liste.
//   [T any] -> on déclare un paramètre de type "T" ; la contrainte "any"
//              signifie "T peut être N'IMPORTE QUEL type".
//   s []T   -> s est une liste DU type T.
//   ... T   -> la fonction renvoie une valeur de ce MÊME type T.
func Premier[T any](s []T) T {
	return s[0] // le tout premier élément (indice 0)
}

// FONCTION GÉNÉRIQUE n°2 : renvoie une NOUVELLE liste, dans l'ordre inverse.
//   Là encore, T peut être n'importe quel type (any).
func Inverser[T any](s []T) []T {
	// On crée une liste vide de même type et même TAILLE que l'entrée.
	resultat := make([]T, len(s))
	for i, v := range s {
		// L'élément qui était au DÉBUT se retrouve à la FIN, et vice-versa.
		resultat[len(s)-1-i] = v
	}
	return resultat
}

func main() {

	// 1. APPEL sur des ENTIERS : Go déduit que T = int.
	nombres := []int{10, 20, 30}
	fmt.Println("Premier des nombres :", Premier(nombres)) // -> 10

	// 2. APPEL sur des TEXTES : la MÊME fonction, mais Go déduit T = string.
	mots := []string{"chat", "chien", "oiseau"}
	fmt.Println("Premier des mots    :", Premier(mots)) // -> chat

	// 3. APPEL d'Inverser() : pareil, ça marche pour les deux types.
	fmt.Println("Nombres inverses    :", Inverser(nombres)) // -> [30 20 10]
	fmt.Println("Mots inverses       :", Inverser(mots))    // -> [oiseau chien chat]

	// 4. Bilan : UNE SEULE écriture de Premier (et d'Inverser) a servi pour
	//    des int ET des string. Voilà toute la force des génériques.
	fmt.Println("Termine : une seule fonction, plusieurs types, grace au parametre [T].")
}
