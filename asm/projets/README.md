# 🛠️ Mini-projets ASSEMBLEUR

Une fois les modules `00` à `07` digérés, voici des **projets complets** qui combinent
plusieurs notions vues séparément. C'est l'étape la plus importante : c'est en assemblant
les briques apprises une par une qu'on construit enfin **quelque chose qui marche tout seul**.

> Chaque programme commence par un bloc **« 🗺️ CHEMINEMENT DU PROGRAMME »** qui résume ses
> étapes : lis-le en premier pour comprendre la logique avant de plonger dans le code.

## Les projets

| Projet | Ce qu'il fait | Modules combinés |
|--------|---------------|------------------|
| [`table_multiplication.s`](./table_multiplication.s) | Affiche la table de multiplication d'un nombre (10 lignes : `7 x 1 = 7` ... `7 x 10 = 70`) | 01/02 (boucle), 04 (nombre → texte), 05 (afficher des chaînes) |

## 🎯 Zoom sur `table_multiplication.s`

Ce programme est un bon résumé du parcours, car il fait travailler **trois idées ensemble** :

1. **Une boucle** (modules 01/02) : un compteur `i` qui va de 1 à 10 et déclenche une ligne
   d'affichage à chaque tour.
2. **Convertir un nombre en texte** (module 04) : un registre contient un entier *binaire*
   (par exemple 14). Pour l'afficher, il faut le transformer en caractères ASCII grâce aux
   **divisions successives par 10**. Comme on traite les chiffres un par un, le même code
   gère sans effort 1, 2 ou 3 chiffres (donc `7` comme `14` ou `70`).
3. **Afficher des chaînes** (module 05) : les morceaux fixes `" x "`, `" = "` et le retour à
   la ligne sont écrits à l'écran avec l'appel système `write`.

> 💡 Le cœur réutilisé est le **sous-programme `afficher_nb`** : on lui donne un nombre dans
> `rax`, et il l'affiche en décimal. On l'appelle trois fois par ligne (le nombre, le
> multiplicateur, le produit). C'est exactement l'intérêt des fonctions vues au module 02 :
> écrire une fois, réutiliser partout.

## ▶️ Assembler, lier et lancer

```bash
# 1. Assembler le .s en fichier objet .o
as asm/projets/table_multiplication.s -o /tmp/t.o

# 2. Lier le .o en un exécutable
ld /tmp/t.o -o /tmp/t

# 3. Lancer
/tmp/t
```

En une seule ligne :

```bash
as asm/projets/table_multiplication.s -o /tmp/t.o && ld /tmp/t.o -o /tmp/t && /tmp/t
```

Tu devrais voir s'afficher :

```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

> 🔧 **À toi de jouer** : change la ligne `mov r12, 7` en `mov r12, 9` (ou 3, 12...) et
> relance. La table s'adapte toute seule. Essaie aussi un nombre qui donne des produits à
> 3 chiffres, comme `12` (jusqu'à `12 x 10 = 120`) : la conversion par divisions s'en occupe.

## Et ensuite ?

Tu as maintenant tout pour inventer tes propres petits programmes : une table d'addition,
une suite de nombres pairs, un compte à rebours... Réutilise le sous-programme `afficher_nb`
et amuse-toi. 🚀
