<#
   MODULE 05 - Les tableaux (arrays) en PowerShell
   ===============================================
   Un tableau range PLUSIEURS valeurs dans l'ordre, repérées par un numéro
   (la position, qui commence à 0). Equivalent de la LISTE en Python.

   Lance-le :  pwsh powershell/05_collections/tableaux.ps1
#>

# ─────────────────────────────────────────────
# 1. CRÉER un tableau avec @( ) (valeurs séparées par des virgules)
# ─────────────────────────────────────────────
$fruits = @("pomme", "banane", "cerise")

# ─────────────────────────────────────────────
# 2. AFFICHER le tableau
# ─────────────────────────────────────────────
# -join colle les éléments avec un séparateur, ici ", " pour une jolie ligne.
Write-Host "Mon tableau : $($fruits -join ', ')"

# Accéder à UN élément : entre crochets, on compte À PARTIR DE 0 !
Write-Host "Le premier fruit (index 0) est : $($fruits[0])"

# ─────────────────────────────────────────────
# 3. SA TAILLE avec .Count
# ─────────────────────────────────────────────
Write-Host "Il y a $($fruits.Count) fruits"

# ─────────────────────────────────────────────
# 4. AJOUTER un élément avec +=
# ─────────────────────────────────────────────
$fruits += "kiwi"                 # le tableau grandit d'une case
Write-Host "Apres ajout, il y a $($fruits.Count) fruits"

# ─────────────────────────────────────────────
# 5. PARCOURIR le tableau avec foreach
# ─────────────────────────────────────────────
# Lecture : "pour chaque $fruit dans $fruits".
foreach ($fruit in $fruits) {
    Write-Host "- $fruit"
}
