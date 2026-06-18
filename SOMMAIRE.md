# 🗺️ Sommaire & parcours d'apprentissage

Ce dépôt enseigne **10 langages** avec la **même pédagogie**. Cette page sert de **point de
départ** : elle te dit *dans quel ordre* apprendre, et te donne tous les liens.

> Tu hésites sur le langage à choisir selon ton objectif ? Lis d'abord le
> **[COMPARATIF.md](./COMPARATIF.md)** (la même chose dans plusieurs langages + « quel langage
> pour quelle tâche »).

---

## 🚦 Par où commencer ? (roadmap conseillée)

L'ordre n'est pas obligatoire, mais voici une progression qui va du plus accessible au plus
technique — chaque étape réutilise des concepts de la précédente.

| Ordre | Langage | Pourquoi à ce moment-là |
|:----:|---------|--------------------------|
| 1 | 🐍 **[Python](./python/)** | Le plus lisible : tu apprends les **concepts** (variables, boucles, fonctions, objets) sans te battre avec la syntaxe. |
| 2 | 🐚 **[Bash](./bash/)** | Automatiser ton terminal et enchaîner des outils : indispensable au quotidien sous Linux/macOS. |
| 3 | 🟦 **[PowerShell](./powershell/)** | L'équivalent côté **Windows**, avec une idée puissante : le pipeline d'**objets**. |
| 4 | 🐹 **[Go](./go/)** | Premier langage **compilé** mais doux : typage statique, mais mémoire automatique. |
| 5 | 🇨 **[C](./c/)** | Tu passes « sous le capot » : compilation, types, **pointeurs et mémoire** manuelle. |
| 6 | ➕ **[C++](./cpp/)** | Le C + les objets et la **STL** : la performance avec des outils modernes. |
| 7 | ⚙️ **[Assembleur](./asm/)** | Le plus bas niveau : tu vois **tout** ce que les autres langages cachent. |

Et trois langages très demandés, à aborder quand tu veux :

| Langage | Pourquoi l'apprendre |
|---------|----------------------|
| 🟨 **[JS / TS](./js-ts/)** | Le langage du **web** et de Node.js ; TypeScript y ajoute les types. |
| ☕ **[Java](./java/)** | Très orienté objet, multiplateforme (JVM), incontournable en entreprise. |
| 🦀 **[Rust](./rust/)** | Performance du C **+ sécurité mémoire** garantie à la compilation. |

> 💡 Tu peux aussi suivre **un seul** langage de bout en bout selon ton besoin. Chaque parcours
> est autonome.

---

## 🧩 La structure commune à chaque langage

Chaque parcours suit **exactement le même plan** (clique sur un langage pour le détail) :

- **00 → 01** — démarrer + les bases (variables, conditions, boucles, fonctions)
- **02 → 06** — le cœur du langage (sa spécialité)
- **07** — **débugger** (trouver et corriger les bugs)
- **08 → 09** — **modules avancés**
- **`projets/`** — un **projet capstone** qui combine plusieurs modules
- **`pentest/`** — un **module sécurité** (éducatif, éthique)
- **Ressources** — aide-mémoire, glossaire, anatomie d'un programme/script

---

## 📚 Les 10 parcours en un coup d'œil

| Langage | Le cœur du parcours (modules 02→06/09) | Sécurité |
|---------|-----------------------------------------|----------|
| 🐍 **[Python](./python/)** | fichiers, web/APIs, données, POO, concurrence | [pentest](./python/pentest/) |
| 🐚 **[Bash](./bash/)** | fichiers/redirections, texte (grep/sed/awk), arguments, tableaux, parallélisme | [pentest](./bash/pentest/) |
| 🟦 **[PowerShell](./powershell/)** | fichiers, **pipeline d'objets**, paramètres, collections, modules | [pentest](./powershell/pentest/) |
| 🇨 **[C](./c/)** | tableaux/chaînes, **pointeurs & mémoire**, structures, fichiers, threads | [pentest](./c/pentest/) |
| ➕ **[C++](./cpp/)** | conteneurs, **classes & objets**, héritage, fichiers, STL, templates | [pentest](./cpp/pentest/) |
| 🐹 **[Go](./go/)** | slices/maps, structs, interfaces, fichiers, **concurrence** | [pentest](./go/pentest/) |
| ⚙️ **[Assembleur](./asm/)** | pile & fonctions, mémoire, E/S, chaînes, interfaçage C, récursion | [pentest](./asm/pentest/) |
| 🦀 **[Rust](./rust/)** | **propriété/ownership**, structs/enums, collections, erreurs, traits, concurrence | [pentest](./rust/pentest/) |
| 🟨 **[JS / TS](./js-ts/)** | objets/tableaux, fonctions, **async/await**, TypeScript, classes, HTTP | [pentest](./js-ts/pentest/) |
| ☕ **[Java](./java/)** | **POO**, héritage/interfaces, collections, exceptions, génériques, streams, threads | [pentest](./java/pentest/) |

---

## 🔭 Ressources transverses

- **[COMPARATIF.md](./COMPARATIF.md)** — le même code dans les 10 langages + guide de choix.
- **[SECURITE.md](./SECURITE.md)** — index de toutes les démos pentest (éducatives), par thème.
- **[Parcours Python complet](./python/)** — le plus fourni (idéal pour débuter).

Bon apprentissage ! 🚀
