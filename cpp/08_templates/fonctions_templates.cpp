// ============================================================================
//  Module 08 (avancé) — Les TEMPLATES : une FONCTION générique
// ----------------------------------------------------------------------------
//  Objectif : écrire UNE SEULE fois la fonction "maximum", et qu'elle marche
//  pour PLUSIEURS types (int, double, std::string) sans rien réécrire.
//  Analogie : un MOULE à gâteau qui produit un gâteau quelle que soit la pâte.
// ============================================================================

#include <iostream>   // pour std::cout (afficher)
#include <string>     // pour std::string (le texte)

// ----------------------------------------------------------------------------
//  LA FONCTION TEMPLATE (le "moule")
// ----------------------------------------------------------------------------
// template<typename T>  : on annonce un MOULE. T est "un type au choix",
//                         encore inconnu. Le compilateur le devinera à l'appel.
template<typename T>
T maximum(T a, T b) {     // a et b sont de type T, et on renvoie un T
    if (a > b) {          // l'opérateur > compare les deux valeurs…
        return a;         // … a est le plus grand : on le renvoie
    }
    return b;             // … sinon c'est b (ou ils sont égaux)
}
// Note : ici "le plus grand" dépend du type. Pour des nombres, c'est la
// valeur la plus grande ; pour du texte, c'est l'ordre ALPHABÉTIQUE.

int main() {
    // -- Appel n°1 : avec des entiers --------------------------------------
    // Le compilateur voit deux int -> il fabrique tout seul la version int.
    int a = 3, b = 9;
    std::cout << "maximum(3, 9)          = " << maximum(a, b) << std::endl;   // 9

    // -- Appel n°2 : avec des nombres à virgule ----------------------------
    // Mêmes lignes de code, mais cette fois T = double. Aucune réécriture !
    double x = 2.5, y = 1.5;
    std::cout << "maximum(2.5, 1.5)      = " << maximum(x, y) << std::endl;   // 2.5

    // -- Appel n°3 : avec du texte -----------------------------------------
    // T = std::string. Le > compare dans l'ordre alphabétique :
    // "banane" vient après "abricot", donc "banane" est "le plus grand".
    std::string mot1 = "abricot";
    std::string mot2 = "banane";
    std::cout << "maximum(abricot, banane) = " << maximum(mot1, mot2) << std::endl; // banane

    // -- Bonus : on peut aussi écrire le type explicitement entre < > -------
    // Utile quand le compilateur ne peut pas deviner (ici, ce n'est pas
    // obligatoire, mais c'est une façon de "forcer" la version voulue).
    std::cout << "maximum<int>(7, 4)     = " << maximum<int>(7, 4) << std::endl;    // 7

    return 0;   // tout s'est bien passé
}
