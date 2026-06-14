#!/usr/bin/env bash
#
# MODULE 01 - Les briques de base en Bash
# =======================================
# Illustre, dans l'ordre : variables & guillemets, calcul, conditions,
# boucles et fonctions.
#
# Lance-le :  bash bash/01_les_bases/bases.sh

# ─────────────────────────────────────────────
# 1. VARIABLES (pas d'espace autour du =) ET GUILLEMETS
# ─────────────────────────────────────────────
nom="Alice"
age=30
# On utilise une variable avec $ devant, et TOUJOURS entre guillemets doubles.
echo "Bonjour $nom, tu as $age ans"

# ─────────────────────────────────────────────
# 2. CALCUL : on entoure l'opération de $(( ))
# ─────────────────────────────────────────────
a=7
b=5
echo "7 + 5 = $(( a + b ))"          # calcul direct dans le texte
produit=$(( a * b ))                 # ou rangé dans une variable
echo "7 * 5 = $produit"

# ─────────────────────────────────────────────
# 3. CONDITIONS : if [[ ... ]]; then ... fi
# ─────────────────────────────────────────────
note=12
if [[ $note -ge 16 ]]; then          # -ge = "supérieur ou égal" (pour des nombres)
    echo "Mention : Tres bien"
elif [[ $note -ge 10 ]]; then
    echo "Mention : Recu"
else
    echo "Mention : A retravailler"
fi

# ─────────────────────────────────────────────
# 4. BOUCLES : for et while (corps entre do ... done)
# ─────────────────────────────────────────────
for fruit in pomme banane cerise; do
    echo "- $fruit"
done

for i in {1..3}; do                  # {1..3} = la liste 1 2 3
    echo "Tour $i"
done

compteur=0
while [[ $compteur -lt 3 ]]; do      # -lt = "strictement inférieur"
    echo "compteur = $compteur"
    compteur=$(( compteur + 1 ))     # indispensable, sinon boucle infinie
done

# ─────────────────────────────────────────────
# 5. FONCTIONS : $1 = premier argument reçu
# ─────────────────────────────────────────────
saluer() {
    echo "Bonjour $1 !"
}
saluer "Alice"
saluer "Bob"

# On récupère ce qu'une fonction affiche avec $( ... )
message=$(saluer "Chloe")
echo "Message capture : $message"
