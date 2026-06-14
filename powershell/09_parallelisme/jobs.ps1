<#
🗺️ CHEMINEMENT DU SCRIPT
1. On lance 3 taches en arriere-plan avec Start-Job (elles demarrent EN MEME TEMPS).
   Chaque tache « attend » un peu (Start-Sleep) pour imiter du reseau ou du disque.
2. On attend que les 3 taches soient terminees avec Wait-Job.
   Comme elles ont attendu en parallele, le total est proche de la PLUS LONGUE,
   pas de la SOMME des durees.
3. On recupere le resultat de chaque tache avec Receive-Job.
4. On agrege (on additionne) les resultats et on affiche le total.
#>

# On annonce ce que fait le script.
Write-Host "=== Taches en arriere-plan avec Start-Job ===" -ForegroundColor Cyan
Write-Host ""

# --- Etape 1 : lancer les taches en arriere-plan -------------------------------
# Start-Job demarre un travail « sur le cote » et REND LA MAIN tout de suite.
# Il renvoie un objet « job » que l'on range dans une variable pour le retrouver.
# Le bloc -ScriptBlock { ... } est le travail a faire :
#   Start-Sleep imite une ATTENTE (reseau, disque...) ; puis on renvoie un nombre.
Write-Host "Lancement de 3 taches..." -ForegroundColor Yellow

$job1 = Start-Job -ScriptBlock { Start-Sleep -Seconds 1; 10 }
$job2 = Start-Job -ScriptBlock { Start-Sleep -Seconds 1; 20 }
$job3 = Start-Job -ScriptBlock { Start-Sleep -Seconds 1; 30 }

# On regroupe les 3 jobs dans un tableau, c'est plus pratique a manipuler ensuite.
$jobs = $job1, $job2, $job3

# --- Etape 2 : attendre la fin des taches --------------------------------------
# Wait-Job met le script EN PAUSE jusqu'a ce que les jobs listes soient finis.
# Out-Null : on jette l'affichage de Wait-Job, on veut juste attendre ici.
Write-Host "On attend que les 3 taches soient terminees..." -ForegroundColor Yellow
Wait-Job -Job $jobs | Out-Null

# --- Etape 3 : recuperer les resultats -----------------------------------------
# Receive-Job va chercher ce que chaque job a PRODUIT (sa valeur renvoyee).
$r1 = Receive-Job -Job $job1
$r2 = Receive-Job -Job $job2
$r3 = Receive-Job -Job $job3

Write-Host ""
Write-Host "Resultats recuperes : $r1, $r2, $r3" -ForegroundColor Green

# --- Etape 4 : agreger (additionner) et afficher -------------------------------
# On additionne les trois resultats pour obtenir un total.
$total = $r1 + $r2 + $r3
Write-Host "Total agrege : $total" -ForegroundColor Green

# Bonne habitude : on fait le menage en supprimant les jobs termines.
Remove-Job -Job $jobs

Write-Host ""
Write-Host "Termine : 3 taches lancees en parallele, ~1 s au lieu de ~3 s." -ForegroundColor Cyan
