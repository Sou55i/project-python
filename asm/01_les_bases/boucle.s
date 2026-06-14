# ============================================================================
#  boucle.s — Une boucle avec un label et un saut conditionnel
# ----------------------------------------------------------------------------
#  Ce que fait ce programme :
#    Il additionne les nombres de 1 à 5  ->  1+2+3+4+5 = 15.
#    Puis il quitte en renvoyant 15 comme CODE DE SORTIE (visible avec echo $?).
#
#  🗺️ CHEMINEMENT DU PROGRAMME (le déroulé, étape par étape) :
#    1. INIT      : compteur (rcx) = 1, somme (rax) = 0.
#    2. boucle:   : COMPARER le compteur à 5.
#                   - s'il est plus grand que 5 -> on saute vers 'fin'.
#    3.           : AJOUTER le compteur à la somme  (somme = somme + compteur).
#    4.           : INCRÉMENTER le compteur         (compteur = compteur + 1).
#    5.           : SAUTER (jmp) vers 'boucle' pour recommencer.
#    6. fin:      : EXIT en renvoyant la somme (15) comme code de sortie.
#
#  Pour l'assembler, le lier et le lancer :
#    as asm/01_les_bases/boucle.s -o /tmp/x.o && ld /tmp/x.o -o /tmp/x && /tmp/x ; echo "exit=$?"
# ============================================================================

.intel_syntax noprefix      # Syntaxe Intel (plus lisible pour débuter).

.section .text
.global _start              # _start = point de départ du programme.

_start:
    # --- 1. INIT : on prépare nos deux registres "compteurs". ---------------
    mov rax, 0            # rax = 0 : la somme (le total) commence à 0.
    mov rcx, 1           # rcx = 1 : le compteur, qui ira de 1 jusqu'à 5.

boucle:                   # <-- étiquette : début de la boucle (on y reviendra).
    # --- 2. COMPARER : a-t-on dépassé 5 ? -----------------------------------
    cmp rcx, 5           # compare le compteur à 5 (sans rien modifier).
    jg fin               # 'jg' = "jump if greater" : si compteur > 5, saute à 'fin'.

    # --- 3. AJOUTER : on ajoute le compteur à la somme. ---------------------
    add rax, rcx         # somme = somme + compteur.

    # --- 4. INCRÉMENTER : on avance le compteur de 1. -----------------------
    inc rcx              # rcx = rcx + 1 ('inc' = incrémenter).

    # --- 5. SAUTER : on retourne au début de la boucle. ---------------------
    jmp boucle           # 'jmp' = saut INCONDITIONNEL : on recommence le tour.

fin:                     # <-- étiquette : on arrive ici quand la boucle est finie.
    # --- 6. EXIT : quitter en renvoyant la somme comme code de sortie. -------
    mov rdi, rax         # rdi = la somme (15) -> ce sera le code de sortie.
    mov rax, 60          # rax = 60 : service "exit".
    syscall              # On quitte. Le code de sortie vaudra 15.
