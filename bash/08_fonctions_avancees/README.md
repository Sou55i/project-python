# Module 08 — Fonctions avancées & bibliothèques de scripts

Tu sais déjà écrire une fonction (module [`01_les_bases`](../01_les_bases/)). On va
maintenant les rendre **propres** et surtout **réutilisables** : on apprendra à isoler les
variables d'une fonction, à « renvoyer » un résultat de deux façons, puis à ranger des
fonctions dans un fichier à part qu'on **importe** dans plusieurs scripts.

> 💡 Même pédagogie que partout : **on explique d'abord, on code ensuite.**
> Fichiers du module : `lib_math.sh` (une petite **bibliothèque** de fonctions) et
> `utiliser.sh` (un script qui s'en sert).

---

## 1. Les variables `local` : ne pas polluer le reste du script

Par défaut, **toute** variable créée dans une fonction est **globale** : elle existe encore
**après** la fonction, et elle peut **écraser** une variable du même nom utilisée ailleurs.
C'est une énorme source de bugs.

```bash
resultat="important"      # une variable du script principal

calculer() {
    resultat=42           # ⚠️ SANS local : on écrase la variable d'au-dessus !
}

calculer
echo "$resultat"          # affiche 42… on a perdu "important" !
```

La solution : déclarer la variable avec **`local`** à l'intérieur de la fonction. Elle
n'existe alors **que** le temps de la fonction, puis disparaît.

```bash
resultat="important"

calculer() {
    local resultat=42     # ✅ AVEC local : cette variable reste DANS la fonction
}

calculer
echo "$resultat"          # affiche "important" : la fonction n'a rien cassé
```

> 🧠 **Analogie.** Une fonction, c'est comme une **cuisine de restaurant**. Avec `local`, ce
> qui se passe en cuisine (les ingrédients, le désordre) **reste en cuisine** : la salle (le
> reste du script) n'est pas dérangée. Sans `local`, la cuisine déborde dans la salle.

> ✅ **Règle d'or :** déclare **toujours** en `local` les variables internes à tes fonctions.

---

## 2. « Renvoyer » un résultat : deux façons bien distinctes

En Bash, une fonction ne renvoie pas une valeur comme `return x` en Python. Il y a **deux
mécanismes différents**, pour **deux usages différents**. Ne les confonds pas !

### (a) Afficher avec `echo`, capturer avec `$( )`

Pour renvoyer une **donnée** (un nombre, un texte), la fonction l'**affiche** avec `echo`, et
l'appelant la **capture** avec `$( ... )` (la « substitution de commande », déjà vue pour
ranger le résultat d'une commande dans une variable).

```bash
additionner() {
    local somme=$(( $1 + $2 ))
    echo "$somme"             # on AFFICHE le résultat
}

total=$(additionner 7 5)      # on CAPTURE ce qui a été affiché
echo "Total : $total"         # Total : 12
```

> 🧠 **Analogie.** La fonction **écrit sa réponse sur un papier** (`echo`) et te le tend ;
> `$( )` c'est **ta main qui attrape le papier** pour lire la réponse.

### (b) Le code de retour `return N`, testé avec `$?`

Pour renvoyer un **verdict** (vrai/faux, réussi/raté), la fonction utilise **`return N`** où
`N` est un entier de **0 à 255**. Comme partout en Bash : **`0` = succès / vrai**, tout autre
nombre = échec / faux (revois le module [`06_robustesse`](../06_robustesse/)).

```bash
est_pair() {
    if (( $1 % 2 == 0 )); then
        return 0              # 0 = "oui, c'est pair" (vrai)
    else
        return 1              # 1 = "non" (faux)
    fi
}

est_pair 10
echo "$?"                     # 0  -> 10 est pair
```

Le code de retour se lit dans la variable spéciale **`$?`**, mais le plus lisible est de
mettre l'appel **directement dans un `if`** (qui teste justement le code de retour) :

```bash
if est_pair 10; then
    echo "10 est pair"
else
    echo "10 est impair"
fi
```

> ⚠️ **Ne mélange pas les deux !** `return` ne sert **pas** à renvoyer un nombre calculé
> (il est limité à 0–255 et signifie « succès/échec »). Pour renvoyer une **valeur**, utilise
> `echo` + `$( )`. Pour renvoyer un **oui/non**, utilise `return` + `if`.

| Tu veux renvoyer… | Méthode | Tu récupères avec… |
|-------------------|---------|--------------------|
| une **donnée** (nombre, texte) | `echo "$x"` | `var=$( ma_fonction )` |
| un **verdict** (vrai/faux) | `return 0` / `return 1` | `if ma_fonction; then …` (ou `$?`) |

---

## 3. Les bibliothèques : réutiliser du code avec `source`

Quand tu écris une fonction utile (additionner, vérifier un fichier…), tu n'as pas envie de la
**recopier** dans chaque script. La bonne pratique : la ranger **une fois** dans un fichier à
part — une **bibliothèque** — puis la **charger** là où tu en as besoin.

On charge un fichier avec **`source fichier.sh`** (ou sa version courte **`. fichier.sh`**, un
simple point). Cela exécute le fichier **dans le script courant** : toutes ses fonctions et
variables deviennent disponibles, comme si tu les avais écrites sur place.

```bash
source lib_math.sh        # charge les fonctions définies dans lib_math.sh
# . lib_math.sh           # exactement pareil (le point = source)

total=$(additionner 7 5)  # on peut maintenant utiliser SES fonctions
```

> 🧠 **Analogie.** C'est exactement l'**`import` de Python** : `import math` te donne accès aux
> fonctions du module `math`. Ici, `source lib_math.sh` te donne accès aux fonctions de ta
> bibliothèque. Tu écris la fonction une fois, tu la réutilises partout.

> 🔑 **`source` n'est PAS `bash fichier.sh`.** `bash fichier.sh` lance le fichier dans un
> **nouveau** shell séparé : tu ne récupères **rien** ensuite. `source` au contraire **fusionne**
> le contenu dans ton script. Pour une bibliothèque, c'est bien `source` qu'il faut.

### Attention au chemin du fichier source

`source lib_math.sh` ne fonctionne que si tu lances le script **depuis le bon dossier**. Pour
que ça marche **quel que soit le dossier courant**, on construit le chemin à partir de
l'emplacement du script lui-même, avec `$(dirname "$0")` (`$0` = chemin du script lancé,
`dirname` = son dossier) :

```bash
source "$(dirname "$0")/lib_math.sh"   # cherche lib_math.sh À CÔTÉ du script
```

---

## 4. Bonus : `"$@"` pour transmettre tous les arguments

À l'intérieur d'une fonction, **`$1`, `$2`…** sont ses arguments (comme vu au module 01).
**`"$@"`** (avec les guillemets) représente **tous les arguments d'un coup**. Pratique pour
**relayer** ce qu'on a reçu à une autre fonction ou commande :

```bash
afficher_tout() {
    for arg in "$@"; do        # parcourt CHAQUE argument reçu
        echo "- $arg"
    done
}

afficher_tout pomme banane cerise
```

> 💡 Mets toujours `"$@"` **entre guillemets** : sinon les arguments contenant un espace sont
> découpés (le même piège que pour les variables, module 01).

---

## ▶️ À toi de jouer

```bash
# lib_math.sh ne fait RIEN tout seul (que des définitions) ; on lance le script qui l'utilise :
bash bash/08_fonctions_avancees/utiliser.sh
```

Lis d'abord `lib_math.sh` (la bibliothèque), puis `utiliser.sh` (qui la `source`). Ensuite
**expérimente** : ajoute une fonction `multiplier` dans `lib_math.sh` et sers-t'en dans
`utiliser.sh` — tu verras, tu n'auras qu'à l'appeler, elle est déjà « importée ».

➡️ La suite du parcours arrivera dans le même style.
