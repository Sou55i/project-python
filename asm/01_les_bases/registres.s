# ============================================================================
#  registres.s — Mettre des valeurs dans des registres et calculer
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    1. Il met 7 dans un registre.
#    2. Il lui ajoute 5  ->  résultat = 12.
#    3. Il quitte en renvoyant ce résultat comme CODE DE SORTIE.
#
#  On "voit" le résultat avec  echo $?  après l'avoir lancé (il vaudra 12).
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/01_les_bases/registres.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- Étape 1 : un petit calcul dans des registres. ----------------------
    mov rax, 7             # rax = 7   (on MET la valeur 7 dans le registre rax).
    add rax, 5            # rax = rax + 5  ->  rax vaut maintenant 12.
    # (Pour info : 'sub rax, 2' ferait rax = rax - 2. On ne s'en sert pas ici.)

    # --- Étape 2 : quitter en renvoyant ce résultat comme code de sortie. ----
    mov rdi, rax          # rdi = rax : le code de sortie sera notre résultat (12).
    mov rax, 60          # rax = 60 : service "exit" (quitter).
    syscall              # On quitte. Le code de sortie vaudra 12.
