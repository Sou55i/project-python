<#
   MODULE 06 - Attraper une erreur avec try / catch
   ================================================
   On tente une operation risquee (convertir un texte en nombre) et, au lieu de
   laisser le script planter, on attrape l'erreur pour afficher un message clair.

   Lance-le :  pwsh powershell/06_robustesse/try_catch.ps1

   🗺️ CHEMINEMENT DU SCRIPT (les grandes etapes, dans l'ordre) :
      1. Preparer un texte qui n'est PAS un nombre.
      2. Dans un try, tenter de le convertir en [int] (operation risquee).
      3. Si ca echoue, le catch affiche un message clair (le script ne plante pas).
      4. Montrer aussi une division protegee dans un try / catch.
#>

# 1. ENTREE : un texte volontairement invalide (ce n'est pas un nombre).
$texte = "bonjour"

# 2. TRAITEMENT : on met l'operation risquee dans le bloc try.
try {
    # Convertir "bonjour" en entier est IMPOSSIBLE : cela declenche une erreur bloquante.
    $nombre = [int]$texte
    # Cette ligne ne s'execute QUE si la conversion a reussi (ici, elle ne reussira pas).
    Write-Host "Conversion reussie : $nombre"
} catch {
    # 3. On arrive ici uniquement si une erreur est survenue dans le try.
    #    $_ represente l'erreur ; $_.Exception.Message en donne le texte explicatif.
    Write-Host "Impossible de convertir '$texte' en nombre."
    Write-Host "Detail de l'erreur : $($_.Exception.Message)"
}

# 4. Deuxieme exemple : une division que l'on protege.
$a = 10
$b = 0

try {
    # Si $b vaut 0, on declenche nous-memes une erreur avec throw (voir erreurs.ps1).
    if ($b -eq 0) {
        throw "Division par zero interdite."
    }
    $resultat = $a / $b
    Write-Host "Resultat de la division : $resultat"
} catch {
    # Le message envoye par throw se retrouve dans $_.Exception.Message.
    Write-Host "Calcul impossible : $($_.Exception.Message)"
}

# Le script arrive ici tranquillement : grace au try / catch, rien n'a plante.
Write-Host "Fin du script (aucun plantage)."
