# 🧭 Anatomie d'un script : dans quel ordre écrire son code ?

Beaucoup de débutants savent taper des commandes Bash dans le terminal, mais ne savent pas
**dans quel ordre les ranger** pour former un vrai script propre. Ce guide explique le
**cheminement logique** d'un script Bash, du début à la fin.

> 📌 À lire après les modules `00_demarrer` et `01_les_bases`, et à garder sous la main
> comme aide-mémoire.

---

## 1. LA règle d'or : Bash lit de HAUT en BAS

C'est le point le plus important, et la cause n°1 des bugs de débutant.

> Bash exécute ton fichier **ligne par ligne, du haut vers le bas**, comme tu lis une
> page. **Une chose doit exister AVANT qu'on l'utilise.**

Tu ne peux pas verser le café dans une tasse que tu n'as pas encore sortie du placard.
En code, c'est pareil : tu ne peux pas utiliser une variable ou une fonction **avant**
de l'avoir créée/définie plus haut.

---

## 2. Le squelette standard d'un script complet

Presque tous les scripts Bash bien écrits suivent **ce même ordre**, de haut en bas :

```bash
#!/usr/bin/env bash                                       ┐  (1) SHEBANG
                                                          ┘     (quel programme lance le fichier)

set -euo pipefail                                         ┐  (2) OPTIONS DE SÉCURITÉ
                                                          ┘     (stoppe le script au moindre souci)

DOSSIER_SORTIE="resultats"                                ┐  (3) CONSTANTES
TIMEOUT=10                                                ┘     (valeurs fixes, EN MAJUSCULES)

telecharger() {                                           ┐
    # Fait une seule chose, bien.                          │  (4) FONCTIONS
    curl ...                                               │     (on les DÉFINIT ici, elles
}                                                          │      ne s'exécutent PAS encore)
                                                          │
sauvegarder() {                                            │
    ...                                                   │
}                                                          ┘

# --- Corps principal du script ---                       ┐  (5) CORPS PRINCIPAL
page=$(telecharger "https://exemple.com")                 │     (le code qui DÉMARRE tout
sauvegarder "$page"                                        ┘      et appelle les fonctions)
```

### Pourquoi cet ordre, étape par étape

| Ordre | Bloc | Pourquoi il est là |
|------|------|--------------------|
| 1 | **Shebang** (`#!/usr/bin/env bash`) | La toute 1re ligne. Elle dit au système : « lance ce fichier avec Bash ». Sans elle, le script peut être exécuté par un autre interpréteur et planter. |
| 2 | **`set -euo pipefail`** | Les **options de sécurité**, juste après le shebang. `-e` stoppe au 1er échec, `-u` interdit les variables non définies, `-o pipefail` détecte un échec dans un `\|` (pipe). On les met en haut pour qu'elles protègent **tout** le script. |
| 3 | **Constantes** | Les réglages fixes, regroupés en haut pour les changer facilement. Par convention, on les écrit `EN_MAJUSCULES`. |
| 4 | **Fonctions** | On **définit** les actions réutilisables. ⚠️ Définir ≠ exécuter : le code d'une fonction ne tourne que lorsqu'on l'**appelle**. Une fonction doit être écrite **AVANT** d'être appelée (Bash lit de haut en bas !). |
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
   read maVariable       if / then / else          echo "..."
   "$1" "$2" (arguments) for / while               écrire un fichier (> fichier)
   $(une commande)       commandes, boucles        renvoyer un résultat
```

Garde cette trame en tête : **d'abord j'obtiens l'info, ensuite je la traite, enfin je
montre le résultat.** Si tu affiches un résultat *avant* de l'avoir calculé, c'est qu'un
bloc est mal placé.

---

## 4. Comment lire un script complexe qu'on découvre

Quand un script te paraît compliqué, ne le lis pas bêtement de haut en bas. Fais ainsi :

1. **Va tout en bas**, au **corps principal** (les lignes qui ne sont *pas* dans une
   fonction). C'est le **point de départ** réel : il montre l'enchaînement principal.
2. **Suis les appels de fonctions** depuis ce corps. Quand tu vois `telecharger "$url"`,
   remonte lire la fonction `telecharger() { ... }` pour comprendre ce qu'elle fait.
3. **Ignore les détails au début.** Comprends d'abord le *cheminement général* (les grandes
   étapes), puis seulement après, plonge dans chaque fonction.

> C'est comme une table des matières : tu lis d'abord les titres de chapitres (le corps
> principal), puis tu ouvres les chapitres qui t'intéressent (les fonctions).

---

## 5. Récapitulatif visuel

```
┌─────────────────────────────────────────────┐
│ 1. #!/usr/bin/env bash : qui lance le fichier │
│ 2. set -euo pipefail   : les sécurités        │  ← on prépare
│ 3. CONSTANTES          : les réglages fixes   │
├─────────────────────────────────────────────┤
│ 4. ma_fonction() {...} : on DÉFINIT les actions│  ← on outille
├─────────────────────────────────────────────┤
│ 5. Corps principal :                          │
│        entrée  -> traitement -> sortie        │  ← on EXÉCUTE
└─────────────────────────────────────────────┘
              (Bash lit de haut en bas)
```

---

## Pour aller plus loin

- 📋 Les commandes et la syntaxe sous les yeux : [`./AIDE_MEMOIRE.md`](./AIDE_MEMOIRE.md)
- 📖 Un mot que tu ne comprends pas (shebang, pipe, variable…) : [`./GLOSSAIRE.md`](./GLOSSAIRE.md)
