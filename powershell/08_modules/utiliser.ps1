<#
    🗺️ CHEMINEMENT DU SCRIPT
    1. On IMPORTE notre caisse à outils (le module outils.psm1) avec Import-Module.
       Le chemin s'appuie sur $PSScriptRoot pour rester robuste où qu'on lance le script.
    2. On UTILISE Get-Carre : on capture son résultat dans une variable, puis on l'affiche.
    3. On UTILISE Test-Pair : il renvoie $true / $false, qu'on teste avec un if.
    4. On UTILISE Get-PlusGrand pour comparer deux nombres et afficher le gagnant.
#>

# 1. On ouvre la caisse à outils. $PSScriptRoot = le dossier de CE script ;
#    -Force recharge le module à chaque exécution (toujours la dernière version).
Import-Module "$PSScriptRoot/outils.psm1" -Force

# 2. On CAPTURE le résultat de Get-Carre dans une variable, puis on l'affiche.
$carre = Get-Carre -Nombre 5
Write-Host "Le carre de 5 vaut $carre"

# 3. Test-Pair renvoie un booleen : on le teste directement dans un if.
$nombre = 4
if (Test-Pair -Nombre $nombre) {
    Write-Host "$nombre est pair"
} else {
    Write-Host "$nombre est impair"
}

# 4. On compare deux nombres grace a Get-PlusGrand et on affiche le plus grand.
$gagnant = Get-PlusGrand -A 12 -B 7
Write-Host "Le plus grand entre 12 et 7 est $gagnant"
