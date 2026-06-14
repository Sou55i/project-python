# Module 09 (avancé) — Le parallélisme en PowerShell

Jusqu'ici, tes scripts faisaient **une seule chose à la fois**, dans l'ordre, de haut en
bas. Mais parfois, attendre une tâche après l'autre fait perdre énormément de temps.
Ce module t'apprend à faire **plusieurs choses « en même temps »** en PowerShell, quand
c'est utile.

C'est un module **avancé** : prends ton temps. L'idée est simple avec une bonne analogie,
mais le vocabulaire (parallèle, jobs, threads…) peut faire peur au début. On va tout
démonter, tranquillement.

> 🧠 Lis cette théorie en entier **avant** d'ouvrir les fichiers `.ps1`. Les deux scripts du
> module sont : `foreach_parallel.ps1` (traiter une collection en parallèle avec
> `ForEach-Object -Parallel`) et `jobs.ps1` (lancer des tâches en arrière-plan avec
> `Start-Job`).

> 🔗 **Lien avec Python** : ce module est le « cousin PowerShell » du
> [module 09 de Python](../../python/automatisation/09_concurrence/). Les idées sont
> **exactement les mêmes** (occuper les temps morts, paralléliser ce qui ATTEND). Si tu
> l'as déjà lu, tu vas te sentir en terrain connu.

---

## 1. Le problème : attendre, c'est perdre du temps

Imagine que tu dois **télécharger 10 pages web**. Chaque téléchargement prend 1 seconde,
mais pendant cette seconde, **ton ordinateur ne fait rien** : il attend que le serveur
réponde, comme toi tu attends que l'eau bout.

- **À la file (séquentiel)** : tu télécharges la page 1, tu attends 1 s, puis la page 2,
  tu attends 1 s… Au total **10 secondes**. Tu passes ton temps à attendre.
- **En même temps (parallèle)** : tu lances les 10 téléchargements **d'un coup**, puis tu
  attends que tous reviennent. Comme ils attendent **en parallèle**, le total est proche de
  **1 seconde**. Dix fois plus rapide !

Analogie de la **cuisine** : pour préparer un repas, tu ne restes pas planté devant la
casserole pendant qu'elle chauffe. Tu mets l'eau à bouillir, **et pendant ce temps** tu
coupes les légumes. Tu **occupes les temps morts**. C'est exactement ça, le parallélisme.

---

## 2. Quand le parallélisme est-il VRAIMENT utile ?

La question à te poser **avant tout** : « est-ce que mes tâches **attendent** beaucoup ? ».

| Type de tâche | Ce qu'elle fait | Exemples | Parallélisme utile ? |
|---------------|-----------------|----------|----------------------|
| **Tâche d'attente** (I/O) | elle **attend** quelque chose d'extérieur | télécharger une page, lire des fichiers, interroger une base | **OUI** 👍 |
| **Tâche de calcul** (CPU) | elle **fait travailler le processeur** sans arrêt | calculs lourds, compression | gain plus limité |

- **Tâche d'attente (I/O = Input/Output)** : pendant qu'une tâche attend (réseau, disque…),
  on peut en faire avancer une autre. C'est **le cas idéal** du parallélisme.
- **Tâche de calcul (CPU)** : là, il n'y a pas de temps mort à occuper. Le gain dépend
  surtout du nombre de cœurs de ton processeur.

> 💡 Retiens la règle d'or : **on parallélise d'abord ce qui ATTEND** (réseau, fichiers).
> C'est exactement la même règle que dans le module 09 de Python.

---

## 3. Première façon : `ForEach-Object -Parallel`

Tu connais déjà `ForEach-Object` (module 03) : il **agit sur chaque objet** d'une
collection, un par un. Avec l'option **`-Parallel`**, il agit sur les objets **en même
temps** au lieu de les traiter à la file.

> ⚠️ **Important** : `ForEach-Object -Parallel` existe seulement en **PowerShell 7+**
> (la version moderne, `pwsh`). Vérifie ta version avec `$PSVersionTable`. Si tu es en
> Windows PowerShell 5.1, utilise plutôt les **jobs** de la section 4.

L'image : au lieu d'**un seul ouvrier** qui prend les pièces une par une sur le tapis, tu
as **une équipe d'ouvriers** qui attrapent chacun une pièce et travaillent **en parallèle**.

```powershell
# traite chaque nombre EN PARALLÈLE ; au plus 3 tâches en même temps
1, 2, 3, 4, 5 | ForEach-Object -Parallel {
    # $_ est l'élément en cours (comme d'habitude)
    "$_ au carré = $($_ * $_)"
} -ThrottleLimit 3
```

Deux points à comprendre :

- **`-Parallel { ... }`** : le bloc entre `{ }` est exécuté **pour chaque élément, en
  parallèle**. À l'intérieur, `$_` reste « l'élément en cours de traitement », comme dans
  le `ForEach-Object` classique.
- **`-ThrottleLimit N`** : c'est le **nombre maximum** de tâches qui tournent **en même
  temps**. C'est un **robinet** (« throttle » = limiter le débit) : si tu mets `-ThrottleLimit 3`,
  PowerShell n'en lance que 3 d'un coup, puis enchaîne. Ça évite de lancer 10 000 tâches
  d'un seul coup et de saturer la machine.

> 💡 À l'intérieur du bloc `-Parallel`, chaque tâche tourne **isolée** : elle ne voit pas
> tes variables habituelles. Pour passer une variable du dehors, on la préfixe avec
> `$using:` (par exemple `$using:prefixe`). Le script `foreach_parallel.ps1` te le montre.

➡️ C'est exactement ce que montre **`foreach_parallel.ps1`**.

---

## 4. Deuxième façon : les tâches en arrière-plan (`Start-Job`)

Une **tâche en arrière-plan** (un **job**), c'est un travail que tu lances « sur le côté »
et qui tourne **pendant que ton script continue**. Tu n'attends pas qu'il finisse pour
passer à la suite : tu le récupères **plus tard**, quand tu en as besoin.

L'image : tu confies du linge à la **machine à laver**. Tu appuies sur « marche »
(`Start-Job`), **tu vas faire autre chose**, puis tu reviens **attendre la fin du cycle**
(`Wait-Job`) et enfin tu **sors le linge** (`Receive-Job`).

Trois cmdlets, dans l'ordre :

| Cmdlet | À quoi elle sert | Image |
|--------|------------------|-------|
| `Start-Job` | **Lancer** une tâche en arrière-plan (rend la main tout de suite) | appuyer sur « marche » |
| `Wait-Job` | **Attendre** qu'un ou plusieurs jobs soient terminés | attendre la fin du cycle |
| `Receive-Job` | **Récupérer le résultat** produit par le job | sortir le linge |

```powershell
# 1. on lance deux jobs : ils démarrent et tournent EN MÊME TEMPS
$job1 = Start-Job -ScriptBlock { Start-Sleep -Seconds 1; "résultat A" }
$job2 = Start-Job -ScriptBlock { Start-Sleep -Seconds 1; "résultat B" }

# 2. on attend que les DEUX soient finis (ils ont attendu en parallèle : ~1 s au total)
Wait-Job -Job $job1, $job2 | Out-Null

# 3. on récupère les résultats produits par chaque job
$a = Receive-Job -Job $job1
$b = Receive-Job -Job $job2
```

Points de repère :

- **`Start-Job -ScriptBlock { ... }`** : le bloc `{ }` est le travail à faire. La cmdlet
  **rend la main immédiatement** et te renvoie un **objet job** (que l'on range dans une
  variable pour le retrouver plus tard).
- **`Wait-Job`** : met ton script **en pause** jusqu'à ce que les jobs listés soient
  terminés. Comme ils ont tourné **en parallèle**, tu attends à peu près la durée **de la
  plus longue** tâche, pas la **somme** des durées.
- **`Receive-Job`** : va **chercher ce que le job a produit** (tout ce qu'il a renvoyé).

> 💡 **Jobs ou `-Parallel` ?** Les **jobs** marchent partout (même en PowerShell 5.1) et
> sont parfaits pour **quelques** grosses tâches indépendantes. **`-Parallel`** (PowerShell 7+)
> est plus simple et plus léger pour **parcourir une collection** en parallèle. En cas de
> doute pour traiter une liste : commence par `-Parallel`.

➡️ C'est exactement ce que montre **`jobs.ps1`**.

---

## 5. Le résumé

| Ta situation | Choisis |
|--------------|---------|
| Parcourir **une collection** en parallèle, PowerShell 7+ | **`ForEach-Object -Parallel`** |
| Lancer **quelques** grosses tâches indépendantes en arrière-plan | **`Start-Job` / `Wait-Job` / `Receive-Job`** |
| Compatibilité avec **Windows PowerShell 5.1** | les **jobs** (pas `-Parallel`) |
| Une seule tâche, rien à attendre | reste **séquentiel**, c'est très bien |

> 💡 En cas de doute, commence **séquentiel**. N'ajoute du parallélisme **que** si ton
> programme est lent **parce qu'il attend**. Le parallélisme ajoute de la complexité : il
> doit servir à quelque chose. (Même conseil que dans le module 09 de Python.)

---

## ▶️ À toi de jouer

```powershell
pwsh powershell/09_parallelisme/foreach_parallel.ps1
pwsh powershell/09_parallelisme/jobs.ps1
```

> ⚠️ `foreach_parallel.ps1` a besoin de **PowerShell 7+** (`pwsh`). Vérifie avec
> `$PSVersionTable`.

Lis les deux fichiers, puis **modifie-les** : ajoute des éléments à la liste, change le
`-ThrottleLimit`, ajoute un troisième job. Essaie de **prédire** le total **avant** de
lancer.

➡️ Retour au sommaire du parcours : [`README.md`](../README.md).
