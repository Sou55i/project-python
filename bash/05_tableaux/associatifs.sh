#!/usr/bin/env bash
#
# MODULE 05 - Les tableaux ASSOCIATIFS en Bash (les "dictionnaires")
# =================================================================
#
# 🗺️ CHEMINEMENT DU SCRIPT
#   1. On DECLARE un tableau associatif avec declare -A (obligatoire).
#   2. On le REMPLIT : chaque cle (un prenom) pointe vers une valeur (un age).
#   3. On LIT une valeur grace a sa cle (et pas grace a un numero).
#   4. On AJOUTE une nouvelle paire cle -> valeur.
#   5. On PARCOURT toutes les cles avec "${!age[@]}" pour afficher cle ET valeur.
#
# Lance-le :  bash bash/05_tableaux/associatifs.sh

# ─────────────────────────────────────────────
# 1. DECLARER : un tableau associatif DOIT etre annonce avec declare -A
#    (-A = Associative). Sans ca, Bash le traiterait comme un tableau indexe.
# ─────────────────────────────────────────────
declare -A age

# ─────────────────────────────────────────────
# 2. REMPLIR : la cle (du texte) pointe vers une valeur
# ─────────────────────────────────────────────
age[alice]=30          # la cle "alice" pointe vers 30
age[bob]=25            # la cle "bob"   pointe vers 25

# ─────────────────────────────────────────────
# 3. LIRE par la cle (et non par un numero d'indice)
# ─────────────────────────────────────────────
echo "Alice a ${age[alice]} ans"
echo "Bob a ${age[bob]} ans"

# ─────────────────────────────────────────────
# 4. AJOUTER une nouvelle paire cle -> valeur
# ─────────────────────────────────────────────
age[chloe]=42
echo "On vient d'ajouter Chloe (${age[chloe]} ans)"

# Le # donne le nombre de paires (comme pour les tableaux indexes).
echo "Nombre de personnes : ${#age[@]}"

# ─────────────────────────────────────────────
# 5. PARCOURIR : "${!age[@]}" donne TOUTES LES CLES (le ! = "les cles")
#    Puis ${age[$prenom]} donne la valeur rangee sous la cle courante.
#    L'ordre des cles n'est pas garanti, c'est normal.
# ─────────────────────────────────────────────
echo "Annuaire des ages :"
for prenom in "${!age[@]}"; do
    echo "- $prenom a ${age[$prenom]} ans"
done
