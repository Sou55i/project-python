# Module 05 — Manipulation de CHAÎNES de caractères

Jusqu'ici, tu affichais des textes **figés** ou tu calculais avec des **nombres**. Dans ce
module, on apprend à **manipuler du texte** : mesurer la longueur d'une chaîne, et la
transformer caractère par caractère (la passer en MAJUSCULES).

> Fichiers du module : [`longueur.s`](./longueur.s) (compter les caractères d'une chaîne) et
> [`majuscules.s`](./majuscules.s) (transformer une chaîne en majuscules puis l'afficher).
> Tout est commenté presque ligne par ligne.

---

## 1. C'est quoi une « chaîne » en mémoire ?

Une **chaîne de caractères**, c'est juste une **suite d'octets** rangés les uns à la suite des
autres en mémoire. Chaque octet contient le **code ASCII** d'un caractère.

Par exemple, la chaîne `"abc"` occupe **3 octets** en mémoire :

```
 adresse :  +0    +1    +2
 octet   :  97    98    99
 (vu     :  'a'   'b'   'c')
```

> 🔑 Rappel du module 04 : un caractère n'est qu'un **nombre**. `'a'` vaut **97**, `'b'` vaut
> **98**, etc. Le processeur ne « voit » que des nombres ; c'est l'écran qui dessine la lettre.

---

## 2. Parcourir une chaîne avec un POINTEUR qui avance

Pour traiter une chaîne, on utilise un **pointeur** : un registre qui contient l'**adresse**
du caractère qu'on est en train de regarder. Pour passer au caractère **suivant**, il suffit
d'**ajouter 1** à ce pointeur — c'est ce que fait l'instruction `inc` (incrémenter = +1).

```asm
lea rsi, [texte]   # rsi pointe sur le 1er caractère
mov al, [rsi]      # al = le caractère sous le pointeur
inc rsi            # le pointeur avance d'une case (caractère suivant)
```

On répète ça dans une **boucle**… mais il faut savoir **quand s'arrêter** !

---

## 3. Deux façons de connaître la FIN d'une chaîne

| Méthode | Comment on sait que c'est fini |
|---------|--------------------------------|
| **Octet 0 final** (style C) | On ajoute un octet **0** (zéro) tout à la fin. Tant que le caractère lu n'est pas 0, on continue. Dès qu'on lit un 0, c'est terminé. |
| **Longueur connue** | On connaît d'avance le **nombre** de caractères. On boucle exactement ce nombre de fois. |

Le **0 final** (on l'appelle aussi *octet nul* ou *null terminator*) est très pratique : la
chaîne « porte sa fin avec elle ». C'est cette méthode qu'on utilise dans `longueur.s`.

> ⚠️ Attention : l'octet **0** (la valeur zéro) n'est **pas** le caractère `'0'` (qui vaut 48,
> cf. module 04). Le 0 final est un **marqueur invisible**, il ne s'affiche pas.

---

## 4. Rappel ASCII : minuscules → MAJUSCULES

Pour `majuscules.s`, le truc clé est dans la table ASCII :

| Caractère | Code ASCII |
|-----------|------------|
| `'A'` | 65 |
| `'a'` | 97 |
| `'Z'` | 90 |
| `'z'` | 122 |

Regarde bien : `'a'` (97) − `'A'` (65) = **32**. Et c'est pareil pour **toutes** les lettres :
la majuscule est toujours **32 de moins** que la minuscule correspondante.

> 🔑 Pour passer d'une **minuscule** à une **MAJUSCULE**, on **SOUSTRAIT 32**.
> Exemple : `'b'` = 98, et 98 − 32 = 66 = `'B'`. ✅

⚠️ Mais attention : on ne soustrait 32 **que** si le caractère est bien une **lettre
minuscule**, c'est-à-dire **entre `'a'` (97) et `'z'` (122)**. Sinon (un espace, un chiffre,
un `'\n'`, une lettre déjà majuscule…), on **n'y touche pas** !

Le plan de `majuscules.s` est donc, pour chaque caractère de la chaîne :

```
   si le caractère est < 'a'  -> on le laisse tel quel
   si le caractère est > 'z'  -> on le laisse tel quel
   sinon (entre 'a' et 'z')   -> on lui soustrait 32 (il devient majuscule)
```

---

## ▶️ À toi de jouer

```bash
# longueur.s : compte les caractères de la chaîne et renvoie ce nombre comme CODE DE SORTIE.
as asm/05_chaines/longueur.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "longueur = $?"

# majuscules.s : transforme "bonjour" en "BONJOUR" et l'affiche.
as asm/05_chaines/majuscules.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x
```

Ensuite, **modifie** les fichiers : change la chaîne déclarée dans `.data` (par ex.
`"salut tout le monde"`) et vérifie que la longueur et la mise en majuscules suivent.

➡️ La suite du parcours arrivera dans le même style.

📎 Besoin d'un rappel rapide ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md) et le
[GLOSSAIRE.md](../GLOSSAIRE.md).
