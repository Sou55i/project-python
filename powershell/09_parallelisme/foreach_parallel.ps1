# foreach_parallel.ps1
# Démo : traiter une collection EN PARALLÈLE avec ForEach-Object -Parallel.
# A besoin de PowerShell 7+ (pwsh). Vérifie ta version avec $PSVersionTable.

# On prévient l'utilisateur de ce que fait le script.
Write-Host "=== Traitement parallele avec ForEach-Object -Parallel ===" -ForegroundColor Cyan
Write-Host ""

# Notre collection de départ : une petite liste de nombres.
# (Un tableau en PowerShell, c'est des valeurs separees par des virgules.)
$nombres = 1, 2, 3, 4, 5

# Une variable « du dehors » que l'on voudra utiliser DANS le bloc parallele.
# Attention : chaque tache parallele tourne ISOLEE et ne voit pas cette variable
# directement. Pour la lui passer, on ecrira $using:prefixe (voir plus bas).
$prefixe = "carre"

# On traite chaque nombre EN PARALLELE.
#   -Parallel { ... } : le bloc est execute pour chaque element, en meme temps.
#   $_              : l'element en cours (comme dans un ForEach-Object classique).
#   $using:prefixe  : permet d'utiliser la variable $prefixe definie au-dessus.
#   -ThrottleLimit 3 : au plus 3 taches tournent en meme temps (le « robinet »).
$resultats = $nombres | ForEach-Object -Parallel {
    # $_ * $_ : le nombre courant multiplie par lui-meme (son carre).
    $valeur = $_ * $_
    # On renvoie une phrase ; $using:prefixe va chercher la variable du dehors.
    "$using:prefixe de $_ = $valeur"
} -ThrottleLimit 3

# ForEach-Object -Parallel renvoie les resultats, mais PAS forcement dans l'ordre
# de depart (les taches finissent dans le desordre). On les trie pour un affichage
# stable et previsible (pratique pour comparer / pour les tests).
$resultats = $resultats | Sort-Object

# On affiche chaque resultat, ligne par ligne.
foreach ($ligne in $resultats) {
    Write-Host "  $ligne" -ForegroundColor Green
}

Write-Host ""
Write-Host "Termine : les 5 calculs ont ete faits en parallele." -ForegroundColor Cyan
