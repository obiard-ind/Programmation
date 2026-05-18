##################################################
#            Remédiation : Appliquer             #
##################################################
"""Enoncé :
Vous aller commencer par créer 2 fiches de contact que vous stockerez chacune dans une variable différente.
- La fiche de contact 1 concerne Laura Dupas, née le 16 janvier 2001 à Namur.  
  son numéro de fixe au travail est le 081/264512; et elle possède un gsm privé; le 0496/241585
- La fiche de contact 2 concerne Sylvain Dubois, né le 19 septembre 1980 à Charleroi.
  Au bureau, son numéro de fixe est le 071/896132; il possède également un gsm pour le travail; le 0474/523145.
  Pour son privé; il a un fixe : le 071/565641 et un gsm : le 0498/561495.

Vous allez maintenant afficher les données de la fiche de contact 2 en les parcourant à l'aide d'une boucle `for`.
On aimerait que les données s'affichent de la façon suivante :
```
Nom : Dubois
Prenom : Sylvain
Date de naissance : 1980-09-19
Lieu de naissance : Charleroi
Telephones :
    - Fixe travail : 071/896132
    - Fixe privé : 071/565641
    - Gsm travail : 0474/523145
    - Gsm privé : 0498/561495
```
Rem : l'ordre d'apparition des téléphones n'a pas d'importance... 
et si le contact n'avait pas de donnée associée pour un type de téléphone; celui-ci n'apparaîtrait pas dans la liste.
"""


contact1 = {
    'nom':"Dupas",
    'prenom':"Laura",
    'date_naissance':"2001-01-16",
    'lieu_naissance':"Namur",
    'telephones':{
        'Fixe travail':"081/264512",
        'Gsm privé':"0496/241585"
    }
}

contact2 = {
    'nom':"Dubois",
    'prenom':"Sylvain",
    'date_naissance':"1980-09-19",
    'lieu__naissance':"Charleroi",
    'telephones':{
        'Fixe travail':"071/896132",
        'Gsm travail':"0474/523145",
        'Fixe privé':"0498/561495",
        'Gsm privé':"0496/241585"
    }
}

for key, value in contact2.items():
    if key != "telephones":
        print(key,' : ', value)
    else:
        print(key,' :')
        for key1, value1 in value.items():
            print('\t', key1,' : ',value1) 

##################################################
#            Remédiation : Tranférer             #
##################################################
"""Enoncé : 
En reprenant l'idée d'une liste de contacts; créez un dictionnaire que vous nommerez `contacts` et qui contiendra les deux contacts que vous avez crééz précédemment.
En outre, vous créerez une application qui répondra aux exigences du menu suivant :
```
0. Quitter le gestionnaire de contacts
1. Ajouter un contact
2. Rechercher si un contact existe sur base de son nom
3. Supprimer un contact
"""



##### Initialisation des variables #####
# Initialisation de notre carnet de contacts avec les deux contacts précédents
contacts = {
    1:contact1,
    2:contact2
}
# Initialisation de la variable qui contient la valeur de la dernière clé.
last_index = 2
# Initialisation du contrôle de sortie de la boucle
continuer = True
# Initialisation du menu à afficher
menu = """
0. Quitter le gestionnaire de contacts
1. Ajouter un contact
2. Rechercher un contact par son nom
3. Supprimer un contact
"""

##### Initialisation des fonctions
def afficher_contact(contact):
    """
    Affiche la fiche d'un contact

    Args:
        contact(dict) : un dictionnaire représentant une fiche de contact
    """

    for key, value in contact.items():
        if key != "telephones":
            print(key,' : ', value)
        else:
            print(key,' :')
            for key1, value1 in value.items():
                print('\t', key1,' : ',value1) 




##### Programme principal

while continuer:
    try:
        print(menu)
        choix_menu = int(input("Veuillez introduire votre choix [0-3] : "))
        if choix_menu == 0:
            # Quitter le programmer
            print("Merci d'avoir utilisé notre programme !")
            continuer = False

        elif choix_menu == 1:
            # Ajouter un nouveau contact
            contact = {}   # Initialiser le contact avec le dictionnaire vide
            contact['nom'] = input("Introduisez le nom du contact : ") 
            contact['prenom'] = input("Introduisez le prénom du contact : ")
            contact['date_naissance'] = input("Introduisez sa date de naissance : ")
            contact['lieu_naissance'] = input("Introduisez son lieu de naissance : ")
            contact['telephones'] = {} # Initialiser le dictionnaire de téléphones avec le dictionnaire vide.
            
            encoder_telephone = input("Ajouter un numéro de téléphone ? [O/N] : ") # Initiliser la variable qui contrôle la condition de sortie de la boucle
            while encoder_telephone.lower() == "o":
                libelle_telephone = input("Introduire un libellé pour ce numéro de téléphone (eg. 'fixe maison') : ")
                if libelle_telephone in contact['telephones'].keys():
                    print("Un libellé du même nom existe déjà ! Veuillez choisir un autre nom")
                else:
                    contact['telephones'][libelle_telephone] = input("Introduire le numéro de téléphone (eg. 071/654123) : ")
                # On doit pouvoir sortir de la boucle => on doit pouvoir modifier la variable dans l'expr. booléenne du while
                encoder_telephone = input("Ajouter un autre numéro de téléphone ? [O/N] : ")
            
            # Ajouter le nouveau contact dans le dictionnaire des contacts ! Attn : ne pas oublier ;-)
            last_index +=1    # On incrémente la clé ! Il ne peut y avoir 2 clés identiques
            contacts[last_index] = contact

        elif choix_menu == 2:
            # Rechercher un contact par son nom
            nom_contact = input("Introduire le nom du contact à rechercher : ")
            contact_trouve = False  # Variable qui indique si un contact au moins a été trouvé
            for key, value in contacts.items():
                if value['nom'].lower() == nom_contact.lower():
                    print(f"########## Contact : {key} ") # On affiche un petit titre avec la clé du contact trouvé
                    contact_trouve = True
                    afficher_contact(value)
                    print() # On affiche une ligne vide après le contact
            if not(contact_trouve):
                print(f"Aucun contact correspondant au nom {nom_contact} n'a été trouvé ! ")
        
        elif choix_menu == 3:
            # Supprimer un contact sur base de sa clé
            cle_contact = int(input("Quel est le numéro de la clé du contact à supprimer ? [un entier] : "))
            resultat = contacts.pop(cle_contact,None)
            if not(resultat):
                print(f"La clé {cle_contact} n'a pu être trouvée ! Aucun contact supprimé.")
            else:
                print(f"Le contact {cle_contact} a bien été supprimé !")

        else:
            # Choix n'est pas dans le menu
            print("Choix incorrect ! Veuillez recommencer.")
    except Exception as e:
        print("Une exception s'est produite ! Le type de valeur introduit est-il correct ?")
        print(e) # Affiche l'exception produite



