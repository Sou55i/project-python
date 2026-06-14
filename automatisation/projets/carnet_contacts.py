"""
MINI-PROJET - Un carnet de contacts en ligne de commande (avec sauvegarde)
==========================================================================
Ce petit programme te permet de gérer un carnet de contacts directement
depuis le terminal : tu peux AJOUTER, LISTER, CHERCHER et SUPPRIMER des
contacts. Et surtout : les contacts sont SAUVEGARDÉS dans un fichier JSON,
donc ils sont toujours là quand tu relances le programme plus tard !

Ce projet combine trois choses apprises dans les modules :
   - module 01 : les DICTIONNAIRES (un contact = {"nom": ..., "tel": ...}) ;
   - module 02 : lire/écrire un fichier JSON (json.load / json.dump) ;
   - module 04 : argparse avec des SOUS-COMMANDES (ajouter, lister, etc.).

Exemples de lancement (recopie une ligne dans ton terminal) :
   python3 automatisation/projets/carnet_contacts.py ajouter --nom Alice --tel 0612345678
   python3 automatisation/projets/carnet_contacts.py ajouter --nom Bob --tel 0700000000 --email bob@mail.fr
   python3 automatisation/projets/carnet_contacts.py lister
   python3 automatisation/projets/carnet_contacts.py chercher --nom alice
   python3 automatisation/projets/carnet_contacts.py supprimer --nom Bob
   python3 automatisation/projets/carnet_contacts.py --help

🗺️ CHEMINEMENT DU SCRIPT (les grandes étapes, dans l'ordre) :
   1. IMPORTS    : argparse (les commandes), json (sauvegarde), pathlib (chemins).
   2. CHEMIN     : on calcule où ranger le fichier "contacts.json" (dossier exemples/).
   3. FONCTIONS  : - charger()      lit le fichier JSON et renvoie la liste des contacts,
                   - sauvegarder()  réécrit la liste des contacts dans le fichier JSON,
                   - ajouter()      ajoute un contact puis sauvegarde,
                   - lister()       affiche tous les contacts,
                   - chercher()     cherche un contact par son nom (sans tenir compte de la casse),
                   - supprimer()    enlève un contact par son nom puis sauvegarde,
                   - creer_parseur()définit les sous-commandes et leurs options (argparse).
   4. PROGRAMME  : la fonction main() lit la commande tapée et appelle la bonne fonction.
   5. DÉMARRAGE  : le bloc __main__ lance main() quand on exécute le fichier.
"""

# 'import argparse' = la caisse à outils pour lire les commandes/options tapées au terminal.
import argparse
# 'import json' = la caisse à outils pour lire/écrire le format JSON (notre sauvegarde).
import json
# 'from pathlib import Path' = pour manipuler facilement les chemins de fichiers/dossiers.
from pathlib import Path


# Path(__file__) = le chemin de CE fichier. .parent = le dossier qui le contient.
# On range le fichier de données dans un sous-dossier "exemples" placé À CÔTÉ du script.
# (Ce dossier "exemples/" est déjà ignoré par git, donc nos contacts ne seront pas commités.)
FICHIER_CONTACTS = Path(__file__).parent / "exemples" / "contacts.json"


def charger():
    """Lit le fichier JSON et renvoie la LISTE des contacts (ou une liste vide)."""
    # .exists() répond True si le fichier existe déjà, False sinon.
    # Au TOUT premier lancement le fichier n'existe pas encore : on renvoie une
    # liste vide [] pour démarrer avec un carnet... vide.
    if not FICHIER_CONTACTS.exists():
        return []

    # Le fichier existe : on l'ouvre en lecture ("r" = read) et on le lit.
    with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
        # json.load(f) LIT le texte JSON du fichier et le retransforme en objet
        # Python (ici une liste de dictionnaires). C'est l'inverse de json.dump.
        return json.load(f)


def sauvegarder(contacts):
    """Écrit la liste des contacts dans le fichier JSON (et crée le dossier si besoin)."""
    # .parent = le dossier "exemples". mkdir crée ce dossier.
    #   parents=True   -> crée aussi les dossiers parents manquants si nécessaire,
    #   exist_ok=True  -> ne plante PAS si le dossier existe déjà.
    FICHIER_CONTACTS.parent.mkdir(parents=True, exist_ok=True)

    # On ouvre le fichier en écriture ("w" = write, écrase l'ancien contenu).
    with open(FICHIER_CONTACTS, "w", encoding="utf-8") as f:
        # json.dump(objet, fichier, ...) ÉCRIT l'objet Python dans le fichier en JSON.
        #   indent=2           -> présentation lisible (2 espaces de décalage),
        #   ensure_ascii=False -> garde les accents é/à/ç tels quels.
        json.dump(contacts, f, indent=2, ensure_ascii=False)


def ajouter(nom, tel, email):
    """Ajoute un nouveau contact dans le carnet, puis sauvegarde."""
    # On part de la liste déjà enregistrée (on ne veut pas perdre les anciens contacts).
    contacts = charger()

    # Un contact est un DICTIONNAIRE : une étiquette (clé) pointe vers une valeur.
    # email peut être None si l'utilisateur ne l'a pas fourni : on met "" à la place.
    nouveau = {"nom": nom, "tel": tel, "email": email if email else ""}

    # .append(...) ajoute un élément à la FIN de la liste.
    contacts.append(nouveau)

    sauvegarder(contacts)   # on réécrit la liste complète sur le disque.
    print(f"[+] Contact ajouté : {nom} ({tel})")


def lister():
    """Affiche tous les contacts enregistrés."""
    contacts = charger()

    # Si la liste est vide, 'not contacts' vaut True (une liste vide est "fausse").
    if not contacts:
        print("Le carnet est vide. Ajoute un contact avec la commande 'ajouter'.")
        return   # 'return' arrête la fonction ici : rien d'autre à afficher.

    print(f"--- {len(contacts)} contact(s) dans le carnet ---")
    # enumerate(...) donne en même temps un numéro (start=1 -> on commence à 1)
    # et l'élément. Pratique pour numéroter l'affichage.
    for numero, contact in enumerate(contacts, start=1):
        # contact["email"] vaut "" s'il n'y en a pas : on n'affiche le mail que s'il existe.
        partie_email = f" - {contact['email']}" if contact["email"] else ""
        print(f"{numero}. {contact['nom']} : {contact['tel']}{partie_email}")


def chercher(nom):
    """Cherche les contacts dont le nom correspond, SANS tenir compte de la casse."""
    contacts = charger()

    # .lower() met un texte en minuscules. En comparant deux textes en minuscules,
    # "Alice", "alice" et "ALICE" deviennent tous "alice" : la recherche devient
    # insensible à la casse (majuscules/minuscules).
    recherche = nom.lower()

    # On construit une nouvelle liste qui ne garde QUE les contacts qui correspondent.
    trouves = [c for c in contacts if c["nom"].lower() == recherche]

    if not trouves:
        print(f"Aucun contact trouvé pour : {nom}")
        return

    print(f"--- {len(trouves)} résultat(s) pour '{nom}' ---")
    for contact in trouves:
        partie_email = f" - {contact['email']}" if contact["email"] else ""
        print(f"{contact['nom']} : {contact['tel']}{partie_email}")


def supprimer(nom):
    """Supprime le(s) contact(s) portant ce nom (insensible à la casse), puis sauvegarde."""
    contacts = charger()
    recherche = nom.lower()

    # On garde tous les contacts SAUF ceux dont le nom correspond.
    #   c["nom"].lower() != recherche  -> "le nom est DIFFÉRENT du nom cherché"
    restants = [c for c in contacts if c["nom"].lower() != recherche]

    # Si la liste n'a pas raccourci, c'est qu'on n'a rien trouvé à supprimer.
    if len(restants) == len(contacts):
        print(f"Aucun contact à supprimer pour : {nom}")
        return

    sauvegarder(restants)
    # len(contacts) - len(restants) = combien de contacts ont disparu.
    print(f"[-] {len(contacts) - len(restants)} contact(s) supprimé(s) pour : {nom}")


def creer_parseur():
    """Définit les SOUS-COMMANDES (ajouter, lister, chercher, supprimer) et leurs options."""
    # On crée l'analyseur principal. La description s'affiche avec --help.
    parseur = argparse.ArgumentParser(description="Un carnet de contacts en ligne de commande.")

    # add_subparsers(...) permet d'avoir PLUSIEURS commandes dans un même programme
    # (comme 'git commit' / 'git push'). Ici : 'ajouter', 'lister', 'chercher', 'supprimer'.
    #   dest="commande" -> le nom de la commande tapée sera rangé dans args.commande,
    #   required=True    -> on OBLIGE l'utilisateur à choisir une commande.
    sous = parseur.add_subparsers(dest="commande", required=True)

    # --- Sous-commande "ajouter" ---
    # add_parser("ajouter") crée la commande, puis on lui ajoute ses propres options.
    p_ajouter = sous.add_parser("ajouter", help="Ajouter un contact")
    #   required=True -> l'option est obligatoire pour cette commande.
    p_ajouter.add_argument("--nom", required=True, help="Nom du contact")
    p_ajouter.add_argument("--tel", required=True, help="Numéro de téléphone")
    #   --email n'a pas required=True : il est facultatif (default=None si absent).
    p_ajouter.add_argument("--email", help="Adresse email (facultative)")

    # --- Sous-commande "lister" --- (aucune option à fournir)
    sous.add_parser("lister", help="Afficher tous les contacts")

    # --- Sous-commande "chercher" ---
    p_chercher = sous.add_parser("chercher", help="Chercher un contact par son nom")
    p_chercher.add_argument("--nom", required=True, help="Nom à rechercher")

    # --- Sous-commande "supprimer" ---
    p_supprimer = sous.add_parser("supprimer", help="Supprimer un contact par son nom")
    p_supprimer.add_argument("--nom", required=True, help="Nom du contact à supprimer")

    return parseur


def main():
    """Lit la commande tapée par l'utilisateur et appelle la bonne fonction."""
    parseur = creer_parseur()
    # .parse_args() lit réellement ce qui a été tapé au terminal et le range dans 'args'.
    # Ex : pour "ajouter --nom Alice --tel 06...", on aura :
    #   args.commande == "ajouter", args.nom == "Alice", args.tel == "06...".
    args = parseur.parse_args()

    # Selon la commande choisie, on appelle la fonction correspondante.
    if args.commande == "ajouter":
        ajouter(args.nom, args.tel, args.email)
    elif args.commande == "lister":
        lister()
    elif args.commande == "chercher":
        chercher(args.nom)
    elif args.commande == "supprimer":
        supprimer(args.nom)


# ─────────────────────────────────────────────
# Ce bloc ne s'exécute QUE si on lance ce fichier directement
# (python3 carnet_contacts.py ...), et PAS si un autre fichier fait 'import'.
#   __name__ vaut "__main__" uniquement quand le fichier est le programme lancé.
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
