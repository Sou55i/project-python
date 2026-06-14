# =====================================================================
# MODULE 05 - Mettre une chaîne en MAJUSCULES (x86-64, Linux, Intel)
# =====================================================================
# On parcourt une chaîne caractère par caractère. Pour chaque LETTRE
# MINUSCULE (entre 'a'=97 et 'z'=122), on SOUSTRAIT 32 pour obtenir la
# MAJUSCULE correspondante. On modifie la chaîne EN PLACE (dans .data),
# puis on l'affiche avec write.
#
# Assembler, lier, lancer :
#     as asm/05_chaines/majuscules.s -o /tmp/x.o
#     ld /tmp/x.o -o /tmp/x
#     /tmp/x          # affiche : BONJOUR
#
# 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
#   1. Faire pointer rsi sur le 1er caractère de la chaîne.
#   2. Boucle : lire un caractère ; si octet 0 -> la chaîne est finie.
#   3. Si le caractère est entre 'a' et 'z' : lui soustraire 32 et le
#      ré-écrire en place (il devient majuscule). Sinon : ne rien changer.
#   4. Avancer le pointeur et recommencer.
#   5. Une fois la chaîne traitée : l'afficher avec write (longueur = 8,
#      les 7 lettres + le '\n'), puis quitter avec exit(0).

.intel_syntax noprefix

.data
texte:
    .ascii "bonjour\n"   # la chaîne à transformer (7 lettres + un retour ligne)
longueur = . - texte     # longueur = adresse courante - adresse de texte = 8

.text
.global _start
_start:
    lea rsi, [texte]     # (1) rsi = POINTEUR sur le 1er caractère

boucle:                  # (2) BOUCLE de transformation
    mov al, [rsi]        #     al = le caractère courant
    cmp al, 0            #     octet 0 ? (sécurité : fin de chaîne)
    je afficher          #     oui -> on a fini, on passe à l'affichage

    cmp al, 'a'          # (3) le caractère est-il AVANT 'a' (97) ?
    jb suivant           #     oui (espace, '\n', majuscule...) -> on ne touche pas
    cmp al, 'z'          #     est-il APRES 'z' (122) ?
    ja suivant           #     oui -> on ne touche pas

    sub al, 32           #     ici : c'est une minuscule -> -32 = MAJUSCULE
    mov [rsi], al        #     on ré-écrit le caractère transformé EN PLACE

suivant:
    inc rsi              # (4) le pointeur avance au caractère suivant
    jmp boucle           #     on recommence

afficher:
    mov rax, 1           # (5) write
    mov rdi, 1           #     descripteur 1 = écran
    lea rsi, [texte]     #     adresse de la chaîne (transformée)
    mov rdx, longueur    #     nombre d'octets à afficher (8)
    syscall

    mov rax, 60          #     exit
    xor rdi, rdi         #     code de sortie 0
    syscall
