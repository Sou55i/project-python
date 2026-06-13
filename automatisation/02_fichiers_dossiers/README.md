# Module 02 — Fichiers et dossiers

C'est **le premier vrai super-pouvoir d'automatisation** : faire en sorte que Python lise,
écrive, déplace et range des fichiers à ta place. Plus de copier-coller manuel pendant
des heures.

> Fichiers du module : `lire_ecrire.py`, `csv_json.py`, `ranger_dossier.py`.
> Un dossier `exemples/` contient des fichiers de test pour que tout fonctionne directement.

---

## 1. Comment l'ordinateur range les fichiers

Ton ordinateur organise les fichiers comme des **dossiers dans des dossiers**, formant une
arborescence (comme un arbre généalogique) :

```
/home/alice/
├── Documents/
│   └── rapport.txt
└── Téléchargements/
    ├── photo.jpg
    └── facture.pdf
```

Pour désigner un fichier, on donne son **chemin** (en anglais *path*) : la suite de dossiers
à traverser pour l'atteindre, par exemple `/home/alice/Documents/rapport.txt`.

Il existe deux sortes de chemins :
- **Chemin absolu** : part de la racine. `C:\Users\Alice\rapport.txt` (Windows) ou
  `/home/alice/rapport.txt` (Mac/Linux).
- **Chemin relatif** : part de l'endroit où tu es. `Documents/rapport.txt`.

> ⚠️ Windows utilise des `\` (antislash) et Mac/Linux des `/` (slash). Pour ne pas s'en
> soucier, on utilise le module **`pathlib`** de Python, qui gère ça automatiquement
> quel que soit le système.

---

## 2. Lire et écrire un fichier texte

L'opération de base. En Python, on **ouvre** un fichier, on travaille avec, puis on le
**ferme**. La bonne pratique est d'utiliser `with`, qui ferme le fichier tout seul :

```python
# Écrire (le "w" = write ; ATTENTION : écrase le contenu existant !)
with open("notes.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Première ligne\n")   # \n = retour à la ligne

# Lire (le "r" = read)
with open("notes.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
print(contenu)
```

Les **modes** d'ouverture les plus courants :

| Mode | Rôle |
|------|------|
| `"r"` | Lire (read). Erreur si le fichier n'existe pas. |
| `"w"` | Écrire (write). **Écrase tout** le contenu existant. |
| `"a"` | Ajouter (append). Écrit **à la fin** sans effacer. |

> 💡 `encoding="utf-8"` garantit que les accents (é, à, ç…) et emojis s'écrivent
> correctement. Mets-le toujours.

---

## 3. Le format CSV : les tableaux en texte

Un **CSV** (*Comma-Separated Values*) est un tableau stocké en texte : chaque ligne est une
rangée, et les colonnes sont séparées par des virgules (ou des points-virgules).

```
nom,age,ville
Alice,30,Paris
Bob,25,Lyon
```

C'est le format **roi de l'automatisation** : Excel, les exports de logiciels, les bases
de données… tout sait lire et écrire du CSV. Python possède un module `csv` dédié qui
gère les pièges (virgules à l'intérieur d'une valeur, guillemets…).

---

## 4. Le format JSON : pour les données structurées

Le **JSON** sert à stocker des données plus riches qu'un simple tableau (des listes dans
des objets, des objets dans des listes…). Sa structure ressemble **exactement** aux
dictionnaires et listes Python :

```json
{
  "nom": "Alice",
  "age": 30,
  "loisirs": ["lecture", "vélo"]
}
```

C'est le format universel des **APIs web** (module 03). Le module `json` de Python
convertit en une ligne :
- un dictionnaire Python **→** texte JSON (`json.dump`),
- du texte JSON **→** dictionnaire Python (`json.load`).

---

## 5. Parcourir un dossier

Pour ranger automatiquement, il faut d'abord **lister** le contenu d'un dossier. `pathlib`
le fait élégamment :

```python
from pathlib import Path

dossier = Path("Téléchargements")
for fichier in dossier.iterdir():     # parcourt chaque élément du dossier
    print(fichier.name, "->", fichier.suffix)   # .suffix = l'extension (.pdf, .jpg…)
```

L'idée du mini-projet `ranger_dossier.py` : regarder l'**extension** de chaque fichier
(`.pdf`, `.jpg`, `.csv`…) et le **déplacer** dans un sous-dossier correspondant
(`PDF/`, `Images/`…). Une corvée manuelle transformée en 1 commande.

---

## ▶️ À toi de jouer

```bash
python3 automatisation/02_fichiers_dossiers/lire_ecrire.py
python3 automatisation/02_fichiers_dossiers/csv_json.py
python3 automatisation/02_fichiers_dossiers/ranger_dossier.py
```

Le script `ranger_dossier.py` travaille sur un dossier de test (`exemples/bazar/`) qu'il
crée lui-même, pour que tu puisses l'exécuter **sans risque pour tes vrais fichiers**.

➡️ Module suivant : [`03_web_apis`](../03_web_apis/).
