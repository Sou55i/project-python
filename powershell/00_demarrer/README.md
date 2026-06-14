# Module 00 — Démarrer en PowerShell

Avant d'écrire un script, comprenons **ce qu'est PowerShell** et comment lancer un premier
programme. Module surtout théorique, avec un script à la fin.

---

## 1. PowerShell : un terminal ET un langage

Comme Bash, PowerShell lit des **commandes** dans un terminal. Mais ses commandes, les
**cmdlets**, ont un nom très lisible de la forme **`Verbe-Nom`** :

| Cmdlet | Ce qu'elle fait | Équivalent Bash |
|--------|-----------------|-----------------|
| `Get-ChildItem` | lister les fichiers | `ls` |
| `Set-Location` | changer de dossier | `cd` |
| `Write-Output` | afficher quelque chose | `echo` |
| `Get-Content` | afficher le contenu d'un fichier | `cat` |

Un **script PowerShell** est un fichier `.ps1` contenant une suite de ces commandes,
exécutées de haut en bas. C'est ainsi qu'on **automatise** des tâches.

---

## 2. Les commentaires

Tout ce qui suit un `#` est un **commentaire** (ignoré par PowerShell). Pour plusieurs
lignes, on utilise `<# ... #>` :

```powershell
# Ceci est un commentaire sur une ligne.

<#
   Ceci est un commentaire
   sur plusieurs lignes.
#>
```

---

## 3. Afficher du texte

Deux façons courantes :

```powershell
Write-Host "Bonjour le monde !"   # affiche directement à l'écran (simple)
Write-Output "Bonjour"            # envoie l'objet dans le "pipeline" (plus avancé)
```

> 💡 Pour débuter, **`Write-Host`** est le plus simple : il affiche du texte, point.
> On découvrira la différence avec `Write-Output` (le pipeline) dans un module ultérieur.

---

## 4. Lancer un script

```bash
pwsh powershell/00_demarrer/premier_script.ps1
```

Sur **Windows**, tu peux aussi cliquer-droit → « Exécuter avec PowerShell », ou taper
`.\premier_script.ps1` dans une console.

> 🔒 Windows bloque parfois les scripts par sécurité. Pour ta session courante :
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

Le cycle de travail est le même qu'en Python ou Bash : **écrire → lancer → observer →
corriger** (pas de compilation, PowerShell est interprété).

---

## ▶️ À toi de jouer

```bash
pwsh powershell/00_demarrer/premier_script.ps1
```

Lis ensuite [`premier_script.ps1`](./premier_script.ps1) (tout est commenté), modifie le
texte, et relance-le.

➡️ Module suivant : [`01_les_bases`](../01_les_bases/).
