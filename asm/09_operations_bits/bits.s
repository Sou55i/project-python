# =====================================================================
# MODULE AVANCÉ 09 - Les OPÉRATIONS BIT À BIT et les MASQUES
#             (x86-64, Linux, syntaxe Intel)
# =====================================================================
# Un nombre, pour le processeur, c'est une SUITE DE BITS (des 0 et des 1).
# Les opérations bit à bit agissent sur CHAQUE bit, colonne par colonne.
#
#   and  (ET)  : 1 seulement si LES DEUX bits sont à 1  -> sert de MASQUE
#   or   (OU)  : 1 si AU MOINS UN bit est à 1            -> ALLUME des bits
#   xor  (OUX) : 1 si LES DEUX bits sont DIFFÉRENTS      -> inverse/compare
#   shl  (<<)  : décale les bits vers la gauche          -> x2 par décalage
#
# Ici on enchaîne 4 opérations pour arriver à un résultat CONNU = 20.
# (Toutes les valeurs tiennent dans 0-255, donc lisibles via echo $?.)
#
#   12 AND 10 = 8     ->  1100 AND 1010 = 1000   (on garde les bits communs)
#    8 OR  1  = 9     ->  1000 OR  0001 = 1001   (on allume le bit de droite)
#    9 XOR 3  = 10    ->  1001 XOR 0011 = 1010   (les bits différents -> 1)
#   10 SHL 1  = 20    ->  1010 << 1     = 10100  (décalage = multiplie par 2)
#
# Résultat final attendu : 20.
#
# Assembler + lier + lancer :
#     as asm/09_operations_bits/bits.s -o /tmp/b.o
#     ld /tmp/b.o -o /tmp/b
#     /tmp/b ; echo "exit=$?"      # doit afficher : exit=20
#
# 🗺️ CHEMINEMENT DU PROGRAMME :
#   1. On met 12 dans rax, puis "and rax, 10" -> rax = 8.
#   2. On fait "or rax, 1" -> rax = 9 (on allume le bit le plus à droite).
#   3. On fait "xor rax, 3" -> rax = 10 (on inverse les bits là où 3 a un 1).
#   4. On fait "shl rax, 1" -> rax = 20 (décalage à gauche = x2).
#   5. On copie rax dans rdi (code de sortie) et on quitte via exit.
#   6. Le shell verra 20 dans $? (echo $?).

.intel_syntax noprefix

.text
.global _start

_start:
    # --- (1) AND : le MASQUE, on ne garde que les bits communs ---------
    mov rax, 12            # rax = 12   ->  binaire 1100
    and rax, 10            # rax = rax AND 10 (1010) = 1000 = 8
                           #   colonne par colonne : 1&1=1, 1&0=0,
                           #   0&1=0, 0&0=0  ->  1000  ->  rax = 8

    # --- (2) OR : on ALLUME un bit (celui de droite) ------------------
    or rax, 1              # rax = 8 OR 1 : 1000 OR 0001 = 1001 = 9
                           #   le OU met 1 dès qu'un des deux bits est 1
                           #   ->  rax = 9

    # --- (3) XOR : on INVERSE les bits là où le masque (3) vaut 1 -----
    xor rax, 3             # rax = 9 XOR 3 : 1001 XOR 0011 = 1010 = 10
                           #   XOR -> 1 quand les bits DIFFÈRENT :
                           #   1^0=1, 0^0=0, 0^1=1, 1^1=0  ->  1010
                           #   ->  rax = 10
                           # (Astuce connue : "xor rax, rax" remet rax à 0,
                           #  car tout bit XOR lui-même donne 0.)

    # --- (4) SHL : DÉCALAGE à gauche = multiplier par 2 ---------------
    shl rax, 1             # rax = 10 << 1 : 1010 décalé -> 10100 = 20
                           #   chaque décalage à gauche DOUBLE la valeur
                           #   ->  rax = 20

    # --- (5) Quitter en renvoyant le résultat comme CODE DE SORTIE ----
    mov rdi, rax           # rdi = résultat (20) = code de sortie voulu
    mov rax, 60            # 60 = numéro du syscall "exit"
    syscall                # on quitte ; (6) le shell verra 20 dans $?

# Petite formalité technique (à garder tel quel) : on indique qu'on n'a
# pas besoin d'une pile exécutable. Évite juste un avertissement de ld.
.section .note.GNU-stack, "", @progbits
