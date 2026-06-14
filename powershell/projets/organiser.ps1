<#
   PROJET CAPSTONE - Organiser un dossier en bazar (version PowerShell)
   ====================================================================
   Le scenario classique : un dossier rempli de fichiers de toutes sortes.
   Ce script les RANGE dans des sous-dossiers selon leur extension
   (.txt -> Documents, .jpg -> Images, .csv -> Tableaux, etc.).
   C'est l'equivalent PowerShell du projet Python "ranger_dossier".

   Pour ne RIEN casser chez toi, le script fabrique d'abord un faux dossier
   de demo "exemples/bazar" rempli de fichiers VIDES, puis il le range.
   Il n'est donc PAS interactif : tu le lances et tu observes le resultat.

   Lance-le depuis la racine du depot :
      pwsh powershell/projets/organiser.ps1

   🗺️ CHEMINEMENT DU SCRIPT (les grandes etapes, dans l'ordre) :
      1. HASHTABLE  : $rangement associe une extension -> un nom de dossier.
      2. CHEMINS    : on calcule ou se trouve le dossier de demo "exemples/bazar".
      3. DEMO       : on fabrique le dossier de demo + des fichiers vides.
      4. LISTER     : Get-ChildItem donne les fichiers a ranger.
      5. BOUCLE     : pour chaque fichier, on lit son extension et on le deplace.
      6. ROBUSTESSE : tout le rangement est dans un try / catch (rien ne plante).
#>

# ─────────────────────────────────────────────
# 1. LA HASHTABLE extension -> dossier de destination (module 05).
#    Cle = l'extension du fichier (avec le point, en minuscules) ;
#    Valeur = le nom du sous-dossier ou ranger ce type de fichier.
# ─────────────────────────────────────────────
$rangement = @{
    ".txt"  = "Documents"
    ".pdf"  = "Documents"
    ".docx" = "Documents"
    ".jpg"  = "Images"
    ".jpeg" = "Images"
    ".png"  = "Images"
    ".csv"  = "Tableaux"
    ".xlsx" = "Tableaux"
    ".mp3"  = "Audio"
    ".zip"  = "Archives"
}

# ─────────────────────────────────────────────
# 2. LES CHEMINS (module 02).
#    $PSScriptRoot = le dossier ou se trouve CE script. On construit a partir
#    de la le chemin du dossier de demo, pour que ca marche peu importe d'ou
#    on lance la commande.
# ─────────────────────────────────────────────
$dossierDemo = Join-Path $PSScriptRoot "exemples"
$bazar       = Join-Path $dossierDemo "bazar"

# ─────────────────────────────────────────────
# 3. FABRIQUER LE DOSSIER DE DEMO + des fichiers vides (module 02).
#    New-Item -ItemType Directory -Force cree le dossier s'il manque, sans
#    rouspeter s'il existe deja. | Out-Null jette l'affichage pour rester propre.
# ─────────────────────────────────────────────
New-Item -ItemType Directory -Path $bazar -Force | Out-Null

# Un tableau (module 05) des faux fichiers a creer pour la demo.
$fauxFichiers = @(
    "facture.pdf", "photo_vacances.jpg", "notes.txt",
    "budget.csv", "musique.mp3", "logo.png", "archive.zip",
    "fichier_inconnu.xyz"   # extension non prevue : on le laissera tranquille
)

# Pour chaque nom, on cree un fichier VIDE (-ItemType File -Force).
foreach ($nom in $fauxFichiers) {
    $chemin = Join-Path $bazar $nom
    New-Item -ItemType File -Path $chemin -Force | Out-Null
}
Write-Host "[+] Dossier de demo pret : $bazar"

# ─────────────────────────────────────────────
# 4. + 5. + 6. RANGER : on liste, on boucle, le tout protege par try / catch.
# ─────────────────────────────────────────────
Write-Host "--- Rangement en cours ---"

# try : on met tout le rangement dans un bloc protege (module 06). Si une seule
# operation echoue (un fichier verrouille, par exemple), le catch s'en occupe
# au lieu de laisser le script planter brutalement.
try {
    # 4. LISTER : Get-ChildItem renvoie les ELEMENTS du dossier (module 03).
    #    -File ne garde que les FICHIERS (pas les sous-dossiers deja crees).
    $fichiers = Get-ChildItem -Path $bazar -File

    # 5. BOUCLE : "pour chaque fichier dans la liste des fichiers" (module 05).
    foreach ($fichier in $fichiers) {

        # $_.Extension -> ici $fichier.Extension : l'extension du fichier (".JPG").
        # .ToLower() la met en minuscules pour que ".JPG" et ".jpg" soient pareils.
        $extension = $fichier.Extension.ToLower()

        # On cherche l'extension dans la hashtable. .ContainsKey repond $true/$false.
        # Si l'extension n'est pas prevue, on ignore le fichier (on le laisse en place).
        if (-not $rangement.ContainsKey($extension)) {
            Write-Host "[ ] Ignore (extension inconnue) : $($fichier.Name)"
            # continue = saute directement au tour de boucle suivant.
            continue
        }

        # On lit le nom du dossier de destination dans la hashtable, par sa cle.
        $nomDossier  = $rangement[$extension]
        $destination = Join-Path $bazar $nomDossier

        # On cree le sous-dossier de destination s'il n'existe pas encore (-Force).
        New-Item -ItemType Directory -Path $destination -Force | Out-Null

        # Move-Item DEPLACE le fichier (couper-coller) vers son dossier de destination.
        Move-Item -Path $fichier.FullName -Destination $destination -Force
        Write-Host "[+] $($fichier.Name)  ->  $nomDossier/"
    }
}
catch {
    # 6. On arrive ici UNIQUEMENT si une erreur est survenue dans le try.
    #    $_.Exception.Message contient le texte explicatif de l'erreur.
    Write-Host "Une erreur est survenue pendant le rangement : $($_.Exception.Message)"
}

# Petit mot de fin (s'affiche que le rangement ait reussi ou ete attrape).
Write-Host "✅ Termine ! Ouvre 'exemples/bazar' pour voir les sous-dossiers ranges."
