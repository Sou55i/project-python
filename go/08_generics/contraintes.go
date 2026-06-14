/*
 * MODULE AVANCÉ 08 - Les CONTRAINTES : limiter les types acceptés
 * ==============================================================
 * "any" accepte TOUT type. Mais pour ADDITIONNER, on ne veut QUE des nombres
 * (on n'additionne pas des true/false ni des textes !). Une CONTRAINTE
 * personnalisée, écrite comme une interface qui liste des types avec "|",
 * dit au compilateur : "voici les SEULS types autorisés dans T".
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer (depuis la racine du dépôt) :
 *     go run go/08_generics/contraintes.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Additionner une liste d'ENTIERS avec Somme() : T devient int.
 *   2. Additionner une liste de FLOTTANTS avec la MÊME Somme() : T = float64.
 *   3. Additionner des Celsius (un type BASÉ sur float64), accepté grâce au "~".
 *   4. Constater qu'une seule Somme() couvre tous ces types numériques.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// LA CONTRAINTE PERSONNALISÉE : "est un Nombre" tout type qui est
// un int, un int64 OU un float64. Le "~" veut dire "ce type OU tout type
// construit à partir de lui" (ex : type Celsius float64 -> accepté par ~float64).
type Nombre interface {
	~int | ~int64 | ~float64
}

// FONCTION GÉNÉRIQUE contrainte : additionne tous les éléments d'une liste.
//   [T Nombre] -> T n'est PLUS "any" : il est limité aux types Nombre.
//                 C'est cette garantie qui autorise le "+" plus bas.
func Somme[T Nombre](s []T) T {
	var total T // démarre à la "valeur zéro" du type T (0 pour int, 0.0 pour float64)
	for _, v := range s {
		total += v // autorisé : la contrainte Nombre garantit que "+" existe
	}
	return total
}

// Un type PERSONNEL basé sur float64, pour montrer l'utilité du "~".
type Celsius float64

func main() {

	// 1. SOMME d'ENTIERS : Go déduit T = int.
	entiers := []int{1, 2, 3, 4}
	fmt.Println("Somme des entiers   :", Somme(entiers)) // -> 10

	// 2. SOMME de FLOTTANTS : la MÊME fonction, mais T = float64.
	flottants := []float64{1.5, 2.5, 3.0}
	fmt.Println("Somme des flottants :", Somme(flottants)) // -> 7

	// 3. SOMME de Celsius : Celsius est "basé sur float64", donc accepté
	//    grâce au "~float64" de la contrainte. Sans le "~", ce serait refusé.
	temperatures := []Celsius{18.0, 20.5, 22.5}
	fmt.Println("Somme des Celsius   :", Somme(temperatures)) // -> 61

	// (À ESSAYER : décommente la ligne suivante. Le programme REFUSERA de
	//  compiler, car string n'est PAS un Nombre — la contrainte te protège.)
	// fmt.Println(Somme([]string{"a", "b"}))

	// 4. Bilan : une seule Somme() additionne int, float64 ET nos Celsius,
	//    tout en INTERDISANT les types qui n'ont pas de sens. C'est la contrainte.
	fmt.Println("Termine : une seule Somme pour tous les nombres, grace a la contrainte.")
}
