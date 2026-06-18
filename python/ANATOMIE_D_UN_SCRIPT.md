# 🧭 Anatomie d'un script Python : dans quel ordre écrire son code ?

Contrairement à d'autres langages, Python est exécuté **ligne par ligne**, de haut en bas.
L'ordre dans lequel tu écris ton code est donc crucial : tu ne peux pas utiliser une
variable ou une fonction qui n'a pas encore été définie.

---

## 🏗️ Le squelette standard

Voici l'ordre conventionnel pour un script propre et professionnel :

### 1. Le Shebang (Optionnel sur Windows, crucial sur Linux/macOS)
C'est la toute première ligne. Elle dit au système quel interprète utiliser.
```python
#!/usr/bin/env python3
```

### 2. Docstring du module
Un commentaire qui explique ce que fait le script.
```python
"""
Ce script automatise la sauvegarde des fichiers de configuration.
Usage: python backup.py --dir /home/user/config
"""
```

### 3. Les Imports
On importe les outils extérieurs. On les regroupe par type :
1. Bibliothèques standards (celles fournies avec Python).
2. Bibliothèques tierces (installées via `pip`).
3. Tes propres modules.

```python
import os            # Standard
import sys           # Standard
import requests     # Tierce (pip install requests)
from mon_module import ma_fonction  # Perso
```

### 4. Les Constantes Globales
Variables qui ne changent jamais, écrites en MAJUSCULES.
```python
VERSION = "1.0.0"
LOG_FILE = "/var/log/mon_script.log"
```

### 5. Les Classes et Fonctions
On définit les outils que le script va utiliser.
```python
def saluer(nom):
    """Affiche un bonjour personnalisé."""
    print(f"Bonjour {nom} !")

class Robot:
    def __init__(self, nom):
        self.nom = nom
```

### 6. Le point d'entrée (`if __name__ == "__main__":`)
C'est ici que le "vrai" travail commence. Cette ligne magique permet de s'assurer que
le code ne s'exécute que si on lance le fichier directement, et pas si on l'importe
comme un module dans un autre script.

```python
def main():
    # C'est ici qu'on appelle nos fonctions
    saluer("Utilisateur")

if __name__ == "__main__":
    main()
```

---

## 🆚 Comparaison avec Go / C

| Caractéristique | Python | Go / C |
|-----------------|--------|--------|
| **Ordre de lecture** | Strict (de haut en bas) | Plus souple (le compilateur voit tout) |
| **Point d'entrée** | `if __name__ == "__main__":` | `func main()` ou `int main()` |
| **Séparateurs** | **Indentation** (espaces) | Accolades `{ }` et `;` |
| **Définitions** | Doivent précéder l'appel | Peuvent être n'importe où (Go) |

> 💡 **Conseil de pro :** Garde toujours ton `main()` en bas de fichier. Ça permet de lire
> les "outils" (fonctions) d'abord, et de voir comment ils sont assemblés à la fin.
