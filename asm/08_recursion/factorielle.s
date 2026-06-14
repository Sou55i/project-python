# =====================================================================
# MODULE AVANCÉ 08 - La RÉCURSION en assembleur
#             factorielle(5) = 5 x 4 x 3 x 2 x 1 = 120
#             (x86-64, Linux, syntaxe Intel)
# =====================================================================
# Une fonction RÉCURSIVE est une fonction qui s'APPELLE ELLE-MÊME.
# Image : des poupées russes. Chaque poupée en contient une plus
# petite, jusqu'à la toute petite qu'on ne peut plus ouvrir : c'est
# le CAS DE BASE qui arrête la descente.
#
# Ici : factorielle(n) =
#     - 1                       si n == 0  (CAS DE BASE, on s'arrête)
#     - n * factorielle(n - 1)  sinon      (APPEL RÉCURSIF)
#
# Pourquoi la PILE est essentielle ?
#   Chaque appel de la fonction se sert du registre rdi pour son n.
#   Mais avant de se rappeler avec (n - 1), il va ÉCRASER rdi.
#   Pour ne pas perdre son propre n, chaque appel le SAUVEGARDE sur la
#   pile (push) AVANT l'appel récursif, puis le RESTAURE (pop) APRÈS,
#   au moment de faire la multiplication. C'est exactement push/pop du
#   module 02, et call/ret y range/reprend aussi l'adresse de retour.
#
# Pourquoi 5 et pas 6 ? On rend le résultat comme CODE DE SORTIE du
# programme. Or un code de sortie va de 0 à 255 seulement.
#   5! = 120   -> tient (120 < 256)        ✅
#   6! = 720   -> NE tient PAS (720 > 255) ❌  (on lirait 720 % 256 = 208)
#
# Assembler + lier + lancer :
#     as asm/08_recursion/factorielle.s -o /tmp/f.o
#     ld /tmp/f.o -o /tmp/f
#     /tmp/f ; echo "exit=$?"      # doit afficher : exit=120
#
# 🗺️ CHEMINEMENT DU PROGRAMME :
#   1. _start : on met n = 5 dans rdi, puis call factorielle.
#   2. factorielle teste le CAS DE BASE : si n == 0, renvoie 1 (rax=1).
#   3. Sinon : SAUVEGARDE n sur la pile (push rdi), prépare n-1 dans
#      rdi, puis APPEL RÉCURSIF (call factorielle).
#   4. Au RETOUR de l'appel, rax = factorielle(n-1). On RESTAURE notre
#      n depuis la pile (pop rdi), puis on MULTIPLIE : rax = n * rax.
#   5. ret : on rend ce résultat à l'appelant (l'appel du dessus).
#   6. Tout en haut, _start récupère 120 dans rax et quitte avec exit,
#      en passant ce 120 comme code de sortie.

.intel_syntax noprefix

.text
.global _start

_start:
    mov rdi, 5              # (1) n = 5, l'argument de départ
    call factorielle       #     calcule factorielle(5) ; résultat dans rax

    # (6) Quitter en utilisant le résultat comme CODE DE SORTIE.
    mov rdi, rax           #     rdi = résultat (120) = code de sortie voulu
    mov rax, 60            #     60 = numéro du syscall "exit"
    syscall                #     on quitte ; le shell verra 120 dans $?

# ---------------------------------------------------------------------
# La fonction RÉCURSIVE
#   Entrée  : rdi = n
#   Sortie  : rax = factorielle(n)
# ---------------------------------------------------------------------
factorielle:
    cmp rdi, 0             # (2) compare n à 0
    jne cas_recursif       #     si n != 0, on descend dans la récursion
    mov rax, 1             #     CAS DE BASE : factorielle(0) = 1
    ret                    #     on remonte d'un cran (fin de cette poupée)

cas_recursif:
    push rdi              # (3) SAUVEGARDE notre n sur la pile (sinon écrasé)
    sub rdi, 1            #     prépare l'argument suivant : n - 1
    call factorielle     #     APPEL RÉCURSIF : rax = factorielle(n - 1)

    pop rdi              # (4) RESTAURE notre n depuis la pile (intact)
    imul rax, rdi       #     MULTIPLICATION : rax = factorielle(n-1) * n
    ret                  # (5) on remonte d'un cran avec n * factorielle(n-1)

# Petite formalité technique (à garder tel quel) : on indique qu'on n'a
# pas besoin d'une pile exécutable. Évite juste un avertissement de ld.
.section .note.GNU-stack, "", @progbits
