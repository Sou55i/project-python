# Module 07 — Débugger : comprendre et corriger les erreurs

Une erreur, ce n'est **pas un échec** : c'est Python qui t'explique ce qui ne va pas.
Apprendre à **lire les erreurs** est sans doute la compétence qui fait le plus progresser
un débutant. Ce module est en grande partie théorique, avec un script qui te montre chaque
erreur en vrai.

> Fichier du module : `erreurs_frequentes.py` (déclenche chaque erreur volontairement,
> l'attrape, et t'explique sa cause + sa solution).

---

## 1. Lire un « traceback » (le message d'erreur)

Quand un programme plante, Python affiche un pavé rouge appelé **traceback**. Exemple :

```
Traceback (most recent call last):
  File "mon_script.py", line 8, in <module>
    resultat = 10 / age
ZeroDivisionError: division by zero
```

> 🔑 **La règle d'or : on lit un traceback DE BAS EN HAUT.**

- **La dernière ligne** est la plus importante : c'est le **type d'erreur** + un message.
  Ici : `ZeroDivisionError: division by zero` → « tu as divisé par zéro ».
- **Juste au-dessus**, Python te montre **la ligne de code fautive** (`resultat = 10 / age`)
  et **son numéro** (`line 8`). Tu sais donc exactement **où** regarder.

Donc : *quel* problème (dernière ligne) → *où* (les lignes au-dessus). C'est tout.

---

## 2. Les erreurs les plus fréquentes (cause → solution)

### `SyntaxError` — faute de grammaire
Tu as mal écrit quelque chose : un `:` oublié, une parenthèse non fermée, un `=` au lieu de
`==`. Le programme **ne démarre même pas**.
➡️ Relis la ligne indiquée, vérifie les `:`, les `()`, les `""`.

### `IndentationError` — mauvais décalage
Les espaces en début de ligne sont incohérents (le bloc d'un `if` n'est pas aligné).
➡️ Utilise **4 espaces** par niveau, sans mélanger tabulations et espaces.

### `NameError` — nom inconnu
Tu utilises une variable/fonction qui n'existe pas (encore). Souvent : faute de frappe, ou
variable créée **plus bas** que là où tu l'utilises.
➡️ Vérifie l'orthographe et que la variable est **définie AVANT** d'être utilisée.

### `TypeError` — mauvais type
Tu mélanges des types incompatibles, ex : `"5" + 5` (texte + nombre).
➡️ Convertis : `int("5") + 5`. Souvent lié à `input()` qui renvoie du texte.

### `ValueError` — bonne nature, mauvaise valeur
Le type est bon mais la valeur n'a pas de sens, ex : `int("bonjour")`.
➡️ Vérifie la donnée (l'utilisateur a-t-il vraiment tapé un nombre ?).

### `IndexError` — hors de la liste
Tu demandes `liste[5]` alors que la liste a moins de 6 éléments.
➡️ Rappelle-toi qu'on compte **à partir de 0** ; vérifie avec `len(liste)`.

### `KeyError` — clé absente
Tu demandes `dico["ville"]` mais cette clé n'existe pas.
➡️ Utilise `dico.get("ville", "valeur par défaut")` pour éviter le plantage.

### `ModuleNotFoundError` — bibliothèque non installée
`import requests` mais `requests` n'est pas installé.
➡️ `pip install requests` (voir module 06).

### `FileNotFoundError` — fichier introuvable
Tu ouvres un fichier qui n'existe pas (ou mauvais chemin).
➡️ Vérifie le chemin ; teste avec `Path(...).exists()`.

### `AttributeError` — méthode/attribut inexistant
Tu appelles `.truc()` sur un objet qui n'a pas ce `.truc()`, ex : `"texte".append(...)`.
➡️ Vérifie le type de l'objet et les méthodes qu'il propose réellement.

### `ZeroDivisionError` — division par zéro
➡️ Vérifie le diviseur avant : `if b != 0:`.

---

## 3. La méthode pour débugger calmement

1. **Ne panique pas, lis le message.** La réponse est presque toujours dedans.
2. **Repère le type d'erreur** (dernière ligne) et **la ligne fautive** (au-dessus).
3. **Affiche pour voir** : ajoute des `print(...)` juste avant la ligne qui plante pour
   inspecter les valeurs. C'est la technique de débogage la plus simple et la plus utilisée.
   ```python
   print("DEBUG age =", age, type(age))   # que vaut age, et de quel type ?
   ```
4. **Isole le problème** : commente des bouts de code pour réduire la zone à examiner.
5. **Cherche le message d'erreur exact** sur Internet : tu n'es jamais le premier à l'avoir.

---

## 4. Anticiper les erreurs avec `try / except`

Quand une erreur est **prévisible** (réseau coupé, fichier absent, saisie invalide), on
l'attrape pour réagir proprement au lieu de planter :

```python
try:
    age = int(input("Ton âge ? "))     # peut échouer si on tape "abc"
except ValueError:
    print("Ce n'est pas un nombre valide.")
```

> ⚠️ N'abuse pas du `try/except` pour **masquer** les bugs. Pendant l'apprentissage, il vaut
> souvent mieux **laisser planter** pour lire le traceback et comprendre — puis corriger la
> cause.

---

## ▶️ À toi de jouer

```bash
python3 python/automatisation/07_debugger/erreurs_frequentes.py
```

Le script déclenche chaque erreur courante, l'attrape, et affiche sa cause et sa solution.
Lis le code : pour chaque erreur, tu verras le bout de code qui la provoque.

➡️ Avec ça, plus aucun pavé rouge ne devrait te faire peur. 💪
