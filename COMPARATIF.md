# 🔬 La même chose dans plusieurs langages

Le meilleur moyen de comprendre la programmation **en général** (et pas juste un langage),
c'est de voir **le même concept** écrit dans plusieurs langages. Tu remarqueras que les
**idées** sont identiques — seule la **façon de l'écrire** (la syntaxe) change.

> Les langages sont rangés du plus haut niveau (proche de l'humain) au plus bas niveau
> (proche de la machine) : **Python → Bash → PowerShell → Go → C++ → C → Assembleur**.
> L'assembleur étant très différent, certaines cases indiquent « concept géré autrement ».

> 🐍 Python sert ici de **point de repère** (le plus lisible). Le **cours Python complet** est
> dans son dépôt dédié : **[TN-RedTeam/Python_guide](https://github.com/TN-RedTeam/Python_guide)**.

---

## 0. Comment on lance le programme

| Langage | Commande |
|---------|----------|
| 🐍 Python | `python3 fichier.py` (interprété, pas de compilation) |
| 🐚 Bash | `bash fichier.sh` (interprété, pas de compilation) |
| 🟦 PowerShell | `pwsh fichier.ps1` (interprété, pas de compilation) |
| 🐹 Go | `go run fichier.go` (compile + exécute) |
| ➕ C++ | `g++ fichier.cpp -o prog && ./prog` |
| 🇨 C | `gcc fichier.c -o prog && ./prog` |
| ⚙️ Asm | `as fichier.s -o f.o && ld f.o -o prog && ./prog` |
| 🦀 Rust | `rustc fichier.rs -o prog && ./prog` (compilé) |
| 🟨 JS / TS | `node fichier.js` (interprété) · TS : `tsc fichier.ts` puis `node fichier.js` |
| ☕ Java | `javac Fichier.java && java Fichier` (compilé en bytecode pour la JVM) |

> 💡 **Python est interprété** : on lance le fichier directement. Les **4 autres sont
> compilés** : il faut d'abord traduire le code source en programme exécutable.

---

## 1. Afficher « Bonjour »

**Python**
```python
print("Bonjour")
```
**Bash**
```bash
echo "Bonjour"
```
**PowerShell**
```powershell
Write-Host "Bonjour"
```
**Go**
```go
package main
import "fmt"
func main() { fmt.Println("Bonjour") }
```
**C++**
```cpp
#include <iostream>
int main() { std::cout << "Bonjour\n"; return 0; }
```
**C**
```c
#include <stdio.h>
int main(void) { printf("Bonjour\n"); return 0; }
```
**Assembleur** (x86-64, simplifié — voir `asm/00_demarrer/`)
```asm
.intel_syntax noprefix
.data
msg: .ascii "Bonjour\n"
.text
.global _start
_start:
    mov rax, 1      # syscall write
    mov rdi, 1      # sortie écran
    lea rsi, [msg]  # adresse du texte
    mov rdx, 8      # nombre d'octets
    syscall
    mov rax, 60     # syscall exit
    mov rdi, 0
    syscall
```

> On voit tout de suite l'écart : ce qui tient en **1 ligne** en Python demande de piloter
> **registre par registre** en assembleur.

---

## 2. Une variable

| Langage | Code | Remarque |
|---------|------|----------|
| Python | `age = 30` | type **deviné** automatiquement |
| Bash | `age=30` | ⚠️ **aucun espace** autour du `=` ; utilisé via `"$age"` |
| PowerShell | `$age = 30` | le nom commence par `$` ; utilisé via `"$age"` |
| Go | `age := 30` | type deviné, mais **statique** |
| C++ | `int age = 30;` | type **déclaré** + `;` |
| C | `int age = 30;` | type **déclaré** + `;` |
| Asm | `mov rax, 30` | une valeur **dans un registre** |

---

## 3. Une condition

**Python**
```python
if note >= 10:
    print("Recu")
else:
    print("Recale")
```
**Bash**
```bash
if [[ $note -ge 10 ]]; then
    echo "Recu"
else
    echo "Recale"
fi
```
**PowerShell** (comparaison avec `-ge`, jamais `>=`)
```powershell
if ($note -ge 10) {
    Write-Host "Recu"
} else {
    Write-Host "Recale"
}
```
**Go**
```go
if note >= 10 {
    fmt.Println("Recu")
} else {
    fmt.Println("Recale")
}
```
**C / C++** (même syntaxe pour le `if`)
```c
if (note >= 10) {
    printf("Recu\n");
} else {
    printf("Recale\n");
}
```
**Assembleur** : il n'y a pas de `if`. On **compare** puis on **saute** :
```asm
    cmp rax, 10     # compare note (rax) à 10
    jl  recale      # "jump if less" : si <10, saute à recale
    # ... cas "Recu" ...
recale:
    # ... cas "Recale" ...
```

> Idée commune : « selon une comparaison, faire ceci ou cela ». En haut niveau c'est
> `if/else` ; en assembleur, c'est **comparer (`cmp`) + sauter (`jl`, `jne`…)**.

---

## 4. Une boucle (répéter 3 fois)

| Langage | Code |
|---------|------|
| Python | `for i in range(3):` |
| Bash | `for i in {1..3}; do ... done` |
| PowerShell | `for ($i = 0; $i -lt 3; $i++) { }` |
| Go | `for i := 0; i < 3; i++ {` |
| C / C++ | `for (int i = 0; i < 3; i++) {` |
| Asm | un **label** + un compteur + un **saut conditionnel** (voir `asm/01_les_bases/boucle.s`) |

> `for` est juste une écriture confortable pour « initialiser un compteur, tester, avancer,
> recommencer » — exactement ce qu'on fait à la main en assembleur.

---

## 5. Une fonction qui additionne

**Python**
```python
def add(a, b):
    return a + b
```
**Bash** (les arguments sont `$1`, `$2`… ; on « renvoie » en affichant)
```bash
add() {
    echo $(( $1 + $2 ))
}
```
**PowerShell**
```powershell
function Add-Numbers {
    param([int]$a, [int]$b)
    return $a + $b
}
```
**Go**
```go
func add(a int, b int) int {
    return a + b
}
```
**C++ / C**
```c
int add(int a, int b) {
    return a + b;
}
```
**Assembleur** (voir `asm/02_pile_fonctions/`)
```asm
add:
    mov rax, rdi    # 1er argument
    add rax, rsi    # + 2e argument -> résultat dans rax
    ret             # revient à l'appelant
```

> Partout, une fonction = « un bloc nommé, qui prend des entrées et renvoie une sortie ».
> En haut niveau on déclare des paramètres ; en assembleur, les arguments arrivent dans des
> **registres** (`rdi`, `rsi`) et le résultat repart dans `rax`.

---

## 6. Les commentaires

| Langage | Une ligne | Plusieurs lignes |
|---------|-----------|------------------|
| Python | `# ...` | `""" ... """` |
| Bash | `# ...` | (ligne par ligne) |
| PowerShell | `# ...` | `<# ... #>` |
| Go / C++ / C | `// ...` | `/* ... */` |
| Asm | `# ...` | (ligne par ligne) |

---

## 7. Ce qui change vraiment d'un langage à l'autre

| Critère | Python | Bash | PowerShell | Go | C++ | C | Asm |
|---------|--------|------|-----------|----|-----|---|-----|
| Compilation | non (interprété) | non (interprété) | non (interprété) | oui | oui | oui | oui (assemblage) |
| Typage | dynamique | faible (tout est texte) | dynamique (objets) | statique | statique | statique | registres |
| Gestion mémoire | automatique | automatique | automatique | automatique | manuelle/outillée | **manuelle** | **totale (toi)** |
| Niveau | très haut | haut (scripts) | haut (scripts) | haut | moyen | bas | **le plus bas** |
| Facilité débutant | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| Point fort | données, web | **automatiser le terminal** | **administrer Windows**, objets | serveurs, outils | logiciels exigeants | système | matériel |

---

## 🎯 Quel langage choisir pour quelle tâche ?

Il n'y a pas de « meilleur » langage dans l'absolu : il y a le **bon outil pour le bon
travail**. Voici des repères concrets.

| Ta tâche | Langage conseillé | Pourquoi |
|----------|-------------------|----------|
| Débuter la programmation | 🐍 **Python** | le plus lisible, parfait pour comprendre les concepts |
| Automatiser fichiers / données, scraping, web, IA | 🐍 **Python** | simple + immense écosystème de bibliothèques |
| Automatiser **Linux/macOS**, enchaîner des outils, traiter des logs | 🐚 **Bash** | natif sur Unix, roi des pipes et du texte |
| Automatiser / administrer **Windows**, manipuler des objets système | 🟦 **PowerShell** | natif Windows, pipeline d'**objets** |
| Serveurs réseau, outils en ligne de commande, conteneurs/cloud | 🐹 **Go** | compilé, rapide, concurrence simple, **un seul binaire** |
| Logiciels exigeants en performance, jeux, moteurs, gros calculs | ➕ **C++** | vitesse du C + objets et STL |
| Systèmes embarqués, OS, pilotes, contrôle fin de la mémoire | 🇨 **C** | proche du matériel, ultra-portable, minimal |
| Comprendre/optimiser au plus bas niveau, reverse engineering | ⚙️ **Assembleur** | contrôle **total** du processeur |
| Sites web, front-end, et back-end avec Node.js | 🟨 **JS / TS** | LE langage du web ; TypeScript ajoute la sûreté des types |
| Applications d'entreprise, Android, gros systèmes multiplateformes | ☕ **Java** | robuste, très outillé, « écris une fois, exécute partout » (JVM) |
| Performance **et** sûreté mémoire (systèmes, outils, WebAssembly) | 🦀 **Rust** | vitesse du C **sans** les bugs mémoire (vérifié à la compilation) |

### Pour la sécurité informatique (pentest)

La sécurité utilise **plusieurs** langages selon le besoin (voir les modules `pentest/` de
chaque langage) :

| Besoin en sécurité | Langage souvent privilégié |
|--------------------|-----------------------------|
| Scripts d'audit, prototypage rapide d'exploits, outils offensifs | 🐍 **Python** (le standard du domaine) |
| Outils réseau rapides et portables (scanners, implants multiplateformes) | 🐹 **Go** |
| Recon « glue » sur Unix, enchaîner nmap/curl/… | 🐚 **Bash** |
| Post-exploitation et administration **Windows** / Active Directory | 🟦 **PowerShell** |
| Exploitation mémoire (buffer overflow), shellcode, outils bas niveau | 🇨 **C** / ⚙️ **Assembleur** |
| Outils de sécurité performants, **reverse engineering**, analyse de malware, exploits navigateurs/jeux | ➕ **C++** |

> ⚖️ Ces compétences sont à usage **strictement éducatif et autorisé** : uniquement sur tes
> propres systèmes, avec autorisation écrite, ou dans des labs/CTF (HackTheBox, TryHackMe…).

### La règle simple

> 🧭 **Tu débutes ?** Python. **Tu automatises Unix ?** Bash. **Tu automatises Windows ?**
> PowerShell. **Tu veux de la performance ou un binaire à distribuer ?** Go, puis C++/C.
> **Tu veux comprendre la machine ?** C, puis l'Assembleur.

---

## 🧭 Conclusion

Les **concepts** (variable, condition, boucle, fonction) sont **universels**. Quand tu en
apprends un nouveau dans un langage, tu le retrouves dans les autres : seule la syntaxe et
le niveau de contrôle changent. C'est pour ça qu'**apprendre un 2ᵉ langage est bien plus
rapide que le premier**.

➡️ Pour démarrer : [Python](https://github.com/TN-RedTeam/Python_guide) (le plus accessible,
dépôt dédié), puis [C](./c/) pour comprendre la machine, puis [Assembleur](./asm/) pour voir
tout en bas.
