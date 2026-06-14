# Module 06 — Écrire des scripts robustes (gestion des erreurs)

Jusqu'ici, dès qu'une erreur survenait, le script **plantait** (ou affichait un gros message
rouge). Un script **robuste**, lui, **prévoit** que les choses peuvent mal se passer et réagit
proprement : il affiche un message clair au lieu de s'effondrer.

> Fichiers du module : `try_catch.ps1` (attraper une erreur) et `erreurs.ps1` (`throw` et
> `finally`). Lance-les avec `pwsh <fichier>` (voir en bas).

---

## 1. L'idée : « essayer, et prévoir le pire »

Imagine que tu prépares un gâteau en suivant une recette. À l'étape « casser un œuf », il se
peut que l'œuf soit pourri. Tu as deux attitudes possibles :

- **Sans filet** : tu continues sans réfléchir, et toute la pâte est gâchée (le script plante).
- **Avec filet** : tu **prévois** ce cas. Si l'œuf est mauvais, tu le jettes, tu prends un
  autre œuf, et tu continues calmement.

En programmation, ce « filet de sécurité » s'écrit avec **`try` / `catch`** (exactement comme
en Python). On met le code risqué dans `try`, et la réaction en cas d'erreur dans `catch` :

```powershell
try {
    # le code qui PEUT échouer
    $nombre = [int]"abc"     # convertir "abc" en entier : impossible !
} catch {
    # ce bloc ne s'exécute QUE si une erreur est survenue au-dessus
    Write-Host "Oups, ce n'est pas un nombre valide."
}
```

> 💡 Comparaison Python : c'est le même principe que `try: ... except: ...`.

---

## 2. Erreurs NON-bloquantes vs erreurs bloquantes

C'est **la** subtilité de PowerShell, à bien comprendre.

- Une erreur **bloquante** (*terminating*) arrête le code : `try` l'envoie aussitôt au `catch`.
- Une erreur **NON-bloquante** (*non-terminating*) affiche un message rouge **mais le script
  continue**... et surtout, elle **n'est PAS attrapée** par `catch` ! Beaucoup de cmdlets
  (`Get-Item`, `Remove-Item`…) produisent ce genre d'erreur.

Analogie : une erreur bloquante, c'est une panne moteur (la voiture s'arrête). Une erreur
non-bloquante, c'est un voyant orange au tableau de bord (ça clignote, mais la voiture roule).

---

## 3. Forcer l'arrêt avec `-ErrorAction Stop`

Pour qu'une erreur non-bloquante devienne **attrapable** par `catch`, on demande à la cmdlet
de **s'arrêter** en cas de problème, avec le paramètre **`-ErrorAction Stop`** :

```powershell
try {
    Get-Item "fichier_qui_nexiste_pas.txt" -ErrorAction Stop
} catch {
    Write-Host "Le fichier est introuvable."
}
```

Sans `-ErrorAction Stop`, le `catch` ci-dessus ne se déclencherait **jamais**.

> 🔑 Règle à retenir : **`try`/`catch` n'attrape que les erreurs bloquantes.** Pour une cmdlet,
> ajoute presque toujours `-ErrorAction Stop` dans le `try`.

Pour rendre **tout le script** strict d'un coup (toute erreur devient bloquante), place cette
ligne tout en haut :

```powershell
$ErrorActionPreference = 'Stop'
```

---

## 4. Dans le `catch` : la variable `$_`

Quand une erreur est attrapée, PowerShell range les détails de l'erreur dans une variable
automatique : **`$_`**. Le plus utile est son **message** :

```powershell
try {
    $nombre = [int]"abc"
} catch {
    Write-Host "Erreur rencontree : $($_.Exception.Message)"
}
```

- `$_` représente l'erreur attrapée.
- `$_.Exception.Message` est le **texte explicatif** de l'erreur (très pratique à afficher).

---

## 5. Déclencher soi-même une erreur avec `throw`

Parfois, **toi** tu décides qu'il y a un problème (ex : un âge négatif n'a pas de sens). Tu
peux alors **lancer** ta propre erreur avec **`throw`** suivi d'un message :

```powershell
if ($age -lt 0) {
    throw "L'age ne peut pas etre negatif."
}
```

Une erreur lancée par `throw` est **toujours bloquante** : elle est donc attrapable par un
`catch` qui l'entoure.

---

## 6. Le bloc `finally` : « quoi qu'il arrive »

Après `try`/`catch`, on peut ajouter un bloc **`finally`** : son code s'exécute **dans tous les
cas**, qu'il y ait eu une erreur ou non. C'est l'endroit idéal pour le **nettoyage** (fermer un
fichier, libérer une ressource).

```powershell
try {
    Write-Host "On tente quelque chose..."
} catch {
    Write-Host "Ca a echoue."
} finally {
    Write-Host "Nettoyage : execute quoi qu'il arrive."
}
```

Analogie : `finally`, c'est « éteindre le four en partant », que le gâteau soit réussi ou raté.

---

## 7. Le code de sortie avec `exit N`

Quand un script se termine, il renvoie un **code de sortie** (un nombre) au système :

- **`exit 0`** signifie « tout s'est bien passé ».
- **`exit 1`** (ou tout autre nombre différent de 0) signifie « il y a eu une erreur ».

C'est utile pour qu'un autre programme sache si ton script a réussi ou non.

```powershell
try {
    Faire-Quelque-Chose -ErrorAction Stop
} catch {
    Write-Host "Echec : $($_.Exception.Message)"
    exit 1            # on quitte en signalant une erreur
}
```

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/06_robustesse/try_catch.ps1
pwsh powershell/06_robustesse/erreurs.ps1
```

Lis les deux fichiers, puis **expérimente** : change le texte à convertir, ajoute un
`-ErrorAction Stop`, déclenche ta propre erreur avec `throw`, observe quand `finally` s'exécute.

➡️ La suite du parcours arrivera dans le même style.
