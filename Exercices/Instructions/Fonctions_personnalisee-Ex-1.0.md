L'obectif ici est double :
- vous initier à la création de fonctions personnalisées
- apprendre à les utiliser ensuite pour réaliser certains calculs / opérations.
Pour chacune de ces fonctions; testez-les en les appelant avec des arguments de valeurs différentes.
# Exercices pour commencer
- Créez une fonction qui prend 2 nombres en paramètres et renvoie leur produit
- Créez une fonction qui calcule si un nombre passé en argument est multiple d'un autre
- Créez une fonction qui calcule la force (en Newton) en fonction de la masse (en kilo) et d'une accélération (en $m/s^2$  ).  En physique, la formule qui relie ces grandeurs s'écrit : $$F = m.a$$
- Créez une fonction qui retourne l'aire d'un cercle en fonction de son rayon.  La formule pour calculer l'aire est : $$A = \pi.r^2$$
- Créez une fonction qui retourne le volume d'une sphère en fonction de son rayon.  La formule de calcul du volume d'une sphère : $$V = \frac{4}{3} * pi * r^3$$
- Créez une fonction qui demande son âge à l'utiliser et renvoie `True` s'il est majeur; et `False` sinon.

# Exercices pour s'entraîner
## Affichage d'un menu

Créez une fonction qui prend une liste de phrases en paramètre; et affiche un menu.
Celui-ci affichera, pour chaque phrase de la liste : une ligne qui commence par un nombre correspondant à l'index de la phrase dans la liste; suivi d'un '.';  et, pour finir, de la phrase.

  ```Exemple de résultat
  0. Quitter le menu
  1. Ajouter un élément
  2. Supprimer un élément
  3. Modifier un élément
  ```
## Vérification d'un mot de passe
### Programme 1 
Créez une fonction qui vérifiera si un mot de passe est valide selon certaines conditions.
Pour ce premier programme, vous ne passerez que le mot de passe en argument; et les critères de validité seront intégrés à la fonction; à savoir que sa longueur est comprise entre 8 et 16 caractères.
### Programme 2
Créez une fonction qui vérifiera si un mot de passe est valide selon certaines conditions.  Cette fois, les critères seront passées sous forme d'arguments aux paramètres suivants :
	- Le 1er paramètre : le mot de passe à tester
	- Le 2ème paramètre : la longueur minimum que doit avoir le mot de passe
	- Le 3ème paramètre : la longueur maximum que doit avoir le mot de passe

## Création d'un tableau
### Tableau vide
Créez une fonction qui prendra 2 arguments : un nombre `m`  de lignes, et un nombre `n` de colonnes.
Affichez un tableau de m lignes x n colonnes; en utilisant les séparateurs `|` entre les colonnes; et `-` entre les lignes.
### Table de multiplication
Reprenez le programme précédent; et assurez vous que chaque case à l'intersection d'une ligne et d'une colonne soit constituée du nombre qui correspond à : `m * n` (où `m` est l'indice des lignes; et `n`, l'indice des colonnes).
## Nombres premiers
Créez une fonction qui retournera une liste des nombres premiers compris entre 1 et le nombre qui sera passé comme argument.
Rappel : un nombre premier est un nombre qui n'est divisible que par 1 et par lui-même.

## Palindrome
Créez une fonction qui prendra en argument une chaîne de caractères et renverra `True` si celui-ci est un palindrome et `False` sinon.
Rem : un palindrome est un mot qui peut se lire dans les deux sens.
Voici quelques exemples :
- Mots : "radar", "ressasser", "kayak",...
- Phrases : "Esope reste ici et se repose", "Engage le jeu que je gagne", "Elu par cette crapule",...
Tip : utiliser l'opérateur de tranchage que nous avons déjà vu `[::-1]`

## Remplacer les espaces par des 'undercores'
Créez une fonction qui prendra une phrase en argument et renverra la même phrase dont tous les espaces auront été remplacés par le caractère de soulignement (underscore) : `_`

## Bannière de texte
Creez une fonction qui prendra une chaîne de caractères en argument et renverra une chaîne de `n` caractères : `n` étant un nombre qui sera également passé en argument.
Si la chaîne de caractère est vide; alors la chaîne en retour sera constituée uniquement de `*`
Si la chaîne n'est pas vide; alors vous veillerez à ce chaque extrémité de la chaîne retournée par la fonction soit constituée d'un unique caractère `*` (à gauche, et à droite); et que la chaîne passée en argument soit bien centrée.
Exemple d'appel :
```
banniere("",80)
banniere("Bonjour la classe",80)
banniere("C'est le printemps",80)
banniere("",80)
```
Exemple de résultat :
```
********************************************************************************
*                              Bonjour la classe                               *
*                              C'est le printemps                              *  
********************************************************************************
```

# Exercices pour approfondir

# Trier une liste
Créez une fonction qui prendra une liste de nombres en argument; et retournera celle-ci triée.
Rem : n'utilisez pas de fonction prédéfinie; mais créez votre propre programme de tri.
Explication de l'algorithme de tri par insertion : https://www.youtube.com/watch?v=bRPHvWgc6YM



