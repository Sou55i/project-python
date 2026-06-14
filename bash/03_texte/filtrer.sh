#!/usr/bin/env bash
#
# MODULE 03 - Filtrer du texte : grep, cut, sort, uniq, wc
# ========================================================
# On crée un petit log de démo, puis on en extrait des infos en
# ENCHAÎNANT les outils avec des pipes ( | ).
#
# ⚠️ LANCE-MOI DEPUIS LA RACINE DU DÉPÔT :  bash bash/03_texte/filtrer.sh
#
# 🗺️ CHEMINEMENT DU SCRIPT
#   1. On prépare un dossier exemples/ et un fichier log de démo.
#   2. grep      → ne garder que certaines lignes.
#   3. cut       → extraire une colonne.
#   4. sort|uniq → trier puis dédoublonner / compter.
#   5. wc -l     → compter des lignes.
#   6. LE COMBO  → tout enchaîner pour répondre à une vraie question.
#   7. On nettoie : le dossier exemples/ est supprimé (anti-pollution).

# ─────────────────────────────────────────────
# 1. PRÉPARATION : un dossier et un fichier de démo
# ─────────────────────────────────────────────
# mkdir -p : crée le dossier s'il n'existe pas (sans erreur s'il existe déjà).
# Chemin RELATIF (pas de / au début) → créé là d'où on lance le script.
mkdir -p bash/03_texte/exemples

# On écrit un faux journal de connexions dans un fichier.
# Format de chaque ligne :  NIVEAU utilisateur action
cat > bash/03_texte/exemples/journal.log <<'FIN'
INFO alice connexion
INFO bob connexion
ERROR bob mot_de_passe
INFO alice deconnexion
ERROR carla mot_de_passe
ERROR bob mot_de_passe
INFO david connexion
FIN

echo "=== Le fichier de démo (bash/03_texte/exemples/journal.log) ==="
cat bash/03_texte/exemples/journal.log
echo

# ─────────────────────────────────────────────
# 2. grep : ne garder que les lignes en ERROR
# ─────────────────────────────────────────────
echo "=== grep : les lignes d'erreur ==="
grep "ERROR" bash/03_texte/exemples/journal.log
echo

# ─────────────────────────────────────────────
# 3. cut : extraire la 2e colonne (le nom d'utilisateur)
# ─────────────────────────────────────────────
# -d' ' : le séparateur est l'espace.   -f2 : on garde le 2e champ.
echo "=== cut : les utilisateurs (2e colonne) ==="
cut -d' ' -f2 bash/03_texte/exemples/journal.log
echo

# ─────────────────────────────────────────────
# 4. sort | uniq : trier puis regrouper
# ─────────────────────────────────────────────
# uniq ne supprime que les doublons QUI SE SUIVENT → on trie AVANT avec sort.
echo "=== sort | uniq : la liste des utilisateurs, sans doublon ==="
cut -d' ' -f2 bash/03_texte/exemples/journal.log | sort | uniq
echo

# uniq -c : en plus, COMPTER combien de fois chaque utilisateur apparaît.
echo "=== sort | uniq -c : nombre de lignes par utilisateur ==="
cut -d' ' -f2 bash/03_texte/exemples/journal.log | sort | uniq -c
echo

# ─────────────────────────────────────────────
# 5. wc -l : compter les lignes
# ─────────────────────────────────────────────
# On compte combien de lignes contiennent ERROR (grep ... | wc -l).
echo "=== wc -l : combien d'erreurs au total ? ==="
grep "ERROR" bash/03_texte/exemples/journal.log | wc -l
echo

# ─────────────────────────────────────────────
# 6. LE COMBO : qui a eu le plus d'erreurs ?
# ─────────────────────────────────────────────
# On lit la chaîne de gauche à droite :
#   grep ERROR        → on ne garde que les erreurs
#   cut -d' ' -f2     → on extrait l'utilisateur
#   sort              → on regroupe les utilisateurs identiques
#   uniq -c           → on compte chacun
#   sort -rn          → on trie par nombre DÉCROISSANT (-r inverse, -n numérique)
echo "=== LE COMBO : utilisateurs classés par nombre d'erreurs ==="
grep "ERROR" bash/03_texte/exemples/journal.log \
  | cut -d' ' -f2 \
  | sort \
  | uniq -c \
  | sort -rn
echo

# ─────────────────────────────────────────────
# 7. NETTOYAGE (anti-pollution) : on supprime le dossier de démo
# ─────────────────────────────────────────────
rm -rf bash/03_texte/exemples
echo "Nettoyage fait : le dossier exemples/ a été supprimé."
