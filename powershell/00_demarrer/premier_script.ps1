<#
   MODULE 00 - Premier script PowerShell
   =====================================
   Ton tout premier script. Objectif : voir le cycle « écrire -> lancer -> observer ».

   Pour le lancer, ouvre un terminal et tape :
       pwsh powershell/00_demarrer/premier_script.ps1

   Les commentaires sont ignorés par PowerShell : sur une ligne avec #,
   ou sur plusieurs lignes entre <# et #> (comme ce bloc).
#>

# Write-Host affiche du texte à l'écran. Mets-le entre guillemets doubles "...".
Write-Host "Bonjour le monde ! 👋"
Write-Host "Je viens de lancer mon premier script PowerShell."

# Le script s'exécute de haut en bas, une ligne après l'autre.
Write-Host "Cette ligne s'affiche apres les precedentes."

# À TOI : change le texte ci-dessus, ajoute un Write-Host, puis relance le script.
Write-Host "Fin du script. Relance-le apres l'avoir modifie. 🚀"
