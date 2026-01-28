# Objectif de ces exercices
L'objectif de ces exercices est de manipuler le type [[Dict|dictionnaire]] au travers divers cas d'usage.
Les compétences à acquérir sont :  de savoir créer un dictionnaire, ajouter des éléments dans celui-ci, en supprimer; en parcourir les éléments; accéder aux clés et aux valeurs associées à ces dernières.
# Exercices pour commencer

## Ex0 : Un petit dictionnaire français <=> anglais
Imaginons que vous souhaitiez créer un petit programme informatique vous permettant de réviser votre vocabulaire en anglais.  Pourquoi ne pas utiliser vos connaissances en Python; et en particulier le type dictionnaire pour vous aider dans cette tâche ?

Créez un petit menu qui s'affichera au démarrage de votre programme; et s'affichera tant que vous n'aurez pas choisi de le quitter.  Essayez de créer le code qui répondra à chacune des entrées affichées, lorsque l'utilisateur les sélectionnera par leur numéro.

```
0. Quitter le programme
1. Ajouter un nouveau mot et sa traduction
2. Afficher la liste de tous les mots (de la langue source)
3. Afficher la liste de tous les mots et leur traduction
4. Recherchez un mot et affichez sa traduction
5. Modifier la traduction associée à un mot
6. Supprimer un mot et sa traduction
```

**Rem :** Les listes de mots seront affichées en colonnes; et s'il y a plusieurs colonnes; vous veillerez à ce que leur contenu soit bien aligné; comme dans l'exemple suivant :
```
     Français     |     Anglais     
------------------------------------
porte             | door
soleil            | sun
```

**Rem**: si le mot demandé (options `4, 5, 6`) n'existe pas; votre programme ne doit pas 'planter'.  Vous afficherez un message pour prévenir l'utilisateur que le mot demandé n'existe pas dans votre dictionnaire.
## Ex1  : Le contrôle technique
Créez, à l'aide d'un dictionnaire, une petite base de données d'une dizaine de véhicules indiquant si ceux-ci sont en ordre ou nom de contrôle technique.  Les clés, qui doivent être uniques, seront représentées par les plaques d'immatriculation des véhicules.
**Rem** : les plaques devront répondre au format N-XXX-YYY (où N peut être : {1,2,M}, X est un lettre, Y est un chiffre).
Vous parcourerez ensuite le dictionnaire et afficherez, chaque fois sur une ligne différente si le véhicule considéré est en ordre de contrôle technique ou non.
## Ex2 : Le contrôle technique (étendu)
Pour chaque véhicule identifié par sa plaque dans l'exemple précédent; l'on souhaiterait disposer des information suivantes :
- "marque" : sa marque,
- "dernier_controle" : la date de son dernier passage au contrôle,
- "prochain_controle" :la date prévue pour sa prochaine révision.
- "resultat_contrôle" : le résultat du contrôle; à savoir :
	- 'rouge' : le véhicule ne peut plus rouler
	- 'jaune' : il y a des points à surveiller.
	- 'vert' : tout va bien.
**Tip** : vous pouvez utiliser des dictionnaires imbriqués (à savoir : un dictionnaire, dans un dictionnaire)

Affichez ensuite ces informations en colonnes; où la première colonne sera la plaque, la seconde, la marque, etc... et où chaque ligne correspondra à un véhicule.
Les colonnes auront une taille fixe de 20 caractères.

# Exercices pour s'entraîner
## Ex3 : Un mini-cabanga !
Chaque élève est identifié par un numéro d'élève constitué de son année d'inscription à l'école, ainsi que par un nombre unique pour l'année considérée, et constitué de 4 chiffres.
Exemple : 20200079, 20201051, 20210079, 20230851,...
Chaque élève possède une fiche qui reprend son nom, son prénom, sa date de naissance et l'année dans laquelle il est inscrit (eg. 4TT, 5TT, 5TQC,...)

On vous demande de créer un dictionnaire comportant déjà une dizaine d'élèves : 5 pour la classe de 4TT, et 5 pour la classe de 5TT.

On vous demande de créer un petit programme qui permettra au secrétariat d'ajouter de nouveaux élèves à ce dictionnaire.
Celui-ci proposera le menu suivant à l'éxécution.  On sélectionnera l'entrée de menu correspondante en tapant son numéro.
```
0. Quitter le programme
1. Ajouter un nouvel élève
2. Afficher la liste de tous les élèves
3. Afficher un élève par son numéro d'inscription
4. Afficher les élèves par classe.
5. Modifier l'année dans laquelle un élève est inscrit
```

On affichera les données correspondant à un élève sur une même ligne; à raison d'un élève par ligne s'il y en a plusieurs à afficher.

Pour modifier la classe dans laquelle un élève est inscrit; on sélectionnera l'élève par son numéro d'identification.

# Ex4 : Gestion de bibliothèques

Vous allez créer un petit programme de gestion de stock de livres d'une bibliothèque.

La bibliothèque possédera les caractéristiques suivantes : un nom, le nom du responsable, une adresse.  Elle disposera en outre d'un catalogue de livres à disposition de ses lecteurs.

Chaque livre sera identifié par son numéro ISBN; et sa fiche proposera les informations suivantes : auteurs (il peut y en avoir plusieurs), éditeur, date de publication; disponible (qui indiquera si le livre est de stock ou non).

Pour vous permettre de gérer votre bibliothèque, vous vous aiderez du menu suivant :
```
0. Quitter le programme
1. Modifier les caractéristiques de la bibliothèque
2. Ajouter une nouvelle référence au catalogue
3. Afficher les références du catalogue et leur disponibilité.
4. Supprimer une référence du catalogue
5. Modifier le statut de disponibilité d'un livre.
```




