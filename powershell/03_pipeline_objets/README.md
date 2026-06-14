# Module 03 — Le pipeline d'OBJETS (le super-pouvoir de PowerShell)

C'est **LA** grande idée de PowerShell, celle qui le distingue le plus de Bash. Si tu ne
retiens qu'une chose de ce parcours, que ce soit **celle-ci**.

> Fichiers du module : `pipeline.ps1` (la visite guidée des cmdlets) et `filtrer_trier.ps1`
> (filtrer + trier + compter). Lance-les avec `pwsh <fichier>` (voir en bas).

---

## 1. Dans le `|`, il circule des OBJETS (pas du texte)

Imagine une **chaîne de montage** dans une usine. Chaque ouvrier (une cmdlet) reçoit une
pièce, fait **un** geste précis, puis fait glisser la pièce vers l'ouvrier suivant. Le `|`
(« pipe »), c'est le **tapis roulant** entre les ouvriers.

La grande différence avec Bash, c'est **ce qui voyage sur le tapis** :

- En **Bash**, sur le tapis voyage du **texte** brut. Pour récupérer une information précise
  (la taille d'un fichier, par exemple), tu dois re-découper ce texte à la main avec `cut`,
  `awk`, `grep`… C'est fragile : si l'affichage change d'un espace, tout casse.
- En **PowerShell**, sur le tapis voyagent de **vrais objets**. Un objet, c'est une petite
  fiche avec des **propriétés nommées** : un fichier a `.Name` (son nom), `.Length` (sa
  taille en octets), `.Extension`… Tu demandes la propriété **par son nom**, sans rien
  re-découper.

```powershell
# Bash : du texte. On doit deviner que la taille est dans la 5e colonne.
ls -l | awk '{ print $5 }'

# PowerShell : un objet. On demande la propriété .Length, point.
Get-ChildItem | ForEach-Object { $_.Length }
```

> 💡 **Une fiche = un objet.** Le nom de famille, l'âge, l'adresse… ce sont ses **propriétés**.
> En PowerShell, tu travailles directement avec ces propriétés (`.Name`, `.Age`…) au lieu de
> lire une ligne de texte et d'essayer d'y retrouver l'info.

---

## 2. `$_` : « l'objet en cours de traitement »

Beaucoup de cmdlets traitent les objets **un par un**. Pour parler de **l'objet courant**
(celui qui est sur le tapis en ce moment), PowerShell utilise une variable spéciale : **`$_`**.

Lis `$_` comme « **l'élément actuel** ». Dans `$_.Age`, tu demandes l'âge de l'élément que
la cmdlet est en train de regarder.

---

## 3. Les cmdlets clés du pipeline

| Cmdlet | À quoi elle sert | Image |
|--------|------------------|-------|
| `Where-Object` | **Filtrer** : ne garder que les objets qui passent un test | un **videur** à l'entrée |
| `Sort-Object` | **Trier** les objets selon une propriété | un **classeur** |
| `Select-Object` | **Choisir** des propriétés, ou les **N premiers** objets | un **photographe** qui cadre |
| `ForEach-Object` | **Agir** sur chaque objet (un geste par objet) | l'**ouvrier** de la chaîne |
| `Measure-Object` | **Compter / sommer / moyenner** | la **caisse** qui totalise |

### `Where-Object` — filtrer

Garde seulement les objets pour lesquels le test (entre `{ }`) est **vrai**.

```powershell
# garde les objets dont la propriété Age est supérieure ou égale à 18
... | Where-Object { $_.Age -ge 18 }
```

### `Sort-Object` — trier

```powershell
... | Sort-Object Age              # du plus petit âge au plus grand
... | Sort-Object Age -Descending  # du plus grand au plus petit
```

### `Select-Object` — choisir des propriétés OU les premiers

```powershell
... | Select-Object Nom, Age       # ne garder que ces deux propriétés
... | Select-Object -First 3       # ne garder que les 3 premiers objets
```

### `ForEach-Object` — agir sur chaque

```powershell
# pour chaque objet, fabrique une phrase avec ses propriétés
... | ForEach-Object { "Bonjour $($_.Nom), tu as $($_.Age) ans" }
```

### `Measure-Object` — compter et agréger

```powershell
... | Measure-Object                       # combien d'objets ? (propriété .Count)
... | Measure-Object Age -Average -Sum     # moyenne et somme de la propriété Age
```

---

## 4. Un exemple complet (à lire de gauche à droite)

```powershell
Get-ChildItem |
    Where-Object   { $_.Length -gt 1MB } |   # 1. garde les fichiers de plus de 1 Mo
    Sort-Object    Length -Descending     |   # 2. trie du plus gros au plus petit
    Select-Object  Name, Length -First 5      # 3. n'affiche que le nom + la taille des 5 premiers
```

Lis-le comme une **phrase** : « prends les fichiers, **garde** ceux de plus de 1 Mo,
**trie**-les du plus gros au plus petit, et **montre** le nom et la taille des 5 premiers ».

Chaque cmdlet fait **un seul** geste et passe le résultat à la suivante. C'est ça, la
puissance du pipeline : on **enchaîne** des gestes simples.

> 💡 Tu peux **couper une longue commande** après chaque `|` et continuer à la ligne, comme
> ci-dessus : c'est plus lisible. (Le `|` en fin de ligne dit à PowerShell « ce n'est pas
> fini ».)

---

## 5. Bash vs PowerShell, le résumé

| | Bash | PowerShell |
|--|------|------------|
| Ce qui circule dans le `|` | du **texte** | des **objets** |
| Pour filtrer | `grep`, `awk` (sur du texte) | `Where-Object { $_.Prop ... }` |
| Pour trier | `sort` (sur des colonnes) | `Sort-Object Prop` |
| Pour compter | `wc -l` | `Measure-Object` |
| Accéder à une info | re-découper le texte | demander `.Propriété` |

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/03_pipeline_objets/pipeline.ps1
pwsh powershell/03_pipeline_objets/filtrer_trier.ps1
```

Ces scripts **fabriquent leurs propres objets** (pas besoin de fichiers du système) : ils
donnent donc toujours le **même** résultat, où que tu sois. Lis-les, puis **modifie-les** :
change le test du `Where-Object`, trie sur une autre propriété, ajoute une colonne au
`Select-Object`.

➡️ La suite du parcours arrivera dans le même style.
