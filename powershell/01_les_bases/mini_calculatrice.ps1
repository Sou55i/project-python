<#
   MODULE 01 - Mini-projet : une calculatrice en PowerShell
   ========================================================
   On combine Read-Host (saisie), la conversion en nombre, le switch et le calcul.

   Lance-le :  pwsh powershell/01_les_bases/mini_calculatrice.ps1

   🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
      1. Demander l'opération (+, -, *, /) avec Read-Host.
      2. Demander deux nombres et les convertir en [double].
      3. Choisir le calcul selon l'opération (switch).
      4. Afficher le résultat.
#>

# 1. ENTRÉE : Read-Host met le script en pause et renvoie ce qui est tapé (du TEXTE).
$op = Read-Host "Operation (+, -, *, /)"

# 2. On convertit les saisies en nombres décimaux avec [double], sinon on ne peut pas calculer.
$n1 = [double](Read-Host "Premier nombre")
$n2 = [double](Read-Host "Deuxieme nombre")

# 3. TRAITEMENT : switch choisit le bloc correspondant à la valeur de $op.
$resultat = $null
switch ($op) {
    "+" { $resultat = $n1 + $n2 }
    "-" { $resultat = $n1 - $n2 }
    "*" { $resultat = $n1 * $n2 }
    "/" {
        # On se protège de la division par zéro.
        if ($n2 -eq 0) {
            Write-Host "Erreur : division par zero impossible."
            exit 1                 # quitter avec un code d'erreur (différent de 0)
        }
        $resultat = $n1 / $n2
    }
    default {
        Write-Host "Operation inconnue."
        exit 1
    }
}

# 4. SORTIE : afficher le résultat.
Write-Host "Resultat : $resultat"
