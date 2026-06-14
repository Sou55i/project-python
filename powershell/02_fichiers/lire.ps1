<#
   MODULE 02 - Lire un fichier
   ===========================
   Lit "exemples/notes.txt" avec Get-Content et l'affiche ligne par ligne,
   en verifiant d'abord que le fichier existe (Test-Path).

   Lance-le :  pwsh powershell/02_fichiers/lire.ps1
   (Lance d'abord ecrire.ps1 pour creer le fichier.)

   🗺️ CHEMINEMENT DU SCRIPT
   1. On range le chemin du fichier dans une variable.
   2. Test-Path : le fichier existe-t-il ?
        - NON  -> on affiche un message et on s'arrete proprement (return).
        - OUI  -> on continue.
   3. Get-Content lit le fichier et renvoie un TABLEAU de lignes.
   4. Une boucle foreach affiche chaque ligne, une par une.
#>

# ─────────────────────────────────────────────
# 1. LE CHEMIN DU FICHIER A LIRE
# ─────────────────────────────────────────────
$fichier = "exemples/notes.txt"

# ─────────────────────────────────────────────
# 2. VERIFIER QUE LE FICHIER EXISTE (Test-Path)
# ─────────────────────────────────────────────
# Lire un fichier absent provoquerait une erreur. Test-Path renvoie $true ou $false.
# -not inverse la reponse : "si le fichier N'existe PAS, alors...".
if (-not (Test-Path -Path $fichier)) {
    Write-Host "Le fichier '$fichier' n'existe pas encore."
    Write-Host "Lance d'abord : pwsh powershell/02_fichiers/ecrire.ps1"
    return                          # on arrete le script ici, proprement
}

# ─────────────────────────────────────────────
# 3. LIRE LE FICHIER (Get-Content renvoie un TABLEAU de lignes)
# ─────────────────────────────────────────────
$lignes = Get-Content -Path $fichier -Encoding utf8

Write-Host "Contenu de $fichier ($($lignes.Count) lignes) :"

# ─────────────────────────────────────────────
# 4. AFFICHER CHAQUE LIGNE, UNE PAR UNE (foreach)
# ─────────────────────────────────────────────
foreach ($ligne in $lignes) {
    Write-Host $ligne
}
