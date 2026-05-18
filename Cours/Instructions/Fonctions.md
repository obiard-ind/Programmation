#def Les **fonctions** sont des instructions qui renvoient une valeur.

Concrètement : les fonctions sont comme des *mini-programmes* que l'on appelle dans notre code afin de réaliser certaines tâches.  
# Fonctions intégrées au langage
Python vient avec un ensemble de fonctions intégrées au langage (+/-70 en Python v3.12).  Elles sont donc directement utilisables dans vos programmes.  Vous en avez d'ailleurs déjà utilisés certaines :  `input()`, `print()`, `range()`, `len()`, `min()`, `max()`,`sum()`,... 
#ref [Liste des fonctions intégrées au langage ](https://docs.python.org/3/library/functions.html)

Mais il existe des fonctions pour à peu près tous les traitements spécialisés que nous pouvons imaginer : de la gestion de fichiers au traitement de l'image, du son ou de la vidéo; en passant par les fonctions mathématiques; et même de l'apprentissage profond ou de l'IA, etc...
Nous verrons par la suite comment accéder à ces fonctions additionnelles en les important au travers de librairies...

... mais avant cela, nous allons apprendre à créer nos propres fonctions :
- pour répondre à des besoins spécifiques
- pour comprendre comment tout cela fonctionne !
# Fonction définies par l'utilisateur
Bien qu'il existe des fonctions pour presque toutes les tâches; il peut arriver que l'on aie besoin de créer une fonction 'sur mesure' pour un besoin particulier.
Ca tombe bien, c'est l'objet de ce chapitre ! :-)

On distinguera donc 2 étapes :
1. La création de la fonction (on parlera de '**définition de la fonction**')
   **Rem** : la plupart du temps, nous utiliserons des fonctions qui auront été créées par d'autres développeurs; mais il pourra arriver que nous ayons à créer nos propres fonctions.
2. L'utilisation de la fonction dans notre code (on dira que l'on '**appelle une fonction**')

## Utilité de l'usage des fonctions
Travailler avec des fonctions présente plusieurs avantages :
#### Structurer et organiser le code
En analysant un problème et en le découpant en sous-problèmes; on rend celui-ci plus facile à comprendre et à résoudre.
#### Eviter la duplication de code
Lorsque l'on doit faire plusieurs fois la même chose dans un programme; l'on peut être tenté de faire du copier/coller de code.  Une fonction permettra d'encapsuler ce code sous un nom; et d'appeller ce bloc de code aux endroits où c'est nécessaire; et ainsi rendre le **code plus lisible**; mais aussi **plus maintenable** (puisqu'une modification réalisée à l'intérieur de la fonction sera disponible partout où cette fonction est appelée).
#### Faciliter la résolution de problèmes
En **divisant un gros problème en plus petits sous problèmes** qui peuvent être résolus indépendamment; on pourra traiter chacun de ceux-ci tour à tour.  Et comme ils sont plus petits; ils seront plus faciles à résoudre.
#### Faciliter la correction d'erreur / améliorer la maintenabilité
Il est plus facile de corriger une erreur dans un petit programme que dans un gros programme.
De plus, toute correction / modification réalisée dans une fonction sera directement accessible partout où celle-ci est appelée.

## Définition de fonctions

## Syntaxe
```python
def nom_fonction(param1,param2,...):
    bloc d'instructions
    return valeur
```

- `def` : est le mot-clé qui indique à notre interpréteur Python que ce qui suit est une définition de fonction.
- `nom_fonction` : un nom que vous choisirez pour nommer votre fonction.  Il répond aux mêmes règles que les noms de variables.
- `(   )` : les parenthèses sont obligatoires après le nom d'une fonction.
	- On peut ne rien mettre entre celles-ci,
	- Ou l'on peut préciser une suite de paramètres
- `param1, param2,...` : il s'agit des paramètres que l'on pourra utiliser avec notre fonction.
	- Les noms 'param1', 'param2',... sont donnés à titre d'illustration; mais il est bien évident que vous les nommerez comme il vous semblera le plus judicieux de les appeler.
	- Les paramètres sont des noms de variables que vous pourrez utiliser à l'intérieur du bloc d'instructions qui constitue le corps de la fonction.  A ce titre, ils répondent aux mêmes règles, notamment de nommage que les variables.
	- Leur **portée**; c'est à dire, la partie du code où une variable est accessible; est limitée au bloc de code qui constitue la fonction.  Les paramètres ne sont donc pas accessibles en dehors de celle-ci.
	- Ces 'variables' recevront leur valeur lors de l'appel de la fonction (que nous verrons plus loin)
- `:` On n'oubliera pas les `:` juste après la parenthèse fermante; afin d'indiquer que ce qui suit est un `bloc d'instructions`.
- `bloc d'instructions` : il s'agit d'une séquence d'instructions qui vont opérer, notamment sur les paramètres afin de réaliser un traitement et retourner une valeur.
- `return` : lorsque le mot-clé return est rencontré; il fait deux choses :
	- Il quitte la fonction (à l'instar de l'instruction 'break' dans d'autres instructions : `while`,...)
	- Il 'renvoie' au code qui 'appelle' la fonction; la valeur de l'expression qui suit le mot-clé 'return'.

## Exemples :
Exemple : définition d'une fonction qui réalise la somme de deux nombres
```python
def somme(a,b):
	return a+b
```

Exemple : définition d'une fonction qui calcule la puissance d'un nombre 
```python
def puissance(base, exposant):
    resultat = 1
    for i in range(exposant):
        resultat *= base
    return resultat
```

Exemple : afficher une phrase un certain nombre de fois
```python
def afficher_phrase(phrase,nb):
    for i in range(nb):
        print(phrase)
```
**Rem** : ce dernier exemple est un cas particulier; car il ne *retourne pas de valeur* au programme qui l'a appelé.  Il se contente d'exécuter une série d'instructions; à savoir d'afficher quelque chose ! 
Si l'on avait voulu rester puriste; on aurait pu mettre `return None` comme dernière instruction de notre fonction.

Exemple : vérifier si un nombre est pair (ou impair)
```python
def est_pair(nombre):
    if nombre %2 ==0:
        return True
    return False
```
**Note** : on observera ici deux choses :
- Que la valeur de retour peut être de n'importe quel type (entier, float, liste, dictionnaire,...).  Ici, c'est un booléen que l'on renvoie !
- Que le mot-clé return peut apparaître plusieurs fois dans une fonction ! C'est notamment le cas lorsque celle-ci contient une instruction conditionnelle (`if`).... à l'instar d'un `break`.  Dès celui-ci atteint, il renvoie la valeur qui le suit; et l'on quitte la fonction.

# Appel de fonction
L'intérêt des fonctions; c'est de créer des mini-programmes que l'on pourra exécuter à la demande avec des valeurs différentes.
On qualifiera d'**appel de fonction**, l'instruction qui consistera faire exécuter le code contenu dans le corps de notre fonction; sur les valeurs qui seront *passées* aux paramètres.
## Syntaxe
```python
nom_fonction(valeur1,valeur2,...)
```
- `nom_fonction` : on **appelle** une fonction (on indique quelle fonction on veut exécuter) par son nom.
- `( )` : celui-ci est suivi obligatoirement des parenthèses.
- `arg1,arg2,...`  : les **arguments** sont les valeurs que l'on va utiliser pour initialiser les **paramètres** (à savoir les variables) utilisées dans la définition de notre fonction.
	- Le nombre d'arguments doit correspondre au nombre de parmètres
	- L'ordre des arguments doit correspondre à l'ordre des paramètres.
### Passage par référence vs passage par valeur
- Lorsque l'argument est un type **immutable**; alors la <u>valeur de l'argument</u> sera passée au paramètre.
	- Le paramètre reçoit une 'copie' de la valeur de l'argument.
	- Si le paramètre est modifié par la fonction; l'argument qui a servi à l'appel n'est jamais modifié.
```python
# Définition de la fonction
def multiplier_nombre(nombre):
    nombre *= 2
    
# Initialisation de l'argument
nombre = 5       # un entier est un type immutable
print(multiplier_nombre(nombre)) # None (voir note ci-dessous)
print(nombre)    # 5
```
- Lorsque l'argument est un type **mutable**; alors c'est une <u>référence vers l'argument</u> qui est passée au paramètre.  
	- Le paramètre travaille directement sur l'argument.
	- Si on modifie la valeur du paramètre; alors l'argument qui a été utilisé pour l'appel sera directement modifié.
```python
# Définition de la fonction
def multiplier_liste(liste):
    i=0
    for element in liste:
       liste[i]*=2
# Initialisation de l'argument        
ma_liste = [1,2,3,4]    # une liste est un type mutable
# Appel de la fonction avec l'argument
print(multiplier_par_deux(ma_liste)) # None (voir note ci-dessous)
print(ma_liste)    # [2,4,6,8]
```

**Note** : vous aurez notez qu'aucune des deux fonctions ne retourne de valeur dans ces exemples.
Quand une fonction ne retourne pas de valeur; elle retourne implicitement la valeur `None`

## Fonctionnement
Lorsque l'on appelle la fonction; l'interpréteur Python va :
1. Initialiser les **paramètres** (variables) avec la valeur des **arguments** transmis lors de l'appel.
2. Exécuter les instructions contenues dans le corps de la fonction.
3. Retourner la valeur qui suit le mot-clé **return**

## Exemples
Exemple : appel de la fonction *somme(a,b)* 
```python
resultat = somme(15,17)    # a <- 15, b <-17; retourne 32
print(resultat)            
```

Exemple : appel de la fonction *puissance(base,exposant)*
```python
resultat = puissance(2,8)   # base <- 2, exposant <- 8; retourne 256
print(resultat)             
```

Exemple : appel de la fonction *afficher_phrase(phrase,nb)*
```python
afficher_phrase("J'aime les fonctions !",50)
# Affichera "J'aime les fonctions !" 50 fois.
```

Exemple: appel de la fonction *est_pair(nombre)*
```python
a = 53
if est_pair(a):             # nombre <- a ; retourne False
    print(f"{a} est pair")
else:
    print(f"{a} est impair")
```
**Rem** : on notera que l'on peut peut passer non seulement directement des valeurs comme argument d'une fonction; mais également toute variable (ici : `a`) qui contient une valeur.
**Rem** : on peut utiliser la valeur de retour de notre fonction à tout endroit de notre code où une valeur de ce type (ici : un booléen), est attendue.

