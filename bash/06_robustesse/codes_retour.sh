#!/usr/bin/env bash
#
# MODULE 06 - Les codes de retour, && et ||
# =========================================
# On observe $? (le code de la dernière commande), puis les enchaînements
# && (si succès) et || (si échec).
#
# Lance-le :  bash bash/06_robustesse/codes_retour.sh
#
# 🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
#    1. Une commande qui RÉUSSIT, puis on lit son code ($? = 0).
#    2. Une commande qui ÉCHOUE, puis on lit son code ($? ≠ 0).
#    3. L'enchaînement && : "ET ENSUITE" (suite seulement si succès).
#    4. L'enchaînement || : "SINON" (secours seulement si échec).
#
# ⚠️ Ici on N'utilise PAS "set -e" : on VEUT voir les échecs sans que le
#    script s'arrête, pour pouvoir lire et commenter leurs codes de retour.

# 1. UNE COMMANDE QUI RÉUSSIT --------------------------------------------------
echo "[1] On liste un dossier qui existe (/tmp) :"
ls /tmp > /dev/null          # > /dev/null = on jette l'affichage, on veut juste le code
echo "    Code de retour \$? = $?   (0 = succès : tout va bien)"
echo

# 2. UNE COMMANDE QUI ÉCHOUE ---------------------------------------------------
echo "[2] On liste un dossier qui n'existe pas :"
ls /dossier_qui_nexiste_vraiment_pas 2> /dev/null   # 2> /dev/null = on cache l'erreur
echo "    Code de retour \$? = $?   (≠ 0 = erreur : ça a raté)"
echo

# 3. L'ENCHAÎNEMENT && ("ET ENSUITE") -----------------------------------------
# La partie de droite ne s'exécute QUE SI la gauche a réussi (code 0).
echo "[3] Enchaînement avec && (ET ENSUITE) :"
true  && echo "    'true' a réussi  -> ce message s'affiche."
false && echo "    Ce message ne s'affichera JAMAIS (car 'false' échoue)."
echo

# 4. L'ENCHAÎNEMENT || ("SINON") ----------------------------------------------
# La partie de droite ne s'exécute QUE SI la gauche a échoué (code ≠ 0).
echo "[4] Enchaînement avec || (SINON) :"
true  || echo "    Ce message ne s'affichera JAMAIS (car 'true' réussit)."
false || echo "    'false' a échoué  -> ce message de secours s'affiche."
echo

echo "Fin : tu as vu \$?, puis && (succès) et || (échec)."
