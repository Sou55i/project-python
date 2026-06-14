# Module 02 — Fichiers, redirections et pipes

Jusqu'ici, tes scripts **affichaient** des choses à l'écran. Maintenant tu vas apprendre à
**écrire dans des fichiers**, à les **relire**, et à **brancher des commandes les unes sur les
autres**. C'est le vrai super-pouvoir du Bash : faire circuler des données.

> Fichiers du module : `redirections.sh` (écrire/ajouter/relire) et `parcourir.sh` (parcourir
> un dossier). Lance-les avec `bash <fichier>` **depuis la racine du dépôt** (voir en bas).

---

## 1. Tout part de `echo`… qui parle à l'écran

Quand tu écris `echo "salut"`, le texte part vers ce qu'on appelle la **sortie standard** :
par défaut, c'est ton **écran** (le terminal).

L'idée des **redirections**, c'est de **détourner ce flux** : au lieu d'aller à l'écran, le
texte peut aller **dans un fichier**.

> 🔧 **Analogie du tuyau d'arrosage.** `echo` est un robinet qui crache de l'eau (du texte).
> Par défaut, l'eau tombe par terre (l'écran). Une redirection, c'est brancher un **tuyau**
> au bout du robinet pour envoyer l'eau ailleurs : dans un seau (un fichier), ou vers un autre
> robinet (une autre commande).

---

## 2. Les redirections : `>`, `>>` et `<`

### `>` — écrire dans un fichier (et **écraser** ce qu'il contenait)

```bash
echo "premiere ligne" > notes.txt
```

Cela crée le fichier `notes.txt` (ou le **vide** s'il existait déjà !) et y met la ligne.

> ⚠️ **Attention danger.** `>` **écrase tout** le contenu précédent, sans prévenir. Le seau est
> vidé avant d'être rempli. C'est l'erreur classique du débutant.

### `>>` — **ajouter** à la fin du fichier (sans rien écraser)

```bash
echo "deuxieme ligne" >> notes.txt
echo "troisieme ligne" >> notes.txt
```

Avec **deux** chevrons, on **ajoute** à la suite. Le seau se remplit, ligne après ligne.

> 🔑 Retiens la différence : **un** chevron `>` = je **remplace**. **Deux** chevrons `>>` =
> j'**ajoute**.

### `<` — lire **depuis** un fichier

`<` fait l'inverse : il prend le contenu d'un fichier et le **donne à manger** à une commande.

```bash
while IFS= read -r ligne; do
    echo "Lu : $ligne"
done < notes.txt        # le < envoie le fichier dans la boucle
```

On y revient en détail au point 5.

---

## 3. Afficher un fichier : `cat`, `head`, `tail`

Pour **regarder** ce qu'il y a dans un fichier :

```bash
cat notes.txt       # affiche TOUT le contenu
head -n 2 notes.txt # affiche les 2 PREMIÈRES lignes
tail -n 2 notes.txt # affiche les 2 DERNIÈRES lignes
```

- `cat` = « concatenate », il crache tout le fichier d'un coup.
- `head` regarde le **début**, `tail` la **fin**. `-n 2` veut dire « 2 lignes ».

---

## 4. Les pipes `|` : brancher une commande sur une autre

Le **pipe** (la barre verticale `|`) prend la **sortie** d'une commande et l'**envoie en
entrée** de la commande suivante. C'est le tuyau qui relie deux robinets.

```bash
cat notes.txt | head -n 1     # tout le fichier... dont on ne garde que la 1re ligne
```

Un autre exemple très courant : compter les lignes d'un fichier avec `wc -l`.

```bash
cat notes.txt | wc -l         # combien de lignes dans notes.txt ?
```

> 💡 On peut enchaîner **plusieurs** pipes : `commande1 | commande2 | commande3`. Chaque `|`
> passe le résultat au suivant, comme une chaîne de montage.

---

## 5. Lire un fichier **ligne par ligne**

La formule à connaître par cœur pour traiter un fichier ligne après ligne :

```bash
while IFS= read -r ligne; do
    echo "-> $ligne"
done < fichier.txt
```

Décortiquons cette formule (elle a l'air bizarre, c'est normal) :

- `while ... ; do ... done` : une boucle, comme au module 01.
- `read -r ligne` : lit **une** ligne du fichier et la range dans la variable `ligne`. La boucle
  se répète tant qu'il reste des lignes.
- `IFS=` (devant `read`) : empêche Bash de **rogner les espaces** en début/fin de ligne.
- `-r` : empêche Bash de **mal interpréter** les `\` (antislash). On garde la ligne telle quelle.
- `< fichier.txt` : la redirection `<` **branche le fichier** sur la boucle.

> 🔑 `IFS= read -r ligne` est une **formule magique** : recopie-la telle quelle. Avec
> l'expérience tu comprendras chaque morceau, mais pour l'instant l'important est qu'elle lit
> proprement **n'importe quelle** ligne, espaces compris.

---

## 6. Tester l'existence d'un fichier ou d'un dossier

Avant de lire un fichier, c'est prudent de **vérifier qu'il existe** (sinon : erreur). On
utilise les crochets `[[ ... ]]` vus au module 01 :

```bash
if [[ -f notes.txt ]]; then
    echo "Le fichier existe."
fi

if [[ -d mon_dossier ]]; then
    echo "Le dossier existe."
fi
```

- `-f fichier` : vrai si **fichier** existe **et** est un fichier normal.
- `-d dossier` : vrai si **dossier** existe **et** est un dossier (répertoire).

---

## 7. Créer un dossier : `mkdir -p`

```bash
mkdir -p exemples
```

`mkdir` (« make directory ») crée un dossier. L'option **`-p`** est précieuse :

- elle **ne râle pas** si le dossier existe déjà (pas d'erreur) ;
- elle crée au besoin **toute l'arborescence** (`mkdir -p a/b/c` crée `a`, puis `b`, puis `c`).

> 💡 On s'en sert dans `redirections.sh` pour ranger tous nos fichiers de test dans un
> sous-dossier `exemples/`, histoire de **ne pas polluer** le dépôt.

---

## ▶️ À toi de jouer

Lance les scripts **depuis la racine du dépôt** (ils créent un dossier `exemples/` local) :

```bash
bash bash/02_fichiers/redirections.sh
bash bash/02_fichiers/parcourir.sh
```

Le dossier `bash/02_fichiers/exemples/` est créé par les scripts pour la démonstration. Tu
peux le supprimer quand tu veux avec :

```bash
rm -rf bash/02_fichiers/exemples
```

Ensuite, **modifie** les scripts : ajoute des lignes, change le nom du fichier, affiche les
lignes dans l'ordre inverse avec `tail`…

➡️ La suite du parcours (arguments de script, petits projets…) arrivera dans le même style.
