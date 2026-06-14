# 🃏 Aide-mémoire Bash (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `00_demarrer`, `01_les_bases` et suivants.

---

## Lancer un script

```bash
bash mon_script.sh        # lancer sans rien changer
chmod +x mon_script.sh    # rendre exécutable (une seule fois)
./mon_script.sh           # lancer directement (besoin du chmod)
```

La 1re ligne du fichier, le « shebang », dit quel programme l'exécute :

```bash
#!/usr/bin/env bash       # toujours en première ligne du script
```

## Afficher et commenter

```bash
echo "Bonjour"            # afficher une ligne
echo -n "sans retour"     # sans saut de ligne à la fin
printf "%s a %d ans\n" "$nom" "$age"   # affichage formaté
# ceci est un commentaire (ignoré par Bash)
```

## Variables

```bash
nom="Alice"               # PAS d'espace autour du = (nom = "x" échoue !)
age=30
echo "$nom"               # toujours entre guillemets : protège les espaces
echo "${nom}_suffixe"     # { } pour coller du texte juste après
chemin="$HOME/Documents"  # $HOME, $USER, $PWD : variables fournies par le système
```

## Demander une saisie (read)

```bash
read -p "Ton nom ? " nom         # affiche le message et lit la réponse
read -p "Mot de passe : " -s mdp # -s masque la saisie
read -r ligne                    # -r recommandé : ne casse pas les \
```

## Calcul (nombres entiers)

```bash
total=$(( 3 + 4 ))        # $(( ... )) pour calculer
n=$(( n + 1 ))            # incrémenter
echo $(( 10 % 3 ))        # reste (modulo) -> 1
echo $(( 2 ** 8 ))        # puissance -> 256
```

## Conditions [[ ]]

```bash
if [[ "$age" -ge 18 ]]; then
    echo "Majeur"
elif [[ "$age" -ge 13 ]]; then
    echo "Ado"
else
    echo "Enfant"
fi
```

```bash
# Nombres :  -eq  -ne  -lt  -le  -gt  -ge   (égal, différent, <, <=, >, >=)
# Texte   :  ==   !=                        (égal, différent)
# Fichiers:  -f fichier existe ?  -d dossier ?  -z chaîne vide ?  -e existe ?
[[ -f "notes.txt" ]] && echo "le fichier existe"
[[ -z "$nom" ]] && echo "nom vide"
```

## Boucles

```bash
for fruit in pomme kiwi banane; do   # do ... done encadre la boucle
    echo "$fruit"
done

for i in {1..5}; do                  # 1 2 3 4 5
    echo "$i"
done

while [[ "$n" -lt 10 ]]; do          # tant que la condition est vraie
    n=$(( n + 1 ))
done
```

## Fonctions

```bash
saluer() {
    echo "Bonjour $1 $2"   # $1, $2 = 1er, 2e argument reçus
}
saluer "Alice" "Martin"    # appel (arguments séparés par des espaces)

resultat=$( saluer "Bob" ) # $( ... ) capture ce qu'affiche la fonction
```

## Arguments du script

```bash
echo "$0"     # nom du script
echo "$1"     # premier argument ;  $2 le deuxième ...
echo "$@"     # tous les arguments
echo "$#"     # combien d'arguments
```

```bash
# Options avec getopts (ex : ./script.sh -n Alice -v)
while getopts "n:v" opt; do
    case "$opt" in
        n) nom="$OPTARG" ;;   # n: attend une valeur (dans $OPTARG)
        v) verbeux=1 ;;       # v est un simple drapeau
    esac
done
```

## Tableaux

```bash
# Indexé (numéroté à partir de 0)
fruits=(pomme kiwi banane)
echo "${fruits[0]}"          # premier élément
echo "${fruits[@]}"          # tous les éléments
echo "${#fruits[@]}"         # nombre d'éléments
fruits+=("orange")           # ajouter à la fin

# Associatif (clé -> valeur)
declare -A age                # déclaration obligatoire
age[alice]=30
echo "${age[alice]}"          # -> 30
for cle in "${!age[@]}"; do echo "$cle = ${age[$cle]}"; done
```

## Redirections

```bash
echo "ligne" > fichier.txt   # >  écrit (écrase le contenu)
echo "suite" >> fichier.txt  # >> ajoute à la fin
commande < fichier.txt       # <  lit le fichier comme saisie
cmd1 | cmd2                   # |  envoie la sortie de cmd1 dans cmd2
commande 2> erreurs.txt      # 2> capture les messages d'erreur

# Lire un fichier ligne par ligne
while read -r ligne; do
    echo "-> $ligne"
done < fichier.txt
```

## Traiter du texte

```bash
grep "motif" fichier.txt      # garder les lignes contenant "motif"
cut -d',' -f2 fichier.csv     # 2e colonne (séparateur virgule)
sort fichier.txt              # trier ;  sort -n pour des nombres
uniq                          # supprimer les doublons consécutifs
sed 's/ancien/nouveau/g'      # remplacer du texte
awk '{ print $1 }'            # afficher la 1re colonne de chaque ligne
sort fichier.txt | uniq -c    # trier puis compter chaque ligne
```

## Robustesse

```bash
set -euo pipefail   # à mettre en haut : stoppe à la 1re erreur,
                    # interdit les variables non définies, surveille les pipes

echo "$?"           # code de la dernière commande (0 = succès)
cmd1 && cmd2        # cmd2 seulement si cmd1 a réussi
cmd1 || cmd2        # cmd2 seulement si cmd1 a échoué

trap 'echo "nettoyage..."' EXIT   # exécuté quoi qu'il arrive à la sortie
```

## Bibliothèques (réutiliser du code)

```bash
source ./outils.sh   # charge les fonctions et variables d'un autre fichier
. ./outils.sh        # « . » est un raccourci pour source
```

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) et [ANATOMIE_D_UN_SCRIPT.md](./ANATOMIE_D_UN_SCRIPT.md).
