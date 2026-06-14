# Module 02 — Lire et écrire des fichiers

Jusqu'ici, tes scripts affichaient des choses à l'écran avec `Write-Host`, puis tout
disparaissait. Un **fichier**, lui, **garde** l'information : tu peux l'écrire aujourd'hui et
la relire demain. C'est exactement ce qu'on apprend ici.

> Comme toujours : **on explique d'abord, on code ensuite.**
> Fichiers du module : `ecrire.ps1` (créer un dossier + écrire) et `lire.ps1` (relire et afficher).
> Lance-les avec `pwsh <fichier>` (voir en bas).

---

## 1. Une analogie pour tout comprendre

Imagine un **cahier** :

- **Écrire** en repartant d'une page blanche (on **efface** l'ancien contenu) → `Set-Content`.
- **Ajouter** une ligne à la suite, sans rien effacer → `Add-Content`.
- **Lire** ce qui est écrit dans le cahier → `Get-Content`.
- Avant d'ouvrir le cahier : **vérifier qu'il existe** → `Test-Path`.
- Ranger ses cahiers dans un **tiroir** (un dossier) → `New-Item -ItemType Directory`.

Garde cette image en tête, on reprend chaque point juste en dessous.

---

## 2. Écrire dans un fichier

### `Set-Content` — écrire (et ÉCRASER)

`Set-Content` écrit du texte dans un fichier. ⚠️ **Attention** : si le fichier existe déjà,
son ancien contenu est **entièrement remplacé** (la page blanche).

```powershell
Set-Content -Path "notes.txt" -Value "Premiere ligne" -Encoding utf8
```

### `Add-Content` — ajouter à la suite

`Add-Content` **ajoute** du texte **à la fin** du fichier, sans toucher à ce qui est déjà là.

```powershell
Add-Content -Path "notes.txt" -Value "Une ligne de plus" -Encoding utf8
```

> 🔤 **L'encodage `-Encoding utf8`** : c'est la « façon » dont les caractères sont enregistrés.
> En utf8, les accents (é, à, ç…) et les emojis sont bien gérés. Prends l'habitude de
> **toujours** préciser `-Encoding utf8` quand tu écris **et** quand tu lis.

### `Out-File` — une autre façon d'écrire

Il existe aussi `Out-File`, très utile à la fin d'un **pipeline** pour envoyer un résultat
dans un fichier (au lieu de l'afficher) :

```powershell
"Bonjour" | Out-File -FilePath "notes.txt" -Encoding utf8
```

> 💡 Pour débuter, retiens surtout `Set-Content` (écraser) et `Add-Content` (ajouter).

---

## 3. Lire un fichier avec `Get-Content`

`Get-Content` lit le contenu d'un fichier.

```powershell
$lignes = Get-Content -Path "notes.txt" -Encoding utf8
```

🔑 **Le point clé à retenir** : `Get-Content` renvoie un **TABLEAU de lignes** (une case par
ligne du fichier), exactement comme le `@(...)` du module 01. Tu peux donc :

- compter les lignes : `$lignes.Count`
- prendre la première : `$lignes[0]`
- les parcourir avec une boucle `foreach` :

```powershell
foreach ($ligne in $lignes) {
    Write-Host $ligne
}
```

---

## 4. Vérifier qu'un fichier existe : `Test-Path`

Lire un fichier qui n'existe pas provoque une **erreur**. Avant de lire, on vérifie donc avec
`Test-Path`, qui répond `$true` (ça existe) ou `$false` (ça n'existe pas) :

```powershell
if (Test-Path -Path "notes.txt") {
    Write-Host "Le fichier existe, je peux le lire."
} else {
    Write-Host "Le fichier n'existe pas encore."
}
```

`Test-Path` fonctionne aussi bien pour un **fichier** que pour un **dossier**.

---

## 5. Créer un dossier : `New-Item -ItemType Directory -Force`

Pour ranger nos fichiers, on crée un dossier (un « tiroir ») :

```powershell
New-Item -ItemType Directory -Path "exemples" -Force | Out-Null
```

- `-ItemType Directory` : on précise qu'on veut un **dossier** (et non un fichier).
- `-Force` : le mot magique. Il **crée le dossier s'il manque**, et **ne râle pas** s'il
  existe déjà. Pratique pour relancer le script sans erreur.
- `| Out-Null` : `New-Item` renvoie des infos sur le dossier créé ; on les jette pour ne pas
  encombrer l'écran.

---

## 6. Les chemins (relatifs vs absolus)

Dans nos scripts, on utilise un **chemin relatif** comme `"exemples/notes.txt"` : il est
calculé **à partir du dossier où tu lances la commande**. Simple et portable.

> 💡 Un chemin **absolu** part de la racine (ex. `C:\Users\...` ou `/home/...`). On préfère
> les chemins relatifs ici pour rester simples.

---

## ▶️ À toi de jouer

Lance d'abord l'écriture, puis la lecture :

```powershell
pwsh powershell/02_fichiers/ecrire.ps1
pwsh powershell/02_fichiers/lire.ps1
```

Ensuite, **expérimente** : ajoute une ligne avec `Add-Content`, relance `lire.ps1`, puis
remplace `Set-Content` par un autre texte et observe que l'ancien contenu a disparu.

➡️ La suite du parcours (le pipeline d'objets, projets…) arrivera dans le même style.
