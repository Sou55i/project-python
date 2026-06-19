# 🔣 Les symboles et les arguments — quand, où, pourquoi ?

Beaucoup de débutants connaissent la syntaxe mais restent bloqués sur des **détails** :
*pourquoi un nombre ici entre parenthèses ? d'où sort ce `exist_ok` ? c'est quoi ce `%` ?
quand met-on `()` plutôt que `[]` ?* Ce guide répond à **toutes** ces questions.

> 🧠 Idée maîtresse : en Python, **chaque symbole a un rôle précis et constant**. Une fois
> ces rôles connus, on « lit » la ponctuation comme on lit les signes en français (la virgule,
> le point…). Et surtout : **on ne devine pas** les arguments d'une fonction — **on les lit**
> dans sa documentation (voir la dernière partie, la plus importante).

---

## 1. La table des symboles (à garder sous les yeux)

| Symbole | Rôle principal | Exemple | Comment le lire |
|---------|----------------|---------|-----------------|
| `( )` après un **nom** | **appeler** (exécuter) une fonction/méthode | `print("ok")` | « exécute `print` avec `"ok"` » |
| `( )` autour d'un calcul | **grouper** pour l'ordre des opérations | `(2 + 3) * 4` | « fais d'abord `2+3` » |
| `[ ]` après un **objet** | **accéder** à un élément (indice/clé) | `liste[0]`, `dico["nom"]` | « l'élément n°0 », « la valeur de la clé `nom` » |
| `[ ]` seuls | **créer une liste** | `[1, 2, 3]` | « une liste de 3 éléments » |
| `{ }` avec `clé: valeur` | **créer un dictionnaire** | `{"age": 30}` | « un dico clé→valeur » |
| `{ }` avec des valeurs | **créer un set** (sans doublon) | `{1, 2, 3}` | « un ensemble » |
| `.` | **accéder à ce qui « appartient » à** un objet | `texte.upper()` | « le `upper()` DE `texte` » |
| `=` (seul) | **ranger** une valeur dans une variable | `x = 5` | « x reçoit 5 » |
| `=` **dans un appel** | **nommer un argument** | `mkdir(exist_ok=True)` | « l'argument `exist_ok` vaut `True` » |
| `==` | **comparer** (égal ?) | `x == 5` | « x est-il égal à 5 ? » |
| `:` | ouvrir un **bloc**, une **tranche**, une **paire** | `if x:` · `liste[1:3]` · `{"a": 1}` | selon le contexte (voir §6) |
| `"..."` / `'...'` | du **texte** (chaîne) | `"bonjour"` | « la chaîne bonjour » |
| `%` | l'opérateur **modulo**, OU un **gabarit de texte** | `7 % 2` · `"%(name)s"` | voir §5 |

Les sections suivantes détaillent les cas qui posent problème.

---

## 2. Les parenthèses `( )` : « appeler » vs « grouper »

### a) Appeler quelque chose
Quand `( )` suit **un nom**, on **appelle** ce nom (on l'exécute) :

```python
print("salut")      # on APPELLE print
ma_liste.sort()     # on APPELLE la méthode sort (les ( ) vides = "exécute, sans rien de plus")
```

> 🔑 **Sans les parenthèses, on ne lance rien.** `ma_liste.sort` (sans `()`) ne trie pas : il
> désigne juste la fonction. `ma_liste.sort()` (avec `()`) la **déclenche**. C'est une erreur
> de débutant classique.

### b) Ce qu'on met ENTRE les parenthèses = les **arguments**

Les valeurs entre `( )` sont les **arguments** : les informations qu'on **donne** à la
fonction pour qu'elle travaille.

```python
round(3.14159, 2)   # deux arguments : le nombre, et "2" (nombre de décimales) -> 3.14
```

➡️ **« Le `2`, il sort d'où ? »** (la question type). Il sort de la **définition de la
fonction** : `round` est *programmée pour accepter* un 2ᵉ argument (le nombre de décimales).
On ne l'invente pas : on le découvre dans sa doc (voir §7). Pareil pour un appel comme
`programmer(2)` : le `2` est juste **la valeur qu'on passe** au paramètre prévu par la
fonction (ici, par exemple, « toutes les 2 unités »).

### c) Grouper un calcul
Sans nom devant, `( )` sert à **forcer l'ordre** des opérations (comme en maths) :

```python
(2 + 3) * 4    # 20  (le +) d'abord)   vs   2 + 3 * 4 = 14
```

---

## 3. Les crochets `[ ]` : « accéder » vs « créer une liste »

### a) Accéder à un élément (indexation)
Quand `[ ]` suit **un objet**, on **va chercher dedans** :

```python
fruits = ["pomme", "kiwi", "fraise"]
fruits[0]          # "pomme"   (on compte à partir de 0)
fruits[-1]         # "fraise"  (le dernier)
fruits[0:2]        # ["pomme", "kiwi"]  (une "tranche" : du 0 au 2 exclu)

ages = {"alice": 30}
ages["alice"]      # 30   (la valeur DE la clé "alice")
```

### b) Créer une liste
Quand `[ ]` ne suit **rien**, ils **fabriquent une liste** :

```python
nombres = [1, 2, 3]        # une nouvelle liste
```

> 🔑 La règle pour distinguer : **y a-t-il un objet juste AVANT le `[` ?**
> `fruits[0]` → après `fruits` → on **accède**. `[1, 2, 3]` → rien avant → on **crée**.

---

## 4. Les accolades `{ }` et le point `.`

### Accolades : dictionnaire ou set
```python
personne = {"nom": "Alice", "age": 30}   # dictionnaire : des paires clé: valeur
couleurs = {"rouge", "vert", "bleu"}       # set : des valeurs uniques, sans clé
```

### Le point `.` : « ce qui appartient à »
Le `.` se lit **« de »** : il accède à une **propriété** ou une **méthode** d'un objet.

```python
texte = "bonjour"
texte.upper()      # la méthode upper DE texte  -> "BONJOUR"
chemin.name        # l'attribut name DE chemin  (pas de () : c'est une donnée, pas une action)
```

> 🔑 **`.methode()` (avec parenthèses) = une action** ; **`.attribut` (sans parenthèses) = une
> donnée**. Comment savoir si ça prend des `()` ? → la doc / `help()` (voir §7).

### Les « chaînes » d'appels (le `a.b(2).c.d(...)`)
Une suite de points enchaînés se lit **de gauche à droite**, étape par étape. Chaque morceau
travaille sur le **résultat** du morceau précédent :

```python
"  Bonjour  ".strip().lower().replace("b", "B")
# 1) "  Bonjour  ".strip()          -> "Bonjour"        (enlève les espaces)
# 2) .lower()                        -> "bonjour"        (sur le résultat de l'étape 1)
# 3) .replace("b", "B")              -> "Bonjour"        (sur le résultat de l'étape 2)
```

> 🧠 Pour décoder une longue chaîne `truc.a(...).b.c(...)`, **coupe-la mentalement à chaque
> point** : « je pars de `truc`, j'appelle `a(...)`, sur le résultat j'accède à `b`, puis
> j'appelle `c(...)` ». Chaque cmdlet/méthode renvoie un objet sur lequel on continue.

---

## 5. Le symbole `%` : deux usages bien distincts

### a) Modulo (le reste d'une division) — un **opérateur**
```python
7 % 2      # 1   (le reste de 7 ÷ 2)
n % 2 == 0 # test "n est pair ?"
```

### b) Un **gabarit de texte** (`%(...)s`) — pas du Python « de base »
Quand on voit quelque chose comme `"%(asctime)s - %(message)s"`, le `%` n'est **pas** un
calcul : c'est un **modèle de texte à trous**. Chaque `%(nom)s` est un **emplacement** qui
sera **rempli plus tard** par la valeur correspondante. Le `s` final veut dire « formate en
texte (*string*) ».

```python
"%(nom)s a %(age)d ans" % {"nom": "Alice", "age": 30}
# -> "Alice a 30 ans"        ( %(nom)s = texte,  %(age)d = nombre entier )
```

> 🔑 **« D'où sortent `asctime`, `message`… ? »** Ce ne sont **pas** des mots Python : ce sont
> des **noms de champs définis par la bibliothèque** qui utilise ce gabarit. Par exemple, le
> module de journalisation `logging` **fournit** une liste de champs disponibles
> (`asctime` = l'heure, `levelname` = le niveau, `message` = le message…). **On les trouve
> dans la documentation de cette bibliothèque**, pas en les devinant. Une autre bibliothèque
> aura ses propres champs.
>
> 💡 Aujourd'hui on écrit plutôt les textes avec des **f-strings** (`f"{nom} a {age} ans"`,
> voir [COMPRENDRE_LE_CODE.md](./COMPRENDRE_LE_CODE.md)). Le style `%(...)s` reste courant
> dans `logging` car la bibliothèque construit le texte **elle-même, plus tard**.

---

## 6. Les deux-points `:` selon le contexte

Le même `:` a trois rôles, reconnaissables au contexte :

```python
if x > 0:                 # 1) OUVRE UN BLOC (if/for/while/def/class...) : ce qui suit est indenté
    ...

liste[1:3]                # 2) UNE TRANCHE (slice) : "du 1 au 3 exclu"

config = {"taille": 20}   # 3) PAIRE clé:valeur dans un dictionnaire

def f(x: int) -> int:     # 4) ANNOTATION de type (x est un int) — info de lecture, optionnelle
    ...
```

---

## 7. ⭐ LE point crucial : comment savoir quels arguments existent ?

C'est **la** question (`exist_ok`, `parents`, `level`, `format`… « comment les deviner ? »).
**Réponse : on ne les devine pas. On les LIT.** Toute fonction **déclare** ses paramètres ;
il suffit de les consulter. Trois façons :

### a) `help()` — la doc, sans quitter Python
Dans le terminal interactif (`python3`) :

```python
>>> from pathlib import Path
>>> help(Path.mkdir)
mkdir(self, mode=511, parents=False, exist_ok=False)
    Create a new directory at this given path.
    ...
```

Cette ligne **est la réponse** : `mkdir` accepte les paramètres `mode`, `parents`, `exist_ok`,
avec leurs **valeurs par défaut**. Donc `exist_ok` n'est pas « sorti de nulle part » : il est
**écrit dans la signature de `mkdir`**. On écrit `exist_ok=True` pour **changer** sa valeur
par défaut (`False`).

### b) La documentation officielle
Sur [docs.python.org](https://docs.python.org/fr/3/), chercher la fonction donne la **liste
complète** de ses paramètres, avec une explication de chacun.

### c) L'autocomplétion de l'éditeur
Dans VS Code (ou autre), taper `Path("x").mkdir(` affiche une **bulle** listant les
paramètres acceptés. C'est la même information, en direct.

### Arguments POSITIONNELS vs NOMMÉS (la distinction qui éclaire tout)

```python
round(3.14159, 2)              # positionnels : l'ordre compte (nombre, puis décimales)
open("f.txt", encoding="utf-8")  # "f.txt" est positionnel ; encoding=... est NOMMÉ
```

- **Positionnel** : on donne juste la valeur, et c'est sa **place** qui dit à quel paramètre
  elle correspond. (Le `2` d'un appel comme `round(x, 2)` ou `programmer(2)` est positionnel.)
- **Nommé** (mot-clé) : on écrit `nom=valeur`. On l'utilise surtout pour les **options**
  (souvent facultatives, avec une valeur par défaut) afin d'être **explicite** :
  `exist_ok=True` est bien plus clair que de se rappeler « le 3ᵉ argument de mkdir ».

> 🧭 **La méthode quand un appel te bloque** :
> 1. Repère **le nom appelé** (`mkdir`, `round`, `basicConfig`…).
> 2. Fais **`help(ce_nom)`** (ou regarde la doc).
> 3. Lis la **signature** : tu y vois TOUS les paramètres possibles et leurs valeurs par
>    défaut. Tu sais alors *exactement* ce que tu peux mettre, et pourquoi.

---

## 8. Récapitulatif express

- `nom(...)` → **on appelle** `nom` ; entre `()` = les **arguments**.
- `objet[...]` → **on accède** dans `objet` ; `[...]` seuls → **on crée une liste**.
- `{clé: valeur}` → **dictionnaire** ; `{valeurs}` → **set**.
- `objet.truc` → ce qui **appartient** à `objet` (`.truc()` = action, `.truc` = donnée).
- `nom=valeur` dans un appel → **argument nommé** (souvent une option).
- `%` → **modulo** (`a % b`) **ou** un **gabarit de texte** propre à une bibliothèque.
- `:` → **bloc**, **tranche**, **paire clé:valeur** ou **annotation**, selon le contexte.
- **Pour les arguments d'une fonction : `help(fonction)` ou la doc. On lit, on ne devine pas.**

➡️ Pour décoder des lignes entières et le code « magique » (`__main__`, `__init__.py`,
`', '.join(...)`…), voir [COMPRENDRE_LE_CODE.md](./COMPRENDRE_LE_CODE.md). Pour la méthode
d'écriture d'un script, voir [ECRIRE_UN_SCRIPT.md](./ECRIRE_UN_SCRIPT.md).
