/*
 * MODULE 04 - La GESTION DES ERREURS en Go
 * =========================================
 * Illustre, dans l'ordre, les notions du README : en Go, PAS d'exceptions.
 * Une fonction qui peut échouer renvoie DEUX choses : un résultat ET une
 * "error". L'appelant TESTE toujours "if err != nil" pour savoir si ça a
 * marché. On crée une erreur avec errors.New ou fmt.Errorf.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/04_erreurs_interfaces/erreurs.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Appeler diviser(10, 2) : un cas qui RÉUSSIT (err vaut nil).
 *   2. Tester "if err != nil" -> ici faux, on affiche le résultat.
 *   3. Appeler diviser(10, 0) : un cas qui ÉCHOUE (division par zéro).
 *   4. Tester "if err != nil" -> ici vrai, on affiche le message d'erreur.
 *   5. Montrer fmt.Errorf, qui glisse une valeur DANS le message d'erreur.
 */

package main

import (
	"errors" // pour fabriquer une erreur simple avec errors.New
	"fmt"    // boîte à outils d'affichage (Println, Printf) + Errorf
)

// diviser prend deux nombres et renvoie DEUX valeurs :
//   - le résultat (un float64)
//   - une "error" : nil si tout va bien, sinon le détail du problème.
// C'est la SIGNATURE typique d'une fonction qui peut échouer en Go.
func diviser(a float64, b float64) (float64, error) {

	// On vérifie le cas interdit : diviser par zéro n'a pas de sens.
	if b == 0 {
		// On RENVOIE un résultat "vide" (0) ET une vraie erreur.
		// errors.New crée une erreur à partir d'un simple texte.
		return 0, errors.New("division par zero impossible")
	}

	// Cas normal : on renvoie le résultat ET nil (= "aucune erreur").
	return a / b, nil
}

// convertirEnAge prend du texte et essaie d'en faire un âge (entier).
// Elle montre fmt.Errorf : comme Printf, mais au lieu d'AFFICHER, il
// FABRIQUE une erreur avec une valeur glissée dedans (ici, le texte fautif).
func convertirEnAge(texte string) (int, error) {
	if texte == "trente" {
		// %q met le texte entre guillemets dans le message : pratique pour
		// montrer EXACTEMENT ce qui posait problème.
		return 0, fmt.Errorf("impossible de convertir %q en nombre", texte)
	}
	// Pour rester simple, on accepte juste une valeur connue.
	return 30, nil
}

func main() {

	// 1. CAS QUI RÉUSSIT : on récupère LES DEUX valeurs renvoyées.
	resultat, err := diviser(10, 2)

	// 2. ON TESTE TOUJOURS l'erreur AVANT d'utiliser le résultat.
	if err != nil {
		// Cette branche ne s'exécute PAS ici (err vaut nil).
		fmt.Println("Erreur :", err)
	} else {
		fmt.Printf("10 / 2 = %.1f\n", resultat)
	}

	// 3. CAS QUI ÉCHOUE : division par zéro.
	resultat, err = diviser(10, 0)

	// 4. Cette fois "if err != nil" est VRAI : on affiche le problème
	//    et on n'utilise PAS le résultat (qui ne veut rien dire).
	if err != nil {
		fmt.Println("Erreur :", err)
	} else {
		fmt.Printf("10 / 0 = %.1f\n", resultat)
	}

	// 5. DÉMO de fmt.Errorf : un message d'erreur qui contient une valeur.
	age, err := convertirEnAge("trente")
	if err != nil {
		fmt.Println("Erreur :", err)
	} else {
		fmt.Println("Age converti :", age)
	}
}
