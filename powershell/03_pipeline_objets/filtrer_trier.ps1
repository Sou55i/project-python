<#
   🗺️ CHEMINEMENT DU SCRIPT (filtrer_trier.ps1)
   ============================================
   Objectif : a partir d'une liste d'objets "produits", on FILTRE, on TRIE,
   puis on COMPTE et on AGREGE. Tout reste reproductible : on fabrique nos
   propres objets, on ne lit aucun fichier du systeme.

   Etape 1 - On cree une liste d'objets produits (.Nom, .Prix, .Categorie, .Stock).
   Etape 2 - Where-Object : on garde les produits en stock et a moins de 50 euros.
   Etape 3 - Sort-Object  : on trie ces produits du moins cher au plus cher.
   Etape 4 - Measure-Object : on compte combien il en reste, et on calcule
             la somme et la moyenne de leur prix.
   Etape 5 - Bonus : on compte les produits par categorie (Group-Object).

   Rappel : dans le |, ce sont des OBJETS qui circulent. $_ = l'objet courant.
   Comparaisons avec -lt / -ge / -eq (jamais < > ==).

   Lance-le :  pwsh powershell/03_pipeline_objets/filtrer_trier.ps1
#>

# ─────────────────────────────────────────────
# ETAPE 1 : la liste d'objets (notre "catalogue")
# ─────────────────────────────────────────────
$produits = @(
    [pscustomobject]@{ Nom = "Stylo";    Prix = 2;   Categorie = "Bureau";  Stock = $true  }
    [pscustomobject]@{ Nom = "Cahier";   Prix = 5;   Categorie = "Bureau";  Stock = $true  }
    [pscustomobject]@{ Nom = "Casque";   Prix = 80;  Categorie = "Audio";   Stock = $true  }
    [pscustomobject]@{ Nom = "Souris";   Prix = 25;  Categorie = "Info";    Stock = $false }
    [pscustomobject]@{ Nom = "Clavier";  Prix = 45;  Categorie = "Info";    Stock = $true  }
    [pscustomobject]@{ Nom = "Cable";    Prix = 8;   Categorie = "Info";    Stock = $true  }
)

Write-Host "Catalogue de depart : $($produits.Count) produits."
Write-Host ""

# ─────────────────────────────────────────────
# ETAPE 2 : FILTRER avec Where-Object
# ─────────────────────────────────────────────
# On garde les produits EN STOCK ($_.Stock vrai) ET a moins de 50 euros.
# -and combine les deux conditions ; $_ est l'objet en cours.
$abordables = $produits | Where-Object { $_.Stock -and $_.Prix -lt 50 }

Write-Host "--- En stock et a moins de 50 euros ---"
$abordables | ForEach-Object { Write-Host "  $($_.Nom) : $($_.Prix) euros" }
Write-Host ""

# ─────────────────────────────────────────────
# ETAPE 3 : TRIER avec Sort-Object
# ─────────────────────────────────────────────
# Du moins cher au plus cher (ordre croissant par defaut).
Write-Host "--- Les memes, tries du moins cher au plus cher ---"
$abordables |
    Sort-Object Prix |
    ForEach-Object { Write-Host "  $($_.Prix) euros - $($_.Nom)" }
Write-Host ""

# ─────────────────────────────────────────────
# ETAPE 4 : COMPTER et AGREGER avec Measure-Object
# ─────────────────────────────────────────────
# Sans propriete : Measure-Object compte les objets (.Count).
$nombre = ($abordables | Measure-Object).Count
Write-Host "Nombre de produits retenus : $nombre"

# Avec une propriete et -Sum -Average : il totalise et fait la moyenne.
$stats = $abordables | Measure-Object Prix -Sum -Average -Minimum -Maximum
Write-Host "Prix total   : $($stats.Sum) euros"
Write-Host "Prix moyen   : $($stats.Average) euros"
Write-Host "Le moins cher: $($stats.Minimum) euros"
Write-Host "Le plus cher : $($stats.Maximum) euros"
Write-Host ""

# ─────────────────────────────────────────────
# ETAPE 5 (bonus) : COMPTER PAR CATEGORIE avec Group-Object
# ─────────────────────────────────────────────
# Group-Object regroupe les objets qui partagent la meme valeur de propriete.
# Chaque groupe a une propriete .Name (la categorie) et .Count (le nombre).
Write-Host "--- Nombre de produits par categorie (catalogue complet) ---"
$produits |
    Group-Object Categorie |
    Sort-Object Count -Descending |
    ForEach-Object { Write-Host "  $($_.Name) : $($_.Count) produit(s)" }
