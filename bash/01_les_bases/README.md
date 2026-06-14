# Module 01 — Les bases du Bash

Les mêmes briques que partout (variables, conditions, boucles, fonctions), mais avec les
**règles bien particulières** de Bash — notamment : **les espaces comptent**, et **les
guillemets sont essentiels**.

> Fichiers du module : `bases.sh` (les briques) et `mini_calculatrice.sh` (un mini-projet).
> Lance-les avec `bash <fichier>` (voir en bas).

---

## 1. Les variables : attention aux espaces !

On crée une variable avec `=`, **sans aucun espace autour** :

```bash
nom="Alice"      # ✅ correct
age=30           # ✅ correct
# nom = "Alice"  # ❌ ERREUR : bash croirait que "nom" est une commande !
```

Pour **utiliser** la valeur, on met un **`$`** devant le nom, et on l'entoure de
**guillemets doubles** :

```bash
echo "Bonjour $nom, tu as $age ans"
```

> 🔑 **Pourquoi les guillemets ?** Sans eux, Bash « découpe » la valeur sur les espaces, ce
> qui casse tout dès qu'une variable contient un espace (un nom de fichier `mon fichier.txt`,
> par exemple). **Règle d'or du débutant : mets TOUJOURS tes variables entre `"..."`.**

On peut aussi écrire `${nom}` (avec accolades) : utile pour coller du texte juste après,
comme `${nom}_sauvegarde`.

---

## 2. Lire une saisie avec `read`

`read` est l'équivalent de `input()` en Python : il met le script en pause et range ce que
tu tapes dans une variable.

```bash
read -p "Comment t'appelles-tu ? " prenom
echo "Enchante, $prenom !"
```

- `-p "..."` affiche un message (le *prompt*) avant de lire.
- Ce que l'utilisateur tape est rangé dans la variable `prenom` (sans `$` au moment du `read`,
  avec `$` quand on la réutilise).

---

## 3. Le calcul : tout est texte par défaut !

⚠️ Surprise : pour Bash, `age=30` est plutôt du **texte**. Pour faire un **calcul**, il faut
l'entourer de **`$(( ))`** (doubles parenthèses) :

```bash
a=7
b=5
echo $(( a + b ))      # affiche 12
somme=$(( a + b ))     # ou on range le résultat dans une variable
```

À l'intérieur de `$(( ))`, on peut écrire `+ - * / %` et même se passer du `$` devant les
variables. C'est **uniquement** pour les nombres entiers (Bash ne gère pas les décimaux nativement).

---

## 4. Les conditions : `if` et les crochets `[[ ]]`

```bash
note=12
if [[ $note -ge 16 ]]; then
    echo "Tres bien"
elif [[ $note -ge 10 ]]; then
    echo "Recu"
else
    echo "A retravailler"
fi
```

Points à retenir :
- La condition va entre **`[[ ... ]]`**, avec **des espaces à l'intérieur** des crochets.
- Le bloc commence après **`then`** et se ferme par **`fi`** (« if » à l'envers !).

Les **opérateurs** dépendent de ce qu'on compare :

| Comparaison | Pour les **nombres** | Pour le **texte** |
|-------------|----------------------|-------------------|
| égal | `-eq` | `==` |
| différent | `-ne` | `!=` |
| supérieur | `-gt` | — |
| supérieur ou égal | `-ge` | — |
| inférieur / inf. ou égal | `-lt` / `-le` | — |

On peut aussi tester des fichiers : `-f fichier` (existe et est un fichier), `-d dossier`,
`-z "$x"` (la variable est vide).

---

## 5. Les boucles : `for` et `while`

```bash
# for : parcourir une liste de valeurs
for fruit in pomme banane cerise; do
    echo "- $fruit"
done

# parcourir une plage de nombres avec {1..3}
for i in {1..3}; do
    echo "Tour $i"
done

# while : tant que la condition est vraie
compteur=0
while [[ $compteur -lt 3 ]]; do
    echo "compteur = $compteur"
    compteur=$(( compteur + 1 ))   # sans ça : boucle infinie !
done
```

Comme pour `if`, le corps de la boucle va entre **`do`** et **`done`**.

---

## 6. Les fonctions

```bash
saluer() {
    # $1 est le PREMIER argument reçu par la fonction, $2 le deuxième, etc.
    echo "Bonjour $1 !"
}

saluer "Alice"     # on appelle la fonction en passant un argument
saluer "Bob"
```

En Bash, une fonction ne « retourne » pas une valeur comme en Python : le plus simple est de
faire afficher (`echo`) son résultat, et de le récupérer avec `$( ... )` :

```bash
resultat=$(saluer "Alice")
```

> 💡 `$1`, `$2`… sont les **arguments**. C'est valable aussi pour le script entier :
> `$1` est le 1er argument passé sur la ligne de commande.

---

## ▶️ À toi de jouer

```bash
bash bash/01_les_bases/bases.sh

# La calculatrice attend une opération et deux nombres (simulation possible) :
echo -e "+\n7\n5" | bash bash/01_les_bases/mini_calculatrice.sh
```

Lis les deux fichiers, puis **modifie-les** : ajoute une opération, change les conditions,
crée ta propre fonction.

➡️ La suite du parcours (fichiers, arguments, projets…) arrivera dans le même style.
