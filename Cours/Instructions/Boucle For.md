# Usages courants
Les boucles `for` sont souvent utilisées pour :
- Parcourir des séquences d'élements (str, list, tuple,...)
- Exécuter un bloc de code un **nombre déterminé de fois**... à l'aide de range()
# Fonctionnement
- la boucle `for` **itère** (çàd : parcourt) une séquence d'éléments, tour à tour, en suivant leur ordre dans la séquence à laquelle ils appartiennent.
- lors de chaque **itération** (ou tour de boucle) l'instruction `for` :
	- **assigne** la valeur de l'élement lu à une variable.
	- **exécute** ensuite le bloc de code qui suit l'instruction `for`

#def un **itérable** est tout objet qui peut être parcouru, élément par élément.
#def une **séquence** est une collection ordonnée et finie d'élements.
**Rem** : du fait que les séquences sont ordonnées, elles sont également itérables.

```
# Structure générale d'une boucle 'for'
for <variable> in <iterable>:
    bloc
```

# Application
## Itérer sur une séquence (str, list, tuple)
La boucle `for` nous permet de parcourir les éléments d'une séquence.

```python
# Parcourir une liste de ville à l'aide d'une boucle 'for'

villes = ["Bruxelles", "Paris", "New York", "Madrid", "Rome"]
i = 0

print("Mes capitales préférées sont, dans l'ordre :")

for ville in villes:
    i+=1
    print("{} - {}".format(i,ville))
```

```python
# Afficher un caractère sur 2 d'une phrase à l'aide d'une boucle 'for'
chaine = "Il fait beau et les oiseaux chantent"
index = 0
for lettre in chaine:
    if index % 2 == 0:
        print(lettre,end='')
    index += 1
```

## Répéter un bloc un nombre déterminé de fois (range)
La boucle `for` peut égalemnet être utilisée pour répéter un bloc d'instructions un nombre déterminé de fois.
**Tip** : l'on utilisera souvent alors pour ce faire, la fonction `range()`

```python
# Bart Simpson est intelligent; et il fait exécuter sa 'punition' par l'ordinateur 
# Celle-ci étant de recopier 1000 fois une phrase donnée.
for i in range(1000):
    print("Je ne boirai plus devant mon ordinateur !")
```

## Boucles 'for' imbriquées
Il est courant de travailler des boucles imbriquées (jusque 2 ou 3 niveaux).
**Tip** : (en général)
- Sur les structures 'linéaires' (1 dimension) : 
	- on utilisera 1 niveau de boucle.
- Sur les structure à 2 dimensions (tableaux à deux dimensions) : 
	- on utilisera 2 niveaux de boucle 
- etc...

**Attn** : on notera dans l'exemple suivant :
- que les variables utilisées dans le parcourt des boucles ont des <u>noms différents</u> !
- En effet, permettre que la variable utilisée au niveau de la boucle 'externe' puisse être modifiée à l'intérieur de celle-ci; et en particulier, en utilisant le même nom de variable dans une boucle imbriquée pourrait conduire à des résultats assez imprévisibles !
```python
for i in range (10):
	print("Boucle extérieure : index vaut {0} : ".format(i))
    for j in range(10):
	    print("{0} x {1} = {2}".format(i,j,i*j))
```