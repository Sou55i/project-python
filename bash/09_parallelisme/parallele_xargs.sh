#!/usr/bin/env bash
#
# 🗺️ CHEMINEMENT DU SCRIPT
# ------------------------------------------------------------------------------
#  Objectif : montrer 'xargs -P N' pour traiter une LISTE d'éléments avec N
#             tâches EN PARALLÈLE.
#
#  1. On prépare une petite liste de "villes" (les éléments à traiter).
#  2. On envoie cette liste dans 'xargs -P 2' : au plus 2 traitements à la fois.
#  3. Chaque élément déclenche la même commande (un petit travail simulé qui
#     affiche un message). Les lignes peuvent sortir DANS LE DÉSORDRE : c'est
#     normal puisque plusieurs tâches s'exécutent en même temps.
# ------------------------------------------------------------------------------

set -euo pipefail   # protections habituelles : stoppe à la 1re erreur

echo "Traitement d'une liste avec xargs -P (2 en parallèle)..."
echo "(l'ordre des lignes peut varier : c'est le signe du parallélisme)"
echo

# 'printf %s\n' imprime chaque élément sur SA propre ligne. C'est ce que xargs
# attend : un élément par ligne.
#
# Ensuite on passe ça dans xargs :
#   -P 2   -> jusqu'à 2 tâches EN MÊME TEMPS (le degré de parallélisme).
#   -I {}  -> '{}' est un marqueur remplacé par CHAQUE élément lu.
#   bash -c '...' -> on lance un petit bout de script pour chaque élément :
#                    un 'sleep' court (travail qui attend) puis un message.
printf '%s\n' Paris Tokyo Lima Oslo Le_Caire \
  | xargs -P 2 -I {} bash -c 'sleep 0.2; echo "Traité : {}"'

echo
echo "Tous les éléments ont été traités."

# Pas de fichier créé, donc rien à nettoyer : aucun trap nécessaire ici.
exit 0
