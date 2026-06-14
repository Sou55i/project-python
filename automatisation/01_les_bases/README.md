# Module 01 — Les bases du langage

Ce module présente les **5 briques fondamentales** de tout programme Python. Une fois ces
briques comprises, tu peux (presque) tout construire.

> 🧠 Lis cette théorie en entier **avant** d'ouvrir les fichiers `.py`. Ensuite, lance-les
> et compare. Les deux scripts du module sont : `bases.py` (les briques) et
> `mini_calculatrice.py` (un mini-projet qui combine tout).

---

## 1. Les variables : des boîtes étiquetées

Une **variable** est une **boîte avec une étiquette** dans laquelle on range une valeur
pour la réutiliser plus tard.

```python
age = 25
prenom = "Alice"
```

- À gauche du `=` : le **nom** de la boîte (l'étiquette).
- À droite : la **valeur** qu'on range dedans.
- Le signe `=` ne veut **pas** dire « égal » au sens mathématique. Il veut dire
  **« range la valeur de droite dans la boîte de gauche »**.

On peut changer le contenu d'une boîte à tout moment :

```python
age = 25
age = age + 1   # on lit l'ancienne valeur (25), on ajoute 1, on remet (26)
```

> 💡 Choisis des noms de variables **clairs** : `age`, `total_ventes`, `nom_fichier`…
> Un bon nom rend le code lisible sans commentaire.

---

## 2. Les types : la nature d'une valeur

Toute valeur a un **type** : sa « nature ». Les 4 types de base à connaître :

| Type | Nom Python | Exemple | C'est quoi |
|------|-----------|---------|------------|
| Nombre entier | `int` | `42` | Un nombre sans virgule |
| Nombre décimal | `float` | `3.14` | Un nombre à virgule (point en anglais !) |
| Texte | `str` | `"bonjour"` | Une *chaîne de caractères*, entre guillemets |
| Booléen | `bool` | `True` / `False` | Vrai ou faux (avec une majuscule !) |

⚠️ **Le type compte.** `5` (nombre) et `"5"` (texte) ne sont pas la même chose :
- `5 + 5` donne `10`
- `"5" + "5"` donne `"55"` (Python colle les deux textes !)

On **convertit** d'un type à l'autre avec `int()`, `float()`, `str()` :

```python
reponse = input("Ton âge ? ")   # input() renvoie TOUJOURS du texte
age = int(reponse)              # on le convertit en nombre pour calculer
```

---

## 3. Les conditions : prendre des décisions

Un programme doit souvent **choisir** quoi faire selon une situation. C'est le rôle de
`if` (si), `elif` (sinon si) et `else` (sinon).

```python
note = 12

if note >= 10:
    print("Reçu ✅")
else:
    print("Recalé ❌")
```

Points clés :
- Après la condition, il y a un **`:`** (deux-points).
- Les lignes « à l'intérieur » du `if` sont **décalées vers la droite** (indentation).
  **En Python, ce décalage est OBLIGATOIRE** : c'est lui qui dit « ces lignes appartiennent
  au `if` ». Par convention, on décale de **4 espaces**.

Les opérateurs de comparaison renvoient `True` ou `False` :

| Opérateur | Signifie |
|-----------|----------|
| `==` | égal à (deux `=` ! un seul `=` sert à ranger dans une variable) |
| `!=` | différent de |
| `>` `<` | supérieur / inférieur |
| `>=` `<=` | supérieur ou égal / inférieur ou égal |

---

## 4. Les boucles : répéter sans se fatiguer

L'automatisation, c'est **répéter une action**. Les boucles servent exactement à ça.

### La boucle `for` : « pour chaque élément… »

```python
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(f"J'aime la {fruit}")
```

Lis-le comme une phrase : *« pour chaque `fruit` dans la liste `fruits`, affiche… »*.
La boucle exécute le bloc indenté **une fois par élément**.

`range(n)` génère les nombres de 0 à n-1, pratique pour répéter N fois :

```python
for i in range(3):     # i vaudra 0, puis 1, puis 2
    print(f"Tour numéro {i}")
```

### La boucle `while` : « tant que… »

```python
compteur = 0
while compteur < 3:
    print(compteur)
    compteur = compteur + 1   # ⚠️ sans ça, la boucle tournerait à l'infini !
```

---

## 5. Les fonctions : emballer du code réutilisable

Une **fonction** est un **bloc de code qu'on nomme** pour le réutiliser, comme un bouton
« faire le café ». On la **définit une fois**, puis on l'**appelle** autant de fois qu'on veut.

```python
def dire_bonjour(prenom):       # def = "définir". 'prenom' est un PARAMÈTRE (une entrée)
    return f"Bonjour {prenom} !" # 'return' renvoie un RÉSULTAT à celui qui a appelé

message = dire_bonjour("Alice")  # ici on APPELLE la fonction avec "Alice"
print(message)                   # affiche : Bonjour Alice !
```

Pourquoi c'est essentiel :
- **Éviter de répéter** le même code (principe DRY : *Don't Repeat Yourself*).
- **Donner un nom** à une idée → le code se lit comme du texte.
- **Corriger à un seul endroit** si quelque chose change.

---

## 6. Bonus : listes et dictionnaires (les rangements)

Souvent on manipule **plusieurs valeurs ensemble**. Deux outils incontournables :

### La liste : une suite ordonnée

```python
courses = ["pain", "lait", "œufs"]
courses.append("café")   # ajoute à la fin
print(courses[0])        # "pain" — on compte à partir de 0 !
```

### Le dictionnaire : des paires clé → valeur

```python
personne = {"nom": "Alice", "age": 30}
print(personne["nom"])   # "Alice"
```

Le dictionnaire est parfait pour décrire **un objet avec plusieurs caractéristiques**
(une personne, un produit, une ligne de tableau…).

---

## ▶️ À toi de jouer

```bash
python3 automatisation/01_les_bases/bases.py
python3 automatisation/01_les_bases/mini_calculatrice.py
```

Lis les deux fichiers, puis **modifie-les** : ajoute une opération à la calculatrice,
change les conditions, crée ta propre fonction.

➡️ Module suivant : [`02_fichiers_dossiers`](../02_fichiers_dossiers/).
