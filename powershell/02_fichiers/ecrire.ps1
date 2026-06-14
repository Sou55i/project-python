<#
   MODULE 02 - Ecrire dans un fichier
   ==================================
   Cree un dossier "exemples", puis ecrit quelques lignes dans
   "exemples/notes.txt" avec Set-Content (ecrase) et Add-Content (ajoute).

   Lance-le :  pwsh powershell/02_fichiers/ecrire.ps1
#>

# ─────────────────────────────────────────────
# 1. CREER LE DOSSIER QUI VA CONTENIR LE FICHIER
# ─────────────────────────────────────────────
# -ItemType Directory : on veut un DOSSIER (et non un fichier).
# -Force : cree le dossier s'il manque, et ne provoque pas d'erreur s'il existe deja.
# | Out-Null : on jette les infos renvoyees par New-Item pour ne pas encombrer l'ecran.
New-Item -ItemType Directory -Path "exemples" -Force | Out-Null

# On range le chemin du fichier dans une variable, pour ne pas le repeter partout.
$fichier = "exemples/notes.txt"

# ─────────────────────────────────────────────
# 2. ECRIRE LA PREMIERE LIGNE (Set-Content ECRASE)
# ─────────────────────────────────────────────
# Set-Content repart d'une page blanche : si le fichier existait deja, son ancien
# contenu est REMPLACE. -Encoding utf8 gere correctement les accents.
Set-Content -Path $fichier -Value "Liste de courses :" -Encoding utf8

# ─────────────────────────────────────────────
# 3. AJOUTER DES LIGNES A LA SUITE (Add-Content)
# ─────────────────────────────────────────────
# Add-Content ecrit A LA FIN du fichier, sans effacer ce qui est deja la.
Add-Content -Path $fichier -Value "- des pommes" -Encoding utf8
Add-Content -Path $fichier -Value "- du pain" -Encoding utf8
Add-Content -Path $fichier -Value "- du chocolat" -Encoding utf8

# ─────────────────────────────────────────────
# 4. CONFIRMER A L'UTILISATEUR
# ─────────────────────────────────────────────
Write-Host "Fichier ecrit : $fichier"
Write-Host "Lance maintenant lire.ps1 pour voir son contenu."
