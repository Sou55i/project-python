# 📖 Glossaire — les mots du Bash expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**Argument positionnel** (`$1`, `$2`, …) — Les valeurs que tu passes à un script ou à une
fonction. `$1` est la première, `$2` la deuxième… `$@` les contient toutes, et `$#` dit
combien il y en a. Comme les ingrédients que tu tends à une recette.

**Arrière-plan** (`&`) — Mettre `&` à la fin d'une commande la lance « en fond » : le
terminal te rend la main tout de suite, sans attendre qu'elle finisse. Pratique pour les
tâches longues.

**awk** — Un mini-langage pour traiter du texte en colonnes. Ex : `awk '{print $2}'` affiche
la 2ᵉ colonne de chaque ligne. Idéal pour les fichiers bien rangés en colonnes.

**Bash** — Le shell le plus répandu sous Linux et Mac. C'est le programme qui lit tes
commandes et les exécute. Son nom vient de *Bourne Again SHell*.

**Boucle** — Une instruction qui répète des actions : `for` (« pour chaque… ») ou `while`
(« tant que… »). C'est le cœur de l'automatisation.

**Code de retour** (`$?`) — Chaque commande laisse un numéro en partant : `0` = tout s'est
bien passé, autre chose = il y a eu un souci. `$?` te donne ce numéro de la dernière
commande. Comme un bulletin de notes après chaque action.

**Commande** — Un mot que tu tapes pour demander une action : `ls`, `cd`, `echo`… Souvent
suivi d'options et d'arguments.

**Condition** (`[[ ... ]]`) — Un test qui oriente le programme avec `if`, `elif`, `else`.
La forme moderne en Bash s'écrit entre doubles crochets : `if [[ -f fichier ]]; then …`.

**Descripteur** (*stdin* / *stdout* / *stderr*) — Les trois « tuyaux » d'un programme :
l'entrée (stdin, n°0, ce qu'on lui donne), la sortie normale (stdout, n°1) et la sortie
des erreurs (stderr, n°2). Les séparer permet de trier les messages utiles des erreurs.

**echo** — La commande qui affiche du texte à l'écran : `echo "Bonjour"`. L'équivalent du
`print` de Python.

**Expansion** (`$`) — Le `$` devant un nom dit à Bash : « remplace ceci par sa valeur ».
`$nom` devient le contenu de la variable `nom`. C'est comme déballer le contenu d'une boîte.

**exit** — La commande qui termine le script tout de suite. On peut donner un code :
`exit 0` (succès) ou `exit 1` (erreur).

**Fonction** — Un bloc de code nommé et réutilisable : `saluer() { echo "Salut $1"; }`.
Comme une recette qu'on peut refaire à volonté. On l'appelle par son nom : `saluer Alice`.

**getopts** — Un outil intégré pour lire proprement les options d'un script (`-v`, `-f mon.txt`…).
Évite de bricoler à la main l'analyse des `-` que l'utilisateur tape.

**grep** — La commande qui cherche un motif dans du texte et affiche les lignes qui
correspondent : `grep "erreur" journal.txt`. Comme un surligneur qui ne garde que ce qui
t'intéresse.

**Guillemets** (simples vs doubles) — Les doubles `"..."` protègent le texte mais laissent
le `$` faire son travail (`"Bonjour $nom"` insère la variable). Les simples `'...'`
protègent **tout**, sans rien remplacer (`'$nom'` reste littéralement `$nom`).

**Pipe** (`|`) — La barre verticale branche la sortie d'une commande sur l'entrée de la
suivante : `ls | grep .txt`. Comme un tuyau qui fait couler le résultat de l'une dans
l'autre.

**Redirection** (`>` `>>` `<`) — Détourne les tuyaux : `> fichier` écrit la sortie dans un
fichier (en l'écrasant), `>>` ajoute à la fin sans effacer, `< fichier` envoie un fichier
en entrée. Comme rediriger l'eau vers un autre bac.

**Script** — Un fichier texte qui contient une suite de commandes, qu'on exécute d'un coup
au lieu de les taper une par une.

**sed** — Un outil pour transformer du texte automatiquement, surtout pour
chercher-remplacer : `sed 's/chat/chien/' fichier`. Comme un « rechercher-remplacer » en
ligne de commande.

**set -euo pipefail** — Une ligne de sécurité à mettre en haut d'un script : `-e` arrête au
premier échec, `-u` interdit les variables non définies, `-o pipefail` détecte une erreur
même au milieu d'un pipe. Comme une ceinture de sécurité pour ton script.

**Shebang** (`#!/usr/bin/env bash`) — La toute première ligne d'un script. Elle indique
quel programme doit l'exécuter. Le mot vient de `#` (*sharp/hash*) + `!` (*bang*).

**Shell** — Le programme qui sert d'intermédiaire entre toi et le système : il lit tes
commandes et les fait exécuter. Bash est un shell parmi d'autres (zsh, sh…).

**shellcheck** — Un outil qui relit ton script et te signale les erreurs et les
maladresses **avant** de l'exécuter. Comme un correcteur orthographique pour le Bash.

**source** — La commande qui exécute un fichier **dans le shell courant** (au lieu d'en
ouvrir un nouveau) : `source config.sh`. Utile pour charger des variables ou des fonctions.
S'écrit aussi avec un point : `. config.sh`.

**Substitution de commande** (`$( )`) — Met le **résultat** d'une commande dans une variable
ou un texte : `aujourdhui=$(date)`. Bash exécute ce qui est entre `$( )` et le remplace par
sa sortie.

**$(( ))** (arithmétique) — Les doubles parenthèses font des calculs sur des nombres :
`echo $(( 2 + 3 ))` affiche `5`. C'est la calculette intégrée de Bash.

**Tableau** (indexé / associatif) — Une variable qui range **plusieurs** valeurs. L'indexé
les numérote à partir de 0 : `fruits=(pomme poire)`, et `${fruits[0]}` vaut `pomme`.
L'associatif les range par étiquette (clé → valeur), comme un dictionnaire.

**Terminal** — La fenêtre noire (ou son onglet) où tu tapes des commandes. C'est juste
l'endroit où le shell discute avec toi.

**test** (`-f` / `-d` / `-z`) — Des petites vérifications utilisées dans les conditions :
`-f` (« est-ce un fichier ? »), `-d` (« est-ce un dossier ? »), `-z` (« cette chaîne
est-elle vide ? »). Ex : `if [[ -d /tmp ]]; then …`.

**trap** — Une instruction qui dit : « si tel signal arrive (ex : Ctrl-C ou la fin du
script), exécute d'abord ce code ». Sert souvent à nettoyer les fichiers temporaires avant
de quitter. Comme un filet de sécurité posé à l'avance.

**Variable** — Une boîte étiquetée qui retient une valeur : `age=30` (⚠️ **pas d'espace**
autour du `=`). On range avec `nom=valeur` et on relit avec `$nom`.

**wait** — La commande qui dit au script « attends que les tâches lancées en arrière-plan
(`&`) soient finies avant de continuer ». Comme attendre tout le monde avant de partir.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
