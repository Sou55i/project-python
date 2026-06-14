#!/usr/bin/env bash
#
# 🗺️ CHEMINEMENT DU SCRIPT
#   1. On CHARGE la bibliothèque lib_math.sh avec `source` (comme un import Python).
#      -> ses fonctions (additionner, est_pair, additionner_tout) deviennent dispo ici.
#   2. On CAPTURE le résultat d'une fonction qui affiche, avec $( ).         [façon (a)]
#   3. On TESTE le code de retour d'une fonction directement dans un if.     [façon (b)]
#   4. On passe PLUSIEURS arguments à une fonction grâce à "$@".
#
# Lance-moi depuis la racine du dépôt :
#   bash bash/08_fonctions_avancees/utiliser.sh

# --- 1. Charger la bibliothèque -------------------------------------------------------
# $0 = chemin de CE script ; dirname "$0" = son dossier. On cherche lib_math.sh À CÔTÉ
# de ce fichier, pour que le source marche quel que soit le dossier courant.
source "$(dirname "$0")/lib_math.sh"

echo "=== La bibliothèque lib_math.sh est chargée ==="
echo

# --- 2. Capturer une valeur renvoyée par echo, avec $( ) ------------------------------
total=$(additionner 7 5)          # additionner AFFICHE 12, $( ) le RANGE dans total
echo "additionner 7 5  ->  $total"

# --- 3. Tester un code de retour avec un if -------------------------------------------
# est_pair ne renvoie pas un nombre : elle renvoie 0 (vrai) ou 1 (faux), que le if teste.
for n in 10 7; do
    if est_pair "$n"; then
        echo "$n est pair"
    else
        echo "$n est impair"
    fi
done

# --- 4. Passer plusieurs arguments d'un coup ("$@" côté fonction) ---------------------
somme=$(additionner_tout 1 2 3 4 5)
echo "additionner_tout 1 2 3 4 5  ->  $somme"

echo
echo "✅ Terminé : on a réutilisé les fonctions de la bibliothèque sans les recopier."
