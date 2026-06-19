# 🐞 Module 07 : Débugger (trouver et corriger ses bugs)

> 🎯 **Objectif** : un bug n'est pas une honte, c'est le quotidien. Ce qui distingue un dev
> aguerri, c'est sa **méthode** pour localiser le problème vite. Tu vas apprendre à lire une
> erreur, à inspecter ton programme en marche, et à raisonner comme un détective.

---

## 1. D'abord : lire le message d'erreur (le *traceback*)

90 % des débutants paniquent devant le « mur rouge » et ne le **lisent pas**. C'est pourtant une
carte au trésor. On le lit **de bas en haut** :

```
Traceback (most recent call last):
  File "calcul.py", line 8, in <module>
    moyenne = total / len(notes)
              ~~~~~~^~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

1. **Dernière ligne** → le **type** (`ZeroDivisionError`) et la **cause** (« division by zero »).
2. **Juste au-dessus** → le **fichier** et le **numéro de ligne** exacts (`line 8`), et même la
   portion fautive soulignée.
3. Si plusieurs `File ...` sont empilés, le **dernier** est l'endroit où ça a vraiment cassé ;
   les précédents montrent **qui a appelé qui** (la « pile d'appels »).

> 🔑 **Le réflexe gagnant** : copier le type d'erreur exact (`ZeroDivisionError`) dans une
> recherche web si tu ne le comprends pas. Tu n'es jamais le premier à l'avoir vu.

---

## 2. La méthode `print` (simple, efficace, universelle)

La technique la plus rapide : afficher la valeur des variables à des moments clés pour voir
**où la réalité diverge de ce que tu crois**.

```python
print(f"DEBUG total = {total!r}  notes = {notes!r}")
```

> 🔎 Le `!r` affiche la valeur en mode « brut » (*repr*) : tu vois les guillemets, donc tu
> distingues `5` (nombre) de `"5"` (texte) et `[]` (liste vide) de `""`. Inestimable pour
> repérer un mauvais **type**.

> 🧠 **L'erreur de raisonnement la plus fréquente** : « le bug est sûrement dans cette fonction
> compliquée ». Souvent il est **avant**, dans une variable qui ne contient pas ce que tu
> imagines. Le `print` te le révèle. **Ne devine pas — vérifie.**

---

## 3. Le debugger : mettre le programme en **pause**

Plus puissant que `print` : un *debugger* **gèle** le programme à un endroit et te laisse
inspecter **toutes** les variables, puis avancer pas à pas.

### `breakpoint()` — intégré, sans rien installer

Pose cette ligne où tu veux que ça s'arrête :

```python
total = 0
for note in notes:
    total += note
breakpoint()        # ⏸ le programme s'arrête ICI et ouvre une console pdb
moyenne = total / len(notes)
```

Au lancement, tu obtiens une invite `(Pdb)`. Les commandes essentielles :

| Commande | Raccourci | Effet |
|----------|-----------|-------|
| `print x` ou juste `x` | `p x` | affiche la valeur d'une variable |
| `next` | `n` | exécute la ligne **suivante** (sans entrer dans les fonctions) |
| `step` | `s` | exécute la ligne suivante **en entrant** dans la fonction appelée |
| `continue` | `c` | reprend l'exécution normale jusqu'au prochain arrêt |
| `list` | `l` | montre le code autour de la ligne courante |
| `quit` | `q` | quitte le debugger |

> 🧠 **`next` vs `step`** : `next` survole un appel de fonction (« je fais confiance à
> `len()` ») ; `step` plonge dedans (« je veux voir ce qui se passe à l'intérieur de **ma**
> fonction »). On alterne selon ce qu'on soupçonne.

### Le debugger graphique (VS Code, PyCharm…)

Dans un éditeur, clique dans la marge à gauche d'un numéro de ligne pour poser un **point
d'arrêt** (point rouge), puis lance en mode *Debug*. Mêmes idées, en visuel : le panneau des
variables se met à jour à chaque pas. **C'est la méthode confortable au quotidien.**

---

## 4. La démarche du détective (le plus important)

Un outil ne remplace pas le raisonnement. Face à un bug :

1. **Reproduire** : trouve l'entrée précise qui déclenche le bug à coup sûr.
2. **Localiser** : encadre la zone fautive (par `print` / point d'arrêt). Réduis le champ de
   recherche par dichotomie : « le problème est-il avant ou après cette ligne ? ».
3. **Comprendre** : compare ce que tu **attends** à ce que tu **observes**. L'écart est le bug.
4. **Corriger un seul truc à la fois**, puis revérifier. Changer dix choses d'un coup t'empêche
   de savoir laquelle a marché.

> 🧠 **Le « canard en plastique »** (*rubber duck debugging*) : explique ton code **à voix
> haute**, ligne par ligne, à un objet (ou un collègue). Très souvent, l'erreur te saute aux
> yeux **pendant** que tu l'expliques. C'est sérieux, et ça marche.

---

## 🏁 Exercices

1. **Lance** [`demo_debug.py`](./demo_debug.py) : il contient un bug subtil.
2. **Pose un `breakpoint()`** avant la ligne suspecte et inspecte la variable `total` (avec `p
   total`), puis avance avec `n`.
3. **Provoque** chaque type d'erreur du tableau du [module 04](../04_exceptions_fichiers/) et
   entraîne-toi à lire le traceback : type + ligne + cause.

➡️ **Prochaine étape** : [module 08 — asyncio](../08_asyncio/).
