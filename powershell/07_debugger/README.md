# Module 07 — Débugger : trouver ce qui cloche dans un script

Quand un script ne fait **pas** ce que tu attends, il ne suffit pas de relire le code en
le fixant des yeux. **Débugger**, c'est mener une petite enquête : on observe ce que fait
vraiment le script, étape par étape, pour repérer **où** et **pourquoi** ça déraille.

> Fichier du module : `demo_debug.ps1` (un script correct qui te montre, en vrai, la trace
> pas à pas et les messages de débogage). Lance-le avec `pwsh <fichier>` (voir en bas).

---

## 1. Débugger par affichage : `Write-Host` et `Write-Debug`

La technique la plus simple, et la plus utilisée : **afficher** la valeur des variables aux
endroits clés, pour voir ce qui se passe réellement.

```powershell
Write-Host "DEBUG age = $age"     # on affiche la valeur pour la verifier de nos yeux
```

`Write-Host` affiche **toujours**. Pratique, mais il faut ensuite enlever ces lignes à la main.

PowerShell propose mieux : **`Write-Debug`**, un affichage **que l'on peut activer ou couper**
sans toucher au code. Par défaut, `Write-Debug` n'affiche **rien**. Pour voir ses messages, on
règle la variable spéciale **`$DebugPreference`** sur `'Continue'` :

```powershell
$DebugPreference = 'Continue'      # a partir d'ici, les Write-Debug s'affichent
Write-Debug "age vaut $age"        # ce message apparait maintenant
$DebugPreference = 'SilentlyContinue'  # on recoupe les messages de debug (valeur par defaut)
```

> 🔑 L'avantage : tu **laisses** tes `Write-Debug` dans le code. Tu les rallumes le jour où tu
> as un bug, sans rien réécrire.

---

## 2. La trace pas à pas : `Set-PSDebug -Trace 1`

Parfois on veut voir le script **dérouler chaque ligne** au fur et à mesure de son exécution.
C'est la **trace**. On l'active avec **`Set-PSDebug -Trace 1`** :

```powershell
Set-PSDebug -Trace 1     # a partir d'ici, PowerShell affiche chaque ligne avant de l'executer
# ... ton code a surveiller ...
Set-PSDebug -Off         # on ARRETE la trace (sinon tout le reste defile aussi)
```

Pendant la trace, chaque ligne s'affiche précédée de `DEBUG:` juste **avant** d'être exécutée.
Tu vois ainsi le **chemin** réellement suivi (quel `if` est entré, combien de tours de boucle…).

> ⚠️ Pense à **toujours** refermer avec `Set-PSDebug -Off`. Sinon, la trace continue pour tout
> le reste du script et l'affichage devient illisible.

> 💡 `Set-PSDebug -Trace 2` est encore plus bavard (il trace aussi l'intérieur des fonctions).
> Pour débuter, `-Trace 1` suffit largement.

---

## 3. Le détail de la dernière erreur : `Get-Error`

Quand une erreur vient de se produire, **`Get-Error`** affiche tout ce que PowerShell sait
d'elle : le message, le type, la ligne, la pile d'appels… bien plus que le message rouge habituel.

```powershell
Get-Error      # affiche le detail complet de la DERNIERE erreur survenue
```

C'est l'outil idéal **juste après** un plantage, pour comprendre la cause exacte au lieu de
deviner.

---

## 4. Les points d'arrêt : `Set-PSBreakpoint` (pour aller plus loin)

Un **point d'arrêt** (*breakpoint*) met le script **en pause** à un endroit précis, pour que tu
puisses inspecter les variables avant de continuer. On le pose avec **`Set-PSBreakpoint`** :

```powershell
Set-PSBreakpoint -Script mon_script.ps1 -Line 12   # pause a la ligne 12
```

C'est un outil **avancé** (surtout utile dans un éditeur comme VS Code). On le mentionne ici
pour que tu saches qu'il existe ; au début, l'affichage et la trace suffisent largement.

---

## 5. Tableau des erreurs FRÉQUENTES en PowerShell (cause → solution)

| Erreur / symptôme | Cause probable | Solution |
|-------------------|----------------|----------|
| `The '<' operator is reserved` (ou comportement bizarre) | Tu as utilisé `<` ou `>` pour comparer | Utilise `-lt` (plus petit) et `-gt` (plus grand) — **jamais** `<` `>` |
| Une variable semble **vide** alors que tu l'as remplie | Faute de frappe sur le `$nom` (ex : `$totl` au lieu de `$total`) | Vérifie l'orthographe **exacte** du nom de variable |
| `The term '...' is not recognized` | Cmdlet mal orthographiée (ex : `Wirte-Host`) | Corrige le nom ; respecte la forme `Verbe-Nom` (`Write-Host`) |
| `Unexpected token` / la variable n'est pas remplacée | Oubli du `$` devant une variable | Mets bien `$` devant : `nom` est un mot, `$nom` est la variable |
| Comparaison qui donne un résultat surprenant | Comparaison de **types** différents (texte vs nombre) | Compare des choses de même type : `[int]$x -eq 5`, pas `"5 " -eq 5` |

> 🔑 Le piège n°1 du débutant en PowerShell : écrire `if ($x < 5)`. En PowerShell, c'est
> **`if ($x -lt 5)`**. Les chevrons `<` `>` servent à la **redirection**, pas à la comparaison.

---

## 6. La méthode pour débugger calmement

1. **Lis le message d'erreur** : la dernière ligne te dit le *quoi*, et souvent le *où*.
2. **Affiche les valeurs** avec `Write-Host` ou `Write-Debug` juste avant la ligne suspecte.
3. **Trace le chemin** avec `Set-PSDebug -Trace 1` pour voir quelles lignes s'exécutent vraiment.
4. **Inspecte la dernière erreur** avec `Get-Error` pour le détail complet.
5. **Isole le problème** : commente des bouts de code pour réduire la zone à examiner.

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/07_debugger/demo_debug.ps1
```

Le script active la trace pas à pas sur une portion, puis la coupe, et utilise `Write-Debug`
avec `$DebugPreference`. Lis le code, observe l'affichage, puis **expérimente** : ajoute tes
propres `Write-Debug`, déplace le `Set-PSDebug -Off`, et regarde la différence.

➡️ Avec ces outils, plus aucun bug ne pourra se cacher bien longtemps. 💪
