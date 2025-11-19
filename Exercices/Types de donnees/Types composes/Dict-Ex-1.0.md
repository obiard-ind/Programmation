# Exercices pour commencer
## Ex1  : Le contrôle technique
Créez, à l'aide d'un dictionnaire, une petite base de données d'une dizaine de véhicules indiquant si ceux-ci sont en ordre ou nom de contrôle technique.  Les clés, qui doivent être uniques, seront représentées par les plaques d'immatriculation des véhicules.
**Rem** : utilisez des plaques d'immatriculation valides selon la DIV (Direction de l'Immatriculation des Véhicules).
## Ex2 : Le contrôle technique (étendu)
Pour chaque véhicule de l'exemple précédent; l'on souhaiterait ajouter
- sa marque,
- la date de son dernier passage au contrôle,
- la date prévue pour sa prochaine révision.
- le résultat du contrôle; à savoir :
	- 'Rouge' : le véhicule ne peut plus rouler
	- 'Jaune' : il y a des points à surveiller.
	- 'Vert' : tout va bien.
**Tip** : vous pouvez utiliser des dictionnaires imbriqués (à savoir : un dictionnaire, dans un dictionnaire)

## Ex3 : Un mini-cabanga !
Chaque élève est identifé par un numéro d'élève constitué de son année d'inscription à l'école, ainsi que par un nombre unique pour l'année considérée, et constitué de 4 chiffres.
Exemple : 20200079, 20201051, 20210079, 20230851,...
Chaque élève possède une fiche qui reprend son nom, son prénom, sa date de naissance et l'année dans laquelle il est inscrit (eg. 4TT, 5TT, 5TQC,...)

On vous demande de créer un dictionnaire comportant déjà une dizaine d'élèves : 5 pour la classe de 4TT, et 5 pour la classe de 5TT.

On vous demande de créer un petit programme qui permettra au secrétariat d'ajouter de nouveaux élèves à ce dictionnaire.
Celui-ci proposera le menu suivant à l'éxécution.  On sélectionnera l'entrée de menu correspondante en tapant son numéro.
```
0. Quitter le programme
1. Ajouter un nouvel élève
2. Afficher la liste des élèves
3. Afficher un élève par son numéro d'inscription
4. Afficher les élèves par classe.
```

On affichera les données correspondant à un élève sur une même ligne; à raison d'un élève par ligne s'il y en a plusieurs à afficher.

