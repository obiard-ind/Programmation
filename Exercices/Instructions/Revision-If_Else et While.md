# Boucles `while`

**Requis** : pour ces exercices, il est interdit d'utiliser l'instruction `break` pour sortir de la boucle.  Vous **devez** utiliser des expressions booléenes dans l'instruction while.
## Ex-0 : Vérification du mot de passe
## Programme 1
Définissez un mot de passe et stockez-le dans une variable.
Créez ensuite un programme qui va demander à l'utilisateur de deviner ce mot de passe.
Si le mot de passe introduit est correct; alors l'utilisateur se verra gratifier d'un message de bienvenue.  Sinon; il se verra reposer la question jusqu'à ce qu'il aie introduit un mot de passe correct.
## Programme 2
Ajoutez à présent un compteur qui va enregistrer le nombre de fois que l'utilisateur tape un mauvais mot de passe.
A chaque fois que l'utilisateur aura tapé un mauvais mot de passe; le programme lui indiquera le nombre de fois qu'il a déjà introduit un mot de passe incorrect; et lui demandera de recommencer; jusqu'à ce qu'il aie réussi.

## Programme 3
Idem que le programme 2; mais cette fois, l'utilisateur n'aura droit qu'à un certain nombre de tentatives.  Vous utiliserez une variable pour enregistrer le nombre de tentatives auxquelles l'utilisateur a droit.  Avant chaque tentative; le programme indiquera à l'utilisateur le nombre d'essais qu'il lui reste.

Si, au terme du nombre de tentatives défini, l'utilisateur n'a toujours pas deviné le mot de passe; le programme se terminera en affichant `désolé, mais votre compte est désormais bloqué !`

# Structures conditionnelles : `if... elif... else`

# Ex-0 : Deviner un nombre
Vous allez créer un petit programme qui permettra à deux utilisateurs de jouer ensemble.
Lors du démarrage; le premier joueur se verra demander d'introduire un nombre entre 0 et 100.  Bien entendu, le second joueur détournera le regard; car il ne doit pas voir la solution ;-).
Le programme demandera ensuite au second joueur de deviner ce nombre.
Si le nombre est trop petit; le programme lui dira qu'il faut viser plus haut; et inversément, si le nombre est trop grand; qu'il faudra viser plus bas.
A chaque tentative; vous informerez aussi le second joueur du nombre de tentatives qu'il a déjà effectuées.
A la fin du jeu; si le joueur a deviné en moins de 3 tentatives; vous le gratifierez d'un `Super ! Tu es vraiment le meilleur !`; entre 4 et 6 tentatives, vous lui direz `Pas mal du tout !`; à partir de la 7ème tentative : `Pas de veine aujourd'hui !`

# Ex-1 : Les formes géométriques
Voici un petit exercice de classification des formes géométriques.
En fonction du nombre de côtés, de leur longueur et/ou des leur angles internes; vous indiquerez à l'aide d'un petit programme de quelle forme il s'agit.
Un polygône qui possède 3 côtés, est un triangle.  
- Il est isocèle s'il possède deux côtés de longueur égale ou deux angles égaux.
- Il est rectangle s'il possède 3 côtés ou trois angles égaux.
Un polygône qui possède 4 côtés est un quadrilatère.
- Il peut s'agir d'un carré, d'un rectangle, d'un losange, d'un parallélogramme ou d'un trapèze.
Un polygône à 5 côtés est dénommé pentagone.









