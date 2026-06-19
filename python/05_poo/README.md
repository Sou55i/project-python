# 🏗️ Module 05 : la Programmation Orientée Objet (POO)

> 🎯 **Objectif** : jusqu'ici, données (variables) et actions (fonctions) étaient séparées. La
> **POO** permet de les **réunir** dans un même « objet ». C'est ce qui structure les gros
> programmes. Concepts à maîtriser : **classe**, **objet**, **`self`**, **`__init__`**,
> **héritage**.

---

## 1. L'idée : regrouper données + actions

Sans POO, pour gérer un chien tu aurais une variable `nom_chien` et une fonction
`aboyer(nom_chien)`, séparées. Avec la POO, tu crées un **objet** `chien` qui contient **à la
fois** son nom (donnée) et sa capacité à aboyer (action).

> 🧠 **L'image fondatrice** : une **classe** est un **moule** (un plan) ; un **objet** est ce
> qu'on fabrique avec le moule. Le moule `Voiture` permet de fabriquer autant de voitures
> qu'on veut, chacune avec ses propres caractéristiques.

| Terme | Définition | Exemple |
|-------|------------|---------|
| **classe** | le plan / le moule | `Voiture` |
| **objet** (ou **instance**) | un exemplaire fabriqué | *ma* Tesla rouge |
| **attribut** | une **donnée** de l'objet | `marque`, `couleur` |
| **méthode** | une **action** de l'objet | `klaxonner()` |

---

## 2. Définir une classe

```python
class Voiture:                              # convention : nom de classe en MajusculeCamel
    def __init__(self, marque, couleur):    # le "constructeur" : appelé à la création
        self.marque = marque                # on RANGE les données DANS l'objet
        self.couleur = couleur

    def klaxonner(self):                     # une méthode = une fonction DANS la classe
        print(f"La {self.marque} fait : POUT POUT !")
```

### `__init__` : le constructeur

`__init__` (un *dunder*, voir [`../COMPRENDRE_LE_CODE.md`](../COMPRENDRE_LE_CODE.md)) est une
méthode **spéciale** que Python appelle **automatiquement** quand tu crées un objet. Son rôle :
**initialiser** les attributs (remplir les cases de l'objet).

### `self` : « moi-même »

`self` est **le** mot qui déroute le plus. C'est simplement **l'objet en cours de manipulation**.

- Dans `def klaxonner(self):`, `self` représente *la voiture sur laquelle on appelle la méthode*.
- `self.marque` = « **la** marque **de cet objet-ci** ».
- Tu écris `self` comme **premier paramètre** de chaque méthode, mais tu ne le passes **pas**
  toi-même à l'appel : Python le fournit tout seul.

```python
ma_caisse.klaxonner()    # tu n'écris PAS ma_caisse.klaxonner(ma_caisse) :
                         # Python met automatiquement ma_caisse dans "self"
```

> 🧠 **Traduction** : quand tu écris `ma_caisse.klaxonner()`, Python comprend
> « exécute `klaxonner` **avec** `self = ma_caisse` ». D'où `self.marque` = la marque de
> `ma_caisse`. C'est ça, le lien entre l'objet et ses méthodes.

---

## 3. Créer et utiliser un objet

```python
ma_caisse = Voiture("Tesla", "Rouge")   # APPELLE __init__ → fabrique un objet
                                        # "Tesla"→marque, "Rouge"→couleur (self est implicite)
print(ma_caisse.marque)                 # "Tesla"     ← lire un attribut (avec le point)
ma_caisse.klaxonner()                   # "La Tesla fait : POUT POUT !"  ← appeler une méthode

autre = Voiture("Renault", "Bleu")      # un AUTRE objet, indépendant : sa propre marque/couleur
```

> 🔎 **Pourquoi pas de `self` à la création ?** Quand tu écris `Voiture("Tesla", "Rouge")`, le
> `self` du `__init__` est l'objet **en train d'être créé**. Tu ne fournis que les arguments qui
> *suivent* `self`.

---

## 4. L'héritage : réutiliser et spécialiser

L'**héritage** permet de créer une classe à partir d'une autre : la classe **enfant** récupère
tout de la classe **parente**, et peut en ajouter ou en modifier.

```python
class Vehicule:                          # la classe PARENTE (générique)
    def __init__(self, nom, vitesse_max):
        self.nom = nom
        self.vitesse_max = vitesse_max

    def se_deplacer(self):
        print(f"Le véhicule {self.nom} avance.")


class Voiture(Vehicule):                 # ENFANT : (Vehicule) = "hérite de Vehicule"
    def __init__(self, nom, vitesse_max, nb_portes):
        super().__init__(nom, vitesse_max)   # appelle le __init__ du PARENT (évite de recopier)
        self.nb_portes = nb_portes           # puis ajoute un attribut propre à l'enfant

    def se_deplacer(self):               # REDÉFINIT (override) la méthode du parent
        print(f"La voiture {self.nom} roule à {self.vitesse_max} km/h.")
```

Deux mécanismes clés :

- **`super()`** = « la classe parente ». `super().__init__(...)` appelle le constructeur du
  parent pour ne **pas recopier** son code. On factorise.
- **La redéfinition (override)** : si l'enfant définit une méthode du même nom que le parent
  (`se_deplacer`), **c'est la version de l'enfant qui gagne** pour les objets enfants.

```python
ma_voiture = Voiture("Peugeot 208", 180, 5)
ma_voiture.se_deplacer()       # version de Voiture : "La voiture Peugeot 208 roule à 180 km/h."
```

> 🧠 **Quand utiliser l'héritage ?** Quand tu peux dire *« X **est un** Y »* : une `Voiture`
> **est un** `Vehicule`, un `Chat` **est un** `Animal`. Si tu dis plutôt *« X **a un** Y »*
> (une voiture **a un** moteur), ce n'est pas de l'héritage : range l'objet `Moteur` dans un
> attribut.

---

## 5. Afficher proprement un objet : `__str__`

Par défaut, `print(mon_objet)` affiche un truc cryptique comme `<__main__.Voiture object at
0x7f...>`. Définis `__str__` pour choisir un affichage lisible :

```python
class Voiture:
    def __init__(self, marque):
        self.marque = marque

    def __str__(self):                 # appelé automatiquement par print(objet)
        return f"Voiture {self.marque}"

print(Voiture("Tesla"))                # "Voiture Tesla"  (au lieu du charabia)
```

---

## 🏁 Exercices

1. **Lis et lance** [`poo.py`](./poo.py) : repère `__init__`, `self`, `super()`, l'override.
2. **Ajoute une classe `Moto`** qui hérite de `Vehicule`, avec un attribut `cylindree` et sa
   propre version de `se_deplacer`.
3. **Compte en banque** : crée une classe `Compte` avec un attribut `solde`, une méthode
   `deposer(montant)` et une méthode `retirer(montant)` qui refuse si le solde est insuffisant.

<details>
<summary>💡 Solution — exercice 2 (Moto)</summary>

```python
class Moto(Vehicule):
    def __init__(self, nom, vitesse_max, cylindree):
        super().__init__(nom, vitesse_max)   # réutilise le constructeur du parent
        self.cylindree = cylindree

    def se_deplacer(self):
        print(f"La moto {self.nom} ({self.cylindree} cm³) file à {self.vitesse_max} km/h.")
```
</details>

<details>
<summary>💡 Solution — exercice 3 (Compte)</summary>

```python
class Compte:
    def __init__(self, solde=0):
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            print("Solde insuffisant.")
            return
        self.solde -= montant

c = Compte(100)
c.deposer(50)        # solde = 150
c.retirer(200)       # "Solde insuffisant."
print(c.solde)       # 150
```
</details>

➡️ **Prochaine étape** : [module 06 — itérateurs & générateurs](../06_iterateurs_generateurs/).
