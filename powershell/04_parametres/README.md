# Module 04 — Les paramètres (`param`)

Jusqu'ici, nos scripts et nos fonctions faisaient toujours **exactement la même chose**.
Un vrai **outil réutilisable**, lui, accepte des **entrées** qui changent son comportement :
on lui dit *sur quoi* travailler. En PowerShell, ces entrées s'appellent des **paramètres**,
et on les déclare dans un bloc **`param( ... )`**.

> C'est l'équivalent de **`argparse`** en Python ou de **`getopts`** en Bash : un même
> script, mais des résultats différents selon ce qu'on lui passe.

> Fichiers du module : `fonction_param.ps1` (param dans une fonction) et `script_param.ps1`
> (param dans un script entier). Lance-les avec `pwsh <fichier>` (voir en bas).

---

## 1. Le bloc `param( ... )`

Le bloc `param( ... )` se place **tout en haut** : soit au début d'une **fonction**, soit
au tout début d'un **script** (avant toute autre instruction). Il liste les paramètres,
séparés par des **virgules** :

```powershell
function Get-Salutation {
    param(
        $Nom,
        $Fois
    )
    # ... le corps de la fonction utilise $Nom et $Fois
}
```

Chaque paramètre est une **variable** (elle commence par `$`) que tu peux utiliser dans
le corps, comme n'importe quelle autre variable.

---

## 2. Les paramètres typés : `[string]$Nom`

Comme pour les variables, on peut **forcer le type** d'un paramètre en mettant un nom de
type entre crochets devant. PowerShell refusera (ou convertira) ce qui ne correspond pas :

```powershell
param(
    [string]$Nom,    # une chaîne de caractères
    [int]$Fois       # un nombre entier
)
```

> 💡 Typer les paramètres, c'est se protéger : si quelqu'un passe du texte là où tu attends
> un nombre, le problème est signalé tout de suite, clairement.

---

## 3. Les valeurs par défaut : `[int]$Fois = 1`

On peut donner une **valeur par défaut** à un paramètre avec `=`. Si l'appelant ne le
fournit pas, c'est cette valeur qui est utilisée. Le paramètre devient donc **optionnel** :

```powershell
param(
    [string]$Nom,
    [int]$Fois = 1     # si on ne précise rien, $Fois vaut 1
)
```

---

## 4. Les paramètres obligatoires : `[Parameter(Mandatory)]`

À l'inverse, pour rendre un paramètre **obligatoire**, on l'annote avec
`[Parameter(Mandatory)]`. Si l'appelant l'oublie, PowerShell le **réclame** au lieu de
planter avec une valeur vide :

```powershell
param(
    [Parameter(Mandatory)]
    [string]$Nom,        # obligatoire : impossible de l'oublier

    [int]$Fois = 1       # optionnel : 1 par défaut
)
```

---

## 5. L'appel par nom : `-Nom Alice`

Pour passer une valeur, on **nomme** le paramètre avec un tiret, suivi de sa valeur. C'est
le style PowerShell, **lisible** car on voit à quoi sert chaque valeur :

```powershell
Get-Salutation -Nom "Alice"            # $Fois prend sa valeur par défaut (1)
Get-Salutation -Nom "Bob" -Fois 3      # on précise les deux
```

L'ordre des arguments **nommés** n'a pas d'importance : `-Fois 3 -Nom "Bob"` marche aussi.

> 💡 **`[CmdletBinding()]`** : placée juste avant `param( ... )`, cette annotation transforme
> ta fonction en « vraie » cmdlet (elle gagne gratuitement des options comme `-Verbose`).

---

## 6. Un script qui prend des paramètres

Un **script entier** peut commencer par un bloc `param( ... )`. On passe alors les valeurs
**sur la ligne de commande**, après le nom du fichier :

```powershell
# Dans script_param.ps1, tout en haut :
param([string]$Nom = "le monde")
Write-Host "Bonjour $Nom"
```

On l'appelle ainsi (essaie les deux) :

```bash
pwsh powershell/04_parametres/script_param.ps1            # affiche : Bonjour le monde
pwsh powershell/04_parametres/script_param.ps1 -Nom Alice # affiche : Bonjour Alice
```

Le même script donne deux résultats différents : il est devenu **réutilisable**.

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/04_parametres/fonction_param.ps1
pwsh powershell/04_parametres/script_param.ps1 -Nom Alice
```

Lis les deux fichiers, puis **modifie-les** : ajoute un paramètre, rends-en un obligatoire,
change une valeur par défaut.

➡️ La suite du parcours arrivera dans le même style.
