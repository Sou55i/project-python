# 📂 Module 04 : Exceptions & fichiers

> 🎯 **Objectif** : un vrai programme rencontre des imprévus (un fichier absent, une saisie
> invalide…) et manipule des données qui **survivent** à la fin du programme (les fichiers). Ce
> module t'apprend à **ne pas planter** au moindre souci et à **lire/écrire** des fichiers.

---

## 1. Les exceptions : quand le code rencontre un problème

Quand quelque chose se passe mal, Python **lève une exception** : il interrompt le programme et
affiche une erreur (le fameux « message rouge »). Une exception n'est **pas** un bug mystérieux :
c'est un signal précis. Apprends à le lire.

```
Traceback (most recent call last):
  File "script.py", line 3, in <module>
    resultat = 10 / nombre
ZeroDivisionError: division by zero
```

- La **dernière ligne** est la plus importante : le **type** (`ZeroDivisionError`) + l'explication.
- Juste au-dessus : le **fichier** et le **numéro de ligne** fautifs.

### Les types d'exceptions les plus courants

| Exception | Cause typique |
|-----------|---------------|
| `ValueError` | mauvaise valeur, ex. `int("abc")` |
| `ZeroDivisionError` | division par zéro |
| `TypeError` | mauvais type, ex. `"5" + 1` |
| `KeyError` | clé absente d'un dictionnaire |
| `IndexError` | index hors limites d'une liste |
| `FileNotFoundError` | fichier introuvable à l'ouverture |

---

## 2. Attraper une erreur : `try` / `except`

Plutôt que de laisser le programme s'arrêter, on **entoure** le code risqué d'un `try`, et on
prévoit quoi faire `except` (en cas d')erreur.

```python
try:
    nombre = int(input("Donne un nombre : "))   # peut lever ValueError
    resultat = 10 / nombre                       # peut lever ZeroDivisionError
    print(f"10 / {nombre} = {resultat}")
except ValueError:
    print("Ce n'est pas un nombre valide.")
except ZeroDivisionError:
    print("Impossible de diviser par zéro !")
```

Comment ça se lit :

- **`try:`** — « essaie d'exécuter ce bloc ».
- **`except XxxError:`** — « si CE type d'erreur survient, fais ça **au lieu** de planter ».
- Dès qu'une ligne du `try` échoue, Python **saute** directement au `except` correspondant ;
  le reste du `try` n'est pas exécuté.

> 🔑 **Sois précis sur le type attrapé.** Écrire `except ValueError` (et pas un `except:` nu qui
> attrape *tout*) est important : un `except:` trop large masque des bugs et rend le débogage
> impossible. N'attrape que les erreurs que tu sais traiter.

### `else` et `finally` (pour aller plus loin)

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("Fichier absent")
else:
    print("Ouverture réussie")   # s'exécute SEULEMENT si le try n'a pas planté
finally:
    print("Toujours exécuté")    # s'exécute TOUJOURS (erreur ou non) : nettoyage
```

> 🧠 **Le bon réflexe** : n'utilise `try/except` que là où une erreur est **attendue et
> récupérable** (saisie utilisateur, fichier réseau…). Ne l'utilise **pas** pour cacher une
> faute de logique — celle-là, il faut la corriger.

---

## 3. Lire et écrire des fichiers : `with open(...)`

Un fichier permet de **conserver** des données après la fin du programme. Pour le manipuler, on
utilise `open(...)`, presque toujours à l'intérieur d'un bloc **`with`**.

### Pourquoi `with` ?

`with` est un *gestionnaire de contexte* : il **referme automatiquement** le fichier à la sortie
du bloc, **même si une erreur survient**. Sans lui, un fichier oublié ouvert peut corrompre des
données ou bloquer des ressources.

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Salut Python !")
# ICI, hors du bloc, le fichier est déjà refermé proprement
```

Décortiquons `open("test.txt", "w", encoding="utf-8")` :

| Argument | Rôle |
|----------|------|
| `"test.txt"` | le **chemin** du fichier |
| `"w"` | le **mode** d'ouverture (voir table ci-dessous) |
| `encoding="utf-8"` | l'encodage : indispensable pour les accents. **Mets-le toujours.** |
| `as f` | range le fichier ouvert dans la variable `f` |

### Les modes d'ouverture

| Mode | Signification | Si le fichier existe déjà |
|------|---------------|---------------------------|
| `"r"` | **read** (lecture, défaut) | le lit ; **erreur** s'il n'existe pas |
| `"w"` | **write** (écriture) | ⚠️ **écrase tout** le contenu |
| `"a"` | **append** (ajout) | ajoute **à la fin**, sans effacer |
| `"x"` | création exclusive | **erreur** si le fichier existe déjà |

> ⚠️ Le mode `"w"` **vide le fichier** avant d'écrire. Pour compléter un journal (log) sans tout
> perdre, c'est `"a"` qu'il te faut.

### Lire un fichier : trois façons

```python
with open("test.txt", "r", encoding="utf-8") as f:
    contenu = f.read()          # TOUT le fichier en une seule chaîne

with open("test.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()      # une LISTE de lignes

with open("test.txt", "r", encoding="utf-8") as f:
    for ligne in f:             # ligne par ligne (idéal pour les gros fichiers : économe)
        print(ligne.strip())    # .strip() enlève le retour à la ligne et les espaces autour
```

> 🔎 **Pourquoi `.strip()` ?** Chaque ligne lue se termine par un caractère de retour à la ligne
> `\n`. `strip()` le retire pour un affichage propre.

---

## 4. Combiner les deux : lire un fichier sans planter s'il manque

C'est le cas réel typique — fichiers **et** exceptions ensemble :

```python
try:
    with open("config.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
    print("Configuration chargée.")
except FileNotFoundError:
    print("Aucune config trouvée, utilisation des valeurs par défaut.")
    contenu = ""
```

> 🧠 Ce motif — *« tente de lire, sinon valeur de repli »* — est le frère du patron de **repli
> (fallback)** vu dans [`../COMPRENDRE_LE_CODE.md`](../COMPRENDRE_LE_CODE.md). On l'utilise
> partout.

---

## 🏁 Exercices

1. **Lis et lance** [`fichiers.py`](./fichiers.py) (création + lecture d'un fichier de log).
2. **Provoque une erreur** volontairement (divise par zéro, ouvre un fichier inexistant) pour
   voir le `try/except` la capturer.
3. **Mini-journal** : écris un programme qui demande une phrase à l'utilisateur et l'**ajoute**
   (mode `"a"`) à un fichier `journal.txt`, puis affiche tout le contenu du journal.

<details>
<summary>💡 Solution — exercice 3 (mini-journal)</summary>

```python
phrase = input("Ton message : ")

with open("journal.txt", "a", encoding="utf-8") as f:   # "a" = ajout, ne pas écraser
    f.write(phrase + "\n")                              # \n = passe à la ligne suivante

print("--- Contenu du journal ---")
with open("journal.txt", "r", encoding="utf-8") as f:
    print(f.read())
```
</details>

➡️ **Prochaine étape** : [module 05 — la POO (classes)](../05_poo/).
