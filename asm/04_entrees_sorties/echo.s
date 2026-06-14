# =====================================================================
# MODULE 04 - echo : lire le clavier et le réafficher (x86-64, Linux)
# =====================================================================
# On réserve un tampon, on appelle read (depuis le clavier, descripteur 0)
# pour y ranger la ligne tapée, puis write (vers l'écran, descripteur 1)
# pour la réafficher : c'est le principe de l'"echo".
#
# Assembler, lier, lancer :
#     as asm/04_entrees_sorties/echo.s -o /tmp/x.o
#     ld /tmp/x.o -o /tmp/x
#     printf "coucou\n" | /tmp/x      # réaffiche : coucou
#     # (ou lance /tmp/x seul et tape une phrase au clavier)

.intel_syntax noprefix

.bss
    .lcomm buffer, 256       # tampon de 256 octets pour stocker ce qui est lu

.text
.global _start
_start:
    # --- read(0, buffer, 256) : lire ce que tape l'utilisateur ---
    mov rax, 0               # service 0 = read (lire)
    mov rdi, 0               # descripteur 0 = entrée (clavier)
    lea rsi, [buffer]        # adresse OU RANGER les octets lus
    mov rdx, 256             # taille maximale à lire
    syscall                  # après l'appel, rax = nombre d'octets réellement lus

    # --- write(1, buffer, rax) : réafficher exactement ce qui a été lu ---
    mov rdx, rax             # longueur à écrire = ce qui a été lu (rax)
    mov rax, 1               # service 1 = write (écrire)
    mov rdi, 1               # descripteur 1 = sortie (écran)
    lea rsi, [buffer]        # adresse D'OU LIRE les octets à afficher
    syscall

    # --- exit(0) : quitter proprement ---
    mov rax, 60
    xor rdi, rdi
    syscall
