#!/usr/bin/env bash
#
# MODULE 03 - Transformer du texte : sed et awk
# =============================================
# sed REMPLACE du texte ; awk découpe chaque ligne en CHAMPS ($1, $2...)
# et sait même CALCULER. On termine par un combo sed | awk.
#
# ⚠️ LANCE-MOI DEPUIS LA RACINE DU DÉPÔT :  bash bash/03_texte/transformer.sh
#
# 🗺️ CHEMINEMENT DU SCRIPT
#   1. On prépare un dossier exemples/ et un fichier de ventes de démo.
#   2. sed           → remplacer un mot (s/ancien/nouveau/).
#   3. awk {print $N}→ extraire un ou plusieurs champs.
#   4. awk + END     → un vrai calcul : le total d'une colonne.
#   5. COMBO sed|awk → on nettoie le texte PUIS on calcule.
#   6. On nettoie : le dossier exemples/ est supprimé (anti-pollution).

# ─────────────────────────────────────────────
# 1. PRÉPARATION : un dossier et un fichier de démo
# ─────────────────────────────────────────────
# mkdir -p : crée le dossier (chemin RELATIF → créé là où on lance le script).
mkdir -p bash/03_texte/exemples

# Un mini fichier de ventes.  Format :  produit prix quantite
cat > bash/03_texte/exemples/ventes.txt <<'FIN'
pomme 2 10
banane 1 20
cerise 5 4
pomme 2 6
FIN

echo "=== Le fichier de démo (bash/03_texte/exemples/ventes.txt) ==="
cat bash/03_texte/exemples/ventes.txt
echo

# ─────────────────────────────────────────────
# 2. sed : REMPLACER un mot
# ─────────────────────────────────────────────
# s/pomme/POMME/  →  "s" = substitute, on remplace pomme par POMME.
# Par défaut sed AFFICHE le résultat sans modifier le fichier d'origine.
echo "=== sed : on met 'pomme' en majuscules ==="
sed 's/pomme/POMME/' bash/03_texte/exemples/ventes.txt
echo

# ─────────────────────────────────────────────
# 3. awk : extraire des CHAMPS ($1, $2, $3)
# ─────────────────────────────────────────────
# Dans awk, chaque ligne est découpée : $1 = 1er mot, $2 = 2e, etc.
echo "=== awk : seulement le produit (champ \$1) ==="
awk '{print $1}' bash/03_texte/exemples/ventes.txt
echo

# On peut aussi RÉORGANISER et ajouter du texte fixe.
echo "=== awk : 'produit -> quantite' (on réorganise \$1 et \$3) ==="
awk '{print $1, "->", $3}' bash/03_texte/exemples/ventes.txt
echo

# ─────────────────────────────────────────────
# 4. awk : un vrai CALCUL (le chiffre d'affaires)
# ─────────────────────────────────────────────
# Pour chaque ligne : total = total + (prix * quantite) = $2 * $3.
# Le bloc END { ... } s'exécute UNE SEULE FOIS, à la toute fin.
echo "=== awk : chiffre d'affaires total (somme de prix x quantite) ==="
awk '{total = total + $2 * $3} END {print "Total :", total, "euros"}' \
    bash/03_texte/exemples/ventes.txt
echo

# ─────────────────────────────────────────────
# 5. LE COMBO sed | awk : nettoyer PUIS calculer
# ─────────────────────────────────────────────
# Imaginons des prix écrits avec une virgule décimale (style français) : "2,5".
# awk calcule en base anglaise (point décimal) → on remplace d'abord , par .
# avec sed, PUIS awk fait la somme. C'est tout le sens du pipe |.
cat > bash/03_texte/exemples/prix_fr.txt <<'FIN'
pomme 2,5
banane 1,0
cerise 5,5
FIN

echo "=== COMBO sed | awk : convertir '2,5' en '2.5' puis additionner ==="
echo "Fichier d'origine (virgule décimale) :"
cat bash/03_texte/exemples/prix_fr.txt
echo "Résultat :"
sed 's/,/./g' bash/03_texte/exemples/prix_fr.txt \
  | awk '{somme = somme + $2} END {print "Somme des prix :", somme}'
echo

# ─────────────────────────────────────────────
# 6. NETTOYAGE (anti-pollution) : on supprime le dossier de démo
# ─────────────────────────────────────────────
rm -rf bash/03_texte/exemples
echo "Nettoyage fait : le dossier exemples/ a été supprimé."
