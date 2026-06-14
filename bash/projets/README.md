# 🛠️ Projets Bash — l'étape « capstone »

Une fois les modules `00` à `07` digérés, place aux **projets complets** : de vrais petits
outils qui **combinent plusieurs modules à la fois**. C'est l'étape la plus importante du
parcours — c'est en construisant des outils utiles qu'on devient autonome.

> Chaque script commence par un bloc **« 🗺️ CHEMINEMENT DU SCRIPT »** qui résume ses étapes :
> lis-le **en premier** pour comprendre la logique avant de plonger dans le code.

---

## Les projets

| Projet | Ce qu'il fait | Modules combinés |
|--------|---------------|------------------|
| [`organiser.sh`](./organiser.sh) | **Range** automatiquement les fichiers d'un dossier dans des sous-dossiers selon leur **extension** (`.txt` → `Documents/`, `.jpg` → `Images/`, `.csv` → `Tableaux/`…) | **02** (fichiers : `for`, `mkdir -p`, `mv`, `[[ -f ]]`) · **01** (conditions, `case`) · **06** (robustesse : `set -euo pipefail`) + manipulation de chemins |

> 💡 `organiser.sh` est l'**équivalent Bash** du projet Python
> [`ranger_dossier.py`](../../python/automatisation/projets/) : même idée, mais en pilotant
> le terminal.

---

## ▶️ Lancer le projet (DEPUIS LA RACINE du dépôt)

```bash
bash bash/projets/organiser.sh
```

Aucun risque : le script **ne touche à aucun fichier réel**. Il commence par **fabriquer
lui-même** un dossier de démonstration rempli de **fichiers vides** dans
`bash/projets/exemples/bazar/`, puis il les range sous tes yeux. Il est **non interactif** :
il ne pose aucune question, tu n'as rien à taper.

Le dossier `bash/projets/exemples/` est **ignoré par git** : tu peux donc expérimenter
sans polluer le dépôt. Pour tout nettoyer :

```bash
rm -rf bash/projets/exemples
```

---

## 🧩 Ce que le projet t'apprend à combiner

- **Robustesse (module 06)** : `set -euo pipefail` pour que le script s'arrête net à la
  moindre erreur, plutôt que de continuer dans le vide.
- **Boucles `for` (module 02)** : parcourir tous les fichiers d'un dossier, un par un.
- **Conditions `[[ ]]` et `case` (modules 01–02)** : tester si c'est un fichier, puis
  choisir le bon dossier de destination selon l'extension.
- **Manipulation de chemins** : isoler le nom (`basename`) et l'extension (`${nom##*.}`).
- **`mkdir -p` et `mv`** : créer les dossiers de destination et y déplacer les fichiers.

---

## Et ensuite ?

Le meilleur exercice : **prends une vraie corvée de ta vie** (un dossier `Téléchargements`
en désordre, par exemple) et adapte `organiser.sh` pour la régler. C'est comme ça qu'on
apprend pour de bon. 🚀
