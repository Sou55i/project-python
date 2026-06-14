# 📖 Glossaire — les mots de PowerShell expliqués simplement

Tu rencontres un mot que tu ne comprends pas dans les cours ? Cherche-le ici. Les termes
sont classés par ordre alphabétique, expliqués en une ou deux phrases simples, souvent
avec une mini-analogie.

---

**[CmdletBinding()]** — Une petite étiquette qu'on pose juste avant `param(...)` dans une
fonction. Elle transforme ta fonction en « vraie » cmdlet, avec des options gratuites comme
`-Verbose` ou `-ErrorAction`. Comme passer ta fonction en version pro.

**Boucle** — Une instruction qui répète des actions : `for` (compte les tours), `foreach`
(« pour chaque élément… ») ou `while` (« tant que… »). C'est le cœur de l'automatisation.

**Cmdlet** (*Verbe-Nom*) — Une commande de PowerShell, toujours nommée `Verbe-Nom` :
`Get-ChildItem`, `Set-Content`, `Sort-Object`. Le verbe dit l'action, le nom dit sur quoi.
Cette régularité te permet de deviner les commandes.

**Comparaison** (`-eq` / `-lt` / `-ge`) — Les tests qui comparent deux valeurs : `-eq`
(égal), `-ne` (différent), `-lt` (plus petit), `-gt` (plus grand), `-le` (≤), `-ge` (≥).
En PowerShell ils s'écrivent avec un tiret, pas avec `<` ou `>`.

**Condition** — Un test qui oriente le programme : `if`, `elseif`, `else`. « Si… alors… ».

**$_** (*objet courant*) — Dans un pipeline, `$_` représente l'élément en train d'être
traité. Ex : `Where-Object { $_.Length -gt 100 }` veut dire « celui dont la taille dépasse
100 ». C'est le « lui » de la phrase. (On peut aussi l'écrire `$PSItem`.)

**$PSScriptRoot** — Une variable automatique qui contient le dossier où se trouve ton
script. Pratique pour retrouver un fichier voisin sans écrire le chemin complet en dur.

**ExecutionPolicy** — Le réglage de sécurité qui décide si PowerShell a le droit de lancer
des scripts. Souvent il faut le passer à `RemoteSigned` une fois pour que tes `.ps1`
démarrent. Comme un cran de sûreté à débloquer.

**-ErrorAction** — L'option qui dit à une cmdlet comment réagir à une erreur :
`-ErrorAction Stop` (arrête et déclenche le `catch`), `SilentlyContinue` (ignore en
silence). Utile pour que `try/catch` attrape bien le problème.

**ForEach-Object** — La cmdlet qui exécute une action sur **chaque** objet d'un pipeline :
`1..3 | ForEach-Object { $_ * 2 }`. À l'intérieur, l'élément courant est `$_`.

**ForEach-Object -Parallel** — La même chose, mais qui traite plusieurs objets **en même
temps** au lieu d'un par un. Idéal pour accélérer un travail répétitif (PowerShell 7+).

**Fonction** — Un bloc de code nommé et réutilisable, défini avec `function`. Comme une
recette qu'on peut refaire à volonté. On l'appelle par son nom.

**Get-ChildItem** — La cmdlet qui liste le contenu d'un dossier (fichiers et sous-dossiers).
C'est l'équivalent de `ls` ou `dir`. Son surnom est d'ailleurs `gci`, `ls` ou `dir`.

**Get-Content / Set-Content** — `Get-Content` **lit** un fichier et te renvoie son texte ;
`Set-Content` **écrit** du texte dans un fichier (en l'écrasant). Lire vs ranger.

**Hashtable** (`@{ }`) — Un rangement de paires `clé = valeur`, entre `@{ }` :
`@{ nom = "Alice"; age = 30 }`. La clé sert d'étiquette pour retrouver la valeur. C'est le
dictionnaire de PowerShell.

**Import-Module** — La cmdlet qui charge un module pour pouvoir utiliser ses fonctions :
`Import-Module ./outils.psm1`. Comme ouvrir une boîte à outils avant de s'en servir.

**Interpolation** — Insérer une variable directement dans un texte entre **guillemets
doubles** : `"Bonjour $nom"` affiche la valeur de `$nom`. Avec des guillemets simples
`'...'`, rien n'est remplacé. Pour une propriété, encadre : `"Taille : $($f.Length)"`.

**Measure-Object** — La cmdlet qui calcule des statistiques sur une série d'objets : compter
(`-Count`), faire la somme (`-Sum`), la moyenne (`-Average`), le min, le max. Ta calculette
de pipeline.

**Module** (`.psm1`) — Un fichier `.psm1` qui regroupe des fonctions réutilisables, qu'on
charge avec `Import-Module`. Comme une bibliothèque d'outils maison.

**Objet** (*vs texte*) — Différence clé avec Bash : les cmdlets ne se passent pas du texte
mais des **objets**, des fiches avec des cases nommées (les *propriétés*). `Get-ChildItem`
te donne des fiches « fichier » avec `.Name`, `.Length`… que tu peux trier ou filtrer
proprement, sans découper du texte à la main.

**Opérateur logique** (`-and` / `-or` / `-not`) — Pour combiner plusieurs tests : `-and`
(et), `-or` (ou), `-not` (non, aussi écrit `!`). Ex : `if ($a -gt 0 -and $a -lt 10)`.

**param** — Le bloc en haut d'une fonction ou d'un script qui déclare ses entrées :
`param($nom, $age)`. Ce sont les « ingrédients » que l'appelant devra fournir.

**Pipeline** (`|`) — La barre verticale branche la sortie d'une cmdlet sur l'entrée de la
suivante : `Get-ChildItem | Where-Object { ... } | Sort-Object`. Comme un tapis roulant qui
fait passer les objets d'un poste au suivant.

**PowerShell** — Un shell **et** un langage de script, créé par Microsoft. Sa particularité :
il fait circuler des **objets** plutôt que du simple texte. Fonctionne sous Windows, Mac et
Linux.

**Propriété** — Une case nommée à l'intérieur d'un objet : un fichier a une propriété `.Name`
(son nom) et `.Length` (sa taille). On y accède avec un point : `$fichier.Name`. Comme une
étiquette sur une fiche.

**pwsh** — La commande qui lance PowerShell 7 (la version moderne, multiplateforme). Sous
l'ancien Windows PowerShell, la commande était `powershell`.

**Script** (`.ps1`) — Un fichier texte d'extension `.ps1` contenant une suite de commandes,
qu'on exécute d'un coup au lieu de les taper une par une.

**Select-Object** — La cmdlet qui **choisit** : soit certaines propriétés
(`Select-Object Name, Length`), soit un nombre d'éléments (`-First 5`, `-Last 3`). Comme ne
garder que les colonnes ou les lignes qui t'intéressent.

**Sort-Object** — La cmdlet qui **trie** les objets selon une propriété :
`Sort-Object Length` (croissant) ou `Sort-Object Length -Descending` (décroissant).

**Start-Job** — La cmdlet qui lance une tâche **en arrière-plan**, dans un processus séparé :
le terminal te rend la main tout de suite. Tu récupères le résultat plus tard avec
`Receive-Job`. Pratique pour les travaux longs.

**Tableau** (`@( )`) — Une variable qui range **plusieurs** valeurs, entre `@( )` :
`@(1, 2, 3)`. On accède à un élément par sa position, à partir de 0 : `$tab[0]` est le
premier.

**Test-Path** — La cmdlet qui vérifie si un fichier ou un dossier **existe** : renvoie
`$true` ou `$false`. Ex : `if (Test-Path "./data.txt") { ... }`. À faire avant de lire un
fichier.

**throw** — Le mot-clé qui **déclenche** volontairement une erreur : `throw "fichier
manquant"`. Le programme s'arrête (ou saute dans le `catch` le plus proche). Comme tirer la
sonnette d'alarme.

**try/catch/finally** — Le filet de sécurité : `try { ... }` tente un code risqué,
`catch { ... }` rattrape l'erreur si elle survient, et `finally { ... }` s'exécute **dans
tous les cas** (souvent pour nettoyer). Évite le plantage brutal.

**Variable** (`$`) — Une boîte étiquetée qui retient une valeur. En PowerShell, son nom
commence **toujours** par `$` : `$age = 30`. Le `=` range la valeur de droite dans la boîte.

**Where-Object** — La cmdlet qui **filtre** un pipeline : elle ne garde que les objets qui
passent un test. Ex : `Get-ChildItem | Where-Object { $_.Length -gt 1000 }` ne garde que les
gros fichiers. Comme un tamis.

**Write-Host / Write-Output** — Deux façons d'afficher. `Write-Host` écrit **directement à
l'écran** (pour parler à l'humain, on peut colorer). `Write-Output` envoie la valeur **dans
le pipeline**, où une autre cmdlet peut la reprendre. En cas de doute pour un résultat,
préfère `Write-Output`.

---

➡️ Un terme manque ? Ajoute-le, c'est ton dépôt. Voir aussi
[AIDE_MEMOIRE.md](./AIDE_MEMOIRE.md) pour la syntaxe.
