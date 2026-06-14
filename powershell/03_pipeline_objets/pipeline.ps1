<#
   MODULE 03 - Le pipeline d'OBJETS en PowerShell
   ==============================================
   On fabrique nos PROPRES objets (pas de fichiers du systeme, pour que le
   resultat soit toujours identique), puis on les fait circuler dans le pipe |
   a travers les cmdlets cles : Where-Object, Sort-Object, Select-Object,
   ForEach-Object.

   Idee centrale : dans le | de PowerShell, ce sont des OBJETS qui voyagent
   (avec des proprietes nommees comme .Nom ou .Age), pas du texte comme en Bash.

   Lance-le :  pwsh powershell/03_pipeline_objets/pipeline.ps1
#>

# ─────────────────────────────────────────────
# 1. FABRIQUER UNE LISTE D'OBJETS
# ─────────────────────────────────────────────
# [pscustomobject]@{ ... } cree un OBJET avec des proprietes nommees.
# Ici, chaque objet est une "fiche personne" avec .Nom, .Age et .Ville.
$personnes = @(
    [pscustomobject]@{ Nom = "Alice";   Age = 30; Ville = "Paris"  }
    [pscustomobject]@{ Nom = "Bob";     Age = 17; Ville = "Lyon"   }
    [pscustomobject]@{ Nom = "Chloe";   Age = 25; Ville = "Paris"  }
    [pscustomobject]@{ Nom = "David";   Age = 42; Ville = "Nantes" }
    [pscustomobject]@{ Nom = "Emma";    Age = 16; Ville = "Lyon"   }
)

# On accede a une propriete avec un point. Pas besoin de decouper du texte !
Write-Host "Le premier de la liste : $($personnes[0].Nom), $($personnes[0].Age) ans"
Write-Host ""

# ─────────────────────────────────────────────
# 2. Where-Object : FILTRER (garder certains objets)
# ─────────────────────────────────────────────
# Le test est entre { }. $_ veut dire "l'objet en cours de traitement".
# Ici : on ne garde que les personnes majeures (Age >= 18).
Write-Host "--- Where-Object : les majeurs (Age -ge 18) ---"
$majeurs = $personnes | Where-Object { $_.Age -ge 18 }
$majeurs | ForEach-Object { Write-Host "  $($_.Nom) ($($_.Age) ans)" }
Write-Host ""

# ─────────────────────────────────────────────
# 3. Sort-Object : TRIER selon une propriete
# ─────────────────────────────────────────────
# Par defaut, du plus petit au plus grand. -Descending inverse l'ordre.
Write-Host "--- Sort-Object : tries par Age decroissant ---"
$personnes |
    Sort-Object Age -Descending |
    ForEach-Object { Write-Host "  $($_.Nom) : $($_.Age) ans" }
Write-Host ""

# ─────────────────────────────────────────────
# 4. Select-Object : CHOISIR des proprietes / les premiers
# ─────────────────────────────────────────────
# -First 2 garde les 2 premiers objets ; Nom, Ville ne garde que ces proprietes.
Write-Host "--- Select-Object : les 2 premiers, colonnes Nom et Ville ---"
$personnes |
    Select-Object -First 2 Nom, Ville |
    Format-Table -AutoSize | Out-Host
Write-Host ""

# ─────────────────────────────────────────────
# 5. ForEach-Object : AGIR sur chaque objet
# ─────────────────────────────────────────────
# Un geste par objet. Ici, on fabrique une phrase a partir des proprietes.
Write-Host "--- ForEach-Object : une phrase par personne ---"
$personnes | ForEach-Object {
    Write-Host "  $($_.Nom) habite a $($_.Ville)."
}
Write-Host ""

# ─────────────────────────────────────────────
# 6. TOUT ENCHAINER (la phrase complete)
# ─────────────────────────────────────────────
# "prends les personnes, garde les majeures, trie par age, montre les 3 premieres".
Write-Host "--- Pipeline complet : majeurs, tries par Age, 3 premiers ---"
$personnes |
    Where-Object  { $_.Age -ge 18 } |
    Sort-Object   Age |
    Select-Object -First 3 Nom, Age |
    Format-Table -AutoSize | Out-Host
