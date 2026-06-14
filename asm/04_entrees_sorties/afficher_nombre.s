# =====================================================================
# MODULE 04 - Afficher un NOMBRE calculé (x86-64, Linux, syntaxe Intel)
# =====================================================================
# Afficher un nombre n'est PAS afficher un texte : il faut d'abord convertir
# l'entier (binaire, dans un registre) en une suite de CARACTERES ASCII.
# Méthode : divisions successives par 10 (le reste = le dernier chiffre).
#
# Assembler, lier, lancer :
#     as asm/04_entrees_sorties/afficher_nombre.s -o /tmp/x.o
#     ld /tmp/x.o -o /tmp/x
#     /tmp/x          # affiche : 12345
#
# 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
#   1. Mettre le nombre à afficher dans rax.
#   2. Placer un '\n' à la fin du tampon, puis remplir les chiffres de DROITE
#      à GAUCHE (car les divisions sortent les chiffres à l'envers).
#   3. Boucle : diviser par 10, convertir le reste en caractère (+48), ranger.
#   4. Quand le quotient vaut 0 : afficher le tampon avec write.
#   5. Quitter avec exit(0).

.intel_syntax noprefix

.bss
    .lcomm buffer, 21        # zone mémoire réservée : 20 chiffres max + 1 pour '\n'

.text
.global _start
_start:
    mov rax, 12345           # (1) le nombre à afficher (essaie 7, 100, 999999...)

    lea rsi, [buffer + 20]   # (2) rsi = adresse de la DERNIERE case du tampon
    mov byte ptr [rsi], 10   #     on y met '\n' (code ASCII 10 = retour à la ligne)
    mov rcx, 10              #     rcx = le diviseur (10)

convert:                     # (3) BOUCLE de conversion
    dec rsi                  #     on recule d'une case (on remplit de droite à gauche)
    xor rdx, rdx             #     IMPORTANT : rdx = 0 avant chaque div (sinon plantage)
    div rcx                  #     rdx:rax / 10  ->  quotient dans rax, reste dans rdx
    add dl, 48               #     reste (0-9) -> caractère ASCII ('0'-'9'), via +48
    mov [rsi], dl            #     on range ce caractère dans le tampon
    test rax, rax            #     le quotient est-il à 0 ?
    jnz convert              #     non -> on continue avec le chiffre suivant

    mov rax, 1               # (4) write
    mov rdi, 1               #     descripteur 1 = écran
    # rsi pointe déjà sur le premier chiffre ; longueur = (buffer+21) - rsi
    lea rdx, [buffer + 21]
    sub rdx, rsi             #     rdx = nombre d'octets à afficher
    syscall

    mov rax, 60              # (5) exit
    xor rdi, rdi             #     code de sortie 0
    syscall
