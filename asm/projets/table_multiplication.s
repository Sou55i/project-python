# =====================================================================
# PROJET CAPSTONE - Table de multiplication (x86-64, Linux, Intel)
# =====================================================================
# Ce mini-projet COMBINE plusieurs modules du parcours :
#   - une BOUCLE de 1 à 10              (modules 01 / 02)
#   - la CONVERSION d'un nombre -> texte décimal (module 04, division par 10)
#   - l'affichage de CHAINES avec write  (module 05)
#
# Il affiche la table de multiplication d'un nombre (ici 7) :
#     7 x 1 = 7
#     7 x 2 = 14
#     ...
#     7 x 10 = 70
#
# Assembler, lier, lancer :
#     as asm/projets/table_multiplication.s -o /tmp/t.o
#     ld /tmp/t.o -o /tmp/t
#     /tmp/t
#
# 🗺️ CHEMINEMENT DU PROGRAMME (les grandes étapes, dans l'ordre) :
#   1. On choisit le NOMBRE de la table (7) et un COMPTEUR i qui va de 1 à 10.
#   2. Boucle : pour chaque i, on calcule le produit  p = nombre * i.
#   3. On affiche le NOMBRE (à gauche du "x")  -> sous-programme afficher_nb.
#   4. On affiche " x ".
#   5. On affiche i (le multiplicateur).
#   6. On affiche " = ".
#   7. On affiche p (le produit, 1 à 3 chiffres : 7, 14, ... 70).
#   8. On affiche un retour à la ligne, on fait i = i + 1 et on recommence.
#   9. Quand i dépasse 10 : on quitte avec exit(0).
#
# 💡 Le coeur réutilisé est le sous-programme "afficher_nb" : il prend un
#    nombre dans rax et l'affiche en décimal. Comme on convertit chiffre par
#    chiffre par divisions par 10, il gère naturellement 1, 2 ou 3 chiffres
#    (donc 7 comme 14 ou 70). Pas de cas particulier à écrire !

.intel_syntax noprefix

# ---------------------------------------------------------------------
# Données : les petits morceaux de texte fixes ("x", "=", retour ligne)
# ---------------------------------------------------------------------
.data
fois:    .ascii " x "         # le " x " entre le nombre et le multiplicateur
egal:    .ascii " = "         # le " = " entre le multiplicateur et le produit
saut:    .ascii "\n"          # un retour à la ligne (code ASCII 10)

# ---------------------------------------------------------------------
# Mémoire de travail : un petit tampon pour convertir un nombre en texte
# ---------------------------------------------------------------------
.bss
    .lcomm buffer, 21         # 20 chiffres max possibles + de la marge

.text
.global _start
_start:
    mov r12, 7               # (1) r12 = LE NOMBRE de la table (essaie 3, 9, 12...)
    mov r13, 1               #     r13 = i, le compteur, démarre à 1

boucle:
    cmp r13, 10              #     i a-t-il dépassé 10 ?
    jg fin                   #     oui -> la table est finie, on quitte

    # --- (2) calcul du produit p = nombre * i ---
    mov rax, r12             #     rax = nombre
    imul rax, r13            #     rax = nombre * i   (le produit)
    mov r14, rax             #     on range le produit dans r14 (rax va resservir)

    # --- (3) afficher le NOMBRE (à gauche du "x") ---
    mov rax, r12             #     rax = nombre à afficher
    call afficher_nb         #     -> écrit "7" par exemple

    # --- (4) afficher " x " ---
    lea rsi, [fois]          #     adresse du texte " x "
    mov rdx, 3               #     longueur = 3 caractères
    call ecrire              #     write

    # --- (5) afficher i (le multiplicateur) ---
    mov rax, r13             #     rax = i
    call afficher_nb

    # --- (6) afficher " = " ---
    lea rsi, [egal]
    mov rdx, 3
    call ecrire

    # --- (7) afficher p (le produit : 7, 14, ... 70) ---
    mov rax, r14             #     rax = produit (rangé tout à l'heure)
    call afficher_nb

    # --- (8) retour à la ligne, puis i = i + 1 ---
    lea rsi, [saut]
    mov rdx, 1
    call ecrire

    inc r13                  #     i = i + 1
    jmp boucle               #     on recommence la ligne suivante

fin:
    mov rax, 60              # (9) exit
    xor rdi, rdi             #     code de sortie 0
    syscall

# =====================================================================
# SOUS-PROGRAMME : afficher_nb
# ---------------------------------------------------------------------
# Rôle   : affiche en décimal le nombre reçu dans rax.
# Méthode: divisions successives par 10 (cf. module 04). Les chiffres
#          sortent À L'ENVERS, donc on remplit le tampon de DROITE à GAUCHE.
# Entrée : rax = le nombre (entier positif).
# Abîme  : rax, rcx, rdx, rsi, rdi (registres de travail) -> c'est pourquoi
#          on garde le nombre, i et le produit dans r12/r13/r14 (préservés).
# =====================================================================
afficher_nb:
    lea rsi, [buffer + 20]   #     rsi pointe sur la DERNIERE case du tampon
    mov rcx, 10              #     rcx = le diviseur (10)

conv:
    dec rsi                  #     on recule d'une case (droite -> gauche)
    xor rdx, rdx             #     IMPORTANT : rdx = 0 avant chaque div
    div rcx                  #     rdx:rax / 10 -> quotient dans rax, reste dans rdx
    add dl, 48               #     reste (0-9) -> caractère ASCII ('0'..'9')
    mov [rsi], dl            #     on range ce chiffre dans le tampon
    test rax, rax            #     le quotient est-il à 0 ?
    jnz conv                 #     non -> on continue avec le chiffre suivant

    # ici rsi pointe sur le PREMIER chiffre ; longueur = (buffer+20) - rsi
    lea rdx, [buffer + 20]
    sub rdx, rsi             #     rdx = nombre de chiffres à afficher
    call ecrire              #     on affiche le nombre
    ret

# =====================================================================
# SOUS-PROGRAMME : ecrire
# ---------------------------------------------------------------------
# Rôle  : affiche à l'écran (write) rdx octets situés à l'adresse rsi.
# Entrée: rsi = adresse du texte, rdx = nombre d'octets.
# =====================================================================
ecrire:
    mov rax, 1               #     1 = write
    mov rdi, 1               #     descripteur 1 = écran
    syscall                  #     rsi et rdx sont déjà positionnés
    ret
