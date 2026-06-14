# Module AVANCÉ 09 — Les OPÉRATIONS BIT À BIT et les masques

Bravo, tu continues à progresser ! Ce module **avancé** t'ouvre une nouvelle façon de
manipuler les nombres : non plus comme des quantités (« 12 », « 20 »), mais comme des
**suites de petits interrupteurs** (les **bits**). C'est une compétence de base pour
comprendre les **drapeaux**, les **permissions**, la **compression**, et plein d'astuces de
calcul rapide.

> Fichier du module : [`bits.s`](./bits.s) — enchaîne `and`, `or`, `xor` et un décalage
> `shl` pour arriver à un résultat **connu** (`20`). Comme d'habitude, tout est commenté
> presque ligne par ligne, avec un bloc **🗺️ CHEMINEMENT DU PROGRAMME** en en-tête.

---

## 1. C'est quoi un BIT ? (la rangée d'interrupteurs)

Pour le processeur, un nombre n'est pas écrit en chiffres « normaux » (base 10) mais en
**binaire** (base 2) : une **suite de bits**, chacun valant **0** ou **1**. Imagine une
**rangée d'interrupteurs** : éteint = `0`, allumé = `1`.

Chaque position vaut une **puissance de 2** (comme les unités/dizaines/centaines en base 10,
mais en doublant à chaque colonne) :

```
position :    8   4   2   1
nombre 12 :   1   1   0   0     ->  8 + 4 = 12
nombre 10 :   1   0   1   0     ->  8 + 2 = 10
```

Donc `12` s'écrit **1100** en binaire, et `10` s'écrit **1010**. Retiens ces deux-là, on
s'en sert tout de suite.

---

## 2. `and` — le ET bit à bit (le MASQUE)

`and` regarde **chaque colonne** : le résultat vaut `1` **seulement si LES DEUX bits sont à
1**. Sinon `0`.

```
   1100   (12)
AND 1010   (10)
   ----
   1000   = 8        # un 1 uniquement là où 12 ET 10 avaient un 1
```

Donc **`12 AND 10 = 8`**. C'est l'opération du **MASQUE** : on s'en sert pour **ne garder
que certains bits** (ceux que le masque laisse passer avec un `1`) et **effacer les autres**.

> 🎯 **Tester un bit** : pour savoir si le bit « des 2 » est allumé dans un nombre, on fait
> `nombre AND 2`. Si le résultat n'est pas 0, le bit était à 1.

---

## 3. `or` — le OU bit à bit (ALLUMER des bits)

`or` met `1` dès qu'**AU MOINS UN** des deux bits vaut `1`.

```
   1000   (8)
OR 0001   (1)
   ----
   1001   = 9        # on a "allumé" le bit le plus à droite
```

Donc **`8 OR 1 = 9`**. Le `or` sert à **allumer** des bits sans toucher aux autres : très
pratique pour **activer un drapeau** (un *flag*).

---

## 4. `xor` — le OU EXCLUSIF (inverser / comparer)

`xor` (prononcé « ksor ») met `1` **quand les deux bits sont DIFFÉRENTS**, et `0` quand ils
sont **identiques**.

```
   1001   (9)
XOR 0011   (3)
   ----
   1010   = 10       # un 1 là où les bits diffèrent, 0 là où ils sont pareils
```

Donc **`9 XOR 3 = 10`**. Le `xor` sert à **inverser** certains bits (ceux où le masque vaut
`1`) et à **comparer**.

> 💡 **L'astuce la plus célèbre** : `xor rax, rax` met `rax` **à 0** ! Pourquoi ? Parce que
> chaque bit comparé **à lui-même** est identique, donc donne `0`. C'est la façon la plus
> rapide de remettre un registre à zéro.

---

## 5. `not` — inverser TOUS les bits

`not` retourne **chaque** bit : les `1` deviennent `0`, les `0` deviennent `1`. (On ne s'en
sert pas dans `bits.s`, mais c'est utile à connaître.)

```
NOT 0000...00001100   (12)
  = 1111...11110011    # tous les bits inversés
```

---

## 6. `shl` / `shr` — les DÉCALAGES (multiplier / diviser par 2)

- `shl rax, 1` (*shift left*) **décale les bits vers la gauche** d'une position. Un `0`
  entre par la droite. Résultat : la valeur est **multipliée par 2**.
- `shr rax, 1` (*shift right*) décale vers la **droite** : la valeur est **divisée par 2**.

```
   1010   (10)
SHL 1      (décale d'une case vers la gauche)
   -----
  10100   = 20        # un 0 est entré à droite, tout a glissé : 10 x 2 = 20
```

Donc **`10 SHL 1 = 20`**. Chaque décalage à gauche **double** ; décaler de `n` cases revient
à **multiplier par 2ⁿ** (ex : `shl rax, 3` = x8). C'est **bien plus rapide** qu'une vraie
multiplication, et c'est pour ça que le processeur l'adore.

---

## 7. À quoi ça sert dans la vraie vie ?

- **Drapeaux / flags** : ranger plusieurs vrais/faux dans un seul nombre (chaque bit = une
  option). On **allume** avec `or`, on **teste** avec `and`, on **bascule** avec `xor`.
- **Permissions de fichiers** sous Linux (`rwx` = lecture/écriture/exécution) : ce sont des
  bits ! `chmod 755`, c'est du binaire déguisé.
- **Multiplier/diviser très vite** par une puissance de 2 avec `shl`/`shr`.
- **Couleurs, masques d'image, réseau (adresses IP)** : partout où on découpe un nombre en
  morceaux de bits.

---

## ▶️ À toi de jouer

```bash
# bits.s : 12 AND 10 = 8, puis OR/XOR, puis SHL -> exit=20
as asm/09_operations_bits/bits.s -o /tmp/b.o && ld /tmp/b.o -o /tmp/b && /tmp/b ; echo "exit=$?"
```

Tu dois lire **`exit=20`**. Le déroulé complet (en binaire) :

```
12 AND 10 = 8     ->  1100 AND 1010 = 1000
 8 OR  1  = 9     ->  1000 OR  0001 = 1001
 9 XOR 3  = 10    ->  1001 XOR 0011 = 1010
10 SHL 1  = 20    ->  1010 << 1     = 10100
```

Ensuite, expérimente (n'oublie pas : le code de sortie va de **0 à 255**) :

- Remplace `shl rax, 1` par `shl rax, 2` : tu liras `exit=40` (10 x 4).
- Remplace `xor rax, 3` par `xor rax, 9` : à partir de 9, `9 XOR 9 = 0`… puis `0 SHL 1 = 0`,
  donc `exit=0` (l'astuce « xor avec soi-même = 0 » en direct).
- Remplace `and rax, 10` par `and rax, 4` : `12 AND 4 = 4` (seul le bit « des 4 » survit),
  la suite donnera un autre résultat — calcule-le à la main avant de lancer !

📎 Besoin d'un rappel ? Va voir l'[AIDE_MEMOIRE.md](../AIDE_MEMOIRE.md), le
[GLOSSAIRE.md](../GLOSSAIRE.md) et le module [`01_les_bases`](../01_les_bases/) (registres,
`mov`, code de sortie).
