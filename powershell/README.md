# 🟦 Apprendre PowerShell — pour grands débutants

**PowerShell** est à la fois un **terminal** et un **langage de script**, créé par Microsoft.
Très utilisé pour **administrer Windows** et automatiser des tâches, il est aujourd'hui
**multiplateforme** (Windows, macOS, Linux) grâce à `pwsh` (*PowerShell Core*).

> 💡 Même pédagogie que le reste du dépôt : **on explique d'abord, on code ensuite.**
> Chaque module a un `README.md` théorique, puis du code **commenté presque ligne par ligne**.

---

## 🆚 Ce qui rend PowerShell unique : le pipeline d'OBJETS

C'est **LA** grande idée à comprendre, surtout si tu connais déjà Bash.

- En **Bash**, les commandes s'échangent du **texte** brut via le pipe `|` (tu dois souvent
  re-découper ce texte avec `cut`, `awk`…).
- En **PowerShell**, les commandes s'échangent de **vrais objets** (avec des propriétés
  nommées). Tu manipules `.Name`, `.Length`… sans rien re-découper.

```powershell
# "donne-moi les fichiers, garde ceux de plus de 1 Mo, affiche leur nom et taille"
Get-ChildItem | Where-Object { $_.Length -gt 1MB } | Select-Object Name, Length
```

Autre particularité : les commandes s'appellent des **cmdlets** et suivent toujours la forme
**`Verbe-Nom`** (`Get-ChildItem`, `Write-Output`, `Set-Location`…). C'est très lisible.

| | Bash | PowerShell |
|--|------|------------|
| Ce qui circule dans le `|` | du **texte** | des **objets** |
| Nom des commandes | court (`ls`, `cat`) | **`Verbe-Nom`** (`Get-ChildItem`) |
| Variable | `x=5` puis `"$x"` | `$x = 5` puis `"$x"` |
| Comparaison | `-eq` / `==` dans `[[ ]]` | `-eq`, `-lt`, `-ge`… (**jamais** `<` `>`) |

---

## 📚 Le parcours (fondations)

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Lancer un script `.ps1`, les cmdlets, `Write-Host`, les commentaires |
| 1 | [`01_les_bases`](./01_les_bases/) | Variables, types, `Read-Host`, conditions, boucles, fonctions |

> 🚧 **Fondations** : ce parcours débute. D'autres modules (fichiers, pipeline & objets,
> projets…) viendront ensuite, dans le même style.

---

## ⚙️ Pré-requis : PowerShell

- **Windows** : PowerShell est déjà là (cherche « PowerShell » dans le menu Démarrer).
- **macOS / Linux** : installe **PowerShell Core**, la commande s'appelle alors `pwsh`
  (voir [aka.ms/powershell](https://aka.ms/powershell)).

Vérifie : `pwsh --version` (ou `$PSVersionTable` dans une console PowerShell).

## ▶️ Lancer un script PowerShell

```bash
pwsh powershell/00_demarrer/premier_script.ps1
```

> 🔒 **Note Windows** : par sécurité, Windows peut bloquer l'exécution des scripts. Si besoin,
> autorise-les pour ta session avec :
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

➡️ Commence par le module [`00_demarrer`](./00_demarrer/).
