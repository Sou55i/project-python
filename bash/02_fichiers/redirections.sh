#!/usr/bin/env bash
#
# MODULE 02 - Redirections : ecrire, ajouter, relire un fichier
# ============================================================
# Montre, dans l'ordre : > (ecrire/ecraser), >> (ajouter), cat,
# la lecture ligne par ligne, et un pipe.
#
# ANTI-POLLUTION : tout se passe dans le sous-dossier "exemples/".
# Lance-le DEPUIS LA RACINE du depot :
#   bash bash/02_fichiers/redirections.sh

# ─────────────────────────────────────────────
# 0. ON PREPARE UN DOSSIER DE TRAVAIL
# ─────────────────────────────────────────────
# mkdir -p cree le dossier "exemples" (sans erreur s'il existe deja).
# Comme on lance le script depuis la racine, on donne le chemin complet.
mkdir -p bash/02_fichiers/exemples

# On range le nom du fichier dans une variable : plus pratique a reutiliser.
fichier="bash/02_fichiers/exemples/notes.txt"

# ─────────────────────────────────────────────
# 1. ECRIRE AVEC > (cree le fichier, ECRASE l'ancien contenu)
# ─────────────────────────────────────────────
echo "premiere ligne" > "$fichier"      # > : remplace TOUT le contenu
echo "(j'ai ecrit la premiere ligne avec >)"

# ─────────────────────────────────────────────
# 2. AJOUTER AVEC >> (ajoute a la fin, sans rien ecraser)
# ─────────────────────────────────────────────
echo "deuxieme ligne" >> "$fichier"     # >> : ajoute a la suite
echo "troisieme ligne" >> "$fichier"
echo "(j'ai ajoute deux lignes avec >>)"

# ─────────────────────────────────────────────
# 3. RELIRE TOUT D'UN COUP AVEC cat
# ─────────────────────────────────────────────
echo
echo "--- Contenu complet (cat) ---"
cat "$fichier"                          # cat affiche tout le fichier

# ─────────────────────────────────────────────
# 4. RELIRE LIGNE PAR LIGNE (la formule magique IFS= read -r)
# ─────────────────────────────────────────────
echo
echo "--- Lecture ligne par ligne (while read) ---"
numero=1
while IFS= read -r ligne; do            # lit une ligne, la range dans "ligne"
    echo "Ligne $numero : $ligne"
    numero=$(( numero + 1 ))            # on incremente le compteur
done < "$fichier"                       # < : on branche le fichier sur la boucle

# ─────────────────────────────────────────────
# 5. UN PIPE | pour compter les lignes
# ─────────────────────────────────────────────
echo
# cat envoie le fichier dans wc -l, qui compte les lignes.
total=$(cat "$fichier" | wc -l)
echo "Le fichier contient $total lignes."
