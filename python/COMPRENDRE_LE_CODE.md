# 🔍 Comprendre le code Python (lire et décoder n'importe quel script)

> Tu as lu les cours, tu connais la syntaxe… mais devant un *vrai* script, tu butes encore ?
> **C'est normal, et ça se travaille.** Lire du code est une compétence **différente** de
> l'écrire. Ce guide t'apprend à **décoder n'importe quelle ligne**, et explique enfin tous
> les « trucs bizarres » (`__main__`, `__init__.py`, `', '.join(...)`, `if not x`…).

---

## 1. La méthode : lire un script qu'on ne comprend pas

Ne lis **pas** un script bêtement de la première à la dernière ligne. Fais comme un détective :

1. **Va tout en bas**, cherche `if __name__ == "__main__":`. C'est le **vrai point de départ**
   du programme (voir §3). Tu y vois l'**enchaînement principal** : « on fait ça, puis ça ».
2. **Suis les appels de fonctions.** Quand tu vois `resoudre(domaine)`, remonte lire la
   fonction `def resoudre` pour comprendre ce qu'elle fait — comme cliquer sur un lien.
3. **Traduis chaque ligne en français**, à voix haute. Une ligne de code = **une phrase**.
4. **Ignore les détails au début.** Comprends d'abord *l'intention générale* (les grandes
   étapes), puis seulement après, plonge dans le « comment ».

> 🧠 Règle d'or : **on lit une expression de l'INTÉRIEUR vers l'EXTÉRIEUR** (voir §2).

---

## 2. Décoder une ligne « de l'intérieur vers l'extérieur »

Prenons un exemple courant :

```python
print(f"  [A] → {', '.join(ips)}")
```

Ça paraît dense. On l'épluche **comme un oignon, du cœur vers la peau** :

| Étape | Le morceau | Ce que ça fait |
|------|-----------|----------------|
| ① le plus interne | `ips` | une **liste** d'adresses, ex. `["1.1.1.1", "8.8.8.8"]` |
| ② | `', '.join(ips)` | **colle** les éléments de la liste en **un seul texte**, séparés par `, ` → `"1.1.1.1, 8.8.8.8"` |
| ③ | `f"  [A] → {…}"` | une **f-string** : le `{…}` est remplacé par le texte de l'étape ② → `"  [A] → 1.1.1.1, 8.8.8.8"` |
| ④ le plus externe | `print(…)` | **affiche** ce texte final à l'écran |

Donc la ligne se lit : *« colle les IP avec des virgules, glisse le résultat dans le texte,
et affiche-le »*.

> ✅ **Le réflexe** : trouve la paire de parenthèses/accolades **la plus intérieure**,
> comprends-la, puis remonte d'un cran. Toujours.

### Et `', '.join(...)`, c'est quoi exactement ?

`join` veut dire **« joindre »** (assembler). Sa logique surprend les débutants car on
l'écrit « à l'envers » :

```python
separateur.join(liste)
```

- On part du **séparateur** (le texte à mettre ENTRE les éléments) : ici `', '`.
- On appelle sa méthode `.join(...)` en lui donnant la **liste** à assembler.

```python
", ".join(["a", "b", "c"])   # → "a, b, c"
" - ".join(["a", "b"])        # → "a - b"
"".join(["a", "b", "c"])      # → "abc"   (séparateur vide = on colle tout)
```

> 💡 **Pourquoi c'est `séparateur.join(liste)` et pas `liste.join(séparateur)` ?**
> Parce que `join` est une **méthode des chaînes de caractères** (`str`), pas des listes.
> Le séparateur EST une chaîne, donc c'est lui qui porte la méthode. À retenir tel quel.
>
> 🔁 L'opération inverse de `join` est `split` (découper) : `"a, b, c".split(", ")` →
> `["a", "b", "c"]`.

---

## 3. Les « dunders » : le code à double underscore `__truc__`

**Dunder** = *Double UNDERscore* = deux tirets bas de **chaque** côté : `__nom__`.
Ce sont des noms **réservés** que Python reconnaît et utilise **automatiquement**. Ce ne sont
pas magiques : ce sont des **conventions que l'interpréteur connaît**.

### 3.1 `if __name__ == "__main__":` — le « point de départ »

C'est **le** truc qui déroute tout le monde. Décodons.

- `__name__` est une **variable que Python crée tout seul** dans chaque fichier.
- Quand tu **lances** un fichier directement (`python3 mon_fichier.py`), Python met
  `__name__ = "__main__"` dans CE fichier.
- Quand le fichier est **importé** par un autre (`import mon_fichier`), Python met à la place
  `__name__ = "mon_fichier"` (le nom du module).

Donc :

```python
if __name__ == "__main__":
    # Ce bloc ne s'exécute QUE si on lance CE fichier directement.
    # Il NE s'exécute PAS si le fichier est importé ailleurs.
    main()
```

> 🧠 Traduction en français : **« Si c'est MOI qu'on a lancé (et pas quelqu'un qui m'importe),
> alors exécute ça. »**
>
> **Pourquoi c'est utile ?** Pour qu'un fichier puisse servir à **deux choses** :
> 1. être **lancé** comme programme (le bloc s'exécute),
> 2. être **importé** pour réutiliser ses fonctions **sans** que tout se déclenche par surprise.
>
> Tu peux le vérifier : `print(__name__)` en haut d'un fichier affiche `__main__` si tu le
> lances, et `nom_du_fichier` si tu l'importes.

### 3.2 `__init__.py` — le fichier qui fait d'un dossier un « paquet »

Un fichier nommé **`__init__.py`** placé dans un dossier dit à Python :
**« ce dossier est un *package* (une boîte de modules) qu'on peut importer. »**

```
mon_projet/
├── outils/
│   ├── __init__.py        ← grâce à lui, "outils" devient importable
│   ├── reseau.py
│   └── fichiers.py
└── main.py
```

```python
# Dans main.py, on peut alors écrire :
from outils import reseau
from outils.fichiers import lire
```

- **Souvent il est VIDE** : sa simple présence suffit à marquer le dossier comme package.
- Il peut aussi contenir du code d'**initialisation** du package, ou choisir ce qui est
  exposé (`from .reseau import resoudre`) pour permettre `from outils import resoudre`.

> 🧠 Image : `__init__.py` est l'**étiquette « ceci est une boîte rangeable »** collée sur un
> dossier. Sans étiquette, Python voit juste un dossier ordinaire.
> *(Note : depuis Python 3.3, on peut importer certains dossiers sans `__init__.py`, mais le
> mettre reste la convention claire et sans surprise.)*

### 3.3 `__init__` (la méthode) — le constructeur d'un objet

À ne pas confondre avec le fichier ! Dans une **classe**, `__init__` est la méthode appelée
**automatiquement** quand on crée un objet — elle **initialise** ses attributs.

```python
class Chien:
    def __init__(self, nom):     # appelé quand on écrit Chien("Rex")
        self.nom = nom           # on range le nom DANS l'objet

rex = Chien("Rex")               # Python appelle __init__ tout seul, ici
```

### 3.4 Les autres dunders (pour info)

Ils permettent à TES objets de réagir aux opérations standard de Python :

| Dunder | Déclenché par | Sert à |
|--------|---------------|--------|
| `__init__` | `Chien("Rex")` | construire/initialiser l'objet |
| `__str__` | `print(objet)` | choisir l'affichage lisible de l'objet |
| `__len__` | `len(objet)` | définir ce que renvoie `len(...)` |
| `__eq__` | `a == b` | définir l'égalité entre deux objets |

> Tu n'as pas besoin de tous les connaître. Retiens juste : **`__x__` = un « branchement »
> que Python appelle automatiquement dans une situation précise.**

### 3.5 Le **simple** underscore `_nom` — « privé par convention »

Quand on voit **un seul** underscore au DÉBUT d'un nom — par exemple
`_un_aide_interne` — ça veut dire :

> 🔒 **« Ceci est un détail interne. Ne l'utilise pas depuis l'extérieur, c'est une fonction
> d'aide privée. »**

Ce n'est **pas** une protection technique (Python ne t'empêche pas de l'appeler), c'est une
**convention** entre développeurs : « touche pas, c'est de la plomberie interne ».

```python
def traiter(donnee):         # ← fonction "publique" : c'est ELLE qu'on appelle de l'extérieur
    ...
    return _traiter_interne(donnee)    # ← aide "privée" : plomberie interne

def _traiter_interne(donnee):   # le _ dit "détail d'implémentation, ne pas appeler dehors"
    ...
```

---

## 4. Les tournures qui reviennent tout le temps

Une fois ces motifs reconnus, **80 % du code devient lisible**.

### `if not x:` — tester « si c'est vide / faux / absent »

```python
if not ips:           # "si ips est vide"
    print("aucune IP")
```

Python considère comme **« faux »** (*falsy*) : `False`, `None`, `0`, `""` (texte vide),
`[]` (liste vide), `{}` (dict vide). Donc `if not ips:` = *« si la liste est vide »*, et
`if ips:` = *« s'il y a au moins une IP »*. Pas besoin de `len(ips) == 0`.

### Le « return tôt » (guard clause) — le patron de **repli** (fallback)

```python
if not DNS_LIB:
    return _resoudre_stdlib(domaine)
# ... ici, le code "normal" qui utilise la bibliothèque DNS ...
```

Décodage **mot à mot** :
- `DNS_LIB` est une variable définie plus haut (souvent un booléen : *« la bibliothèque
  `dnspython` est-elle installée ? »*). Généralement posée ainsi :
  ```python
  try:
      import dns.resolver        # on tente d'importer la lib optionnelle
      DNS_LIB = True             # réussi → on a la lib
  except ImportError:
      DNS_LIB = False            # échoué → pas installée
  ```
- `if not DNS_LIB:` = *« si la bibliothèque n'est PAS disponible »*.
- `return _resoudre_stdlib(domaine)` = *« alors fais le travail avec une méthode de secours
  (la bibliothèque standard) et ARRÊTE ici la fonction »* (`return` quitte la fonction tout
  de suite).

> 🧠 **C'est le patron « solution de repli » (fallback).** L'idée : *« si l'outil idéal n'est
> pas là, j'utilise un plan B, et je sors. »* Le `return` en haut évite d'imbriquer un gros
> `if/else` : on traite le cas particulier d'abord, puis le reste du code suppose le cas normal.

➡️ **« Comment savoir qu'il fallait écrire ça ? »** Tu ne le « devines » pas par magie : tu
le **décides** parce que tu as un besoin précis (« mon script doit marcher même si `dnspython`
n'est pas installé »). On apprend à transformer un besoin en code dans le guide
**[ECRIRE_UN_SCRIPT.md](./ECRIRE_UN_SCRIPT.md)**.

### Le ternaire `A if condition else B`

Une mini-décision sur une ligne :

```python
etat = "ouvert" if port_repond else "ferme"
# se lit : etat vaut "ouvert" SI port_repond, SINON "ferme"
```

### `.get(clé, défaut)` — lire un dict sans planter

```python
version = service.get("version", "inconnue")
# "donne service['version'], ou 'inconnue' si la clé n'existe pas"
```

### La compréhension de liste `[... for ... in ...]`

```python
carres = [n * n for n in nombres]
# "pour chaque n dans nombres, calcule n*n, et mets tout dans une liste"
```

### `with ... as f:` — ouvrir/fermer proprement

```python
with open("data.txt") as f:    # ouvre le fichier, le range dans f
    contenu = f.read()
# à la sortie du bloc, le fichier est AUTOMATIQUEMENT refermé
```

### `*args` et `**kwargs` — « un nombre quelconque d'arguments »

Ces deux-là intimident à cause des étoiles, mais l'idée est simple : ils permettent à une
fonction d'accepter **autant d'arguments qu'on veut**, sans les nommer un par un d'avance.

Tu en connais déjà un sans le savoir : `print("a", "b", "c", "d")` accepte 1, 2 ou 50
arguments. C'est grâce à `*args`.

**`*args`** = « récupère tous les arguments **positionnels** restants dans un **tuple** ».

```python
def additionner(*args):       # args sera un tuple : (1, 2, 3)
    total = 0
    for n in args:            # on parcourt chaque argument reçu
        total += n
    return total

additionner(1, 2, 3)          # → 6
additionner(10, 20)           # → 30   (marche avec n'importe combien de nombres)
```

**`**kwargs`** = « récupère tous les arguments **nommés** restants dans un **dictionnaire** ».
(*kwargs* = *keyword arguments*, « arguments-mot-clé ».)

```python
def afficher(**kwargs):       # kwargs sera un dict : {"nom": "Ada", "age": 36}
    for cle, valeur in kwargs.items():
        print(f"{cle} = {valeur}")

afficher(nom="Ada", age=36)
# nom = Ada
# age = 36
```

> 🔑 **Ce qui compte, ce n'est pas le mot, c'est l'étoile.** `*` = « regroupe les arguments
> **positionnels** » ; `**` = « regroupe les arguments **nommés** ». Les noms `args` et `kwargs`
> sont une simple **convention** : `def f(*valeurs)` marche tout aussi bien. Quand tu vois ces
> étoiles **dans une définition** `def`, traduis : *« cette fonction accepte un nombre variable
> d'arguments »*.

**L'étoile sert aussi à l'INVERSE** (au moment de l'appel) : « déplie » une liste/un dict en
arguments séparés.

```python
nombres = [1, 2, 3]
additionner(*nombres)         # équivaut à additionner(1, 2, 3) → 6   (* "déballe" la liste)

infos = {"nom": "Ada", "age": 36}
afficher(**infos)             # équivaut à afficher(nom="Ada", age=36)  (** "déballe" le dict)
```

> 🧠 **La règle pour lire les étoiles** : `*`/`**` **dans un `def`** = « j'**emballe** ce que je
> reçois » ; `*`/`**` **dans un appel** = « je **déballe** ce que j'envoie ». Approfondi au
> module [`03_fonctions_modules`](./03_fonctions_modules/).

---

## 5. Exercice guidé : « décode chaque symbole de cette ligne »

L'objectif n'est pas seulement de comprendre *ce que fait* une ligne, mais de savoir **nommer
le rôle de chaque symbole**. Entraîne-toi sur celle-ci :

```python
resultats = [str(n).zfill(3) for n in donnees if n > 0]
```

Avant de regarder, essaie de répondre : *à quoi sert chaque `( )`, `[ ]`, `.` ?*

<details>
<summary>💡 Décodage complet, symbole par symbole</summary>

On lit **de l'intérieur vers l'extérieur**, et on nomme chaque symbole :

| Morceau | Symbole(s) | Rôle |
|---------|-----------|------|
| `donnees` | — | la liste de départ, ex. `[5, -2, 17]` |
| `if n > 0` | `>` | **filtre** : on ne garde que les éléments positifs |
| `str(n)` | `( )` d'**appel** | **convertit** le nombre `n` en texte (ex. `5` → `"5"`) |
| `.zfill` | `.` d'**accès** | accède à la **méthode** `zfill` de la chaîne |
| `.zfill(3)` | `( )` d'**appel** + arg `3` | complète avec des zéros à gauche jusqu'à 3 caractères : `"5"` → `"005"` |
| `[ ... for ... in ... if ... ]` | `[ ]` de **création de liste** | **compréhension** : construit une nouvelle liste |

Résultat pour `donnees = [5, -2, 17]` : on jette `-2`, et on obtient `["005", "017"]`.

Traduction en français : *« pour chaque nombre positif de `donnees`, transforme-le en texte
rembourré de zéros sur 3 chiffres, et range tout ça dans une nouvelle liste »*.

> 🔎 Et `zfill`, comment le « connaître » ? On ne le devine pas : on a un **besoin** (« afficher
> `5` comme `005` »), on cherche *« python pad number with zeros »*, et la doc des chaînes donne
> `zfill`. C'est exactement la démarche de [ECRIRE_UN_SCRIPT.md](./ECRIRE_UN_SCRIPT.md).
</details>

> 🎯 **Refais ce travail** sur 3 lignes denses de n'importe quel script : pour chaque symbole,
> dis à voix haute « ça, c'est un appel / un accès / une création de liste / un filtre… ».
> C'est l'exercice qui fait passer de « je récite la syntaxe » à « je lis le code ».

---

## 6. S'entraîner à lire

Reprends **n'importe quel script** du dépôt (par ex. dans [`pentest/`](./pentest/)) et, pour
chaque ligne qui te bloque :
1. trouve le **morceau le plus interne** et traduis-le ;
2. remonte d'un cran ;
3. note le **patron** que tu reconnais (join, guard clause, compréhension…).

Au bout de quelques scripts, ton œil reconnaîtra les motifs **instantanément**. C'est
exactement comme apprendre à lire : au début on déchiffre lettre par lettre, puis on lit des
mots entiers.

➡️ Maintenant que tu sais **lire**, apprends à **écrire et raisonner** :
**[ECRIRE_UN_SCRIPT.md](./ECRIRE_UN_SCRIPT.md)**.
