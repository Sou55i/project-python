# 📖 Glossaire — les mots de Python expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**Argument** — La valeur concrète que tu donnes à une fonction quand tu l'appelles.
Dans `saluer("Alice")`, `"Alice"` est l'argument. (Côté définition, on parle de *paramètre*.)

**Bibliothèque** (*library*) — Une boîte à outils écrite par d'autres, qu'on réutilise.
Ex : `pandas` pour les tableaux. On en parle au module 06.

**Booléen** (`bool`) — Un type qui ne vaut que `True` (vrai) ou `False` (faux). Sert aux
conditions.

**Boucle** — Une instruction qui répète des actions : `for` (« pour chaque… ») ou `while`
(« tant que… »). C'est le cœur de l'automatisation.

**Chaîne de caractères** (`str`) — Du texte, écrit entre guillemets : `"bonjour"`.

**Commentaire** — Une note écrite pour les humains, ignorée par Python. Commence par `#`.

**Compréhension de liste** (*list comprehension*) — Une façon courte de créer une liste en
une ligne : `[x * 2 for x in nombres]`. Équivaut à une petite boucle.

**Condition** — Un test qui oriente le programme : `if`, `elif`, `else`. « Si… alors… ».

**Constante** — Une variable dont la valeur ne change pas. Par convention, on l'écrit
`EN_MAJUSCULES`.

**Dictionnaire** (`dict`) — Un rangement de paires `clé: valeur`, entre `{ }`. Parfait pour
décrire un objet : `{"nom": "Alice", "age": 30}`. La clé sert d'étiquette pour retrouver
la valeur.

**Docstring** — Le texte entre `"""..."""` au début d'un fichier ou d'une fonction, qui
explique à quoi il sert.

**Encodage** (`encoding="utf-8"`) — La table qui dit comment écrire les caractères (accents,
emojis) dans un fichier. Mets toujours `utf-8`.

**Exception** — Une erreur qui survient pendant l'exécution (ex : diviser par zéro). On peut
l'« attraper » avec `try/except` pour éviter le plantage.

**f-string** — Une chaîne préfixée par `f` où l'on insère des variables entre accolades :
`f"Bonjour {nom}"`.

**Fonction** — Un bloc de code nommé et réutilisable. On la *définit* avec `def`, on
l'*appelle* par son nom. Comme une recette qu'on peut refaire à volonté.

**Float** — Un nombre à virgule (avec un point) : `3.14`.

**Import** — L'action d'ouvrir une boîte à outils pour s'en servir : `import os`.

**Indentation** — Le décalage des lignes vers la droite (4 espaces). En Python, il est
**obligatoire** : c'est lui qui délimite les blocs (le contenu d'un `if`, d'une boucle…).

**Index (indice)** — La position d'un élément dans une liste. ⚠️ On compte **à partir de 0** :
`liste[0]` est le premier élément.

**Int** — Un nombre entier (sans virgule) : `42`.

**Itérer** — Parcourir les éléments un par un (ce que fait une boucle `for`).

**JSON** — Un format texte pour stocker des données structurées, très utilisé par les APIs.
Ressemble aux dictionnaires Python.

**Liste** (`list`) — Une suite ordonnée et modifiable de valeurs, entre crochets `[ ]`.

**Module** — Un fichier `.py` regroupant des fonctions réutilisables. `json` est un module.

**None** — La valeur spéciale qui signifie « rien », « pas de valeur ».

**Paramètre** — Le nom d'une entrée dans la *définition* d'une fonction :
`def saluer(nom):` → `nom` est un paramètre. (La valeur fournie à l'appel est l'*argument*.)

**pip** — L'outil qui installe les bibliothèques tierces : `pip install requests`.

**Programme principal** — Le code qui démarre tout, souvent placé dans
`if __name__ == "__main__":`, tout en bas du fichier.

**return** — Le mot-clé qui fait *renvoyer* un résultat par une fonction à celui qui
l'a appelée.

**Slice (tranche)** — Une portion d'une liste ou d'un texte : `liste[1:3]`, `texte[:10]`.

**Set (ensemble)** — Une collection **sans doublons**, entre `{ }`. Utile pour dédupliquer.

**Syntaxe** — Les règles d'écriture du langage (où mettre les `:`, les guillemets…). Une
faute de syntaxe empêche le programme de démarrer.

**Traceback** — Le message d'erreur complet qu'affiche Python quand ça plante. Il se lit
**de bas en haut** pour trouver la cause. (Voir le module `07_debugger`.)

**Tuple** — Une liste **non modifiable**, entre parenthèses : `(48.85, 2.35)`.

**Type** — La nature d'une valeur : `int`, `float`, `str`, `bool`, `list`, `dict`…

**Variable** — Une boîte étiquetée qui retient une valeur : `age = 30`. Le `=` *range* la
valeur de droite dans la boîte de gauche.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
