# 🏗️ Module 01 : Les bases (variables, types & contrôle)

> 🎯 **Objectif** : savoir **stocker** des informations (variables), connaître les **types** de
> base, et **piloter** le déroulement d'un programme avec les conditions et les boucles. Ce sont
> les 4 briques avec lesquelles on construit **tout** le reste.

---

## 1. Les variables : donner un nom à une valeur

Une **variable** est une **étiquette** posée sur une valeur, pour pouvoir la réutiliser par son
nom plus tard. On la crée avec le signe `=`, qui se lit « **reçoit** » (et **pas** « égal ») :

```python
age = 25
```

Ça se lit : « la variable `age` **reçoit** la valeur `25` ». À partir de là, écrire `age` dans
le code, c'est écrire `25`.

> 🧠 **L'image** : une variable est une **boîte étiquetée**. `age = 25` met `25` dans une boîte
> étiquetée `age`. Plus tard, `age = 30` jette l'ancien contenu et met `30` à la place.

### Le typage dynamique

En Python, tu n'annonces **pas** le type d'une variable : Python le **devine** d'après la valeur.

```python
age = 25            # un nombre entier        → type int
nom = "Marc"        # du texte                → type str  (string)
taille = 1.75       # un nombre à virgule     → type float (à cause du point décimal)
est_content = True  # vrai ou faux            → type bool (booléen)
```

Pour vérifier le type d'une valeur, utilise la fonction `type()` :

```python
print(type(age))    # <class 'int'>
print(type(nom))    # <class 'str'>
```

> ⚠️ **Python est sensible à la casse** : `age`, `Age` et `AGE` sont **trois variables
> différentes**. Une erreur de majuscule est une cause classique de `NameError`.

### Bien nommer ses variables

Un bon nom explique **ce que contient** la boîte. Conventions Python :

- en **minuscules**, mots séparés par des `_` : `nom_joueur`, `prix_total` (style *snake_case*) ;
- **descriptif** : `vitesse` plutôt que `v`, `nombre_essais` plutôt que `n` ;
- pas d'accents, pas d'espaces, ne commence pas par un chiffre.

---

## 2. Les types de base, en détail

| Type | À quoi ça sert | Exemples |
|------|----------------|----------|
| `int` | nombres **entiers** | `0`, `42`, `-7` |
| `float` | nombres **à virgule** | `1.75`, `-0.5`, `3.0` |
| `str` | **texte** (entre guillemets) | `"bonjour"`, `'A'`, `""` |
| `bool` | **vrai / faux** | `True`, `False` |

### Opérations sur les nombres

```python
print(7 + 3)    # 10   addition
print(7 - 3)    # 4    soustraction
print(7 * 3)    # 21   multiplication
print(7 / 3)    # 2.33...  division (donne TOUJOURS un float)
print(7 // 3)   # 2    division ENTIÈRE (on garde le quotient)
print(7 % 3)    # 1    MODULO : le reste de la division (utile pour "est-ce pair ?")
print(2 ** 10)  # 1024 puissance (2 à la puissance 10)
```

> 🔎 Le **modulo** `%` revient souvent : `nombre % 2 == 0` teste si un nombre est **pair**.
> (Attention : ce même symbole `%` a un autre usage avec le texte — voir
> [`../LES_SYMBOLES.md`](../LES_SYMBOLES.md).)

### Opérations sur le texte

```python
prenom = "Ada"
nom = "Lovelace"
print(prenom + " " + nom)   # "Ada Lovelace"  : le + COLLE les chaînes (concaténation)
print("ha" * 3)             # "hahaha"        : le * RÉPÈTE une chaîne
print(len(prenom))          # 3               : len() donne la longueur
```

### Les f-strings : mélanger texte et variables

La façon **moderne et lisible** d'insérer des variables dans du texte : on met un `f` juste
avant le guillemet ouvrant, et on place les variables entre **accolades** `{ }`.

```python
nom = "Baba"
score = 100
print(f"Joueur : {nom} | Score : {score}")   # Joueur : Baba | Score : 100
```

> 🧠 **Pourquoi le `f` ?** Il signale à Python : « dans ce texte, ce qui est entre `{ }` n'est
> **pas** du texte littéral, c'est une **expression à calculer** ». Sans le `f`, tu obtiendrais
> littéralement `{nom}` à l'écran.

### Convertir un type en un autre

Les valeurs tapées au clavier ou lues dans un fichier sont du **texte**. Pour calculer avec,
il faut les **convertir** :

```python
age_texte = "25"          # c'est du texte, PAS un nombre
age = int(age_texte)      # int(...) convertit le texte en entier → 25
print(age + 1)            # 26

prix = float("1.75")      # texte → nombre à virgule → 1.75
message = str(42)         # nombre → texte → "42"
```

> ⚠️ Erreur classique : `"25" + 1` plante (`TypeError`) car on ne peut pas additionner du texte
> et un nombre. Il faut d'abord `int("25") + 1`.

---

## 3. Prendre des décisions : `if` / `elif` / `else`

Un programme doit souvent **choisir** quoi faire selon une situation. C'est le rôle du `if`
(« si »).

```python
age = 20

if age >= 18:
    print("Majeur")
elif age >= 13:
    print("Adolescent")
else:
    print("Enfant")
```

Comment ça se lit :

- **`if condition:`** — si la condition est vraie, on exécute le bloc indenté en dessous.
- **`elif autre_condition:`** — « sinon, si… » : testé seulement si le `if` était faux.
  (On peut en mettre plusieurs, ou aucun.)
- **`else:`** — « sinon » : exécuté si **rien** au-dessus n'était vrai. (Facultatif.)

### Le `:` et l'indentation : la règle d'or de Python

Deux choses **obligatoires** ici, et c'est ce qui déroute le plus au début :

1. La ligne du `if` se **termine par deux-points** `:`. Le `:` annonce : « un bloc commence ».
2. Les lignes du bloc sont **décalées vers la droite** (par convention **4 espaces**). C'est
   cette **indentation** qui dit à Python « ces lignes appartiennent au `if` ». D'autres
   langages utilisent des accolades `{ }` ; Python, lui, utilise l'**alignement du texte**.

```python
if age >= 18:
    print("Cette ligne est DANS le if")   # indentée → fait partie du if
    print("Celle-ci aussi")
print("Cette ligne est DEHORS")           # pas indentée → s'exécute toujours
```

> ⚠️ Mélanger espaces et tabulations, ou mal aligner, provoque une `IndentationError`.
> Configure ton éditeur pour insérer **4 espaces** quand tu appuies sur Tab.

### Les opérateurs de comparaison et logiques

```python
==   # égal à        (À NE PAS confondre avec = qui AFFECTE une valeur)
!=   # différent de
<  <=  >  >=          # inférieur, inférieur ou égal, supérieur, supérieur ou égal
```

On combine des conditions avec `and`, `or`, `not` :

```python
if age >= 18 and a_le_permis:     # les DEUX doivent être vraies
    print("Peut conduire")

if est_weekend or est_ferie:      # AU MOINS une des deux
    print("Repos")

if not est_connecte:              # inverse : vrai si est_connecte est faux
    print("Veuillez vous connecter")
```

> 🔑 **`=` vs `==`** : le piège n°1 des débutants. `=` **range** une valeur dans une variable ;
> `==` **compare** deux valeurs et répond `True`/`False`. Dans un `if`, c'est presque toujours `==`.

---

## 4. Répéter des actions : les boucles

### La boucle `for` — « pour chaque… »

On l'utilise pour **parcourir** une série d'éléments, ou **répéter** un nombre **connu** de fois.

```python
# Parcourir une liste, élément par élément
for fruit in ["pomme", "poire", "kiwi"]:
    print(fruit)

# Répéter un nombre précis de fois avec range()
for i in range(5):        # range(5) produit 0, 1, 2, 3, 4  (5 valeurs, à partir de 0)
    print(f"Tour numéro {i}")
```

> 🔎 **`range(5)` commence à 0 et s'arrête AVANT 5** : tu obtiens `0,1,2,3,4`, soit bien 5 tours.
> On peut aussi écrire `range(2, 6)` → `2,3,4,5`, ou `range(0, 10, 2)` → `0,2,4,6,8` (pas de 2).

### La boucle `while` — « tant que… »

On l'utilise quand on **ne sait pas d'avance** combien de fois répéter : on continue **tant
qu'**une condition reste vraie.

```python
compteur = 3
while compteur > 0:           # tant que compteur est strictement positif
    print(f"{compteur}...")
    compteur -= 1             # compteur = compteur - 1  → IMPORTANT : fait avancer vers la fin
print("Décollage !")
```

> ⚠️ **La boucle infinie** : si tu oublies de faire évoluer la condition (ici `compteur -= 1`),
> le `while` ne s'arrête **jamais**. Pour interrompre un programme bloqué dans le terminal :
> **`Ctrl + C`**.

### `for` ou `while` : lequel choisir ?

| Tu connais le nombre de tours ? | Utilise |
|---------------------------------|---------|
| Oui (parcourir une liste, répéter N fois) | **`for`** |
| Non (attendre une condition, une saisie valide…) | **`while`** |

### Les raccourcis d'affectation

```python
compteur += 1   # compteur = compteur + 1
total   -= 5    # total = total - 5
prix    *= 2    # prix = prix * 2
```

---

## 5. Tout assembler : un mini-programme

```python
# Demande un nombre et dit s'il est pair, impair, ou nul
texte = input("Entre un nombre entier : ")   # input() lit ce que l'utilisateur tape (du TEXTE)
nombre = int(texte)                          # on convertit ce texte en entier pour calculer

if nombre == 0:
    print("C'est zéro.")
elif nombre % 2 == 0:                        # reste nul dans la division par 2 → pair
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")
```

Ce court programme réunit **tout le module** : variable, conversion de type, `input`, `if/elif/else`,
modulo, f-string. Relis-le jusqu'à comprendre **chaque** symbole.

---

## 🏁 Exercices

1. **Lis et lance** [`bases.py`](./bases.py), puis modifie les valeurs pour observer les
   changements (mets `vie = 10`, change le score…).
2. **Table de multiplication** : écris une boucle qui affiche la table de 7 (de `7 x 1` à `7 x 10`).
3. **Compte à rebours** : avec un `while`, affiche `10, 9, 8, … 1, Partez !`.
4. **FizzBuzz (le classique des entretiens)** : pour les nombres de 1 à 20, affiche `Fizz` si
   le nombre est divisible par 3, `Buzz` s'il est divisible par 5, `FizzBuzz` si les deux, sinon
   le nombre lui-même.

<details>
<summary>💡 Solution — exercice 2 (table de 7)</summary>

```python
for i in range(1, 11):           # 1 à 10 inclus
    print(f"7 x {i} = {7 * i}")
```
</details>

<details>
<summary>💡 Solution — exercice 4 (FizzBuzz)</summary>

```python
for n in range(1, 21):
    if n % 3 == 0 and n % 5 == 0:    # divisible par 3 ET par 5 → on teste ce cas EN PREMIER
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```
> 🧠 **Pourquoi tester `and` en premier ?** Si on testait `n % 3 == 0` avant, le nombre 15
> (divisible par les deux) afficherait `Fizz` et on n'arriverait jamais au cas `FizzBuzz`.
> **L'ordre des conditions compte** : du plus spécifique au plus général.
</details>

➡️ **Prochaine étape** : [module 02 — les collections](../02_collections/) (listes, dictionnaires…).
