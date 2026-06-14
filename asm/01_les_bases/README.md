# Module 01 — Les bases : registres, calculs, sauts et boucles

Maintenant qu'on sait afficher du texte et quitter, on va apprendre à **calculer** dans les
registres et à **faire des choix** (sauts, boucles). C'est le cœur de l'assembleur.

> Fichiers du module : [`registres.s`](./registres.s) (mettre des valeurs, calculer) et
> [`boucle.s`](./boucle.s) (une vraie boucle). Tout est commenté ligne par ligne.

---

## 1. Les registres : les « cases » de calcul du processeur

Un **registre** est une case ultra-rapide **dans** le processeur. Le processeur ne sait
calculer **que** dans ces cases. Dans ce module on utilise surtout :

- `rax` : on y range nos résultats de calcul.
- `rcx` : on s'en sert comme **compteur** dans la boucle.
- `rdi` : on y met le **code de sortie** avant de quitter.

---

## 2. `mov` : mettre une valeur dans un registre

`mov destination, source` **copie** la source dans la destination :

```asm
mov rax, 7        # rax = 7   (met le nombre 7 dans rax)
mov rdi, rax      # rdi = rax (copie le contenu de rax dans rdi)
```

> 💡 Lis `mov A, B` comme « **A reçoit B** » (la destination est **à gauche**, comme un
> `=` en maths).

---

## 3. `add` et `sub` : additionner et soustraire

```asm
add rax, 5        # rax = rax + 5  (ajoute 5 à rax)
sub rax, 2        # rax = rax - 2  (retire 2 de rax)
inc rcx           # rcx = rcx + 1  (raccourci pratique pour "+1")
```

Le résultat est **rangé dans le registre de gauche**. Donc après `mov rax, 7` puis
`add rax, 5`, le registre `rax` contient **12**.

---

## 4. Voir le résultat : le **code de sortie** et `echo $?`

On n'a pas encore appris à afficher un **nombre** (c'est plus long en assembleur). En
attendant, on utilise une astuce : **renvoyer le résultat comme code de sortie** du
programme, puis le lire avec `echo $?`.

Le **code de sortie**, c'est le nombre que l'on met dans `rdi` avant l'appel `exit` :

```asm
mov rdi, rax      # le code de sortie = le contenu de rax
mov rax, 60       # service exit
syscall           # quitte avec ce code
```

Puis dans le terminal, `echo $?` affiche ce nombre. C'est notre façon de **« voir »** le
résultat d'un calcul.

> ⚠️ Le code de sortie va seulement de **0 à 255**. Parfait pour nos petits calculs (12, 15),
> mais retiens qu'on ne peut pas y mettre n'importe quel grand nombre.

---

## 5. `cmp` et les **sauts** : faire des choix

`cmp A, B` **compare** A et B (sans rien modifier). Juste après, un **saut** décide où aller
selon le résultat de la comparaison :

| Saut | Veut dire | Saute si… |
|------|-----------|-----------|
| `jmp` | *jump* | **toujours** (saut inconditionnel) |
| `je`  | *jump if equal* | A **=** B |
| `jne` | *jump if not equal* | A **≠** B |
| `jl`  | *jump if less* | A **<** B |
| `jg`  | *jump if greater* | A **>** B |

```asm
cmp rcx, 5        # compare rcx et 5
jg fin            # si rcx > 5, saute à l'étiquette 'fin'
```

---

## 6. Les **labels** (étiquettes) : des points de repère

Une **étiquette** est un **nom posé sur un endroit** du code, suivi de `:`. Les sauts s'en
servent comme destination :

```asm
boucle:           # on pose le nom 'boucle' ici
    ...
    jmp boucle    # on saute vers 'boucle' -> on recommence
fin:              # un autre point de repère
    ...
```

En combinant `cmp` + saut conditionnel + `jmp` + labels, on obtient une **boucle** : c'est
exactement ce que fait [`boucle.s`](./boucle.s), qui additionne 1+2+3+4+5 = **15**. Va lire
son en-tête : le bloc **🗺️ CHEMINEMENT DU PROGRAMME** détaille chaque étape.

---

## ▶️ À toi de jouer

```bash
# registres.s : calcule 7 + 5 et quitte avec ce résultat -> exit=12
as asm/01_les_bases/registres.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"

# boucle.s : additionne 1..5 et quitte avec la somme -> exit=15
as asm/01_les_bases/boucle.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
```

Lis les deux fichiers, puis **modifie-les** : change `add rax, 5` en `add rax, 10` (tu
devrais lire `exit=17`), ou fais la boucle aller jusqu'à 6 (la somme deviendra 21).

➡️ La suite du parcours (mémoire & pile, fonctions, affichage de nombres…) arrivera dans le
même style.
