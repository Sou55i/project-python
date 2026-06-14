#!/usr/bin/env bash
#
# MODULE 02 - Parcourir les fichiers d'un dossier
# ===============================================
# Cree quelques fichiers de demo, puis parcourt le dossier et,
# pour chaque element, teste si c'est bien un fichier avant de l'afficher.
#
# Lance-le DEPUIS LA RACINE du depot :
#   bash bash/02_fichiers/parcourir.sh
#
# 🗺️  CHEMINEMENT DU SCRIPT
# ─────────────────────────
#   1. On prepare un dossier "exemples/" (mkdir -p).
#   2. On y cree 3 petits fichiers de demonstration (avec >).
#   3. On boucle (for) sur tout ce qu'il y a dans exemples/.
#   4. Pour chaque element, on teste [[ -f ... ]] : est-ce un fichier ?
#   5. Si oui, on l'affiche (nom + nombre de lignes). Sinon, on signale.

# ─────────────────────────────────────────────
# 1. DOSSIER DE TRAVAIL
# ─────────────────────────────────────────────
dossier="bash/02_fichiers/exemples"
mkdir -p "$dossier"                     # cree le dossier si besoin

# ─────────────────────────────────────────────
# 2. ON CREE QUELQUES FICHIERS DE DEMO
# ─────────────────────────────────────────────
echo "pomme"  > "$dossier/fruits.txt"   # > cree (ou ecrase) le fichier
echo "banane" >> "$dossier/fruits.txt"  # >> ajoute une ligne
echo "bonjour" > "$dossier/salutation.txt"
echo "1 2 3 4 5" > "$dossier/nombres.txt"

# ─────────────────────────────────────────────
# 3. ON PARCOURT LE DOSSIER (for sur exemples/*)
# ─────────────────────────────────────────────
echo "Contenu du dossier '$dossier' :"
echo

# exemples/* designe tous les elements du dossier, un par un.
for element in "$dossier"/*; do
    # ─────────────────────────────────────────
    # 4. EST-CE UN FICHIER ? (test [[ -f ... ]])
    # ─────────────────────────────────────────
    if [[ -f "$element" ]]; then        # -f : vrai si c'est un fichier normal
        # wc -l < fichier compte les lignes du fichier.
        nb_lignes=$(wc -l < "$element")
        echo "[fichier] $element  ($nb_lignes ligne(s))"
    else
        # Au cas ou ce serait un sous-dossier ou autre chose.
        echo "[autre  ] $element  (ce n'est pas un fichier normal)"
    fi
done
