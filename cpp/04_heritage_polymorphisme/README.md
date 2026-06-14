# Module 04 — Héritage & polymorphisme : réutiliser et spécialiser

Au module 03, tu as appris à ranger données et actions dans une **classe**. Mais quand
plusieurs classes se ressemblent beaucoup (un `Chien` et un `Chat` ont tous les deux un
nom, mangent, dorment…), réécrire le même code dans chacune serait fastidieux et
risqué. Le C++ propose deux outils puissants pour éviter ça : l'**héritage** (réutiliser)
et le **polymorphisme** (spécialiser).

> Fichiers du module : `heritage.cpp` (une classe mère `Animal` et une classe fille
> `Chien`) et `polymorphisme.cpp` (plusieurs animaux qui « parlent » chacun à leur façon).
> Pour chacun : on **compile** puis on **lance** (voir en bas).

---

## 1. C'est quoi l'HÉRITAGE ?

L'**héritage**, c'est créer une nouvelle classe à partir d'une classe existante : la
nouvelle (**la fille**) **récupère automatiquement** tout ce que possède l'ancienne (**la
mère**), puis peut **ajouter** ses propres choses ou **modifier** certaines.

L'analogie clé : « **EST UN** ». Un **chien EST UN animal**. Donc tout ce qu'un animal
sait faire, un chien sait le faire aussi — plus ses spécificités à lui (aboyer).

```
   CLASSE MÈRE   Animal   (a un nom, sait decrire())
        │
        │  « un Chien EST UN Animal »
        ▼
   CLASSE FILLE  Chien    (hérite de nom + decrire(), et AJOUTE aboyer())
```

Autres analogies qui marchent bien :
- Une **voiture électrique EST UNE voiture** : elle a les roues et le volant de toute
  voiture, et ajoute sa batterie.
- Un **carré EST UN rectangle** : il a tout du rectangle, en plus simple.

---

## 2. La SYNTAXE de l'héritage

On écrit `class Fille : public Mère`. Les deux points `:` se lisent « hérite de », et le
mot `public` signifie « garde la même visibilité » (à ce stade, mets toujours `public`).

```cpp
class Animal {                 // la classe MÈRE
public:
    std::string nom;
    void decrire() {
        std::cout << "Je suis " << nom << std::endl;
    }
};

class Chien : public Animal {  // la classe FILLE : « Chien hérite de Animal »
public:
    void aboyer() {            // une action EN PLUS, propre au chien
        std::cout << nom << " fait Wouf !" << std::endl;  // 'nom' vient de la mère
    }
};
```

Remarque importante : `aboyer()` utilise directement `nom`, **sans le redéclarer** : il a
été **hérité** de `Animal`. La fille profite gratuitement de tout ce que possède la mère.

```cpp
Chien rex;
rex.nom = "Rex";
rex.decrire();   // « Je suis Rex »  ← méthode HÉRITÉE de Animal
rex.aboyer();    // « Rex fait Wouf ! » ← méthode AJOUTÉE par Chien
```

---

## 3. C'est quoi le POLYMORPHISME ?

**Poly-morphisme** veut dire « **plusieurs formes** ». L'idée : on demande la **même
chose** à des objets différents, et **chacun répond à sa façon**.

L'analogie : tu réunis plein d'animaux et tu leur demandes à tous « **parle !** ». Le
chien répond « Wouf », le chat répond « Miaou »… Même ordre, réponses différentes. Toi,
tu n'as pas besoin de savoir lequel est lequel : tu dis juste « parle ».

Pour que ça marche en C++, il faut deux mots-clés :

- `virtual` sur la méthode de la **mère** : « cette méthode pourra être **redéfinie** par
  les filles ». C'est l'autorisation.
- `override` sur la méthode de la **fille** : « je **redéfinis** ici la méthode de la
  mère ». C'est une étiquette qui rend l'intention claire (et fait vérifier au
  compilateur qu'on ne s'est pas trompé de nom).

```cpp
class Animal {
public:
    virtual void parler() {            // virtual = redéfinissable par les filles
        std::cout << "..." << std::endl;
    }
};

class Chien : public Animal {
public:
    void parler() override {           // override = je redéfinis parler()
        std::cout << "Wouf !" << std::endl;
    }
};

class Chat : public Animal {
public:
    void parler() override {
        std::cout << "Miaou !" << std::endl;
    }
};
```

---

## 4. Le cœur du polymorphisme : un pointeur de type MÈRE

Le vrai pouvoir arrive ici. Un **pointeur de type mère** (`Animal*`) peut pointer vers un
objet **fille** (un `Chien`, un `Chat`…). Et grâce à `virtual`, quand on appelle
`parler()` à travers ce pointeur, c'est **la bonne version** (celle de la vraie fille) qui
s'exécute.

```cpp
Animal* a = new Chien();   // un pointeur Animal* qui pointe vers un Chien
a->parler();               // affiche « Wouf ! » → la version du Chien, pas celle d'Animal
```

> 💡 Un **pointeur** (`Animal*`) est une variable qui contient l'**adresse** d'un objet,
> au lieu de l'objet lui-même. On crée l'objet avec `new` et on appelle ses méthodes avec
> la flèche `->` (au lieu du point `.`). C'est cette indirection qui permet de manipuler
> un chien et un chat « comme des animaux ».

Du coup, on peut ranger des animaux variés dans **un seul `std::vector<Animal*>`** et les
faire tous parler dans une boucle, sans se soucier de leur type exact :

```cpp
std::vector<Animal*> animaux;
animaux.push_back(new Chien());
animaux.push_back(new Chat());

for (Animal* a : animaux) {
    a->parler();      // chacun répond à SA façon : Wouf, puis Miaou
}
```

---

## 5. ⚠️ Le destructeur `virtual` : ranger après soi

Quand on crée un objet avec `new`, il faut le **libérer** avec `delete` quand on a fini
(sinon la mémoire reste occupée pour rien). Mais si on supprime un `Chien` à travers un
`Animal*`, le C++ doit savoir appeler le **bon** nettoyage. Pour ça, on ajoute à la mère
un **destructeur virtual** :

```cpp
class Animal {
public:
    virtual ~Animal() {}      // destructeur VIRTUAL : nettoyage correct via Animal*
    virtual void parler() { ... }
};
```

Le destructeur, c'est l'inverse du constructeur : une méthode spéciale, nommée
`~NomDeLaClasse`, appelée **automatiquement** quand l'objet est détruit. Le mettre
`virtual` dès qu'on manipule des objets via un pointeur de type mère est une bonne
habitude (et ça évite un avertissement du compilateur).

```cpp
for (Animal* a : animaux) {
    delete a;     // on libère chaque animal : le destructeur virtual fait le bon ménage
}
```

---

## 6. 🆚 Récapitulatif des mots-clés

| Mot-clé | Où | Rôle |
|---------|-----|------|
| `class Fille : public Mère` | en-tête de la fille | la fille **hérite** de la mère |
| `virtual` | méthode de la mère | autorise les filles à **redéfinir** cette méthode |
| `override` | méthode de la fille | indique qu'on **redéfinit** la méthode de la mère |
| `virtual ~Mère()` | destructeur de la mère | **nettoyage correct** via un pointeur mère |

---

## ▶️ À toi de jouer

```bash
# L'héritage : une classe fille Chien qui hérite d'Animal
g++ -Wall cpp/04_heritage_polymorphisme/heritage.cpp -o heritage && ./heritage

# Le polymorphisme : des Animal* qui parlent chacun à leur façon
g++ -Wall cpp/04_heritage_polymorphisme/polymorphisme.cpp -o polymorphisme && ./polymorphisme
```

Lis les deux fichiers, puis **modifie-les** et **recompile** : ajoute une classe fille
`Vache` qui fait « Meuh », ajoute-la au `std::vector`, ou enlève le mot `virtual` de
`parler()` et observe que tous les animaux se mettent à répondre pareil (la version de la
mère).

➡️ La suite du parcours arrivera dans le même style.

## 📎 Ressources

- [`../AIDE_MEMOIRE.md`](../AIDE_MEMOIRE.md) — la syntaxe C++ en une page.
- [`../GLOSSAIRE.md`](../GLOSSAIRE.md) — les mots du C++ expliqués simplement.
