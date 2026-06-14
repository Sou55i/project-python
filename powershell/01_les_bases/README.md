# Module 01 — Les bases de PowerShell

Les mêmes briques que partout (variables, conditions, boucles, fonctions), avec deux
particularités PowerShell à bien retenir : les variables commencent par **`$`**, et les
comparaisons utilisent des **opérateurs en lettres** (`-eq`, `-lt`…), **jamais** `<` ou `>`.

> Fichiers du module : `bases.ps1` (les briques) et `mini_calculatrice.ps1` (un mini-projet).
> Lance-les avec `pwsh <fichier>` (voir en bas).

---

## 1. Les variables : un `$` devant le nom

On crée une variable avec `=`, et **son nom commence toujours par `$`** :

```powershell
$nom = "Alice"
$age = 30
$taille = 1.68
$actif = $true        # booléen : $true ou $false (avec un $ !)
```

Pour **afficher** une variable dans du texte, mets-la dans des **guillemets doubles** : elle
est remplacée par sa valeur (c'est l'**interpolation**) :

```powershell
Write-Host "Bonjour $nom, tu as $age ans"
```

> 💡 Pour insérer un **calcul** ou une **propriété** dans le texte, entoure-le de `$( )` :
> `Write-Host "Total : $($a + $b)"`. Les **guillemets simples** `'...'`, eux, n'interprètent
> PAS les variables (le texte est affiché tel quel).

---

## 2. Les types

PowerShell devine le type, mais on peut le **forcer** avec un nom entre crochets :

```powershell
[int]$entier = 42        # nombre entier
[double]$decimal = 3.14  # nombre à virgule
[string]$texte = "salut" # chaîne de caractères
[bool]$vrai = $true      # vrai / faux
```

Pour connaître le type d'une valeur : `$age.GetType().Name`.

---

## 3. Lire une saisie avec `Read-Host`

L'équivalent de `input()` en Python :

```powershell
$prenom = Read-Host "Comment t'appelles-tu"
Write-Host "Enchante, $prenom !"
```

⚠️ Comme `input()`, `Read-Host` renvoie du **texte**. Pour calculer dessus, **convertis** en
nombre avec `[int]` ou `[double]` :

```powershell
$age = [int](Read-Host "Quel age as-tu")
```

---

## 4. Les conditions : `if` / `elseif` / `else`

```powershell
$note = 12
if ($note -ge 16) {
    Write-Host "Tres bien"
} elseif ($note -ge 10) {
    Write-Host "Recu"
} else {
    Write-Host "A retravailler"
}
```

Points clés : la condition va entre **`( )`**, le bloc entre **`{ }`**.

> 🔑 **Le piège n°1 du débutant** : en PowerShell, on **n'utilise jamais** `<`, `>`, `==`
> pour comparer (ils servent à autre chose). On utilise des **opérateurs en lettres** :

| Comparaison | Opérateur |
|-------------|-----------|
| égal | `-eq` |
| différent | `-ne` |
| inférieur / inf. ou égal | `-lt` / `-le` |
| supérieur / sup. ou égal | `-gt` / `-ge` |

Et pour combiner des conditions : `-and` (ET), `-or` (OU), `-not` (NON).

---

## 5. Les boucles : `for`, `foreach`, `while`

```powershell
# for : répéter un nombre précis de fois
for ($i = 0; $i -lt 3; $i++) {     # $i++ veut dire "$i = $i + 1"
    Write-Host "Tour $i"
}

# foreach : "pour chaque élément d'une collection"
$fruits = @("pomme", "banane", "cerise")
foreach ($fruit in $fruits) {
    Write-Host "- $fruit"
}

# while : tant que la condition est vraie
$compteur = 0
while ($compteur -lt 3) {
    Write-Host "compteur = $compteur"
    $compteur++                    # sans ça : boucle infinie !
}
```

Une **liste** (tableau) se crée avec `@(...)` : `$fruits[0]` est le premier élément (on
compte à partir de 0), `$fruits.Count` donne le nombre d'éléments, et `$fruits += "kiwi"`
ajoute un élément.

---

## 6. Les fonctions

```powershell
# Par convention, on nomme une fonction Verbe-Nom (comme les cmdlets).
function Get-Salutation {
    param([string]$Nom)          # 'param' déclare les paramètres (avec leur type)
    return "Bonjour $Nom !"      # 'return' renvoie un résultat
}

# Appel : on nomme l'argument avec un tiret (style PowerShell)...
Write-Host (Get-Salutation -Nom "Alice")
# ...ou on le passe directement.
Write-Host (Get-Salutation "Bob")
```

> 💡 Les parenthèses autour de `Get-Salutation ...` servent à récupérer son résultat pour
> le passer à `Write-Host`.

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/01_les_bases/bases.ps1

# La calculatrice attend une opération et deux nombres (saisie simulée possible) :
"+`n7`n5" | pwsh powershell/01_les_bases/mini_calculatrice.ps1
```

Lis les deux fichiers, puis **modifie-les** : ajoute une opération, change les conditions,
crée ta propre fonction.

➡️ La suite du parcours (fichiers, le pipeline d'objets, projets…) arrivera dans le même style.
