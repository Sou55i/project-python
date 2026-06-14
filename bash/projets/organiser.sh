#!/usr/bin/env bash
#
# PROJET CAPSTONE - L'organiseur de dossier (rangement par extension)
# ===================================================================
# Ce script RANGE automatiquement les fichiers d'un dossier "en bazar" dans des
# sous-dossiers, selon leur extension :
#     .txt / .md      -> Documents/
#     .jpg / .png     -> Images/
#     .csv            -> Tableaux/
#     .mp3            -> Musique/
#     (le reste)      -> Autres/
#
# C'est l'equivalent Bash du projet Python "ranger_dossier.py" :
# meme idee, mais en pilotant le terminal.
#
# 🧩 MODULES COMBINES (le but d'un "capstone" : tout reunir) :
#     - Module 02 (Fichiers)     : boucle "for" sur un dossier, mkdir -p, mv, [[ -f ]].
#     - Module 01 (Les bases)    : conditions [[ ... ]], variables, "case".
#     - Module 06 (Robustesse)   : set -euo pipefail (le trio de la mefiance).
#     - Manipulation de chemins  : recuperer le nom et l'extension d'un fichier.
#
# Lance-le DEPUIS LA RACINE du depot (il ne casse RIEN : il travaille sur une
# demo de fichiers VIDES qu'il fabrique lui-meme) :
#     bash bash/projets/organiser.sh
#
# 🗺️  CHEMINEMENT DU SCRIPT (les grandes etapes, dans l'ordre)
# ────────────────────────────────────────────────────────────
#     1. Activer les protections (set -euo pipefail).
#     2. Fabriquer un dossier de DEMO "bazar/" rempli de fichiers VIDES (touch).
#     3. Parcourir ce dossier fichier par fichier (boucle for).
#     4. Pour chaque fichier : lire son extension, choisir le bon sous-dossier (case).
#     5. Creer le sous-dossier au besoin (mkdir -p), puis y deplacer le fichier (mv).
#     6. Afficher un petit bilan de ce qui a ete range.

# ─────────────────────────────────────────────────────────────
# 1. LES PROTECTIONS (Module 06) — le trio de la mefiance
# ─────────────────────────────────────────────────────────────
#    -e          : on s'arrete a la 1re commande qui echoue.
#    -u          : interdit d'utiliser une variable non definie.
#    -o pipefail : detecte une erreur meme au milieu d'un pipe a | b.
set -euo pipefail

# ─────────────────────────────────────────────────────────────
# 2. ON FABRIQUE UN DOSSIER DE DEMO (pour ne RIEN casser de reel)
# ─────────────────────────────────────────────────────────────
# Tout se passe sous "exemples/", un dossier IGNORE par git : on peut donc
# experimenter sans polluer le depot.
dossier="bash/projets/exemples/bazar"

# On (re)part d'une demo propre : on efface une eventuelle ancienne demo,
# puis on recree le dossier vide. ( -rf ne rale pas si rien n'existe. )
rm -rf "$dossier"
mkdir -p "$dossier"                       # mkdir -p : cree toute l'arborescence

# touch cree un fichier VIDE (donc zero risque de perdre des donnees).
# On simule un vrai "bazar" : plusieurs types de fichiers melanges.
touch "$dossier/rapport.txt"
touch "$dossier/notes.md"
touch "$dossier/photo_vacances.jpg"
touch "$dossier/logo.png"
touch "$dossier/budget.csv"
touch "$dossier/chanson.mp3"
touch "$dossier/mystere.xyz"              # extension inconnue -> ira dans "Autres/"

echo "Dossier de demo prepare : $dossier"
echo "Contenu AVANT rangement :"
ls -1 "$dossier"                          # ls -1 : un fichier par ligne
echo

# ─────────────────────────────────────────────────────────────
# 3 & 4 & 5. ON RANGE : boucle for + choix du dossier + mv
# ─────────────────────────────────────────────────────────────
echo "Rangement en cours…"

# "$dossier"/* designe tous les elements du dossier, un par un.
for chemin in "$dossier"/*; do

    # On ne traite que les vrais FICHIERS (Module 02 : test [[ -f ]]).
    # (Les sous-dossiers qu'on va creer juste apres seront ainsi ignores.)
    if [[ ! -f "$chemin" ]]; then
        continue                          # continue : passe au tour suivant
    fi

    # --- Manipulation de chemin : isoler le nom puis l'extension ---
    # basename enleve le chemin : "…/bazar/budget.csv" -> "budget.csv".
    nom_fichier="$(basename "$chemin")"
    # "${nom##*.}" garde tout APRES le dernier point -> l'extension ("csv").
    extension="${nom_fichier##*.}"

    # --- On choisit le bon sous-dossier selon l'extension (case) ---
    # "case" est un "if/elif" plus lisible quand on compare UNE valeur a
    # plusieurs possibilites. Le "|" separe les variantes equivalentes.
    case "$extension" in
        txt|md)   sous_dossier="Documents" ;;
        jpg|png)  sous_dossier="Images"    ;;
        csv)      sous_dossier="Tableaux"  ;;
        mp3)      sous_dossier="Musique"   ;;
        *)        sous_dossier="Autres"    ;;   # * = tout le reste (cas par defaut)
    esac

    # --- On cree le sous-dossier au besoin, puis on deplace le fichier ---
    cible="$dossier/$sous_dossier"
    mkdir -p "$cible"                     # mkdir -p : ne rale pas s'il existe deja
    mv "$chemin" "$cible/"                # mv : deplace le fichier dans sa categorie

    echo "  $nom_fichier  ->  $sous_dossier/"
done

# ─────────────────────────────────────────────────────────────
# 6. PETIT BILAN
# ─────────────────────────────────────────────────────────────
echo
echo "Range ! Voici la nouvelle organisation de '$dossier' :"
# Pour chaque sous-dossier cree, on liste ce qu'il contient.
for categorie in "$dossier"/*/; do        # le / final ne garde QUE les dossiers
    nom_categorie="$(basename "$categorie")"
    echo "📁 $nom_categorie/"
    for f in "$categorie"*; do
        [[ -e "$f" ]] && echo "     - $(basename "$f")"
    done
done

echo
echo "Termine avec succes. (Tu peux tout supprimer avec : rm -rf bash/projets/exemples)"
