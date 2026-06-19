# 🔐 Index sécurité — toutes les démos pentest du dépôt

> ⚠️ **CADRE STRICTEMENT ÉDUCATIF.** Toutes ces démonstrations sont destinées à
> **l'apprentissage défensif, la sensibilisation et les labs/CTF**. Utilise-les **uniquement**
> sur **tes propres systèmes** ou avec une **autorisation écrite**. Toute utilisation contre un
> système tiers sans accord est **illégale**. Chaque fichier montre aussi **comment se défendre**.

Chaque langage possède un dossier `pentest/` (un scanner réseau) et `pentest/offensif/`
(des démos d'attaques, *version vulnérable vs corrigée*). Cette page les regroupe **par
thème**, pour comparer une même attaque d'un langage à l'autre.

> 🐍 Les démos **Python** vivent désormais dans le dépôt dédié
> **[Python_guide](https://github.com/TN-RedTeam/Python_guide/tree/main/pentest)** ; les liens
> « Python » ci-dessous y pointent.

---

## 🔎 Reconnaissance réseau (scanners de ports)

Un scanner se trouve dans le `pentest/` de chaque langage compilable/scriptable :

[Python](https://github.com/TN-RedTeam/Python_guide/tree/main/pentest) · [Bash](./bash/pentest/02_network/scan_ports.sh) ·
[PowerShell](./powershell/pentest/02_network/Test-Ports.ps1) · [C](./c/pentest/scanner.c) ·
[C++](./cpp/pentest/scanner.cpp) · [Go](./go/pentest/02_network/port_scanner.go) ·
[Rust](./rust/pentest/02_network/port_scanner.rs) · [JS](./js-ts/pentest/scanner.js) ·
[Java](./java/pentest/02_network/ScannerPorts.java) — tous limités à `127.0.0.1`.

---

## 🔑 Mots de passe & cryptographie

| Technique | Langages |
|-----------|----------|
| Cassage par dictionnaire (hash rapide = mot de passe faible cassé vite) | [Python](https://github.com/TN-RedTeam/Python_guide/blob/main/pentest/offensif/cassage_mot_de_passe.py), [Go](./go/pentest/offensif/brute_force.go), [Rust](./rust/pentest/offensif/cassage.rs), [JS](./js-ts/pentest/offensif/cassage.js), [Java](./java/pentest/offensif/Cassage.java) |
| Sel & rainbow tables (pourquoi saler les hashs) | [Python](https://github.com/TN-RedTeam/Python_guide/blob/main/pentest/offensif/sel_et_rainbow.py) |
| Tokens de session faibles (prévisibles vs `crypto/rand`) | [Go](./go/pentest/offensif/token_faible.go) |

**🛡️** Hashs lents (argon2/bcrypt), sel unique, MFA, mots de passe longs, aléatoire cryptographique.

---

## 💉 Injections

| Technique | Langages |
|-----------|----------|
| Injection SQL (`' OR '1'='1`) vs requêtes paramétrées | [Python](https://github.com/TN-RedTeam/Python_guide/blob/main/pentest/offensif/injection_sql.py) |
| Injection de commande (shell) | [Python](https://github.com/TN-RedTeam/Python_guide/blob/main/pentest/offensif/injection_commande.py), [Bash](./bash/pentest/offensif/injection_commande.sh) |
| XSS (échappement de sortie) | [JS](./js-ts/pentest/offensif/xss_demo.js) |
| XXE (entités externes XML) | [Java](./java/pentest/offensif/XmlXxe.java) |

**🛡️** Requêtes paramétrées, pas de `shell=True`/`eval`, échapper la sortie, désactiver les DTD, valider/allowlist.

---

## 🚪 Contrôle d'accès & web

| Technique | Langages |
|-----------|----------|
| IDOR / contrôle d'accès cassé | [JS](./js-ts/pentest/offensif/idor.js) |
| SSRF (requête vers ressources internes) | [Python](https://github.com/TN-RedTeam/Python_guide/blob/main/pentest/offensif/ssrf.py) |
| Traversée de chemin (`../../etc/passwd`) | [Go](./go/pentest/offensif/traversee_chemin.go), [Java](./java/pentest/offensif/TraverseeChemin.java) |
| Pollution de prototype (JS) | [JS](./js-ts/pentest/offensif/pollution_prototype.js) |

**🛡️** Vérifier l'autorisation côté serveur, canonicaliser les chemins + vérifier le préfixe, listes blanches, rejeter `__proto__`.

---

## 🧠 Vulnérabilités mémoire (bas niveau)

| Technique | Langages |
|-----------|----------|
| Buffer overflow (écrasement d'adresse de retour) | [C](./c/pentest/offensif/vulnerable.c) |
| Use-after-free | [C++](./cpp/pentest/offensif/use_after_free.cpp) |
| Shellcode `execve("/bin/sh")` + loader | [Asm](./asm/pentest/offensif/shellcode.s) |
| Pourquoi Rust **empêche** ces failles (ownership) | [Rust](./rust/pentest/offensif/securite_memoire.rs) |

**🛡️** Vérifier les bornes, `snprintf`, stack canaries, ASLR, NX/DEP, sanitizers, langages mémoire-sûrs (Rust).

---

## 🐚 Post-exploitation & configuration

| Technique | Langages |
|-----------|----------|
| Reverse shell (lab, `127.0.0.1`, garde-fou) | [Bash](./bash/pentest/offensif/reverse_shell.sh), [PowerShell](./powershell/pentest/offensif/Invoke-ReverseShellDemo.ps1), [Go](./go/pentest/offensif/reverse_shell.go), [Java](./java/pentest/offensif/ReverseShell.java) |
| Désérialisation non sécurisée (RCE) | [Python](https://github.com/TN-RedTeam/Python_guide/blob/main/pentest/offensif/deserialisation.py) |
| Énumération de mauvaises permissions (privesc) | [Bash](./bash/pentest/offensif/enum_privesc.sh) |
| Reverse engineering / désassemblage | [Asm](./asm/pentest/) |

**🛡️** Pare-feu sortant, EDR, surveillance des connexions, moindre privilège, ne pas désérialiser de données non fiables.

---

## ▶️ Comment lancer une démo

Chaque fichier indique en en-tête sa commande exacte. Exemples :

```bash
node js-ts/pentest/offensif/idor.js
go run go/pentest/offensif/traversee_chemin.go
bash bash/pentest/offensif/injection_commande.sh
rustc rust/pentest/offensif/cassage.rs -o /tmp/c && /tmp/c
javac -d build java/pentest/offensif/*.java && java -cp build XmlXxe
```

> 🐍 Pour les démos **Python**, voir le dépôt [Python_guide](https://github.com/TN-RedTeam/Python_guide/tree/main/pentest).

➡️ Voir aussi le volet « sécurité » du [COMPARATIF.md](./COMPARATIF.md) (quel langage pour
quelle tâche offensive) et le [SOMMAIRE.md](./SOMMAIRE.md).
