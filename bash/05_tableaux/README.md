# Module 05 — Les tableaux en Bash

Jusqu'ici, une variable rangeait **une seule** valeur (`nom="Alice"`). Mais souvent, on veut
ranger **plusieurs** valeurs ensemble : une liste de courses, des notes, des noms… C'est le
rôle des **tableaux**.

> 💡 Même pédagogie que partout : **on explique d'abord, on code ensuite.**
> Fichiers du module : `tableaux.sh` (tableaux indexés) et `associatifs.sh` (tableaux associatifs).

---

## 🧠 L'analogie : une boîte à plusieurs casiers

Une variable normale, c'est **une boîte** avec **une étiquette** et **une seule** chose dedans.

Un **tableau**, c'est une **commode** : une seule étiquette (le nom du tableau), mais **plusieurs
casiers** numérotés, chacun contenant une valeur. On ouvre le casier qu'on veut grâce à son
**numéro**.

---

## 1. Les TABLEAUX INDEXÉS (rangés par numéro)

### Créer un tableau

On met les valeurs entre **parenthèses**, séparées par des **espaces** (⚠️ pas de virgules !) :

```bash
fruits=(pomme banane cerise)
```

### Accéder à un élément : on compte à partir de 0 !

Chaque casier a un **numéro** appelé **indice**. Surprise classique du débutant :
**on compte à partir de 0**, pas de 1.

```bash
echo "${fruits[0]}"    # pomme   (le 1er casier)
echo "${fruits[1]}"    # banane  (le 2e casier)
echo "${fruits[2]}"    # cerise  (le 3e casier)
```

> 🔑 Les **accolades** `${ ... }` sont **obligatoires** pour les tableaux. Sans elles, Bash ne
> comprend pas l'indice entre crochets.

### Tous les éléments d'un coup

```bash
echo "${fruits[@]}"    # pomme banane cerise
```

Le `@` veut dire « **tous les casiers** ». **Garde les guillemets** : ils protègent les
valeurs qui contiennent des espaces.

### Le nombre d'éléments (la taille)

```bash
echo "${#fruits[@]}"   # 3
```

Le `#` devant le nom veut dire « **combien y en a-t-il ?** ».

### Ajouter un élément à la fin

```bash
fruits+=(kiwi)         # le tableau devient : pomme banane cerise kiwi
```

Le `+=` ajoute **à la suite**, sans toucher aux casiers existants.

### Parcourir le tableau avec une boucle `for`

```bash
for f in "${fruits[@]}"; do
    echo "- $f"
done
```

C'est exactement la boucle `for` du Module 01, mais nourrie par **tous les éléments** du tableau.

### 🐍 Comparaison avec Python

C'est l'équivalent des **listes** Python :

| | Python | Bash |
|--|--------|------|
| Créer | `fruits = ["pomme", "banane", "cerise"]` | `fruits=(pomme banane cerise)` |
| 1er élément (indice 0) | `fruits[0]` | `"${fruits[0]}"` |
| Tous les éléments | `fruits` | `"${fruits[@]}"` |
| La taille | `len(fruits)` | `"${#fruits[@]}"` |
| Ajouter à la fin | `fruits.append("kiwi")` | `fruits+=(kiwi)` |
| Parcourir | `for f in fruits:` | `for f in "${fruits[@]}"; do` |

---

## 2. Les TABLEAUX ASSOCIATIFS (les dictionnaires)

Parfois, numéroter les casiers ne suffit pas : on veut ranger une valeur sous un **nom** plutôt
que sous un **numéro**. Exemple : l'âge de chaque personne (`alice → 30`, `bob → 25`).

C'est un **tableau associatif** : à la place des indices `0, 1, 2…`, on utilise des **clés** (du
texte) qui pointent vers des **valeurs**. En Python, ça s'appelle un **dictionnaire**.

### Le déclarer d'abord avec `declare -A`

⚠️ Contrairement aux tableaux indexés, un tableau associatif **doit être annoncé** avant usage,
avec `declare -A` (le `-A` veut dire *Associative*) :

```bash
declare -A age
```

### Remplir et lire

```bash
age[alice]=30          # la clé "alice" pointe vers 30
age[bob]=25            # la clé "bob"   pointe vers 25

echo "${age[alice]}"   # 30   (on lit par la clé, pas par un numéro)
```

### Parcourir les clés

Pour obtenir **toutes les clés**, on ajoute un **`!`** : `${!age[@]}`.

```bash
for prenom in "${!age[@]}"; do
    echo "$prenom a ${age[$prenom]} ans"
done
```

- `"${!age[@]}"` = **toutes les clés** (alice, bob…).
- `"${age[$prenom]}"` = la **valeur** rangée sous la clé courante.

> 💡 L'ordre des clés n'est **pas garanti** : un tableau associatif ne respecte pas forcément
> l'ordre dans lequel tu as ajouté les éléments. C'est normal.

### 🐍 Comparaison avec Python

C'est l'équivalent des **dictionnaires** Python :

| | Python | Bash |
|--|--------|------|
| Déclarer | `age = {}` | `declare -A age` |
| Ajouter / modifier | `age["alice"] = 30` | `age[alice]=30` |
| Lire par la clé | `age["alice"]` | `"${age[alice]}"` |
| Toutes les clés | `age.keys()` | `"${!age[@]}"` |
| Parcourir | `for k in age:` | `for k in "${!age[@]}"; do` |

---

## ▶️ À toi de jouer

```bash
bash bash/05_tableaux/tableaux.sh
bash bash/05_tableaux/associatifs.sh
```

Lis les deux fichiers, puis **modifie-les** : ajoute des fruits, change les indices, crée ton
propre annuaire (prénom → numéro de téléphone) avec un tableau associatif.

➡️ La suite du parcours arrivera dans le même style.
