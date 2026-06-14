# 🧭 Anatomie d'un script : dans quel ordre écrire son code ?

Beaucoup de débutants savent taper des commandes PowerShell dans la console, mais ne savent
pas **dans quel ordre les ranger** pour former un vrai script propre. Ce guide explique le
**cheminement logique** d'un script PowerShell, du début à la fin.

> 📌 À lire après les modules `00_demarrer` et `01_les_bases`, et à garder sous la main
> comme aide-mémoire.

---

## 1. LA règle d'or : PowerShell lit de HAUT en BAS

C'est le point le plus important, et la cause n°1 des bugs de débutant.

> PowerShell exécute ton fichier **ligne par ligne, du haut vers le bas**, comme tu lis une
> page. **Une chose doit exister AVANT qu'on l'utilise.**

Tu ne peux pas verser le café dans une tasse que tu n'as pas encore sortie du placard.
En code, c'est pareil : tu ne peux pas utiliser une variable ou une fonction **avant**
de l'avoir créée/définie plus haut.

---

## 2. Le squelette standard d'un script complet

Presque tous les scripts PowerShell bien écrits suivent **ce même ordre**, de haut en bas :

```powershell
<#                                                        ┐  (1) COMMENTAIRE D'EN-TÊTE
    Description du script : à quoi il sert,                │     (à quoi sert le script,
    comment le lancer.                                     │      comment le lancer)
#>                                                        ┘

param(                                                    ┐  (2) BLOC param( ... )
    [string]$Url,                                          │     (les paramètres d'entrée ;
    [int]$Timeout = 10                                     │      DOIT être la 1re instruction
)                                                         ┘      exécutable du script)

$DOSSIER_SORTIE = "resultats"                             ┐  (3) CONSTANTES
$SEPARATEUR     = ";"                                     ┘     (valeurs fixes, EN MAJUSCULES)

function Get-Page {                                       ┐
    # Fait une seule chose, bien.                          │  (4) FONCTIONS
    param([string]$Adresse)                                │     (on les DÉFINIT ici, elles
    Invoke-WebRequest $Adresse                             │      ne s'exécutent PAS encore)
}                                                          │
                                                          │
function Save-Result {                                     │
    param($Donnees)                                        │
    ...                                                   │
}                                                          ┘

# --- Corps principal du script ---                       ┐  (5) CORPS PRINCIPAL
$page = Get-Page -Adresse $Url                            │     (le code qui DÉMARRE tout
Save-Result -Donnees $page                                ┘      et appelle les fonctions)
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 1 | **Commentaire d'en-tête** (`<# ... #>`) | La 1re chose qu'on lit : « ce script sert à… ». Un bloc `<# ... #>` peut s'étaler sur plusieurs lignes, parfait pour décrire le script et la façon de le lancer. |
| 2 | **Bloc `param( ... )`** | La liste des **paramètres d'entrée** du script (ses « réglages » donnés au lancement). ⚠️ Règle stricte de PowerShell : `param( ... )` **DOIT être la première instruction exécutable** du script (seuls des commentaires peuvent le précéder). S'il arrive après une autre ligne de code, PowerShell refuse de le lire. |
| 3 | **Constantes** | Les réglages fixes, regroupés en haut pour les changer facilement. Par convention, on les écrit `EN_MAJUSCULES`. |
| 4 | **Fonctions (`function`)** | On **définit** les actions réutilisables. ⚠️ Définir ≠ exécuter : le code d'une fonction ne tourne que lorsqu'on l'**appelle**. Une fonction doit être écrite **AVANT** d'être appelée (PowerShell lit de haut en bas !). |
| 5 | **Corps principal** | Le **chef d'orchestre** : il appelle les fonctions dans le bon ordre. C'est la partie qui s'exécute vraiment, tout en bas. |

> 💡 « Définir une fonction » = écrire la recette. « Appeler la fonction » = cuisiner le
> plat. On écrit toutes les recettes en haut, puis on cuisine en bas.

---

## 3. La logique INTERNE : entrée → traitement → sortie

À l'intérieur du corps principal (ou d'une fonction), le code suit presque toujours
**3 phases**, dans cet ordre :

```
   1. ENTRÉE             2. TRAITEMENT             3. SORTIE
   (je récupère          (je calcule, je décide,   (j'affiche ou
    les données)          je transforme)            j'enregistre)
   ──────────            ───────────────           ──────────
   Read-Host "Nom ?"     if / else                 Write-Host "..."
   $Url (param)          foreach / while           Set-Content / Out-File
   Get-Content fichier   cmdlets, pipeline ( | )   renvoyer un résultat
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

---

## 4. Comment lire un script complexe qu'on découvre

Quand un script te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va tout en bas**, au **corps principal** (les lignes qui ne sont *pas* dans une
   fonction). C'est le **point de départ** réel : il montre l'enchaînement principal.
2. **Suis les appels de fonctions** depuis ce corps. Quand tu vois `Get-Page -Adresse $Url`,
   remonte lire la fonction `function Get-Page { ... }` pour comprendre ce qu'elle fait.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le corps
> principal), puis tu ouvres les chapitres qui t'intéressent (les fonctions).

---

## 5. Récapitulatif visuel

```
┌──────────────────────────────────────────────┐
│ 1. <# ... #>         : à quoi sert le script   │
│ 2. param( ... )      : les paramètres d'entrée │  ← on prépare
│ 3. CONSTANTES        : les réglages fixes      │
├──────────────────────────────────────────────┤
│ 4. function Verbe-Nom {...} : on DÉFINIT       │  ← on outille
│                              les actions       │
├──────────────────────────────────────────────┤
│ 5. Corps principal :                           │
│        entrée  -> traitement -> sortie         │  ← on EXÉCUTE
└──────────────────────────────────────────────┘
            (PowerShell lit de haut en bas)
```

---

## Pour aller plus loin

- 📋 Les commandes et la syntaxe sous les yeux : [`./AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md)
- 📖 Un mot que tu ne comprends pas (param, cmdlet, pipeline…) : [`./GLOSSAIRE.md`](./GLOSSAIRE.md)
