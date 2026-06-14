# Module 07 — Débugger : voir ce que fait vraiment ton script

Un script Bash qui ne fait **pas** ce que tu attendais, ce n'est pas une fatalité. Le
problème, c'est qu'on **ne voit pas** ce que Bash exécute réellement : les variables sont
remplacées par leurs valeurs en coulisses, et tout va trop vite. Débugger, c'est
**rallumer la lumière** pour observer le script en train de travailler, étape par étape.

> 💡 Même pédagogie que partout : **on explique d'abord, on code ensuite.**
> Fichier du module : `demo_debug.sh` (un petit calcul correct qui allume puis éteint la trace).

---

## 1. La technique reine : `set -x` (la trace)

C'est l'outil **numéro un** pour débugger en Bash. `set -x` dit à Bash :

> « À partir de maintenant, **affiche chaque commande** que tu exécutes, **avec les valeurs
> réelles** des variables, juste avant de la lancer. »

Chaque ligne tracée apparaît préfixée par un **`+`** (un plus). C'est ça, la **trace**.

Imagine ce minuscule bout de script :

```bash
prix=12
quantite=3
set -x                          # on ALLUME la trace
total=$(( prix * quantite ))
echo "Total : $total euros"
```

À l'exécution, Bash affiche (sur la sortie d'erreur) **ce qu'il fait vraiment** :

```
+ total=36
+ echo 'Total : 36 euros'
Total : 36 euros
```

> 🔑 **Lis bien la différence.** Les lignes qui commencent par `+` sont la **trace** (ce que
> Bash exécute, **avec les variables déjà remplacées** : on voit `36`, pas `$total`). La ligne
> **sans `+`** (`Total : 36 euros`) est la **vraie sortie** de ton `echo`. La trace te montre
> donc, en direct, la valeur de chaque variable au moment où elle est utilisée — c'est
> exactement ce qu'on cherche quand « ça ne marche pas ».

### L'allumer et l'éteindre

- **`set -x`** → **allume** la trace.
- **`set +x`** → **l'éteint** (le `+` au lieu du `-` coupe l'option).

> 🧠 **Analogie.** `set -x`, c'est mettre des **lunettes à rayons X** : tu vois soudain
> l'intérieur de la machine. Tu ne les gardes pas toute la journée : tu les chausses **autour
> de la zone louche**, le temps de comprendre, puis tu les enlèves avec `set +x`.

### Tout tracer sans toucher au script : `bash -x`

Tu peux aussi tracer un script **entier** sans y ajouter une seule ligne, en le lançant
avec l'option `-x` directement :

```bash
bash -x bash/07_debugger/demo_debug.sh
```

Pratique pour inspecter un script qui n'est pas le tien, ou pour tout voir d'un coup.

---

## 2. Le débogage par `echo` (inspecter une variable)

La technique la plus simple du monde, et la plus utilisée : **afficher une variable** juste
avant la ligne qui te pose problème, pour vérifier **ce qu'elle contient vraiment**.

```bash
echo "DEBUG : age=$age"      # que vaut age exactement, à cet instant ?
```

Souvent, le bug saute aux yeux : la variable est **vide**, contient un **espace en trop**, ou
n'est pas du tout ce que tu croyais. C'est le cousin du `print(...)` de Python.

> 💡 Préfixe tes messages par `DEBUG` pour les repérer (et penser à les enlever après).

---

## 3. `shellcheck` : l'analyseur qui repère les erreurs AVANT l'exécution

`shellcheck` est un outil **gratuit** qui **lit ton script sans l'exécuter** et te signale
les erreurs classiques : guillemets oubliés, variable jamais utilisée, faute de syntaxe…
C'est un **correcteur orthographique pour Bash**.

Il n'est pas toujours installé. Pour l'ajouter :

```bash
sudo apt install shellcheck       # Debian / Ubuntu
brew install shellcheck           # macOS (avec Homebrew)
```

Puis tu le lances sur ton script :

```bash
shellcheck bash/07_debugger/demo_debug.sh
```

Il t'affiche chaque problème avec le **numéro de ligne**, une **explication**, et souvent la
**correction** à appliquer. À prendre comme un coéquipier qui relit par-dessus ton épaule.

> 💡 Au quotidien : passe `shellcheck` **d'abord** (il attrape les fautes évidentes), et
> garde `set -x` pour les bugs de **logique** qui demandent de voir les valeurs en direct.

---

## 4. Les erreurs FRÉQUENTES en Bash (cause → solution)

Le tableau à garder sous la main. La plupart des bugs de débutant sont là-dedans :

| Erreur / symptôme | Cause fréquente | Solution |
|-------------------|-----------------|----------|
| `command not found` | Faute de frappe dans le nom, **ou** des **espaces autour du `=`** : `x = 5` (Bash croit alors que `x` est une commande !) | Vérifie l'orthographe. Pour affecter : **`x=5`** sans espace autour du `=`. |
| `unbound variable` | Avec `set -u`, tu utilises une variable **jamais définie** (souvent une faute de frappe sur son nom). | Définis-la **avant**, et corrige son nom. Valeur par défaut possible : `"${nom:-inconnu}"`. |
| Une valeur se « coupe » / résultat bizarre | **Guillemets oubliés** autour d'une variable qui contient des **espaces** : `cp $fichier dest` se casse si le nom a une espace. | Mets **toujours** les guillemets : `cp "$fichier" dest`. |
| Comparaison qui se comporte mal dans `[[ ]]` | Confusion **`-eq`** (comparer des **NOMBRES**) et **`==`** (comparer du **TEXTE**). | Nombres : `[[ "$a" -eq 3 ]]`. Texte : `[[ "$mot" == "oui" ]]`. |
| `syntax error near unexpected token` (souvent `done`/`fi`) | Oubli du **`; then`** après un `if`, ou du **`; do`** après un `for`/`while`. | Écris `if ...; then`, `for ...; do`, `while ...; do` (le `;` puis `then`/`do`). |

> 🧠 **Le piège n°1 du débutant Bash, c'est l'espace.** `x=5` ✅ contre `x = 5` ❌, et
> `"$fichier"` ✅ contre `$fichier` ❌. Garde-le en tête : la moitié des bugs viennent de là.

---

## ▶️ À toi de jouer

Lance d'abord le script **normalement** : il fait un petit calcul et allume la trace sur une
portion, pour que tu voies les lignes `+ ...` apparaître au milieu de la sortie.

```bash
bash bash/07_debugger/demo_debug.sh
```

Puis relance-le en **trace totale** pour voir CHAQUE ligne exécutée du début à la fin :

```bash
bash -x bash/07_debugger/demo_debug.sh
```

Compare les deux sorties : tu verras où la trace (`+ ...`) s'allume et s'éteint dans le
premier cas, et comment tout est tracé dans le second.

➡️ Avec `set -x`, `echo` et `shellcheck`, tu as de quoi traquer n'importe quel bug Bash. 💪
