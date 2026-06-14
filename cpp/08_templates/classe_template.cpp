// ============================================================================
//  Module 08 (avancé) — Les TEMPLATES : une CLASSE générique
// ----------------------------------------------------------------------------
//  Objectif : une petite classe Boite<T> qui RANGE une valeur de N'IMPORTE
//  quel type (un int, un double, du texte…). Un seul "moule" de classe, qui
//  s'adapte au type qu'on lui demande entre les < >.
//
//  🗺️ CHEMINEMENT DU PROGRAMME (ce qui se passe, dans l'ordre)
//  1. On définit la classe template Boite<T> (le moule, type T au choix).
//  2. main() crée b1 : une Boite<int> qui range l'entier 42.
//  3. On lit puis on modifie son contenu, et on l'affiche.
//  4. main() crée b2 : une Boite<std::string> qui range du texte.
//  5. On lit son contenu et on l'affiche.
//  6. On souligne : std::vector, std::map… sont AUSSI des classes templates.
//  7. return 0 : fin du programme.
// ============================================================================

#include <iostream>   // pour std::cout (afficher)
#include <string>     // pour std::string (le texte)

// ----------------------------------------------------------------------------
//  LA CLASSE TEMPLATE (le "moule" de classe)
// ----------------------------------------------------------------------------
// template<typename T> : toute la classe dépend d'un type T au choix.
template<typename T>
class Boite {
private:
    T contenu;                 // l'ATTRIBUT est de type T (int, double, string…)

public:
    // CONSTRUCTEUR : reçoit une valeur de type T et la range dans l'attribut.
    Boite(T valeur) {
        contenu = valeur;
    }

    // Méthode pour LIRE ce qu'il y a dans la boîte (renvoie un T).
    T lire() {
        return contenu;
    }

    // Méthode pour REMPLACER le contenu par une nouvelle valeur de type T.
    void remplacer(T nouvelle) {
        contenu = nouvelle;
    }
};

int main() {
    // -- Une boîte qui range un ENTIER -------------------------------------
    // Entre les < >, on précise le type voulu : ici int. Le compilateur
    // "coule" la version int du moule Boite.
    Boite<int> b1(42);
    std::cout << "b1 contient : " << b1.lire() << std::endl;   // 42

    b1.remplacer(100);                                         // on change le contenu
    std::cout << "b1 contient maintenant : " << b1.lire() << std::endl; // 100

    // -- Une boîte qui range du TEXTE --------------------------------------
    // Même classe, mais cette fois T = std::string. Aucune réécriture !
    Boite<std::string> b2("coucou");
    std::cout << "b2 contient : " << b2.lire() << std::endl;   // coucou

    // -- Le clin d'oeil à la STL (module 06) -------------------------------
    // std::vector<int>, std::map<std::string,int>… sont des CLASSES TEMPLATES.
    // Les < > que tu y mets, c'est EXACTEMENT le T que tu viens de voir.
    std::cout << "(std::vector<int>, std::map<...> sont aussi des classes templates !)"
              << std::endl;

    return 0;   // tout s'est bien passé
}
