<#
   MODULE 07 - Debugger un script PowerShell
   =========================================
   Ce script est CORRECT : il ne plante pas. Son but est de te MONTRER, en vrai,
   deux outils de debogage : la trace pas a pas (Set-PSDebug -Trace 1) et les
   messages Write-Debug que l'on allume avec la variable speciale DebugPreference.

   Lance-le :  pwsh powershell/07_debugger/demo_debug.ps1

   CHEMINEMENT DU SCRIPT (les grandes etapes, dans l'ordre) :
      1. Allumer les messages de debug (DebugPreference sur Continue).
      2. Calculer une moyenne, avec des Write-Debug pour suivre les valeurs.
      3. Activer la trace pas a pas, derouler une petite boucle, puis la couper.
      4. Recouper les messages de debug et conclure proprement.
#>

# La ligne ci-dessus en forme de carte (emoji) figure dans le README ; ici on reste sobre
# pour que la trace reste lisible. On va maintenant suivre les 4 etapes annoncees.

# -----------------------------------------------------------------------------
# 1. ALLUMER LES MESSAGES DE DEBUG
# -----------------------------------------------------------------------------
# Par defaut, Write-Debug n'affiche RIEN. On regle DebugPreference sur 'Continue'
# pour que nos messages de debug deviennent visibles.
$DebugPreference = 'Continue'

Write-Host "=== Calcul d'une moyenne (avec messages de debug) ==="

# -----------------------------------------------------------------------------
# 2. UN CALCUL SUIVI PAS A PAS AVEC Write-Debug
# -----------------------------------------------------------------------------
# On part d'une liste de notes. On veut leur moyenne.
$notes = 12, 8, 15, 10

# Write-Debug nous montre le contenu de la variable (utile quand un bug se cache la).
Write-Debug "Les notes sont : $notes"

# On additionne les notes une par une, en affichant le total a chaque tour.
$total = 0
foreach ($note in $notes) {
    # On ajoute la note courante au total. Attention a bien ecrire $total (le $ !).
    $total = $total + $note
    # Ce message n'apparait que parce que DebugPreference vaut 'Continue'.
    Write-Debug "Apres avoir ajoute $note, le total vaut $total"
}

# .Count donne le nombre d'elements ; on s'en sert pour diviser le total.
$moyenne = $total / $notes.Count
Write-Host "Moyenne = $moyenne"

# -----------------------------------------------------------------------------
# 3. LA TRACE PAS A PAS : on l'ALLUME, on deroule, puis on la COUPE
# -----------------------------------------------------------------------------
Write-Host "=== Trace pas a pas d'une petite boucle ==="

# A partir d'ici, PowerShell affiche chaque ligne (precedee de DEBUG:) avant de l'executer.
Set-PSDebug -Trace 1

# Petite boucle volontairement simple, pour voir la trace defiler ligne par ligne.
foreach ($i in 1..3) {
    # On compare avec -lt (plus petit que) : en PowerShell on n'utilise JAMAIS le chevron.
    if ($i -lt 3) {
        Write-Host "Tour numero $i (encore des tours apres)"
    } else {
        Write-Host "Tour numero $i (le dernier)"
    }
}

# TRES IMPORTANT : on COUPE la trace, sinon tout le reste du script defilerait aussi.
Set-PSDebug -Off

# -----------------------------------------------------------------------------
# 4. ON RECOUPE LE DEBUG ET ON CONCLUT
# -----------------------------------------------------------------------------
# On remet DebugPreference a sa valeur par defaut : les Write-Debug se taisent a nouveau.
$DebugPreference = 'SilentlyContinue'

# Ce message de debug ne s'affichera PLUS (la preference est revenue a SilentlyContinue).
Write-Debug "Ceci ne devrait PAS apparaitre."

Write-Host "Fin du script : trace coupee, debug recoupe, tout est propre."
