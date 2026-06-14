<#
   MODULE 04 - Les paramètres d'une FONCTION (param)
   =================================================
   Une fonction qui accepte des paramètres devient un petit outil réutilisable :
   on lui donne des entrées, elle s'adapte. Ici, un paramètre OBLIGATOIRE et un
   paramètre avec une VALEUR PAR DÉFAUT.

   Lance-le :  pwsh powershell/04_parametres/fonction_param.ps1
#>

# ─────────────────────────────────────────────
# DÉFINITION DE LA FONCTION
# ─────────────────────────────────────────────
# Par convention PowerShell, on nomme une fonction Verbe-Nom.
function Get-Salutation {
    param(
        [Parameter(Mandatory)]      # ce paramètre est OBLIGATOIRE
        [string]$Nom,               # ... et typé : c'est une chaîne de caractères

        [int]$Fois = 1              # optionnel : si on ne précise rien, vaut 1
    )

    # On répète la salutation $Fois fois (boucle classique).
    for ($i = 0; $i -lt $Fois; $i++) {     # $i++ veut dire $i = $i + 1
        Write-Host "Bonjour $Nom !"        # $Nom est remplacé par sa valeur
    }
}

# ─────────────────────────────────────────────
# APPELS PAR NOM (-Nom, -Fois)
# ─────────────────────────────────────────────
# On nomme chaque argument avec un tiret : c'est lisible et l'ordre est libre.

# 1) On ne donne que le paramètre obligatoire : $Fois prend sa valeur par défaut (1).
Get-Salutation -Nom "Alice"

# 2) On précise les deux : la salutation s'affiche 3 fois.
Get-Salutation -Nom "Bob" -Fois 3

# 3) L'ordre des arguments nommés n'a pas d'importance.
Get-Salutation -Fois 2 -Nom "Chloe"
