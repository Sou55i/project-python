"""
MODULE 07 - Les erreurs fréquentes en vrai
===========================================
Ce script DÉCLENCHE volontairement les erreurs les plus courantes du débutant,
les ATTRAPE avec try/except, et affiche pour chacune : le type, le message de
Python, la cause et la solution. Ainsi tu apprends à les reconnaître.

Lance-le :  python3 automatisation/07_debugger/erreurs_frequentes.py

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS  : aucun (on n'a besoin d'aucun outil externe).
   2. FONCTION : demonstration() exécute un bout de code risqué, attrape
                 l'erreur, et affiche son type + son message + une explication.
   3. PROGRAMME: le bloc __main__ appelle demonstration() pour chaque erreur.
"""


# Décodage de la signature :
#   titre        -> le nom de l'erreur (du texte affiché)
#   code_risque  -> une FONCTION sans argument qui contient le code qui plante.
#                   (On passe une fonction pour pouvoir l'exécuter ici, dans le try.)
#   explication  -> la cause + la solution, en mots simples.
def demonstration(titre, code_risque, explication):
    """Exécute un code qui plante, attrape l'erreur et l'explique."""
    print(f"\n=== {titre} ===")
    try:
        # On EXÉCUTE le code risqué. S'il lève une erreur, on saute dans 'except'.
        code_risque()
    # 'Exception as e' attrape l'erreur et range ses détails dans la variable e.
    except Exception as e:
        # type(e).__name__ = le NOM du type d'erreur (ex : "TypeError").
        print(f"  Python a levé : {type(e).__name__}: {e}")
        print(f"  💡 {explication}")


# ─────────────────────────────────────────────
# Chaque "code_risque" ci-dessous est une petite fonction qui PLANTE exprès.
# On utilise 'lambda' = une mini-fonction écrite sur une seule ligne.
# Ex : lambda: 10 / 0   signifie "une fonction qui, appelée, fait 10 / 0".
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("Démonstration des erreurs courantes (chacune est attrapée, pas de crash).")

    # TypeError : on additionne du texte et un nombre.
    demonstration(
        "TypeError (mélange de types)",
        lambda: "5" + 5,
        "On ne peut pas additionner du texte et un nombre. "
        "Convertis : int('5') + 5. Pense-y avec input() qui renvoie du texte.",
    )

    # ValueError : on convertit en nombre un texte qui n'est pas un nombre.
    demonstration(
        "ValueError (valeur impossible)",
        lambda: int("bonjour"),
        "Le type est bon (on veut un nombre) mais 'bonjour' n'en est pas un. "
        "Vérifie la donnée avant de convertir.",
    )

    # ZeroDivisionError : division par zéro.
    demonstration(
        "ZeroDivisionError (division par zéro)",
        lambda: 10 / 0,
        "Diviser par zéro est impossible. Teste avant : if diviseur != 0.",
    )

    # IndexError : on demande un élément qui n'existe pas dans la liste.
    demonstration(
        "IndexError (hors de la liste)",
        lambda: [1, 2, 3][10],
        "La liste a 3 éléments (indices 0 à 2), il n'y a pas d'indice 10. "
        "Vérifie avec len(liste). On compte à partir de 0 !",
    )

    # KeyError : on demande une clé absente d'un dictionnaire.
    demonstration(
        "KeyError (clé absente)",
        lambda: {"nom": "Alice"}["ville"],
        "La clé 'ville' n'existe pas dans le dictionnaire. "
        "Utilise dico.get('ville', 'défaut') pour éviter le plantage.",
    )

    # NameError : on utilise une variable qui n'existe pas.
    demonstration(
        "NameError (nom inconnu)",
        lambda: variable_qui_nexiste_pas,  # noqa: F821 (erreur volontaire)
        "Cette variable n'a jamais été créée (ou faute de frappe), "
        "ou elle est définie PLUS BAS. Définis-la AVANT de l'utiliser.",
    )

    # AttributeError : on appelle une méthode qui n'existe pas pour ce type.
    demonstration(
        "AttributeError (méthode inexistante)",
        lambda: "texte".append("x"),
        "Un texte (str) n'a pas de méthode .append() (ça, c'est pour les listes). "
        "Vérifie le type de l'objet et ses méthodes réelles.",
    )

    # ModuleNotFoundError : on importe une bibliothèque non installée.
    def importer_module_absent():
        import module_qui_nexiste_pas  # noqa: F401 (erreur volontaire)

    demonstration(
        "ModuleNotFoundError (bibliothèque manquante)",
        importer_module_absent,
        "La bibliothèque n'est pas installée. Installe-la : pip install <nom> "
        "(voir module 06).",
    )

    # FileNotFoundError : on ouvre un fichier qui n'existe pas.
    demonstration(
        "FileNotFoundError (fichier introuvable)",
        lambda: open("/chemin/qui/nexiste/pas.txt", "r"),
        "Le fichier ou le chemin est faux. Vérifie le chemin ; "
        "teste avec Path(chemin).exists().",
    )

    print("\n✅ Fin de la démo. Tu sais maintenant reconnaître ces erreurs !")
