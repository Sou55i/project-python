# Module 08 — Réutiliser du code : fonctions avancées et modules

Au fil des modules, tu as écrit de plus en plus de fonctions. Vient toujours un moment où
tu te dis : « cette fonction `Get-Carre`, je l'ai déjà écrite la semaine dernière dans un
autre script… ». Recopier du code, c'est l'erreur du débutant : si tu corriges un bug, tu
dois le corriger **partout**. La solution s'appelle la **réutilisation** : on range les
fonctions utiles dans **un seul endroit**, et tous les scripts viennent y **puiser**.

> 🧰 **Analogie.** Imagine une **caisse à outils**. Tu n'achètes pas un nouveau tournevis
> pour chaque meuble : tu ouvres la caisse, tu prends le tournevis, tu l'utilises, tu le
> ranges. Un **module** PowerShell, c'est exactement ça : une caisse à outils (des
> fonctions) que n'importe quel script peut **ouvrir** et **utiliser**.

---

## 1. Le problème : ne pas se répéter

Une bonne règle de programmation : **DRY** — *Don't Repeat Yourself* (« ne te répète
pas »). Plutôt que de recopier les mêmes fonctions dans dix scripts, on les écrit **une
fois** dans un fichier dédié, et chaque script va les **chercher** quand il en a besoin.

---

## 2. Rappel : la fonction avancée (typée, avec `return`)

Avant de ranger nos fonctions, écrivons-les proprement. Une **fonction avancée**, c'est une
fonction qui :

- déclare ses entrées dans un bloc **`param( ... )`** avec des **types** (`[int]`,
  `[string]`…), comme vu au module 04 ;
- renvoie un résultat clair avec **`return`**.

```powershell
function Get-Carre {
    param(
        [int]$Nombre        # l'entrée, typée : un entier
    )
    return $Nombre * $Nombre  # on RENVOIE le résultat à l'appelant
}
```

> 💡 En PowerShell, toute valeur « lâchée » dans une fonction part vers la sortie. Écrire
> `return` explicitement rend l'intention **limpide** : « voici le résultat, et je m'arrête ».

---

## 3. Le fichier MODULE `.psm1`

Un **module** est un simple fichier texte dont l'extension est **`.psm1`** (au lieu de
`.ps1`). On y place **uniquement des définitions de fonctions** : pas de code qui s'exécute
tout seul, juste la boîte à outils. Notre module s'appelle `outils.psm1`.

> 🐍 **En Python**, tu ranges tes fonctions dans un fichier `outils.py`, puis tu écris
> `import outils` (ou `from outils import get_carre`). Un fichier `.psm1`, c'est le **même
> rôle** : un fichier qui regroupe des fonctions destinées à être importées ailleurs.

---

## 4. Choisir ce qu'on expose : `Export-ModuleMember`

Dans un module, on précise **quelles fonctions sont publiques** (visibles de l'extérieur)
grâce à **`Export-ModuleMember -Function ...`**, tout en bas du fichier. Les fonctions non
exportées restent **privées** : elles servent en interne au module, mais l'appelant ne les
voit pas.

```powershell
Export-ModuleMember -Function Get-Carre, Test-Pair
```

> 🔒 C'est une question de **propreté** : tu n'exposes que les outils finis. Comme une vraie
> caisse à outils dont certains compartiments restent fermés.

---

## 5. Importer le module : `Import-Module`

Côté script, on **ouvre la caisse** avec **`Import-Module`**, en lui donnant le chemin du
fichier `.psm1` :

```powershell
Import-Module ./outils.psm1 -Force
```

- L'option **`-Force`** dit : « recharge le module même s'il était déjà chargé ». Très utile
  quand tu modifies le module et relances le script : tu obtiens toujours la **dernière
  version**.
- Pour que le chemin marche **où que tu lances le script**, on s'appuie sur la variable
  automatique **`$PSScriptRoot`** : elle vaut toujours le dossier **du script lui-même**.

```powershell
Import-Module "$PSScriptRoot/outils.psm1" -Force
```

> 🐧 **En Bash**, l'équivalent du « charger des fonctions depuis un autre fichier » s'appelle
> le **`source`** (ou son raccourci `.`) : `source outils.sh`. Ça **injecte** les fonctions du
> fichier dans le shell courant.

---

## 6. Le « dot-sourcing » `. ./fichier.ps1`

PowerShell connaît aussi cette idée du `source` Bash : ça s'appelle le **dot-sourcing**. On
met un **point**, une **espace**, puis le chemin d'un script `.ps1` :

```powershell
. ./fichier.ps1      # le point + espace : on EXÉCUTE le fichier DANS le contexte courant
```

La différence avec un appel normal (`./fichier.ps1`) : sans le point, le script tourne dans
son propre coin et ses fonctions/variables disparaissent ensuite. **Avec** le point, ses
définitions **restent disponibles** après coup.

| Façon de réutiliser | PowerShell | Équivalent ailleurs |
|---------------------|-----------|---------------------|
| Module dédié        | `Import-Module ./outils.psm1` | `import outils` (Python) |
| Charger un script   | `. ./fichier.ps1` (dot-sourcing) | `source fichier.sh` (Bash) |

> 💡 **Règle simple pour débuter :** pour une vraie boîte à outils partagée, préfère le
> **module `.psm1` + `Import-Module`**. Garde le **dot-sourcing** pour charger vite fait un
> petit script de fonctions.

---

## 7. Utiliser les fonctions importées

Une fois le module importé, ses fonctions s'utilisent **comme si tu les avais écrites sur
place** : tu captures leur résultat dans une variable, tu testes leur booléen avec `if`…

```powershell
$resultat = Get-Carre -Nombre 5     # on CAPTURE le résultat (25)
if (Test-Pair -Nombre 4) {          # Test-Pair renvoie $true / $false
    Write-Host "4 est pair"
}
```

---

## ▶️ À toi de jouer

Ce module contient deux fichiers :

- **`outils.psm1`** : la caisse à outils (les fonctions `Get-Carre` et `Test-Pair`).
- **`utiliser.ps1`** : un script qui **importe** le module et **se sert** de ses fonctions.

```powershell
pwsh powershell/08_modules/utiliser.ps1
```

Lis les deux fichiers, puis **enrichis** la caisse à outils : ajoute une fonction (par
exemple `Get-Cube`), pense à l'**exporter** avec `Export-ModuleMember`, puis appelle-la
depuis `utiliser.ps1`.

➡️ La suite du parcours arrivera dans le même style.
