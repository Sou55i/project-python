/*
 * MODULE 04 - Les INTERFACES (un "contrat") en Go
 * ===============================================
 * Illustre, dans l'ordre, les notions du README : une interface est une
 * LISTE DE MÉTHODES à posséder (un "contrat"). Tout type qui possède ces
 * méthodes satisfait l'interface AUTOMATIQUEMENT (rien à déclarer). On peut
 * alors traiter des types DIFFÉRENTS de la même façon, via l'interface.
 *
 * ⚠️ Ce fichier a SON PROPRE func main : on le lance SEUL.
 * Lancer :
 *     go run go/04_erreurs_interfaces/interfaces.go
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (ce que main fait, dans l'ordre)
 *   1. Créer un Rectangle et un Cercle (deux types DIFFÉRENTS).
 *   2. Les ranger dans une SEULE liste de type Forme (le contrat commun).
 *   3. Parcourir la liste avec range, sans savoir QUI est quoi.
 *   4. Pour chaque forme, appeler Aire() : chaque type répond À SA FAÇON.
 *   5. Constater qu'on a traité des types différents avec le MÊME code.
 */

package main

import "fmt" // boîte à outils d'affichage (Println, Printf)

// LE CONTRAT : toute "Forme" doit savoir calculer son Aire() (un float64).
// On ne dit PAS comment : juste QUE la méthode doit exister.
type Forme interface {
	Aire() float64
}

// PREMIER TYPE : un Rectangle, avec ses deux champs.
type Rectangle struct {
	Largeur float64
	Hauteur float64
}

// Rectangle possède la méthode Aire() -> il satisfait Forme AUTOMATIQUEMENT.
// (On n'écrit nulle part "Rectangle implements Forme" : Go le déduit seul.)
func (r Rectangle) Aire() float64 {
	return r.Largeur * r.Hauteur
}

// DEUXIÈME TYPE : un Cercle, avec son rayon.
type Cercle struct {
	Rayon float64
}

// Cercle possède AUSSI une méthode Aire() -> il satisfait Forme lui aussi.
// La formule est différente, mais le CONTRAT (le nom + le type) est respecté.
func (c Cercle) Aire() float64 {
	return 3.14159 * c.Rayon * c.Rayon
}

func main() {

	// 1. CRÉER deux objets de types DIFFÉRENTS.
	rect := Rectangle{Largeur: 4, Hauteur: 3}
	cercle := Cercle{Rayon: 2}

	// 2. Les RANGER dans une seule liste de Forme : c'est permis car
	//    chacun respecte le contrat (chacun a une méthode Aire()).
	formes := []Forme{rect, cercle}

	// 3. PARCOURIR la liste : on ne se soucie PAS de qui est rectangle ou
	//    cercle. On les voit tous comme des "Forme".
	for i, f := range formes {
		// 4. Appeler Aire() via l'interface : Go choisit TOUT SEUL la bonne
		//    version (celle du Rectangle ou celle du Cercle).
		fmt.Printf("Forme %d -> aire = %.2f\n", i+1, f.Aire())
	}

	// 5. Bilan : un MÊME code (la boucle) a traité deux types différents,
	//    grâce au contrat partagé. C'est toute la force des interfaces.
	fmt.Println("Termine : meme code pour des types differents, grace au contrat Forme.")
}
