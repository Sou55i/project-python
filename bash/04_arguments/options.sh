#!/usr/bin/env bash
#
# MODULE 04 - Les OPTIONS d'un script avec getopts
# ================================================
# On accepte une option -n NOM (qui attend une valeur) et un drapeau -v (verbeux).
#
# Lance-le :
#    bash bash/04_arguments/options.sh -n Alice -v
#    bash bash/04_arguments/options.sh -n Bob
#    bash bash/04_arguments/options.sh            (rien : valeurs par défaut)
#
# 🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
#    1. Fixer les valeurs PAR DÉFAUT (avant de lire les options).
#    2. Lire les options avec getopts (boucle while + case).
#    3. Afficher le résultat, en parlant plus si le mode verbeux est actif.

# 1. VALEURS PAR DÉFAUT : si l'option n'est pas fournie, ces valeurs restent.
nom="inconnu"
verbeux=0

# 2. LECTURE DES OPTIONS avec getopts.
#    La chaîne "n:v" décrit ce qu'on accepte :
#      - "n:"  -> l'option -n attend une VALEUR (le : signifie « avec valeur »)
#      - "v"   -> l'option -v est un simple drapeau (sans valeur)
while getopts "n:v" option; do
    case "$option" in
        n) nom="$OPTARG" ;;        # la valeur de -n arrive dans $OPTARG
        v) verbeux=1 ;;            # -v présent -> on active le mode verbeux
        *) echo "Option inconnue. Usage : $0 [-n NOM] [-v]"
           exit 1 ;;              # toute autre option -> on quitte en erreur
    esac
done

# 3. SORTIE : on utilise les valeurs récupérées.
if [[ $verbeux -eq 1 ]]; then
    # Mode verbeux : on donne plus de détails.
    echo "[mode verbeux activé]"
    echo "Bonjour $nom, content de te voir !"
else
    # Mode normal : on reste bref.
    echo "Bonjour $nom"
fi
