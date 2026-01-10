L'obectif ici est de vous initiez à la création de fonctions personnalisées; et de les utiliser pour réaliser certains calculs / opérations.
Pour chacune de ces fonctions; testez-les en les appelant avec des arguments de valeurs différentes.
# Exercices pour commencer
- Créez une fonction qui prend 2 nombres en paramètre et renvoie leur produit
- Créez une fonction qui calcule si un nombre est multiple d'un autre
- Créez une fonction qui calcule la force (en Newton) en fonction de la masse (en Kilo) et d'une accélération (en m/s^2 ).  En physique, la formule qui relie ces grandeurs s'écrit : $$F = m.a$$
- Créez une fonction qui retourne l'aire d'un cercle en fonction de son rayon.  La formule pour calculer l'air est : $$A = \pi.r^2$$
- Créez une fonction qui retourne le volume d'une sphère en fonction de son rayon.  La formule de calcul du volume d'une sphère : $$V = \frac{4}{3} * pi * r^3$$
- Créez une fonction qui demande son âge à l'utiliser et renvoie `True` s'il est majeur; et `False` sinon.

# Exercices pour s'entraîner
- Créez une fonction qui prend une liste de phrases en paramètre; et affiche un menu qui affichera, pour chaque phrase de la liste : une ligne qui commence par un nombre correspondant à l'index de la phrase dans la liste; suivi d'un '.';  et de la phrase.
- Créez une fonction qui vérifiera si un mot de passe est valide selon certaines conditions.
- 
# Exercices pour se dépasser
- Créez une fonction qui retournera une liste des nombres premiers compris entre 1 et le nombre qui sera passé comme argument.
  Rappel : un nombre premier est un nombre qui n'est divisible que par 1 et par lui-même.
- Créez une fonction qui vérifiera si un mot de passe est valide selon certaines conditions.  Le mot de passe à tester; et les critères auxquels il doit répondre seront passés comme arguments aux paramètres suivants :
	- Le 1er paramètre : le mot de passe à tester
	- Le 2ème paramètre : la longueur minimum que doit avoir le mot de passe
	- Le 3ème paramètre : la longeur maximum que doit avoir le mot de passe
- Une extension de la fonction précédente pourrait être de fournir des paramètres additionnels qui indiqueront combien de caractères minuscules, majuscules, chiffres doivent figurer dans le mot de passe.

# Exercices pour s'amuser (encore plus)
- Vous êtes un brillant physicien, et l'on vous demande de calculer la force de gravité qui s'exerce entre 2 corps massifs en fonction de leur distance.  La formule est la suivante : $$F_g = G*\frac{m_1*m_2}{r^2}$$Il s'agit de la  **loi de gravitation universelle de Newton**.
	- Pour G (la constante gravitationnelle), utilisez comme valeur un nombre en virgule flottante (type `float`).  Dans votre fonction; utilisez la constante suivante 
	  `G = 6.67430e-11     # m^3 kg^-1 s^-2`
	- Votre fonction prendra donc 3 paramètres :
		- m1 : la masse du premier corps (exprimée en kilos `[kg]`)
		- m2 : la mase du second corps (exprimée en kilos `[kg`)
		- r : la distance entre ces deux corps (exprimée en mètres `[m]`)
	- Votre fonction retournera le résultat du calcul sous forme d'une force (exprimée en Newton `[N]`)

	Utilisez à présent votre nouvelle fonction pour calculer les forces de gravité suivantes :
	- Entre le soleil la terre :
		- $m_{soleil}$ : 1.989e30
		- $m_{terre}$ : 5.972e24
		- $d_{terre-soleil}$ : 149597870700 (ou 1.496e11 en notation scientifique)
	- Entre la terre et la lune :
		- $m_{terre}$ : 5.972e24
		- $m_{lune}$ : 7.34e22
		- $d_{terre-lune}$ : 384400000 (ou 3.844e8 en notation scientifique)
	- De la terre sur un homme à sa surface :
		- $m_{terre}$ : 5.972e24
		- $m_{homme}$ : 100
		- $d_{terre-homme}$ : 6371000 (ou 6.371e6 en notation scientifique)
		  Rem : toute la masse est considérée concentrée au centre de la terre.
	- Essayez avec d'autres combinaison de cors (Homme sur la Lune, Homme sur Mars, Homme sur Jupiter,...) et d'autre distances (homme dans une station orbitale à 400km d'altitude,...)
