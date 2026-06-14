#!/usr/bin/env bash
#
# MODULE 01 - Mini-projet : une calculatrice en Bash
# ==================================================
# On combine read (saisie), les conditions et le calcul $(( )).
#
# Lance-le :  bash bash/01_les_bases/mini_calculatrice.sh
# Saisie simulée :  echo -e "+\n7\n5" | bash bash/01_les_bases/mini_calculatrice.sh
#
# 🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
#    1. Demander l'opération (+, -, *, /) avec read.
#    2. Demander les deux nombres avec read.
#    3. Choisir le calcul selon l'opération (if/elif/else).
#    4. Afficher le résultat.

# 1. ENTRÉE : read met le script en pause et range la saisie dans une variable.
read -p "Operation (+, -, *, /) : " op
read -p "Premier nombre  : " n1
read -p "Deuxieme nombre : " n2

# 2. TRAITEMENT : on compare l'opération (du TEXTE -> on utilise == et "...").
if [[ "$op" == "+" ]]; then
    resultat=$(( n1 + n2 ))
elif [[ "$op" == "-" ]]; then
    resultat=$(( n1 - n2 ))
elif [[ "$op" == "*" ]]; then
    resultat=$(( n1 * n2 ))
elif [[ "$op" == "/" ]]; then
    # On se protège de la division par zéro.
    if [[ "$n2" -eq 0 ]]; then
        echo "Erreur : division par zero impossible."
        exit 1                      # quitter avec un code d'erreur (≠ 0)
    fi
    resultat=$(( n1 / n2 ))         # ⚠️ division ENTIÈRE en Bash (10 / 3 = 3)
else
    echo "Operation inconnue."
    exit 1
fi

# 3. SORTIE : afficher le résultat.
echo "Resultat : $resultat"
