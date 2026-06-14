#!/usr/bin/env bash
#
# lib_math.sh — une petite BIBLIOTHÈQUE de fonctions mathématiques.
#
# ⚠️ Ce fichier ne FAIT rien tout seul : il ne contient QUE des définitions de fonctions.
#    On ne le lance pas directement. On le CHARGE depuis un autre script avec :
#
#        source "$(dirname "$0")/lib_math.sh"
#
#    C'est l'équivalent d'un "import" en Python : ça rend les fonctions ci-dessous
#    disponibles dans le script qui fait le source. (Voir utiliser.sh pour un exemple.)


# additionner — renvoie la SOMME de deux nombres.
# Façon (a) : on AFFICHE le résultat avec echo ; l'appelant le capture avec $( ).
additionner() {
    local a=$1                 # local : ces variables n'existent QUE dans la fonction
    local b=$2                 #         (elles ne polluent pas le script appelant)
    local somme=$(( a + b ))   # le calcul entier va dans $(( ))
    echo "$somme"              # on AFFICHE le résultat -> capturable avec $( )
}


# est_pair — dit si un nombre est PAIR ou non.
# Façon (b) : on renvoie un CODE DE RETOUR (0 = vrai/oui, 1 = faux/non),
#             testable avec un if ou via $?.
est_pair() {
    local n=$1                 # le nombre à tester, rangé en local
    if (( n % 2 == 0 )); then  # reste de la division par 2 ; (( )) = calcul entier
        return 0               # 0 = "oui, il est pair" (succès / vrai en Bash)
    else
        return 1               # 1 = "non" (échec / faux)
    fi
}


# additionner_tout — fait la somme de TOUS les arguments reçus (autant qu'on veut).
# Montre l'usage de "$@" (= tous les arguments) pour les parcourir un par un.
additionner_tout() {
    local total=0
    for nombre in "$@"; do     # "$@" : chaque argument passé à la fonction
        total=$(( total + nombre ))
    done
    echo "$total"              # on AFFICHE la somme finale
}
