# Module 09 (avancé) — Lancer des tâches EN PARALLÈLE

Jusqu'ici, tes scripts faisaient **une seule chose à la fois**, dans l'ordre, de haut en
bas. Par défaut, Bash **attend** que chaque commande soit **complètement finie** avant de
passer à la suivante. On dit qu'il travaille en **séquentiel** (à la file). C'est sûr et
prévisible… mais parfois on perd beaucoup de temps à attendre.

Ce module **avancé** t'apprend à lancer plusieurs tâches **« en même temps »** quand c'est
utile, et à **attendre** proprement qu'elles soient toutes terminées.

> 🧠 Lis cette théorie en entier **avant** d'ouvrir les fichiers `.sh`. Les deux scripts du
> module sont : `jobs.sh` (lancer plusieurs tâches en arrière-plan avec `&` puis `wait`) et
> `parallele_xargs.sh` (traiter une liste d'éléments en parallèle avec `xargs -P`).

---

## 1. Le comportement par défaut : séquentiel (à la file)

Quand tu écris deux commandes l'une après l'autre, Bash exécute la première **jusqu'au
bout**, **puis** seulement il lance la deuxième :

```bash
sleep 1     # Bash attend 1 seconde ici, sans rien faire d'autre
sleep 1     # PUIS il attend encore 1 seconde
# Total : 2 secondes
```

> 🧠 **Analogie.** Tu as deux machines à laver pleines de linge. En séquentiel, tu lances la
> première machine, tu **restes planté** devant jusqu'à la fin du cycle, **puis** tu lances la
> deuxième. Deux cycles complets, l'un après l'autre. Quel gâchis de temps !

---

## 2. Le `&` : lancer une commande EN ARRIÈRE-PLAN

Si tu ajoutes un **`&`** à la **fin** d'une commande, Bash la lance **en arrière-plan** : il
**n'attend pas** qu'elle finisse et passe **tout de suite** à la ligne suivante.

```bash
sleep 1 &    # lancée en arrière-plan : Bash N'ATTEND PAS, il continue
sleep 1 &    # lancée elle aussi tout de suite
# Les deux 'sleep' tournent EN MÊME TEMPS -> total proche de 1 seconde
```

> 🧠 **Analogie (la bonne !).** Tu lances la **première machine à laver**, et **sans
> attendre**, tu vas lancer la **deuxième** machine à côté. Maintenant **les deux tournent en
> même temps**. Tu as occupé le temps mort. C'est exactement ce que fait le `&`.

Chaque commande lancée avec `&` devient une **tâche d'arrière-plan** (en anglais, un *job*).
Bash te rend la main immédiatement pour faire autre chose.

---

## 3. Le `wait` : attendre que TOUTES les tâches finissent

Problème : si ton script se termine alors que des tâches d'arrière-plan tournent encore, tu
risques de lire des résultats **pas encore prêts**. Il faut donc un moyen de dire « **stop, je
patiente jusqu'à ce que tout le monde ait fini** ».

C'est le rôle de **`wait`** (sans argument) : il **attend que TOUTES** les tâches
d'arrière-plan lancées soient **terminées**, puis laisse le script continuer.

```bash
sleep 1 &    # machine 1 en route
sleep 1 &    # machine 2 en route
wait         # j'attends ici que LES DEUX machines aient fini leur cycle
echo "Tout le linge est lavé !"   # ne s'affiche qu'une fois les deux finies
```

> 🧠 **Analogie.** Tu as lancé tes deux machines en même temps. `wait`, c'est toi qui
> **t'assieds devant la buanderie** et qui attends que **les deux** aient sonné avant
> d'étendre le linge. Tu ne commences pas à étendre tant qu'une machine tourne encore.

> ✅ **Le schéma à retenir :** on **lance** tout avec `&`, **puis** on **rassemble** avec
> `wait`. Lancer d'abord, attendre ensuite.

---

## 4. Quand c'est utile ? (la question la plus importante)

Le parallélisme n'accélère pas tout. Il aide surtout les tâches qui **ATTENDENT** quelque
chose d'extérieur, exactement comme dans le [module 09 de Python](../../python/automatisation/09_concurrence/)
sur la concurrence.

- **Tâche qui attend (réseau, disque…)** : télécharger plusieurs fichiers, interroger
  plusieurs serveurs. Pendant qu'une commande **attend** la réponse, les autres peuvent
  avancer. 👉 **le parallélisme fait gagner beaucoup de temps.**
- **Tâche de calcul pur** : compresser, chiffrer, calculer sans arrêt. Là, il faut **plusieurs
  cœurs** du processeur ; le gain dépend du nombre de cœurs disponibles.

> 💡 La même règle qu'en Python : on accélère surtout ce qui **attend**. Si une commande
> passe son temps à patienter (un téléchargement), la lancer en arrière-plan avec `&` pendant
> que d'autres tournent fait une **énorme** différence.

> ⚠️ **Attention à l'ordre.** Les tâches d'arrière-plan finissent dans le **désordre** (on ne
> sait pas laquelle d'abord). Pour un résultat **déterministe** (toujours le même), chaque
> tâche écrit dans **son propre fichier** (indexé), et on **agrège** seulement **après**
> `wait`. C'est précisément la technique de `jobs.sh`.

---

## 5. Traiter une liste en parallèle : `xargs -P N`

Lancer 3 `&` à la main, ça va. Mais pour appliquer **la même commande** à **plein**
d'éléments, le faire à la main devient pénible. L'outil **`xargs`** est fait pour ça, et son
option **`-P N`** dit : « exécute jusqu'à **N** tâches **en parallèle** ».

```bash
# Imprime 3 noms, un par ligne, et lance 'echo Bonjour <nom>' avec 2 en parallèle :
printf '%s\n' Alice Bob Chloe | xargs -P 2 -I {} echo "Bonjour {}"
```

Décortiquons les options :

- **`-P 2`** → au maximum **2** tâches tournent **en même temps** (le « degré » de
  parallélisme). Mets `-P 4` pour quatre à la fois, etc.
- **`-I {}`** → définit un **marqueur** (`{}`) qui sera **remplacé** par chaque élément lu.
  Ici chaque ligne reçue remplace le `{}` dans la commande.

> 🧠 **Analogie.** `xargs -P N`, c'est un **chef d'équipe** : tu lui donnes une **pile de
> tickets** (la liste) et tu lui dis « fais bosser **N ouvriers à la fois** ». Dès qu'un
> ouvrier a fini son ticket, il en prend un nouveau, jusqu'à ce que la pile soit vide.

> ⚠️ Comme avec `&`, les lignes peuvent **sortir dans le désordre**, puisque plusieurs tâches
> écrivent en même temps. C'est normal et attendu en parallèle.

➡️ C'est exactement ce que montre **`parallele_xargs.sh`**.

---

## 6. Le résumé

| Ta situation | L'outil |
|--------------|---------|
| Lancer **quelques** tâches en même temps, puis les attendre | **`&`** puis **`wait`** |
| Appliquer **une commande** à **plein** d'éléments, N en parallèle | **`xargs -P N`** |
| Une seule tâche, ou des tâches qui ne font que **calculer** un peu | reste **séquentiel** |

> 💡 En cas de doute, commence **séquentiel** (c'est plus simple et plus sûr). N'ajoute du
> parallélisme **que** si ton script est lent **parce qu'il attend**. Le parallélisme ajoute
> de la complexité (ordre imprévisible) : il doit servir à quelque chose.

---

## ▶️ À toi de jouer

```bash
# Lance plusieurs tâches en arrière-plan, attend tout, agrège (total toujours identique) :
bash bash/09_parallelisme/jobs.sh

# Traite une petite liste en parallèle avec xargs -P :
bash bash/09_parallelisme/parallele_xargs.sh
```

Lis les deux fichiers, puis **expérimente** : dans `jobs.sh`, enlève le `wait` et observe que
le total devient faux (on agrège avant la fin des tâches !). Dans `parallele_xargs.sh`, change
le `-P` et regarde l'ordre des lignes bouger.

➡️ Retour au sommaire du parcours : [`README.md`](../README.md).
