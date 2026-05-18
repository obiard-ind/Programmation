# Rappel de théorie
## Type scalaire vs composé
Contrairement aux types scalaires (int, bool, float,...) qui ne contiennent qu'une seule valeur; on a parfois besoin de types de données qui peuvent contenir plusieurs données.
## Types composés : liste vs dictionnaire
Dans les types composés; nous avons vu le type Liste et le type Dictionnaire.
- On utilisera le type liste pour stocker des éléments sans véritable structure
- On utilisera le type dictionnaire pour stocker des données qui possèdent une structure.

## Revoir
1. Créer un dictionnaire vide
2. Ajouter des éléments dans un dictionnaire... dont des types composés : liste, dictionnaire
3. Créer un dictionnaire global
4. Parcourir les éléments... du dictionnaire principal (.items(), .keys(), .values())
	1. Boucles imbriquées (quand une valeur est elle-même un type composé)
5. Modifier, supprimer une valeur associée à une clé.
# Exercices
## Ex-0 : Fiche de généalogie
Supposons que nous désirions créer une application de généalogie.
Dans cette application, nous stockerons les données suivantes concernant les personnes.
- Le nom
- Le prénom
- La date de naissance
- Le lieu de naissance
- Les enfants
- Les parents

Nous avons besoin d'un identifiant pour distinguer les personnes entre elles.  Dans la vie réelle; on utilise souvent le numéro national.  Dans notre application; nous utiliserons un code unique de 6 caractères; qui commence par M (Masculin) pour un homme, et F (Féminin) pour une femme; suivi de 5 chiffres.  Chaque code doit être différent.

Vous allez commencer par créer 2 fiches; une pour chacune des personnes suivantes; que vous stockerez dans des variable distinctes.
La personne 1 s'appelle Jean Dumont; né le 24 novembre 1963 à Namur; et on ne connait pas ses parents; ni ses enfants.
La personne 2 s'appelle Isablle Poirot; née le 15 juillet 1975 à Charleroi; et pour elle non plus, on ne connait ni ses parents; ni ses enfants.
## Ex-1 : Fiche de contact
Vous allez créer un dictionnaire permettant d'enregistrer vos contacts.
Chaque contact contient les informations suivantes :
- Nom
- Prénom
- Date de naissance
- Lieu de naissance
- Telephones
Une personne peut posséder jusqu'à 4 téléphones; qui seront distingués selon leur usage : { fixe-prive, fixe-travail, gsm-prive, gsm-travail }
### Appliquer
Vous aller commencer par créer 2 fiches de contact que vous stockerez chacune dans une variable différente.
- La fiche de contact 1 concerne Laura Dupas, née le 16 janvier 2001 à Namur.  Son numéro de fixe au travail est le 081/264512; et elle possède un gsm privé; le 0496/241585
- La fiche de contact 2 concerne Sylvain Dubois, né le 19 septembre 1980 à Charleroi.  Au bureau, son numéro de fixe est le 071/896132; il possède également un gsm pour le travail; le 0474/523145.  Pour son privé; il a un fixe : le 071/565641 et un gsm : le 0498/561495.

Vous allez maintenant afficher les données de la fiche de contact 2 en les parcourant à l'aide d'une boucle `for`.  On aimerait que les données s'affichent de la façon suivante :
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
Rem : l'ordre d'apparition des téléphones n'a pas d'importance... et si le contact n'avait pas de donnée associée pour un type de téléphone; celui-ci n'apparaîtrait pas dans la liste.

### Transférer
En reprenant l'idée d'une liste de contacts; créez un dictionnaire que vous nommerez `contacts` et qui contiendra les deux contacts que vous avez crééz précédemment.
En outre, vous créerez une application qui répondra aux exigences du menu suivant :
```
0. Quitter le gestionnaire de contacts
1. Ajouter un contact
2. Rechercher si un contact existe sur base de son nom
3. Supprimer un contact
```

Exercice résolu : [contacts.py ](attachments/contacts.py)


## Ex-2 : Anacardes

### Transférer

```
Votre client, 'Cajou & Co', vend des anacardes (l'autre nom des noix de cajou).
Il met à votre disposition son catalogue, lequel reprend les différents types de noix de cajou qu'il propose à la vente.  Chaque catégorie de noix est identifiée par un code unique; et possède quelques caractéristiques descriptives; lesquelles sont détaillées ci-dessous.

Il aimerait que vous mettiez en place un système de gestion de panier d'achat pour ses clients.
--- Gestion des clients
S'il s'agit d'un nouveau client; celui-ci devra s'inscire en donnant une adresse email est un mot de passe; ainsi qu'un nom et un prénom.
S'il s'agit d'un client existant; celui-ci devra se logger en utilisant l'adresse email et le mot de passe qu'il a déjà fourni.
--- Gestion du panier
Chaque client pourra; s'il est loggé, ajouter à son panier une référence article du catalogue de la société 'Cajou & Co'; et préciser la quantité souhaitée.
S'il a déjà cet article en stock; la nouvelle quantité sera simplement ajoutée à la quantité déjà existante.
Il pourra à tout moment afficher le contenu de son panier; lequel se terminera toujours par le montant total du panier d'achat.
Il pourra également; s'il le souhaite; modifier la quantité d'un article; ou supprimer l'entrée correspondant à cet artile.

Catalogue de produits :
Chaque entrée dans le catalogue est constituée des informations suivantes :
- Nom de l'article :
- Taille (exprimé e nombre de noix par livre) : 150,180,210,240,320,450,500
- Sa classe : Extra, Class I, Class II
- Sa couleur : roussie, blanche
- Son prix au kilo : en euros
```

Pour information > catalogue de références (en anglais) : [cashew_technical](attachments/cashew_technical_information_english_file_22.pdf)

Exercice résolu : [anacarde.py](attachments/anacarde.py)









