# ============================================================================
#  hello.s — Afficher "Bonjour" en assembleur x86-64 (Linux)
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    1. Il affiche le texte "Bonjour\n" à l'écran (appel système write).
#    2. Il quitte proprement avec le code 0 (appel système exit).
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/00_demarrer/hello.s -o /tmp/p.o && ld /tmp/p.o -o /tmp/p && /tmp/p
# ============================================================================

.intel_syntax noprefix      # On écrit en syntaxe Intel (plus lisible pour débuter).

# --- Section des DONNÉES : ce qui ne change pas, comme notre texte. ----------
.section .data
message:                    # 'message' = une étiquette = l'adresse où commence le texte.
    .ascii "Bonjour\n"      # Le texte à afficher. \n = retour à la ligne.

# --- Section du CODE : les instructions à exécuter. -------------------------
.section .text
.global _start              # On rend '_start' visible : c'est le POINT DE DÉPART du programme.

_start:
    # --- Appel système n°1 : write(1, message, 8) -> afficher du texte. ------
    mov rax, 1              # rax = 1 : on choisit le service "write" (écrire).
    mov rdi, 1              # rdi = 1 : où écrire ? 1 = l'écran (la sortie standard).
    lea rsi, [message]      # rsi = adresse du texte à afficher (où il commence).
    mov rdx, 8              # rdx = combien d'octets écrire ? "Bonjour\n" en fait 8.
    syscall                 # On déclenche la demande : Linux affiche le texte.

    # --- Appel système n°60 : exit(0) -> quitter le programme. ---------------
    mov rax, 60            # rax = 60 : on choisit le service "exit" (quitter).
    mov rdi, 0             # rdi = 0  : le code de sortie (0 = tout s'est bien passé).
    syscall               # On déclenche : le programme s'arrête ici.
