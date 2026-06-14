#!/usr/bin/env bash
#
# MODULE 07 - Débugger : voir le script PENSER avec set -x
# =======================================================
# Ce petit script est CORRECT et instructif. Il fait un calcul tout simple,
# puis ALLUME la "trace" (set -x) sur une portion pour te montrer chaque
# commande exécutée avec ses vraies valeurs, et la ré-ÉTEINT (set +x) ensuite.
#
# Lance-le normalement :  bash bash/07_debugger/demo_debug.sh
# Ou en mode trace TOTAL : bash -x bash/07_debugger/demo_debug.sh
#
# 🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
#    1. Définir quelques variables (un prix, une quantité).
#    2. Afficher un petit message de départ (mode NORMAL, sans trace).
#    3. ALLUMER la trace avec set -x, puis faire le calcul du total.
#       -> Bash affiche chaque ligne exécutée, préfixée par "+", avec les VALEURS.
#    4. ÉTEINDRE la trace avec set +x : on revient en mode normal.
#    5. Afficher le résultat final proprement, puis finir (code 0).

# 1. NOS VARIABLES -------------------------------------------------------------
#    Rappel du module 01 : PAS d'espaces autour du = en Bash.
prix_unitaire=12        # le prix d'un article, en euros
quantite=3              # combien d'articles on achète
nom_client="Sasha"      # un texte (avec guillemets car ce sont des mots)

# 2. UN MESSAGE DE DÉPART (mode normal, AUCUNE trace ici) ----------------------
echo "Bonjour $nom_client, on calcule ton total..."

# 3. ON ALLUME LA TRACE -------------------------------------------------------
# À partir d'ici, Bash AFFICHE chaque commande qu'il exécute, préfixée par "+",
# en remplaçant les variables par leur VALEUR réelle. C'est la loupe du débogueur :
# tu vois EXACTEMENT ce que Bash calcule, étape par étape.
set -x

# Le calcul : en Bash, on entoure une opération de nombres par $(( ... )).
total=$(( prix_unitaire * quantite ))

# Une petite remise de 2 euros si on prend 3 articles ou plus.
remise=0
if [[ "$quantite" -ge 3 ]]; then     # -ge = "supérieur ou égal" (NOMBRES)
    remise=2
fi

total_final=$(( total - remise ))

# 4. ON ÉTEINT LA TRACE -------------------------------------------------------
# set +x : on rallume la lumière normale. Les lignes suivantes ne sont plus
# tracées. On allume la trace UNIQUEMENT autour de la zone qu'on veut inspecter.
set +x

# 5. LE RÉSULTAT, PROPREMENT --------------------------------------------------
# Technique de débogage par echo : afficher une variable pour vérifier sa valeur.
echo "DEBUG : total=$total, remise=$remise"      # on inspecte au passage
echo "$nom_client, ton total est de $total_final euros (remise de $remise euros incluse)."

# Fin normale : le script se termine tout seul avec le code 0 (succès).
