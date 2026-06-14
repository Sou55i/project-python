# Module 05 — Les collections : tableaux et tables de hachage

Jusqu'ici, une variable ne contenait **qu'une seule valeur** (`$age = 30`). Mais souvent, on
veut ranger **plusieurs valeurs ensemble** : une liste de fruits, les âges de plusieurs
personnes… C'est le rôle des **collections**.

On en voit deux, les plus utiles :

- les **tableaux** (*arrays*) : une suite de valeurs **dans l'ordre**, repérées par un **numéro**.
- les **tables de hachage** (*hashtables*) : des paires **clé → valeur**, repérées par un **nom**.

> Fichiers du module : `tableaux.ps1` et `hashtables.ps1`.
> Lance-les avec `pwsh <fichier>` (voir en bas).

---

## 1. Les tableaux : une liste ordonnée

### L'analogie

Imagine une **boîte d'œufs** : une rangée de cases numérotées, chacune contient un œuf. Le
tableau, c'est pareil : une suite de cases, et chaque case a un **numéro** (sa position).

> 🐍 **Tu connais Python ?** Un tableau PowerShell, c'est l'équivalent d'une **liste** Python
> (`["pomme", "banane"]`). Mêmes idées : ordre, position qui commence à 0, parcours.

### Créer un tableau

On utilise `@(...)`, avec les valeurs séparées par des **virgules** :

```powershell
$fruits = @("pomme", "banane")
```

### Accéder à un élément : `[ ]` et on compte à partir de 0

```powershell
$fruits[0]    # "pomme"  (le PREMIER élément a le numéro 0 !)
$fruits[1]    # "banane"
```

> 🔑 Comme en Python, on **commence à compter à 0**. Le premier élément est `[0]`, le
> deuxième `[1]`, etc. C'est le piège classique du débutant.

### Combien d'éléments ? `.Count`

```powershell
$fruits.Count    # 2
```

### Ajouter un élément : `+=`

```powershell
$fruits += "kiwi"   # le tableau contient maintenant pomme, banane, kiwi
```

### Parcourir tous les éléments : `foreach`

```powershell
foreach ($fruit in $fruits) {
    Write-Host "- $fruit"
}
```

> 💡 Lis ça comme une phrase : **« pour chaque `$fruit` dans `$fruits` »**. À chaque tour de
> boucle, `$fruit` prend la valeur de l'élément suivant.

---

## 2. Les tables de hachage : des paires clé → valeur

### L'analogie

Imagine un **annuaire** ou un **carnet d'adresses** : tu ne cherches pas « la 3ᵉ ligne », tu
cherches **« le numéro d'Alice »**. Tu retrouves une valeur grâce à un **nom** (la *clé*), pas
grâce à une position.

> 🐍 **Tu connais Python ?** Une table de hachage, c'est l'équivalent d'un **dictionnaire**
> Python (`{"alice": 30, "bob": 25}`). Mêmes idées : des clés, des valeurs, pas d'ordre garanti.

### Créer une table de hachage

On utilise `@{ ... }` (des **accolades**), avec des paires `clé = valeur` séparées par des
**points-virgules** :

```powershell
$age = @{ alice = 30; bob = 25 }
```

### Accéder à une valeur : par sa clé

Deux écritures, au choix :

```powershell
$age["alice"]    # 30  (avec les crochets et la clé entre guillemets)
$age.alice       # 30  (écriture courte avec un point)
```

### Ajouter (ou modifier) une paire

```powershell
$age["chloe"] = 35    # ajoute la clé "chloe" avec la valeur 35
```

> 💡 La même écriture **modifie** la valeur si la clé existe déjà. `$age["bob"] = 26`
> remplacerait l'âge de Bob.

### Parcourir les paires

Deux façons utiles :

```powershell
# A) Parcourir les CLÉS, puis lire la valeur de chaque clé
foreach ($nom in $age.Keys) {
    Write-Host "$nom a $($age[$nom]) ans"
}

# B) Parcourir les PAIRES directement avec .GetEnumerator()
foreach ($paire in $age.GetEnumerator()) {
    Write-Host "$($paire.Key) a $($paire.Value) ans"
}
```

> 💡 `.GetEnumerator()` donne, à chaque tour, une **paire** avec deux propriétés : `.Key` (la
> clé) et `.Value` (la valeur).

---

## 3. Tableau ou table de hachage ? Comment choisir

| | Tableau `@( )` | Table de hachage `@{ }` |
|--|----------------|--------------------------|
| On range… | une **liste ordonnée** de valeurs | des paires **clé → valeur** |
| On retrouve une valeur par… | sa **position** (`$t[0]`) | sa **clé** (`$h["alice"]`) |
| Équivalent Python | **liste** `[ ]` | **dictionnaire** `{ }` |
| Exemple | des fruits, des notes | un nom → un âge, un produit → un prix |

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/05_collections/tableaux.ps1
pwsh powershell/05_collections/hashtables.ps1
```

Lis les deux fichiers, puis **modifie-les** : ajoute des fruits, change les âges, ajoute une
nouvelle personne, parcours-les à ta façon.
