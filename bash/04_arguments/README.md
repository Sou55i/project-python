# Module 04 — Les arguments et options d'un script

Jusqu'ici, nos scripts demandaient les infos avec `read` (ils se mettaient en pause pour
te poser une question). Mais un « vrai » script de terminal, comme `git`, `ls` ou `cp`,
reçoit ses infos **directement sur la ligne de commande** :

```bash
cp  fichier.txt  copie.txt      # cp reçoit DEUX arguments : la source et la destination
ls  -l  /home                   # ls reçoit une OPTION (-l) et un argument (/home)
```

Ces mots écrits **après** le nom du script sont les **arguments**. Apprendre à les lire,
c'est rendre ton script **réutilisable** : au lieu de modifier le code à chaque fois, tu
changes juste ce que tu tapes après son nom.

> 💡 **Analogie.** Un script sans argument, c'est un distributeur qui ne vend qu'un seul
> produit. Avec des arguments, c'est un distributeur où **tu choisis** : tu appuies sur le
> bouton (le script) et tu indiques **ce que tu veux** (les arguments).

> 🐍 **Le lien avec Python.** C'est exactement le rôle de **`argparse`** (module 04 du
> parcours Python). En Bash, pas besoin de bibliothèque : le langage met les arguments à ta
> disposition tout seul, dans des variables spéciales `$1`, `$2`…

---

## 1. Les variables spéciales : `$0`, `$1`, `$2`…

Quand tu lances un script avec des arguments, Bash les range **automatiquement** dans des
variables numérotées :

```bash
bash mon_script.sh  pomme  banane  cerise
#         |           |       |       |
#        $0          $1      $2      $3
```

| Variable | Contient | Dans l'exemple |
|----------|----------|----------------|
| `$0` | **le nom du script** lui-même | `mon_script.sh` |
| `$1` | le **1er** argument | `pomme` |
| `$2` | le **2e** argument | `banane` |
| `$3` | le **3e** argument | `cerise` |

> 🔑 On utilise ces variables **comme n'importe quelle variable** : avec un `$` et entre
> guillemets, `"$1"`, `"$2"`… (même règle d'or qu'au module 01 : **toujours les guillemets**).

---

## 2. `$#` : combien d'arguments ai-je reçus ?

`$#` te donne le **nombre** d'arguments reçus (le `#` se lit « compte »). Très pratique
pour **vérifier** que l'utilisateur a bien fourni ce qu'il faut :

```bash
if [[ $# -lt 1 ]]; then
    echo "Erreur : il faut au moins un argument !"
    exit 1
fi
```

> 💡 `$0` (le nom du script) **n'est pas compté** dans `$#`. Avec `pomme banane cerise`,
> `$#` vaut **3**.

---

## 3. `$@` et l'importance de `"$@"` (entre guillemets)

`$@` représente **tous les arguments d'un coup** (« la liste complète »). C'est ce qu'on
parcourt dans une boucle `for` pour traiter chaque argument :

```bash
for a in "$@"; do
    echo "argument : $a"
done
```

> 🔑 **Pourquoi `"$@"` entre guillemets, c'est CRUCIAL.** Avec les guillemets, chaque
> argument reste **entier**, même s'il contient des espaces. Sans guillemets, un argument
> comme `"mon fichier.txt"` serait **découpé en deux** (`mon` et `fichier.txt`) — la même
> catastrophe qu'au module 01. **Écris donc toujours `"$@"`.**

---

## 4. `shift` : décaler les arguments

`shift` **jette le 1er argument** et décale tous les autres d'un cran : `$2` devient `$1`,
`$3` devient `$2`, etc. C'est comme une **file d'attente** où l'on fait avancer tout le monde
après avoir servi le premier.

```bash
echo "$1"     # premier argument
shift         # on le retire ; tout le monde avance
echo "$1"     # ce qui était $2 est maintenant $1
```

C'est utile pour **traiter les arguments un par un** dans une boucle `while [[ $# -gt 0 ]]`.

---

## 5. `getopts` : les **options** de type `-n valeur` et `-v`

Les arguments « positionnels » dépendent de leur **place**. Mais les outils du terminal
acceptent souvent des **options** repérées par un tiret, dans n'importe quel ordre :

```bash
mon_script.sh  -n Alice  -v        # -n attend une valeur (Alice) ; -v est un simple drapeau
```

Pour lire proprement ces options, Bash fournit **`getopts`**. On l'utilise dans une boucle
`while` :

```bash
while getopts "n:v" option; do
    case "$option" in
        n) nom="$OPTARG" ;;   # n: (avec deux-points) -> -n attend une VALEUR, rangée dans $OPTARG
        v) verbeux=1 ;;       # v (sans deux-points) -> simple drapeau on/off
        *) echo "Option inconnue" ; exit 1 ;;
    esac
done
```

Les deux points à retenir :
- La chaîne `"n:v"` liste les options acceptées. **Un `:` après une lettre = cette option
  attend une valeur** (`-n NOM`). **Sans `:` = c'est un simple drapeau** (`-v`, activé ou non).
- La valeur d'une option (le `Alice` de `-n Alice`) arrive dans la variable spéciale
  **`$OPTARG`**.

> 💡 **Valeur par défaut.** On donne une valeur à la variable **avant** la boucle. Si
> l'option n'est pas fournie, la valeur par défaut reste : `nom="inconnu"` puis, si `-n Alice`
> est passé, `nom` devient `Alice`.

---

## 🧩 Récapitulatif

| Élément | Rôle |
|---------|------|
| `$0` | le nom du script |
| `$1`, `$2`… | les arguments positionnels (selon leur place) |
| `$#` | le nombre d'arguments |
| `"$@"` | tous les arguments (toujours entre guillemets !) |
| `shift` | retirer le 1er argument et décaler les autres |
| `getopts` | lire les options `-n valeur` et les drapeaux `-v` |

---

## ▶️ À toi de jouer

Deux fichiers dans ce module : `arguments.sh` (les variables positionnelles) et `options.sh`
(les options avec `getopts`).

```bash
# arguments.sh : passe-lui autant de mots que tu veux
bash bash/04_arguments/arguments.sh un deux trois
bash bash/04_arguments/arguments.sh pomme

# essaie un argument AVEC un espace (les guillemets le gardent entier) :
bash bash/04_arguments/arguments.sh "mon fichier.txt" autre

# options.sh : -n attend un nom, -v active le mode verbeux
bash bash/04_arguments/options.sh -n Alice -v
bash bash/04_arguments/options.sh -n Bob          # sans -v
bash bash/04_arguments/options.sh                 # rien : la valeur par défaut s'applique
```

Modifie-les : ajoute un 4e argument à afficher, ou une nouvelle option `-c` dans `options.sh`.

➡️ La suite du parcours arrivera dans le même style.
