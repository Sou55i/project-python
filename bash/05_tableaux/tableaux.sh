#!/usr/bin/env bash
#
# MODULE 05 - Les tableaux INDEXES en Bash
# ========================================
# Illustre, dans l'ordre : creer un tableau, l'afficher, connaitre sa taille,
# ajouter un element, puis le parcourir.
#
# Lance-le :  bash bash/05_tableaux/tableaux.sh

# ─────────────────────────────────────────────
# 1. CREER UN TABLEAU INDEXE
#    Valeurs entre parentheses, separees par des ESPACES (pas de virgules !)
# ─────────────────────────────────────────────
fruits=(pomme banane cerise)

# ─────────────────────────────────────────────
# 2. ACCEDER A UN ELEMENT : on compte a partir de 0 !
#    Les accolades ${ ... } sont OBLIGATOIRES pour les tableaux.
# ─────────────────────────────────────────────
echo "Premier fruit (indice 0) : ${fruits[0]}"   # pomme
echo "Deuxieme fruit (indice 1) : ${fruits[1]}"  # banane

# ─────────────────────────────────────────────
# 3. AFFICHER TOUS LES ELEMENTS : le @ veut dire "tous les casiers"
#    On garde les guillemets pour proteger les espaces eventuels.
# ─────────────────────────────────────────────
echo "Tous les fruits : ${fruits[@]}"

# ─────────────────────────────────────────────
# 4. LA TAILLE : le # devant le nom veut dire "combien y en a-t-il ?"
# ─────────────────────────────────────────────
echo "Nombre de fruits : ${#fruits[@]}"          # 3

# ─────────────────────────────────────────────
# 5. AJOUTER UN ELEMENT A LA FIN avec +=
# ─────────────────────────────────────────────
fruits+=(kiwi)
echo "Apres ajout de kiwi : ${fruits[@]}"
echo "Nouveau nombre de fruits : ${#fruits[@]}"  # 4

# ─────────────────────────────────────────────
# 6. PARCOURIR LE TABLEAU avec une boucle for
#    On boucle sur TOUS les elements ("${fruits[@]}").
# ─────────────────────────────────────────────
echo "Liste des fruits :"
for f in "${fruits[@]}"; do
    echo "- $f"
done
