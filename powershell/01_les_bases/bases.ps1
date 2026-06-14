<#
   MODULE 01 - Les briques de base en PowerShell
   =============================================
   Illustre, dans l'ordre : variables & types, interpolation, conditions,
   boucles et fonctions.

   Lance-le :  pwsh powershell/01_les_bases/bases.ps1
#>

# ─────────────────────────────────────────────
# FONCTIONS (définies avant d'être appelées)
# ─────────────────────────────────────────────
# Par convention PowerShell, on nomme une fonction Verbe-Nom.
function Get-Salutation {
    param([string]$Nom)        # param() déclare les paramètres et leur type
    return "Bonjour $Nom !"    # return renvoie le résultat à l'appelant
}

# ─────────────────────────────────────────────
# 1. VARIABLES ET TYPES (le nom commence par $)
# ─────────────────────────────────────────────
$nom = "Alice"
$age = 30
$taille = 1.68
$actif = $true                 # booléen : $true / $false

# Interpolation : dans des guillemets DOUBLES, $nom est remplacé par sa valeur.
Write-Host "$nom, $age ans, $taille m. Actif ? $actif"

# Pour insérer un CALCUL dans le texte, on l'entoure de $( ).
Write-Host "Dans 5 ans, $nom aura $($age + 5) ans"

# ─────────────────────────────────────────────
# 2. CONDITIONS : on compare avec -eq, -lt, -ge... (jamais < ou >)
# ─────────────────────────────────────────────
$note = 12
if ($note -ge 16) {
    Write-Host "Mention : Tres bien"
} elseif ($note -ge 10) {
    Write-Host "Mention : Recu"
} else {
    Write-Host "Mention : A retravailler"
}

# ─────────────────────────────────────────────
# 3. BOUCLES
# ─────────────────────────────────────────────
# for : un nombre précis de répétitions
for ($i = 0; $i -lt 3; $i++) {     # $i++ = $i + 1
    Write-Host "Tour numero $i"
}

# foreach : pour chaque élément d'un tableau (créé avec @( ))
$fruits = @("pomme", "banane", "cerise")
foreach ($fruit in $fruits) {
    Write-Host "- $fruit"
}
Write-Host "Il y a $($fruits.Count) fruits ; le premier est $($fruits[0])"

# while : tant que la condition est vraie
$compteur = 0
while ($compteur -lt 3) {
    Write-Host "compteur = $compteur"
    $compteur++                    # indispensable, sinon boucle infinie
}

# ─────────────────────────────────────────────
# 4. APPELER NOS FONCTIONS
# ─────────────────────────────────────────────
Write-Host (Get-Salutation -Nom "Alice")
Write-Host (Get-Salutation "Bob")
