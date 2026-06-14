# =====================================================================
# MODULE 05 - LONGUEUR d'une chaîne (x86-64, Linux, syntaxe Intel)
# =====================================================================
# On parcourt une chaîne terminée par un octet 0 (style C) avec un POINTEUR
# qui avance d'une case à la fois (inc). On COMPTE les caractères jusqu'à
# tomber sur l'octet 0 final. On quitte ensuite avec ce compte comme CODE
# DE SORTIE (visible avec : echo $?).
#
# Assembler, lier, lancer :
#     as asm/05_chaines/longueur.s -o /tmp/x.o
#     ld /tmp/x.o -o /tmp/x
#     /tmp/x ; echo "longueur = $?"
#
# La chaîne "bonjour" fait 7 caractères -> LONGUEUR ATTENDUE = 7.

.intel_syntax noprefix

.data
texte:
    .asciz "bonjour"     # .asciz = la chaîne SUIVIE d'un octet 0 automatique
                         # ('b','o','n','j','o','u','r', puis 0 = fin)

.text
.global _start
_start:
    lea rsi, [texte]     # rsi = POINTEUR sur le 1er caractère de la chaîne
    xor rcx, rcx         # rcx = compteur de longueur, mis à 0

boucle:                  # BOUCLE : on lit un caractère à chaque tour
    mov al, [rsi]        # al = l'octet (le caractère) pointé par rsi
    cmp al, 0            # est-ce l'octet 0 final (la fin de la chaîne) ?
    je fin               # oui -> on sort de la boucle

    inc rcx              # non -> c'est un vrai caractère : on compte +1
    inc rsi              # le pointeur avance vers le caractère suivant
    jmp boucle           # on recommence

fin:
    mov rax, 60          # exit
    mov rdi, rcx         # code de sortie = la longueur calculée
    syscall
