<#
   MODULE 06 - Declencher une erreur avec throw, et nettoyer avec finally
   ======================================================================
   On verifie un age : s'il est invalide, on declenche nous-memes une erreur
   avec throw, attrapee par un try / catch. Le bloc finally s'execute toujours.

   Lance-le :  pwsh powershell/06_robustesse/erreurs.ps1

   🗺️ CHEMINEMENT DU SCRIPT (les grandes etapes, dans l'ordre) :
      1. Definir une petite fonction qui verifie un age et fait throw si invalide.
      2. Appeler cette fonction dans un try avec un age VALIDE.
      3. L'appeler dans un autre try avec un age INVALIDE (le catch attrape l'erreur).
      4. Observer que le bloc finally s'execute dans les DEUX cas.
#>

# 1. Une fonction qui controle l'age. Si l'age est negatif, elle declenche une erreur.
function Test-Age {
    param([int]$Age)            # 'param' declare le parametre attendu (un entier)

    if ($Age -lt 0) {
        # throw lance une erreur BLOQUANTE avec notre message : elle sera attrapable par catch.
        throw "L'age $Age est invalide (il ne peut pas etre negatif)."
    }

    Write-Host "Age $Age accepte."
}

# 2. Premier essai : un age VALIDE. Le try reussit, le catch est ignore.
Write-Host "--- Essai 1 : age valide (25) ---"
try {
    Test-Age -Age 25
} catch {
    # Ignore ici, car aucune erreur n'est declenchee.
    Write-Host "Erreur attrapee : $($_.Exception.Message)"
} finally {
    # finally s'execute QUOI QU'IL ARRIVE (succes ou echec). Ideal pour le nettoyage.
    Write-Host "finally : verification terminee."
}

# 3. Deuxieme essai : un age INVALIDE. Le throw declenche l'erreur, le catch l'attrape.
Write-Host "--- Essai 2 : age invalide (-5) ---"
try {
    Test-Age -Age -5
} catch {
    # On arrive ici grace au throw ci-dessus. $_.Exception.Message contient notre message.
    Write-Host "Erreur attrapee : $($_.Exception.Message)"
} finally {
    # 4. Encore une fois, finally s'execute, meme apres une erreur attrapee.
    Write-Host "finally : verification terminee."
}

# Le script se termine proprement : les deux erreurs ont ete gerees.
Write-Host "Fin du script."
