# Catalogue de produits
catalogue = {
    'A-150-E-R':{
        'taille':150,
        'classe':'Extra',
        'couleur':'Roussie',
        'prix':2.50
    },
    'A-180-E-R':{
        'taille':180,
        'classe':'Extra',
        'couleur':'roussie',
        'prix':2.30
    },
    'A-210-C1-B':{
        'taille':210,
        'classe':'Class I',
        'couleur':'blanche',
        'prix':2.75
    },
    'A-210-C2-B':{
        'taille':210,
        'classe':'Class II',
        'couleur':'blanche',
        'prix':2.05
    },
    'A-210-C2-R':{
        'taille':450,
        'classe':'Class II',
        'couleur':'roussie',
        'prix':2.05
    }
}
utilisateurs = {
    "jd@whitehouse.gov":{
        'nom':'Vance',
        'prenom':'JD',
        'mdp':'Ormouz%26',
        'panier':{'A-150-E-R': 25, 'A-180-E-R': 20}
    }
}
utilisateur_connecte = None

menu_utilisateur = """
0. Quitter le programme
1. Créer un nouvel utilisateur
2. Se logger avec un utilisateur existant
"""

menu_panier = """
0. Revenir au menu précédent
1. Afficher le catalogue
2. Ajouter un article du catalogue au panier
3. Visualiser le panier (et son prix)
4. Modifier la quantité pour un article du panier
5. Supprimer un article du panier
"""

continuer = True

# Définition des fonctions
def afficher_menu(menu):
    """
    Affiche le menu passé en argument

    Args:
        menu (str) : un menu à proposer à l'utilisateur
    """
    print(menu)

def afficher_catalogue(catalogue):
    """
    Affiche le catalogue de produits passé en argument
    
    Args :
        catalogue(dict) : catalogue de produits
         clé(str) : nom de l'article
         valeur(dict) : description de l'article; avec les clés suivantes ('taille','classe','couleur','prix')
    """
    en_tete = f"{'Reference':^12} | {'Taille':^8} | {'Classe':^10}  | {'Couleur':^10} | {'Prix':^6}"
    print(en_tete)
    for reference,article in catalogue.items():
        print(f"{reference:^12} | {article['taille']:^8} | {article['classe']:^10} | {article['couleur']:^10} | {article['prix']:^6}")

def afficher_panier(panier,catalogue):
    """
    Affiche le panier passé en arguement; et le prix total de celui-ci.

    Args :
        panier(dict): le panier de l'utilisateur
            clé(str): une référence produit référençant un produit du catalogue
            valeur(int) : une quantité
        catalogue(dict) : le catalogue de produits
            clé(str) : nom de l'article
            valeur(dict) : description de l'article; avec les clés suivantes ('taille','classe','couleur','prix')
    """
    panier_prix_tot = 0 # Montant total du panier
    en_tete = f"{'Reference':^12} | {'Taille':^8} | {'Classe':^10}  | {'Couleur':^10} | {'Prix_Unit':^6} | {'Qté':^5} | {'Prix_Tot':^10} "
    print(en_tete)
    for reference, quantite in panier.items():
        if reference in catalogue:
            article = catalogue[reference]
            article_prix_tot = quantite * article['prix'] # Montant total pour cet article
            panier_prix_tot += article_prix_tot
            print(f"{reference:^12} | {article['taille']:^8} | {article['classe']:^10} | {article['couleur']:^10} | {article['prix']:^6} | {quantite:^5} | {article_prix_tot:^10}")
        else:
            print("L'article n'existe pas / plus dans le catalogue !")
    print(f"Le montant de total de votre panier s'élève à : {panier_prix_tot} euros !")


while continuer:
    # Utilisateur non connecté => afficher le 'menu_utilisateur'
    print(f"Utilisateur connecté : {utilisateur_connecte}")
    if utilisateur_connecte is None:
        afficher_menu(menu_utilisateur)
        choix = int(input("Effectuez votre choix [0-2] : "))
        
        if choix == 0:
            # Quitter le programme
            print("Merci d'avoir utilisé notre programme")
            continuer = False
        elif choix == 1:
            # Créer un nouvel utilisateur
            email = input("Veuillez saisir votre adresse email : ")
            if email in utilisateurs:
                print("L'utilisateur existe déjà !")
            else:
                nom = input("Veuillez saisir votre nom :")
                prenom = input("Veuillez saisir votre prénom :")
                mdp = input("Veuillez choisir un mot de passe : ")
                utilisateur = {
                    'nom':nom,
                    'prenom':prenom,
                    'mdp':mdp
                }
                utilisateurs[email] = utilisateur
        elif choix == 2:
            # Se logger avec un utilisateur existant
            email = input("Veuillez saisir votre adresse email : ")
            if email not in utilisateurs:
                print("Aucune utilisateur identifié avec cette adresse email n'a été trouvé !")
            else:
                mdp = input("Veuillez saisir votre mot de passe : ")
                if utilisateurs[email].get('mdp') == mdp:
                    utilisateur_connecte = email
                else:
                    print("Mot de passe incorrect !")

    else:
    # Si l'utilisateur est connecté => afficher le menu_panier
        afficher_menu(menu_panier)
        choix = int(input("Effectuez votre choix [0-5] : "))
        if choix == 0:
            # Déconnecter l'utilisateur
            print(f"Déconnexion de {utilisateur_connecte}...")
            utilisateur_connecte = None
        elif choix == 1:
            # Affichage du catalogue d'articles
            afficher_catalogue(catalogue)
        elif choix == 2:
            # Ajouter un article du catalogue au panier
            # Si une entrée 'panier' existe déjà pour l'utilisateur; on la récupère; sinon, on la crée
            panier = utilisateurs[utilisateur_connecte].get('panier')
            if not panier:
                panier = {}
                utilisateurs[utilisateur_connecte]['panier'] = panier
            # On ajoute la référence et la quantité désirée au panier
            reference = input("Veuillez saisir la référence du catalogue à ajouter")
            if reference not in catalogue:
                print("La référence introduite n'est pas valide !")
            else:
                quantite = int(input("Veuillez saisisr une quantité pour cette référence ! (Quantités entières uniquement) : "))
                # Si la référence existe déjà dans le panier, on ajoute la quantité à l'ancienne; sinon on indique simplement cette quantité
                panier[reference]  = panier[reference] + quantite if (reference in panier) else quantite
                utilisateurs[utilisateur_connecte]['panier'] = panier
        elif choix == 3:
            # Affiche le panier de l'utilisateur et son prix
            panier = utilisateurs[utilisateur_connecte].get('panier')
            if not panier:
                print("Le panier de l'utilisateur est vide !")
            else:
                afficher_panier(panier,catalogue)
        elif choix == 4:
            # Modifier la quantité d'un article du panier
            # On commence par afficher le contenu du panier
            panier = utilisateurs[utilisateur_connecte].get('panier')
            if not panier:
                print("Il n'existe aucun panier pour cet utilisateur !")
            else:
                afficher_panier(panier,catalogue)
                # On demande à l'utilsateur d'introduire la référence de l'article dont on veut modifier la quantité
                reference = input("Veuillez introduire la référence dont vous souhaitez modifier la quantité : ")
                if reference not in panier:
                    print("La référence n'existe pas dans le panier de l'utilisateur !")
                else:
                    quantite = int(input("Veuillez introduire la nouvelle quantité pour cette référence : "))
                    utilisateurs[utilisateur_connecte]['panier'][reference] = quantite
        elif choix == 5:
            # Supprimer un article du panier
            panier = utilisateurs[utilisateur_connecte].get('panier')
            if not panier:
                print("Il n'existe aucun panier pour cet utilisateur !")
            else:
                afficher_panier(panier,catalogue)
                # On demande à l'utilsateur d'introduire la référence de l'article dont on veut modifier la quantité
                reference = input("Veuillez introduire la référence à supprimer du panier ")
                if reference not in panier:
                    print("La référence n'existe pas dans le panier de l'utilisateur !")
                else:
                    utilisateurs[utilisateur_connecte]['panier'].pop(reference)
        else:
            # L'entrée choisie n'est pas valide !
            print("L'entrée choisie n'est pas valide ! Veuillez recommencer !")










