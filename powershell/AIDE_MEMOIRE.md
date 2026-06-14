# 🃏 Aide-mémoire PowerShell (cheat-sheet)

Une page pour retrouver vite la syntaxe essentielle. Garde-la sous la main.
Pour les explications détaillées, retourne aux modules `00_demarrer`, `01_les_bases` et suivants.

---

## Lancer un script

```powershell
pwsh mon_script.ps1        # lancer le script avec PowerShell
./mon_script.ps1           # lancer directement (depuis le dossier)

# Si « l'exécution de scripts est désactivée » :
Get-ExecutionPolicy                              # voir la règle actuelle
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned   # autoriser tes scripts
pwsh -ExecutionPolicy Bypass -File mon_script.ps1     # juste pour cette fois
```

## Afficher et commenter

```powershell
Write-Host "Bonjour"       # afficher une ligne à l'écran
# ceci est un commentaire (ignoré par PowerShell)

<#
Commentaire sur
plusieurs lignes (bloc).
#>
```

## Variables

```powershell
$x = 5                     # une variable commence par $
$nom = "Alice"
Write-Host "$nom"          # guillemets doubles : insère la variable
Write-Host '$nom'          # guillemets simples : affiche tel quel ($nom)
Write-Host "Total : $($x + 1)"   # $( ) pour insérer un calcul
```

## Types

```powershell
[int]    $age = 30         # entier
[double] $prix = 9.99      # nombre à virgule (point décimal)
[string] $nom = "Alice"    # texte
[bool]   $actif = $true    # vrai/faux : $true ou $false (avec le $ !)

$age.GetType().Name        # connaître le type
[int]"42"                  # convertir un texte en entier
```

## Demander une saisie (Read-Host)

```powershell
$nom = Read-Host "Ton nom ?"          # renvoie TOUJOURS du texte
$age = [int](Read-Host "Ton âge ?")   # convertir pour calculer
$mdp = Read-Host "Mot de passe" -AsSecureString   # saisie masquée
```

## Comparaisons

```powershell
# JAMAIS < > == en PowerShell ! On utilise des mots :
-eq  -ne          # égal, différent
-lt  -le  -gt  -ge   # <, <=, >, >=
-and  -or  -not   # ET, OU, NON logiques (! marche aussi pour NON)

if ($age -ge 18 -and $actif) { Write-Host "OK" }
```

## Conditions

```powershell
if ($age -ge 18) {
    Write-Host "Majeur"
} elseif ($age -ge 13) {
    Write-Host "Ado"
} else {
    Write-Host "Enfant"
}
```

## Boucles

```powershell
for ($i = 0; $i -lt 5; $i++) {        # 0,1,2,3,4
    Write-Host $i
}

foreach ($fruit in "pomme","kiwi") {  # pour chaque élément
    Write-Host $fruit
}

while ($n -lt 10) {                   # tant que la condition est vraie
    $n++
}
```

## Fonctions

```powershell
function Get-Salutation {
    param(
        [string]$Nom,
        [bool]$Poli = $true        # valeur par défaut
    )
    if ($Poli) { return "Bonjour $Nom" }
    return "Salut $Nom"
}

Get-Salutation -Nom "Alice"        # appel (Verbe-Nom : nom recommandé)
```

## Paramètres du script

```powershell
# Tout en haut du fichier .ps1 :
param(
    [string]$Nom = "monde",
    [int]$Fois = 1
)
Write-Host "Bonjour $Nom"          # ./script.ps1 -Nom Alice -Fois 3
```

## Tableaux et tables de hachage

```powershell
$fruits = @("pomme", "kiwi", "banane")   # tableau (numéroté à partir de 0)
$fruits[0]                 # premier élément
$fruits.Count              # nombre d'éléments
$fruits += "orange"        # ajouter à la fin

$personne = @{ Nom = "Alice"; Age = 30 } # table de hachage (clé -> valeur)
$personne["Nom"]           # accès par clé -> "Alice"
$personne["Ville"] = "Paris"             # ajouter / modifier
```

## Pipeline d'objets ( | )

```powershell
# Le | passe des OBJETS d'une commande à l'autre ; $_ = l'objet courant
Get-ChildItem |
    Where-Object { $_.Length -gt 1000 } |   # filtrer
    Sort-Object Length |                     # trier
    Select-Object Name, Length |             # garder certaines colonnes
    ForEach-Object { Write-Host $_.Name }    # agir sur chacun

1,2,3,4 | Measure-Object -Sum -Average       # compter / additionner / moyenne
```

## Fichiers

```powershell
Set-Content notes.txt "ligne"      # écrire (écrase le contenu)
Add-Content notes.txt "suite"      # ajouter à la fin
$contenu = Get-Content notes.txt   # lire (tableau de lignes)

if (Test-Path notes.txt) {         # le fichier existe-t-il ?
    Write-Host "présent"
}
```

## Robustesse (gérer les erreurs)

```powershell
try {
    Get-Content "absent.txt" -ErrorAction Stop   # Stop = vraie erreur attrapable
} catch {
    Write-Host "Erreur : $_"       # on attrape sans planter
} finally {
    Write-Host "toujours exécuté"  # nettoyage quoi qu'il arrive
}

throw "message d'erreur"           # déclencher soi-même une erreur
```

## Modules (réutiliser du code)

```powershell
Import-Module ./outils.psm1        # charge les fonctions d'un autre fichier
Import-Module Pester               # charge un module installé
# Un fichier .psm1 regroupe tes fonctions pour les partager entre scripts
```

➡️ Voir aussi : [GLOSSAIRE.md](./GLOSSAIRE.md) et [ANATOMIE_D_UN_SCRIPT.md](./ANATOMIE_D_UN_SCRIPT.md).
