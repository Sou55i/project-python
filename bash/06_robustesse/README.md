# Module 06 — Écrire des scripts robustes (gestion des erreurs)

Jusqu'ici, nos scripts supposaient que **tout se passe bien**. Mais dans la vraie vie, un
fichier peut manquer, un dossier peut être protégé, une commande peut échouer… Un script
**robuste**, c'est un script qui **détecte les problèmes** et **réagit proprement** au lieu
de continuer comme si de rien n'était.

> 💡 Même pédagogie que partout : **on explique d'abord, on code ensuite.**
> Fichiers du module : `codes_retour.sh` (les briques) et `robuste.sh` (un script modèle).

---

## 1. Chaque commande renvoie un code de retour

> 🧠 **Analogie.** Imagine un employé à qui tu confies une tâche. Quand il a fini, il revient
> te voir et te dit soit « **c'est bon** » (tout s'est bien passé), soit « **ça a raté** »
> (et il y a plusieurs façons de rater). En Bash, c'est pareil : **chaque commande** te
> rapporte un petit numéro quand elle se termine, son **code de retour**.

La règle est simple, mais **contre-intuitive** au début :

- **`0` = succès** (« c'est bon »).
- **tout autre nombre = erreur** (1, 2, 127…). Le numéro précise *quel genre* d'erreur.

> 🔑 **Retiens bien : `0`, c'est la réussite.** L'inverse de ce qu'on croirait ! Vois `0`
> comme « zéro problème ».

Ce code est rangé dans une **variable spéciale : `$?`** (le point d'interrogation). Elle
contient toujours le code de la **toute dernière** commande exécutée :

```bash
ls /tmp
echo "$?"        # affiche 0  -> ls a réussi

ls /dossier_qui_nexiste_pas
echo "$?"        # affiche un nombre ≠ 0  -> ls a échoué
```

> ⚠️ `$?` change **à chaque commande**. Lis-le tout de suite, sinon il est déjà écrasé par
> la commande suivante (même un simple `echo` a son propre code de retour !).

---

## 2. Enchaîner selon le succès ou l'échec : `&&` et `||`

Plutôt que de tester `$?` à la main à chaque fois, Bash offre deux raccourcis très pratiques
pour enchaîner des commandes **selon le résultat** de la précédente :

- **`commande && suite`** → exécute `suite` **seulement si** `commande` a **réussi** (code 0).
  Lis-le « **ET ENSUITE** ».
- **`commande || secours`** → exécute `secours` **seulement si** `commande` a **échoué**.
  Lis-le « **SINON** ».

```bash
mkdir mon_dossier && echo "Dossier créé !"     # le echo ne s'affiche QUE si mkdir a réussi

cd /dossier_absent || echo "Impossible d'y aller"   # le echo s'affiche SI cd a échoué
```

> 🧠 **Analogie.** `&&` c'est « **range ta chambre ET ENSUITE tu auras un dessert** » (le
> dessert seulement si la chambre est rangée). `||` c'est « **sois à l'heure SINON tu seras
> puni** » (la punition seulement en cas d'échec).

---

## 3. Le trio magique : `set -euo pipefail`

On met souvent cette ligne **tout en haut** d'un script sérieux (juste après le shebang) :

```bash
set -euo pipefail
```

Elle active **trois protections** d'un coup. Décortiquons chaque option **une par une** :

### `-e` → quitte à la première erreur

Sans `-e`, si une commande échoue, Bash **continue** la ligne suivante comme si de rien
n'était (dangereux !). Avec `-e`, dès qu'une commande **échoue** (code ≠ 0), le script
**s'arrête immédiatement**.

> 🧠 **Analogie.** C'est le disjoncteur de la maison : à la première anomalie électrique, il
> **coupe tout** au lieu de laisser un incendie se propager.

### `-u` → interdit les variables non définies

Sans `-u`, utiliser une variable qui **n'existe pas** donne juste du **vide**, silencieusement.
C'est la source de bugs terribles (`rm -rf "$DOSSIER/"` quand `$DOSSIER` est vide efface… la
racine !). Avec `-u`, lire une variable **jamais définie** provoque une **erreur** et arrête
le script.

> 🧠 **Analogie.** C'est le correcteur qui souligne en rouge un mot que tu n'as **pas écrit** :
> il refuse de deviner à ta place.

### `-o pipefail` → détecte une erreur dans un pipe

Un **pipe** `a | b` enchaîne deux commandes (la sortie de `a` nourrit `b`). Par défaut, Bash
ne regarde que le code de la **dernière** (`b`). Donc si `a` échoue mais que `b` réussit, Bash
croit que **tout va bien** ! Avec `pipefail`, le pipe est considéré en **échec** dès qu'**une**
de ses commandes échoue.

> 🧠 **Analogie.** Une chaîne de montage : si le **premier** ouvrier rate sa pièce, le produit
> est défectueux, **même si** le dernier ouvrier a bien fait son travail.

> ✅ **À retenir :** `set -euo pipefail` transforme un script « optimiste » en script
> « méfiant » qui **s'arrête au premier vrai problème** au lieu de foncer dans le mur.

---

## 4. Renvoyer son propre code avec `exit N`

Ton script aussi peut **rendre un compte rendu** quand il se termine, avec `exit` :

```bash
exit 0     # « tout s'est bien passé » (succès)
exit 1     # « il y a eu un problème » (erreur)
```

C'est utile parce qu'**un autre script** (ou `&&` / `||`) pourra réagir à TON résultat. Par
convention : `exit 0` = succès, un nombre ≠ 0 = erreur. On accompagne toujours une sortie en
erreur d'un **message clair** pour l'utilisateur :

```bash
if [[ ! -f "$fichier" ]]; then
    echo "Erreur : le fichier $fichier est introuvable." >&2   # >&2 = canal des erreurs
    exit 1
fi
```

> 💡 `>&2` envoie le message sur la **sortie d'erreur** (et non la sortie normale). C'est la
> bonne habitude pour les messages d'erreur — mais ce n'est pas obligatoire pour débuter.

---

## 5. Nettoyer quoi qu'il arrive : `trap '...' EXIT`

Souvent un script crée un **fichier temporaire** pendant son travail. Problème : s'il s'arrête
en plein milieu (à cause d'une erreur, de `-e`…), ce fichier **traîne** et pollue le disque.

La commande **`trap`** dit à Bash : « quoi qu'il arrive, **avant de quitter**, exécute ce
ménage ». On l'attache à l'événement **`EXIT`** (= « au moment de sortir, peu importe la raison »).

```bash
trap 'rm -f "$fichier_temp"' EXIT
```

> 🧠 **Analogie.** C'est la **consigne de sortie** affichée près de la porte : « **en partant,
> éteins la lumière** ». Que tu partes content, pressé, ou parce qu'il y a une alarme incendie,
> la consigne s'applique **toujours**. Le `trap` est ton réflexe de sortie automatique.

L'intérêt : tu écris le ménage **une seule fois, au début**, et tu n'as plus à y penser. Même
si le script plante 10 lignes plus loin, le nettoyage **aura lieu**.

---

## 🛠️ Pour créer un fichier temporaire proprement : `mktemp`

`mktemp` crée un fichier temporaire avec un **nom unique** (pas de collision avec un autre
script) et te renvoie son chemin :

```bash
fichier_temp=$(mktemp)     # crée /tmp/tmp.XXXXXX et range son chemin dans la variable
```

Combiné avec `trap`, c'est la recette **propre** pour travailler avec un fichier jetable.

---

## ▶️ À toi de jouer

```bash
# Voir les codes de retour, && et || en action :
bash bash/06_robustesse/codes_retour.sh

# Lancer le script modèle robuste (il se termine proprement, code 0) :
bash bash/06_robustesse/robuste.sh
```

Lis les deux fichiers, puis **expérimente** : enlève le `set -e` et provoque une erreur pour
voir la différence, ou supprime le `trap` et observe le fichier temporaire qui reste.

➡️ La suite du parcours arrivera dans le même style.
