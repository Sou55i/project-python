#!/usr/bin/env bash
#
# MODULE 04 - Les arguments positionnels d'un script
# ==================================================
# Ce script lit ce que tu écris APRÈS son nom, sur la ligne de commande,
# grâce aux variables spéciales $0, $#, $@.
#
# Lance-le AVEC des arguments :
#    bash bash/04_arguments/arguments.sh un deux trois

# 1. $0 contient le NOM du script lui-même (tel que tu l'as tapé).
echo "Nom du script : $0"

# 2. $# contient le NOMBRE d'arguments reçus (le nom du script n'est PAS compté).
echo "Nombre d'arguments : $#"

# 3. On parcourt TOUS les arguments avec "$@" (entre guillemets : chaque
#    argument reste entier, même s'il contient un espace).
echo "Liste des arguments :"
for a in "$@"; do
    echo "  - $a"        # $a vaut tour à tour chaque argument
done
