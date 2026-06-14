# Module 03 — La manipulation de texte (le super-pouvoir du shell)

Voici **LA** raison pour laquelle Bash est incontournable. Sur ta machine, presque tout est
du **texte** : les logs d'un serveur, un export `CSV`, la sortie d'une commande… Et Bash sait
**filtrer**, **trier**, **compter** et **transformer** ce texte en quelques caractères, sans
ouvrir le moindre logiciel.

> 💡 Même pédagogie que partout : **on explique d'abord, on code ensuite.**
> Fichiers du module : `filtrer.sh` (chercher / extraire / compter) et `transformer.sh`
> (remplacer / calculer). Lance-les **depuis la racine du dépôt** (voir en bas).

---

## 🧠 L'idée centrale : une chaîne de petits outils

En Bash, on n'a pas UN gros outil qui fait tout. On a **plein de petits outils** qui font
**chacun une seule chose, mais très bien**. On les **branche les uns aux autres** avec le
**tube** (le caractère `|`, appelé *pipe*).

> 🔧 **Analogie : la chaîne de tri à la poste.** Le courrier passe sur un tapis roulant. Une
> première machine **écarte** les lettres sans timbre (`grep`), une deuxième **découpe** pour
> ne garder que le code postal (`cut`), une troisième **range** par ordre (`sort`)… À la fin,
> le travail est fait, alors qu'aucune machine seule ne savait tout faire. Le `|`, c'est le
> **tapis roulant** : il fait passer le résultat d'un outil **vers l'entrée du suivant**.

```bash
commande1 | commande2 | commande3
#        ↑           ↑
#     la sortie de gauche devient l'entrée de droite
```

---

## 1. `grep` — chercher des lignes

`grep` garde **uniquement les lignes** qui contiennent un mot (comme la touche « Rechercher »
d'un éditeur, mais qui te renvoie **toutes** les lignes trouvées d'un coup).

```bash
grep "ERROR" journal.log       # affiche les lignes contenant ERROR
grep -i "error" journal.log    # -i : ignore la casse (error, ERROR, Error...)
grep -v "INFO" journal.log     # -v : INVERSE → les lignes qui N'ont PAS "INFO"
grep -c "ERROR" journal.log    # -c : COMPTE les lignes trouvées
```

---

## 2. `cut` — extraire des colonnes

`cut` **découpe** chaque ligne et n'en garde qu'un **morceau**. Très pratique pour un fichier
où les champs sont séparés par un caractère (une virgule dans un CSV, un `:` dans `/etc/passwd`).

```bash
cut -d',' -f1 clients.csv      # -d',' : le séparateur est la virgule
                               # -f1   : on garde le 1er champ (field)
cut -d',' -f1,3 clients.csv    # le 1er ET le 3e champ
```

> 🔧 **Analogie :** `cut`, c'est le **massicot**. Tu lui dis où couper (`-d`) et quelle
> bande garder (`-f`).

---

## 3. `sort` — trier

`sort` **range les lignes** par ordre alphabétique (ou numérique avec `-n`).

```bash
sort noms.txt                  # ordre alphabétique
sort -n nombres.txt            # ordre NUMÉRIQUE (sinon 10 passe avant 2 !)
sort -r noms.txt               # -r : ordre inverse (reverse)
```

---

## 4. `uniq` — dédoublonner

`uniq` **supprime les doublons**… mais **seulement s'ils se suivent**. C'est pour ça qu'on
fait presque toujours **`sort | uniq`** : on trie d'abord pour regrouper les identiques.

```bash
sort noms.txt | uniq           # chaque nom une seule fois
sort noms.txt | uniq -c        # -c : COMPTE combien de fois chacun apparaît
```

---

## 5. `wc -l` — compter

`wc` compte (*word count*). L'option qui sert le plus est **`-l`** : compter les **lignes**.

```bash
wc -l journal.log              # combien de lignes dans le fichier ?
grep "ERROR" journal.log | wc -l   # combien de lignes contiennent ERROR ?
```

---

## 6. `sed 's/x/y/'` — remplacer

`sed` est le **chercher-remplacer** du terminal. La formule magique est `s/ancien/nouveau/`
(*s* comme *substitute*) :

```bash
sed 's/chat/chien/'  animaux.txt   # remplace le 1er "chat" de chaque ligne
sed 's/chat/chien/g' animaux.txt   # g = GLOBAL → TOUS les "chat" de la ligne
echo "bonjour" | sed 's/o/0/g'     # affiche : b0nj0ur
```

> ⚠️ Par défaut `sed` **affiche** le résultat sans toucher au fichier d'origine. Parfait pour
> s'entraîner sans rien casser.

---

## 7. `awk '{print $1}'` — champs et calculs

`awk` est le plus puissant : il voit chaque ligne **découpée en champs** appelés `$1`, `$2`,
`$3`… (`$0` = la ligne entière). Il sait aussi **calculer**.

```bash
awk '{print $1}'        fichier   # affiche le 1er champ de chaque ligne
awk '{print $2, $1}'    fichier   # le 2e puis le 1er (on réorganise !)
awk -F',' '{print $1}'  data.csv  # -F',' : champs séparés par une virgule

# Un vrai petit calcul : additionner la colonne 2 et afficher le total à la fin
awk '{total = total + $2} END {print "Total :", total}' ventes.txt
```

> 🔑 `$1` dans `awk` = **un champ de la ligne** (à ne pas confondre avec `$1` en Bash, qui est
> un argument du script !).

---

## 🔗 On ENCHAÎNE tout avec des pipes

C'est là que la magie opère. Question : **quelles sont les 3 adresses IP qui apparaissent le
plus dans un log ?**

```bash
grep "ERROR" acces.log \
  | cut -d' ' -f1 \
  | sort \
  | uniq -c \
  | sort -rn \
  | head -3
```

En français, ligne par ligne :
1. `grep "ERROR"` → ne garde que les lignes en erreur,
2. `cut -d' ' -f1` → extrait la 1re colonne (l'IP),
3. `sort` → regroupe les IP identiques,
4. `uniq -c` → compte chaque IP,
5. `sort -rn` → trie par nombre décroissant,
6. `head -3` → garde le top 3.

> 🚀 **C'est ÇA, le super-pouvoir.** Une question concrète sur un fichier de 100 000 lignes,
> résolue en une ligne, en une fraction de seconde. Aucun tableur ne va aussi vite. Voilà
> pourquoi Bash reste **incontournable** pour traiter logs et CSV.

---

## ▶️ À toi de jouer

```bash
# IMPORTANT : lance ces scripts DEPUIS LA RACINE du dépôt.
bash bash/03_texte/filtrer.sh
bash bash/03_texte/transformer.sh
```

Les deux scripts **créent un petit fichier de démo**, montrent les commandes en action, puis
**nettoient tout derrière eux** : ils ne laissent aucune trace sur ta machine.

Lis-les, puis **bidouille** : change le mot cherché par `grep`, le séparateur de `cut`, ou
le calcul de `awk`.

➡️ La suite du parcours arrivera dans le même style.
