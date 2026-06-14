<#
   MODULE 05 - Les tables de hachage (hashtables) en PowerShell
   ============================================================
   Une table de hachage range des paires CLÉ -> VALEUR. On retrouve une
   valeur grâce à sa clé (un nom), pas grâce à une position.
   Equivalent du DICTIONNAIRE en Python.

   🗺️ CHEMINEMENT DU SCRIPT
   ------------------------
   1. On crée une table de hachage : un nom -> un age.
   2. On LIT l'age d'une personne par sa clé (deux ecritures possibles).
   3. On AJOUTE une nouvelle personne.
   4. On PARCOURT toutes les paires cle/valeur (deux methodes).

   Lance-le :  pwsh powershell/05_collections/hashtables.ps1
#>

# ─────────────────────────────────────────────
# 1. CRÉER une table de hachage avec @{ } (paires cle = valeur, separees par ;)
# ─────────────────────────────────────────────
$age = @{ alice = 30; bob = 25 }

# ─────────────────────────────────────────────
# 2. LIRE une valeur par sa CLÉ (deux ecritures, au choix)
# ─────────────────────────────────────────────
Write-Host "Age d'Alice (crochets) : $($age['alice'])"   # ecriture avec [ ]
Write-Host "Age de Bob (point)     : $($age.bob)"         # ecriture courte avec .

# ─────────────────────────────────────────────
# 3. AJOUTER une paire (la meme ecriture MODIFIE si la cle existe deja)
# ─────────────────────────────────────────────
$age["chloe"] = 35
Write-Host "Apres ajout, il y a $($age.Count) personnes"

# ─────────────────────────────────────────────
# 4. PARCOURIR les paires cle/valeur
# ─────────────────────────────────────────────
# Methode A : on parcourt les CLÉS (.Keys), puis on lit la valeur de chaque cle.
Write-Host "--- via .Keys ---"
foreach ($nom in $age.Keys) {
    Write-Host "$nom a $($age[$nom]) ans"
}

# Methode B : on parcourt les PAIRES avec .GetEnumerator() ; chaque paire a
# une propriete .Key (la cle) et .Value (la valeur).
Write-Host "--- via .GetEnumerator() ---"
foreach ($paire in $age.GetEnumerator()) {
    Write-Host "$($paire.Key) a $($paire.Value) ans"
}
