# 🛠️ Projets — le grand combo (capstone)

Tu as digéré les modules `00` à `07` ? Bravo. Place maintenant aux **projets** :
de petits programmes complets qui **combinent plusieurs modules à la fois**. C'est
l'étape la plus importante : c'est en assemblant les briques qu'on devient vraiment
autonome.

> 🗺️ Chaque programme commence par un bloc **« CHEMINEMENT DU PROGRAMME »** qui
> résume ses étapes : lis-le en premier pour voir la logique avant de plonger dans le code.

## Les projets

| Projet | Ce qu'il fait | Modules combinés |
|--------|---------------|------------------|
| [`carnet_notes.c`](./carnet_notes.c) | Gère des notes scolaires (matière + note), calcule la moyenne, **sauvegarde** dans un fichier puis **relit** et **affiche** | 02 (tableaux/moyenne) · 04 (structures) · 05 (fichiers) |

## ▶️ Compiler et lancer

⚠️ **Lance toujours DEPUIS LA RACINE du dépôt.** Le programme écrit ses données
dans un sous-dossier `exemples/` (créé tout seul), au bon endroit seulement si tu
pars de la racine.

```bash
# Carnet de notes (non interactif : il remplit, sauvegarde, recharge, affiche)
gcc -Wall c/projets/carnet_notes.c -o carnet_notes
./carnet_notes
```

> 💡 **Non interactif** : pas besoin de taper quoi que ce soit. Le programme remplit
> des données d'exemple, les enregistre dans `exemples/notes.dat`, les recharge depuis
> le fichier, puis les affiche avec la moyenne. Parfait pour tester directement.

> 🧹 **Anti-pollution** : le fichier de données va dans `exemples/`, à part du code.
> Tu peux supprimer ce dossier quand tu veux : `rm -rf exemples`.

## Et ensuite ?

Le meilleur exercice : **pars de ce projet et fais-le grandir**. Ajoute une matière,
trie les notes, affiche la meilleure et la pire… À toi de jouer ! 🚀
