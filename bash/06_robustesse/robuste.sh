#!/usr/bin/env bash
#
# MODULE 06 - Un script ROBUSTE de bout en bout
# =============================================
# On combine TOUT le module : set -euo pipefail (méfiance), un trap pour le
# nettoyage automatique, une vérification avec exit 1 propre, et un fichier
# temporaire jetable créé avec mktemp.
#
# Lance-le :  bash bash/06_robustesse/robuste.sh
#
# 🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
#    1. Activer les protections : set -euo pipefail.
#    2. Créer un fichier temporaire (mktemp) et programmer son nettoyage (trap).
#    3. Vérifier une condition ; si problème -> message + exit 1 propre.
#    4. Faire le "vrai" travail en utilisant le fichier temporaire.
#    5. Finir normalement -> le trap nettoie tout seul -> code 0.

# 1. LES PROTECTIONS (le trio magique, expliqué dans le README) ----------------
#    -e  : on quitte à la 1re commande qui échoue.
#    -u  : on interdit les variables non définies.
#    -o pipefail : on détecte une erreur même au milieu d'un pipe a | b.
set -euo pipefail

# 2. FICHIER TEMPORAIRE + NETTOYAGE AUTOMATIQUE --------------------------------
# mktemp crée un fichier au nom UNIQUE et nous renvoie son chemin.
fichier_temp=$(mktemp)

# trap : "quoi qu'il arrive, AVANT de sortir (EXIT), exécute ce ménage".
# Même si le script plante plus bas, ce rm aura lieu -> pas de fichier qui traîne.
trap 'rm -f "$fichier_temp"; echo "(nettoyage : fichier temporaire supprime)"' EXIT

echo "Fichier temporaire cree : $fichier_temp"

# 3. UNE VÉRIFICATION, AVEC SORTIE PROPRE EN CAS DE PROBLÈME -------------------
# On vérifie ici une condition simple : le dossier /tmp doit exister pour
# travailler. S'il manquait, on préviendrait clairement et on sortirait en
# erreur (exit 1) -> et le trap nettoierait quand même le fichier temporaire.
dossier_de_travail="/tmp"
if [[ ! -d "$dossier_de_travail" ]]; then
    echo "Erreur : le dossier $dossier_de_travail est introuvable." >&2
    exit 1                      # sortie en ERREUR (code ≠ 0), proprement
fi
echo "Verification OK : $dossier_de_travail existe."

# 4. LE "VRAI" TRAVAIL --------------------------------------------------------
# On écrit quelques lignes dans le fichier temporaire, puis on les compte.
# Le pipe ci-dessous (cat ... | wc -l) est protégé par pipefail.
printf 'pomme\nbanane\ncerise\n' > "$fichier_temp"
nb_lignes=$(cat "$fichier_temp" | wc -l)
echo "Le fichier temporaire contient $nb_lignes ligne(s)."

# 5. FIN NORMALE --------------------------------------------------------------
# On arrive ici sans erreur : Bash sort avec le code 0 (succès).
# Juste avant de sortir, le trap se déclenche et supprime le fichier temporaire.
echo "Travail termine avec succes."
