# Projet capstone — Un gestionnaire de tâches (la « to-do list »)

Bravo, tu es arrivé au bout du parcours Java ! Ce **projet final** rassemble TOUT ce que tu
as appris pour construire une vraie petite application : un **gestionnaire de tâches** qui
crée des tâches, les coche, les **sauvegarde dans un fichier** et les **recharge**.

> Programme **non interactif** : il utilise des données de démo et affiche le résultat. La
> sortie est **déterministe** (toujours identique).

---

## Ce que ce projet réutilise du parcours

| Notion | Module | Où, dans le projet |
|--------|--------|--------------------|
| Classe, attributs privés, getters | 02 (POO) | la classe `Tache` |
| `ArrayList` | 04 (Collections) | la liste `List<Tache>` |
| Génériques `<T>` | 06 (Génériques) | `List<Tache>`, `ArrayList<>` |
| `try` / `catch`, exception vérifiée | 05 (Exceptions) | `IOException` à la sauvegarde |
| Lambdas & streams | 08 (Streams) | le résumé `filter(...).count()` |

---

## Les deux fichiers

- **`Tache.java`** : la classe `Tache` (id, titre, fait/pas fait). Elle sait se **convertir
  en ligne de texte** (`versLigne`) pour la sauvegarde et se **reconstruire** depuis une
  ligne (`depuisLigne`) pour le chargement. *(Pas de `main` : elle est utilisée par l'autre.)*
- **`GestionnaireDeTaches.java`** : la classe **publique avec `main`**. Elle gère la liste,
  l'ajout, le marquage, l'affichage, et la **sauvegarde / chargement** dans un fichier.

> ⚠️ **Règle Java** : une classe publique doit être dans un fichier du même nom. D'où deux
> fichiers `Tache.java` et `GestionnaireDeTaches.java`.

---

## Le format de sauvegarde

Chaque tâche devient **une ligne** de texte, champs séparés par `;` :

```
1;1;Apprendre les generiques
2;0;Lire une stack trace
```

`id;faite(1/0);titre`. Au chargement, on `split(";")` pour reconstruire chaque `Tache`. Le
fichier est écrit dans le sous-dossier **`exemples/`** (`exemples/taches.txt`).

---

## 🗺️ CHEMINEMENT du programme (`main`)

1. Créer un gestionnaire (liste vide au départ).
2. **Ajouter** des tâches de démo (l'id est attribué automatiquement).
3. **Marquer** deux tâches comme faites.
4. **Afficher** toutes les tâches + un résumé (faites / restantes) calculé avec un **stream**.
5. **Sauvegarder** la liste dans `exemples/taches.txt`.
6. **Recharger** depuis ce fichier dans un NOUVEAU gestionnaire, et réafficher pour prouver
   que la sauvegarde/chargement fonctionne.

---

## ▶️ À toi de jouer

```bash
# On compile les DEUX fichiers ensemble, puis on lance la classe avec main :
javac -d /tmp/jb java/projets/Tache.java java/projets/GestionnaireDeTaches.java
java -cp /tmp/jb GestionnaireDeTaches
```

Après l'exécution, ouvre le fichier **`java/projets/exemples/taches.txt`** : tu y verras tes
tâches sauvegardées. Puis **modifie le code** : ajoute une tâche, change celles qui sont
faites, ou ajoute une méthode `supprimer(int id)`.

🎉 **Félicitations** : tu as parcouru les bases, la POO, l'héritage, les collections, les
exceptions, les génériques, le débogage, les streams, les threads, et un vrai projet. Tu sais
désormais lire et écrire du Java. Continue à construire !
