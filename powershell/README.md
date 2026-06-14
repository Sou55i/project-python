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

## 📚 Le parcours

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 0 | [`00_demarrer`](./00_demarrer/) | Lancer un script `.ps1`, les cmdlets, `Write-Host`, les commentaires |
| 1 | [`01_les_bases`](./01_les_bases/) | Variables, types, `Read-Host`, conditions, boucles, fonctions |
| 2 | [`02_fichiers`](./02_fichiers/) | Lire/écrire des fichiers : `Get-Content`, `Set-Content`, `Test-Path` |
| 3 | [`03_pipeline_objets`](./03_pipeline_objets/) | **Le point fort** : le pipeline d'**objets** (`Where-Object`, `Select-Object`, `Sort-Object`…) |
| 4 | [`04_parametres`](./04_parametres/) | Rendre un script réutilisable avec `param( )` (paramètres typés, obligatoires) |
| 5 | [`05_collections`](./05_collections/) | Tableaux `@( )` et tables de hachage `@{ }` (dictionnaires) |
| 6 | [`06_robustesse`](./06_robustesse/) | Gérer les erreurs : `try`/`catch`/`finally`, `-ErrorAction Stop`, `throw` |
| 7 | [`07_debugger`](./07_debugger/) | Déboguer : `Set-PSDebug -Trace`, `Write-Debug`, erreurs fréquentes |

### 🚀 Modules avancés

| Étape | Module | Ce que tu apprends |
|-------|--------|--------------------|
| 8 | [`08_modules`](./08_modules/) | Réutiliser du code : modules `.psm1`, `Import-Module`, `Export-ModuleMember` |
| 9 | [`09_parallelisme`](./09_parallelisme/) | Paralléliser : `ForEach-Object -Parallel`, `Start-Job`/`Wait-Job` |

Puis, pour pratiquer : le **[projet capstone](./projets/)** (ranger des fichiers par
extension), qui combine plusieurs modules.

> 📎 **Ressources** : l'[`AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md) (cheat-sheet),
> le [`GLOSSAIRE.md`](./GLOSSAIRE.md) (les mots de PowerShell) et le guide
> [`ANATOMIE_D_UN_SCRIPT.md`](./ANATOMIE_D_UN_SCRIPT.md) (dans quel ordre écrire un script).

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
