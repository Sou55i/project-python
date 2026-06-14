<#
   MODULE 04 - Les paramètres d'un SCRIPT (param)
   ==============================================
   Un script entier peut commencer par un bloc param( ... ). On lui passe alors
   les valeurs sur la ligne de commande, après le nom du fichier. Même script,
   résultats différents : il est devenu réutilisable (comme argparse en Python).

   Lance-le :  pwsh powershell/04_parametres/script_param.ps1 -Nom Alice

   🗺️ CHEMINEMENT DU SCRIPT
   ------------------------
   1. Le bloc param() lit le paramètre -Nom passé en ligne de commande.
   2. Si -Nom est absent, $Nom prend sa valeur par défaut : "le monde".
   3. On affiche la salutation avec Write-Host.
#>

# ─────────────────────────────────────────────
# 1. PARAMÈTRES DU SCRIPT (tout en haut, avant toute autre instruction)
# ─────────────────────────────────────────────
# [string]$Nom : un paramètre typé (chaîne) avec une valeur par défaut.
param([string]$Nom = "le monde")

# ─────────────────────────────────────────────
# 2. UTILISATION DU PARAMÈTRE
# ─────────────────────────────────────────────
# Dans des guillemets DOUBLES, $Nom est remplacé par sa valeur (interpolation).
Write-Host "Bonjour $Nom"
