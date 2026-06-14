/*
 * MODULE 04 - Le polymorphisme : un même ordre, des réponses différentes
 * ======================================================================
 * On demande à plusieurs animaux de "parler" via un pointeur de type mère
 * (Animal*). Grâce à 'virtual', chacun répond à SA façon.
 *
 * Compiler puis lancer :
 *     g++ -Wall cpp/04_heritage_polymorphisme/polymorphisme.cpp -o polymorphisme
 *     ./polymorphisme
 *
 * 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
 *    1. INCLUDE   : iostream, string, vector.
 *    2. CLASSES   : Animal (mère, parler() virtual) + Chien et Chat (filles,
 *                   parler() override).
 *    3. main      : (a) ranger des Animal* (Chien, Chat) dans un vector,
 *                   (b) tous les faire parler dans une boucle (chacun à sa façon),
 *                   (c) libérer la mémoire avec delete.
 */

#include <iostream>
#include <string>
#include <vector>

// Classe MÈRE : parler() est 'virtual' = les filles pourront la redéfinir.
class Animal {
public:
    // Destructeur virtual : nettoyage correct quand on delete via un Animal*.
    virtual ~Animal() {}

    virtual void parler() {
        std::cout << "..." << std::endl;
    }
};

// Chaque fille REDÉFINIT parler() avec 'override'.
class Chien : public Animal {
public:
    void parler() override {
        std::cout << "Wouf !" << std::endl;
    }
};

class Chat : public Animal {
public:
    void parler() override {
        std::cout << "Miaou !" << std::endl;
    }
};

int main() {
    // (a) Un vector de POINTEURS vers Animal : il peut contenir des Chien, des Chat...
    std::vector<Animal*> animaux;
    animaux.push_back(new Chien());   // 'new' crée l'objet et renvoie son adresse
    animaux.push_back(new Chat());
    animaux.push_back(new Chien());

    // (b) On les fait tous parler SANS savoir lequel est lequel.
    //     Grâce à virtual, chacun exécute SA version de parler().
    for (Animal* a : animaux) {
        a->parler();   // flèche -> car 'a' est un pointeur
    }

    // (c) On libère chaque objet créé avec 'new'.
    for (Animal* a : animaux) {
        delete a;      // le destructeur virtual fait le bon ménage
    }

    return 0;
}
