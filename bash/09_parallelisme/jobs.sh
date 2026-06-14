#!/usr/bin/env bash
#
# 🗺️ CHEMINEMENT DU SCRIPT
# ------------------------------------------------------------------------------
#  Objectif : montrer le schéma "lancer avec & puis attendre avec wait".
#
#  1. On active les protections (set -euo pipefail) et on prépare un dossier
#     'exemples/' pour y ranger les résultats (un fichier par tâche).
#  2. On installe un 'trap' qui nettoiera 'exemples/' QUOI QU'IL ARRIVE.
#  3. On LANCE plusieurs tâches EN ARRIÈRE-PLAN avec '&'. Chaque tâche simule un
#     petit travail (un court 'sleep') puis écrit son résultat dans SON PROPRE
#     fichier (indexé par son numéro). Elles tournent donc EN MÊME TEMPS.
#  4. On appelle 'wait' : on patiente jusqu'à ce que TOUTES les tâches aient fini.
#  5. SEULEMENT APRÈS, on AGRÈGE les résultats (on additionne) et on affiche.
#     -> Comme chaque tâche écrit une valeur FIXE dans un fichier propre, le
#        total est toujours le MÊME (déterministe), même si l'ordre des tâches
#        varie.
# ------------------------------------------------------------------------------

set -euo pipefail   # script "méfiant" : stoppe à la 1re erreur, interdit les variables vides

# --- 1. Préparation -----------------------------------------------------------

# Dossier de travail RELATIF (anti-pollution : on reste dans le module, jamais ailleurs).
dossier="exemples"

# On (re)crée le dossier proprement. '-p' ne râle pas s'il existe déjà.
mkdir -p "$dossier"

# --- 2. Nettoyage automatique en sortie ---------------------------------------

# 'trap ... EXIT' : à la sortie du script (succès, erreur, peu importe), on efface
# le dossier 'exemples/'. Ainsi le dépôt reste propre, on ne laisse aucune trace.
trap 'rm -rf "$dossier"' EXIT

# --- 3. Lancer les tâches EN ARRIÈRE-PLAN -------------------------------------

# On va lancer 4 "tâches". Chacune vaut 10 (valeur FIXE), donc le total attendu
# est 4 x 10 = 40, à chaque exécution. C'est ce déterminisme qu'on veut prouver.
nb_taches=4
valeur=10

echo "Lancement de $nb_taches tâches EN PARALLÈLE (arrière-plan)..."

# Boucle de 1 à nb_taches : on démarre chaque tâche SANS attendre la précédente.
for i in $(seq 1 "$nb_taches"); do
    # Le bloc '( ... ) &' lance un sous-shell EN ARRIÈRE-PLAN (le '&' final) :
    #   - 'sleep' simule un petit travail qui ATTEND (durée volontairement courte) ;
    #   - puis la tâche écrit SA valeur dans SON fichier 'exemples/resultat_<i>.txt'.
    # Comme chaque tâche a son propre fichier, elles n'écrasent jamais leurs voisines.
    (
        sleep 0.2                                  # petit temps d'attente simulé
        echo "$valeur" > "$dossier/resultat_$i.txt" # résultat rangé dans un fichier propre
    ) &
done

# --- 4. Attendre que TOUTES les tâches soient finies --------------------------

# 'wait' sans argument : on patiente jusqu'à ce que TOUTES les tâches d'arrière-plan
# ci-dessus aient terminé. Sans cette ligne, on agrégerait des fichiers pas prêts !
wait

echo "Toutes les tâches sont terminées. Agrégation des résultats..."

# --- 5. Agréger les résultats (APRÈS wait) ------------------------------------

# On additionne le contenu de tous les fichiers de résultat. On part de 0.
total=0
for i in $(seq 1 "$nb_taches"); do
    # On lit la valeur écrite par la tâche i.
    contenu=$(cat "$dossier/resultat_$i.txt")
    # Addition en Bash : $(( ... )) fait du calcul sur des entiers.
    total=$(( total + contenu ))
done

# Affichage final. Ce total doit TOUJOURS valoir 40 (4 tâches x 10).
echo "Total agrégé : $total"

# Le 'trap' ci-dessus s'occupe d'effacer 'exemples/' en sortant. Rien à faire ici.
exit 0
