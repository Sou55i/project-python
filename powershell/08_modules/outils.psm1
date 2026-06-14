<#
    outils.psm1 — notre première CAISSE À OUTILS (un MODULE PowerShell).

    Un fichier .psm1 ne contient QUE des définitions de fonctions : pas de code
    qui s'exécute tout seul. Les scripts viendront y puiser avec Import-Module.

    Tout en bas, Export-ModuleMember précise quelles fonctions sont PUBLIQUES.
#>

# ----------------------------------------------------------------------------
# Get-Carre : renvoie le carré d'un nombre entier.
# ----------------------------------------------------------------------------
function Get-Carre {
    param(
        [int]$Nombre            # l'entrée, typée : un entier
    )
    return $Nombre * $Nombre    # on RENVOIE le carré à l'appelant
}

# ----------------------------------------------------------------------------
# Test-Pair : renvoie $true si le nombre est pair, $false sinon.
# Convention PowerShell : une fonction qui répond oui/non commence par "Test-".
# ----------------------------------------------------------------------------
function Test-Pair {
    param(
        [int]$Nombre
    )
    # Le reste de la division par 2 (%) vaut 0 quand le nombre est pair.
    return ($Nombre % 2 -eq 0)
}

# ----------------------------------------------------------------------------
# Get-Plus-Grand : renvoie le plus grand des deux nombres reçus.
# ----------------------------------------------------------------------------
function Get-PlusGrand {
    param(
        [int]$A,
        [int]$B
    )
    if ($A -ge $B) {            # -ge : "supérieur ou égal" (jamais le signe >)
        return $A
    }
    return $B
}

# On EXPOSE explicitement les trois outils : ils deviennent utilisables après
# Import-Module. Toute fonction non listée ici resterait privée au module.
Export-ModuleMember -Function Get-Carre, Test-Pair, Get-PlusGrand
