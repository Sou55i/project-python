# 🛠️ Projet capstone — Organiser un dossier en bazar

Tu as parcouru les modules `00` à `06` ? Bravo ! Voici le moment le plus
important : un **vrai petit projet** qui **combine plusieurs notions à la fois**.
C'est en assemblant ce que tu sais qu'on devient autonome.

> 🐍 **Tu viens de Python ?** C'est l'équivalent PowerShell du projet
> [`ranger_dossier.py`](../../python/10_fichiers_dossiers/ranger_dossier.py).
> Même idée, autre langage : compare les deux, c'est très instructif.

---

## 🎯 Ce que fait le projet

Le scénario classique : un dossier « Téléchargements » en **bazar**, plein de
fichiers de toutes sortes. Le script `organiser.ps1` les **range** dans des
sous-dossiers selon leur **extension** :

| Extension | Va dans le dossier… |
|-----------|---------------------|
| `.txt`, `.pdf`, `.docx` | `Documents` |
| `.jpg`, `.jpeg`, `.png` | `Images` |
| `.csv`, `.xlsx` | `Tableaux` |
| `.mp3` | `Audio` |
| `.zip` | `Archives` |

> 🔒 **Sans aucun risque.** Le script n'est **pas interactif** : il fabrique
> d'abord un faux dossier de démo `exemples/bazar` rempli de **fichiers vides**,
> puis il le range. Tu peux le relancer autant de fois que tu veux sans rien
> casser. Le dossier `exemples/` est **ignoré par git**.

---

## 🧩 Les modules combinés

Ce projet rassemble presque tout le parcours :

| Module | Ce qu'on réutilise ici |
|--------|------------------------|
| [`02_fichiers`](../02_fichiers/) | Créer des dossiers (`New-Item -ItemType Directory -Force`) et des chemins |
| [`03_pipeline_objets`](../03_pipeline_objets/) | Lister des fichiers avec `Get-ChildItem` et lire `.Extension`, `.Name` |
| [`05_collections`](../05_collections/) | La **hashtable** `extension -> dossier`, et la boucle `foreach` |
| [`06_robustesse`](../06_robustesse/) | Le `try / catch` qui évite que le script plante |

> 🗺️ Le script commence par un bloc **« CHEMINEMENT DU SCRIPT »** qui résume ses
> étapes : lis-le en premier pour comprendre la logique avant de plonger dans le code.

---

## ▶️ Lancer le projet

Depuis la **racine du dépôt** :

```bash
pwsh powershell/projets/organiser.ps1
```

Tu verras défiler le rangement, puis tu pourras ouvrir
`powershell/projets/exemples/bazar` pour admirer les sous-dossiers créés.

---

## 🚀 Et ensuite ?

- **Relance** le script et observe que `-Force` évite les erreurs même si les
  dossiers existent déjà.
- **Ajoute une extension** dans la hashtable `$rangement` (par exemple
  `.mp4 = "Videos"`), ajoute un faux fichier dans la démo, et relance.
- Le meilleur exercice : **prends une vraie corvée de rangement** chez toi et
  adapte le script pour l'automatiser. C'est comme ça qu'on apprend pour de bon.
