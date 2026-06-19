# 🧑‍💻 Apprendre à programmer — 9 langages, une seule pédagogie

[![CI](https://github.com/TN-RedTeam/apprendre-programmation/actions/workflows/ci.yml/badge.svg)](https://github.com/TN-RedTeam/apprendre-programmation/actions/workflows/ci.yml)

Ce dépôt enseigne **9 langages de programmation en français**, avec **la même approche
pédagogique** : on explique d'abord avec des mots simples, puis on illustre avec du code
**commenté presque ligne par ligne**.

> 🐍 **Tu cherches le cours de Python ?** Il a désormais son **dépôt dédié** :
> **👉 [TN-RedTeam/Python_guide](https://github.com/TN-RedTeam/Python_guide)** — c'est *la*
> référence pour apprendre à coder en partant de zéro. Ce dépôt-ci regroupe les **autres
> langages**.

> 💡 **On explique d'abord, on code ensuite.**
> Chaque module commence par un `README.md` qui pose la théorie avec des analogies, puis du
> code commenté. Lis, lance, modifie.

---

## 🗺️ Les langages

Du plus accessible au plus proche de la machine — chaque parcours est **autonome**.

| Langage | Pour quoi faire | Niveau |
|---------|-----------------|:------:|
| 🐚 **[Bash](./bash/)** | automatiser le terminal Linux/macOS, enchaîner des outils | ⭐⭐ |
| 🟦 **[PowerShell](./powershell/)** | automatiser/administrer Windows (pipeline d'objets) | ⭐⭐ |
| 🐹 **[Go](./go/)** | serveurs, outils en ligne de commande, un seul binaire | ⭐⭐ |
| 🦀 **[Rust](./rust/)** | performance **+ sûreté mémoire** garantie à la compilation | ⭐⭐⭐ |
| ➕ **[C++](./cpp/)** | logiciels exigeants, jeux, moteurs, la STL | ⭐⭐⭐ |
| 🇨 **[C](./c/)** | systèmes, embarqué, pointeurs et mémoire manuelle | ⭐⭐⭐⭐ |
| ⚙️ **[Assembleur](./asm/)** | le plus bas niveau : voir **tout** ce que les autres cachent | ⭐⭐⭐⭐⭐ |
| 🟨 **[JS / TS](./js-ts/)** | le langage du **web** et de Node.js (TypeScript ajoute les types) | ⭐⭐ |
| ☕ **[Java](./java/)** | applications d'entreprise, Android, multiplateforme (JVM) | ⭐⭐⭐ |

> 🐍 **Python** n'est plus ici : il vit dans son propre dépôt →
> **[Python_guide](https://github.com/TN-RedTeam/Python_guide)** (idéal pour **débuter**).

---

## 🚦 Par où commencer ?

- **Tu débutes totalement** → commence par **[Python](https://github.com/TN-RedTeam/Python_guide)**
  (dépôt dédié), puis reviens ici pour un 2ᵉ langage.
- **Tu automatises Unix** → [Bash](./bash/). **Windows** → [PowerShell](./powershell/).
- **Tu veux comprendre la machine** → [C](./c/), puis [Assembleur](./asm/).
- **Tu veux de la perf** → [Go](./go/), [Rust](./rust/), [C++](./cpp/).

➡️ Détails et ordre conseillé : **[SOMMAIRE.md](./SOMMAIRE.md)**.

---

## 📎 Ressources transverses

- 🔬 **[COMPARATIF.md](./COMPARATIF.md)** — le **même** concept (variable, boucle, fonction…)
  écrit dans chaque langage, + « quel langage pour quelle tâche ».
- 🔐 **[SECURITE.md](./SECURITE.md)** — index des démos de sécurité **éducatives** (scanners,
  démos offensives *vulnérable vs corrigé*). ⚠️ Usage autorisé uniquement.

---

## 🚀 Démarrer

```bash
git clone <url-de-ce-depot>
cd apprendre-programmation
# Puis ouvre le dossier du langage qui t'intéresse, ex. :
bash bash/00_demarrer/hello.sh
go run go/00_demarrer/hello.go
```

Chaque module indique en en-tête comment le lancer.

---

## 📄 Licence

Voir le fichier [LICENSE](./LICENSE). Contenu à but **éducatif**.
