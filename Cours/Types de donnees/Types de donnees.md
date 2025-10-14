#description Cette fiche expliquera ce que sont les types de données; et présentera succinctement celles que nous verrons dans le cadre de ce cours.

#def Un **type de données** (ou *datatype*, en anglais) 
- définit l'<u>ensemble des valeurs</u> que peut prendre une donnée
- définit les <u>opérations</u> qui peuvent lui être appliqués.

Dans un premier temps, on distinguera les types de données en fonction du nombre de valeurs que peut contenir chaque élément :
- Les *types 'scalaires'* : sont des types dont les éléments :
	- ne contiennent qu'<u>une seule valeur</u>
	- et cette valeur est dite #def '<u>atomique</u>' : c'est à dire qu'elle ne peut est décomposée en éléments plus simples.
- Les *types 'composés'* : sont des types dont les éléments :
	- peuvent être composés <u>plusieurs valeurs</u> 
	- et ces valeurs peuvent elles-mêmes, appartenir à des types composés; c'est à dire qu'elles ne sont pas nécessairement 'atomiques'.

#attn Toute valeur possède un type (c'est à dire, appartient à un *type de donnée*)
 
# Les types 'scalaires'
#def Un type scalaire est un type dont la donnée ne peut contenir qu'<u>une seule valeur</u>; et cette valeur est <u>atomique</u>; c'est à dire qu'elle ne peut pas être scindée en éléments plus petits.

## Le type 'None' : NoneType
- **Ensemble des valeurs** : {`None`}

La valeur`None` signifie l'absence de valeur.
**Note** : en Python, pour pouvoir utiliser une variable, celle-ci doit avoir été **déclarée** et, une variable n'y est déclarée qu'au moment où elle reçoit une valeur.  
Parfois, on ne connaît pas la valeur que va posséder la variable avant de l'utiliser.  Au lieu d'utiliser une valeur *par défaut*, on utilisera alors la valeur `None`, pour indiquer à l'interpréteur Python, que la variable existe; mais qu'elle n'a pas encore reçu de valeur.

```python
prenom = None
```
## Le type 'Booléen' : bool
- **Ensemble des valeurs** : {`True`, `False`}

**Note** : Le type booléen permet de représenter le résultat d'une une *expression booléenne* ; à savoir, une expression dont la valeur est soit : `True` (vraie) ou `False` (fausse).  Les *expressions booléennes* sont utilisées pour exprimer des *conditions*.
## Le type 'Entier' : int
- **Ensemble des valeurs** : les nombres entiers (eg. -17, 5, 0, 189,...)
## Le type 'Float' : float
- **Ensemble des valeurs** : le nombres en virgule flottante (eg. 3.14, 32.5, -7.689, 0.0,...)

# Les types composés 
#def Un type composé est un type dont la donnée peut contenir plusieurs valeurs.

On y distinguera les **types de séquence** et les **types de mapping**
## Les types de séquence
#def Les types de séquence sont des types composés qui possèdent les caractéristiques suivantes : 
- Les **éléments sont ordonnés** : il y a un premier, un second, un troisème, etc...
  De ce fait, les éléments peuvent être accédés en utilisant leur position dans la séquence.
  **Tip** : Pour ce faire, il suffira de faire suivre la séquence par des crochets `[]`; en indiquant entre ceux-ci, l'indice de l'élément à récupérer. Notez que le premier élément commence toujours à l'indice `0`. 
- Les **répétitions sont autorisées** : on peut avoir plusieurs fois un même élément, à des positions différentes.

### Le type 'Liste' : list
#def Une liste est un type de séquence dont les éléments peuvent être modifiés

Une liste en python :
- est délimitée par une paire de crochets :  `[ ]`
- entre lesquels on viendra placer les éléments, séparés entre eux par des virgules.
```python
ma_liste = ['abc', 12, 3.14]
liste_vide = []
```
### Le type 'tuple' : tuple
#def Un tuple est un type de séquence dont on ne peut modifier le contenu après sa création.

Un tuple en Python :
- est délimité par une paire de parenthèses : `( )`
- entre lesquelles on viendra placer les éléments, séparés entre eux par des virgules.
**Rem** : un tuple en Python, se définit donc presque comme une liste; si ce n'est qu'on ne peut en modifier le contenu après sa création.
```python
mon_tuple = ('abc', 12, 3.14)
tuple_vide = ()
```
### Le type 'Chaîne de caractère' : str
#def Une 'chaîne de caractères' est une séquence de caractères.

Une 'chaîne de caractères' en Python :
- est délimitée par une paire d'apostrophe `' '` ou de guillemets `" "` 
- entre lesquels on viendra placer les caractères.
```python
ma_chaine1 = 'Le soleil brille'
ma_chaine2 = "Le soleil brille"
```
**Attn** : si l'on veut utiliser à l'intérieur de la chaîne, le même type de guillemet que celui qui sert de délimiteur (apostrophe ou guillemet); il faudra *l'échapper* (escape); à laide du caractère d'échappement : `\` (backslash).

### Le type 'range'
#def Un 'range' est une séquence de nombres.

Un range en Python :
- est généré à l'aide de la fonction `range()`
	- `range(stop)` : génère une séquence d'entiers allant de `0` à `stop-1`
	- `range(start,stop)` : génère une séquence d'entiers allant de `start` à `stop-1`
	- `range(start,stop,step)` : génère une séquence d'entiers allant de `start` à `stop-1`, par pas de `step`
- dont les arguments `start`, `stop` et `step` détermineront la liste de nombres ainsi générée.
**Note** : `range` est très utilisé dans les boucles `for` afin de répéter une séquence un certain nombre de fois.

```python
list(range(10))         # génère une liste de 10 nombres allant de 0 à 9
list(range(5,10))       # [5,6,7,8,9]
list(range(0,-20,-2))   # [0,-2,-4,-6,-8,-10,-12,-14,-16,-18]
for i in range(10):     # parcourt la boucle 10 fois (pour i allant de 0 à 9)
    print(i)
```

## Les types de mapping
### Le type 'dictionnaire' (dict)
#def un **dictionnaire** est une collection de paires de la forme `clé:valeur`

Un 'dictionnaire' en Python :
- est délimité par des accolades `{ }`, dont les paires `clé:valeur` seront séparées par des virgules.
```python
utilisateurs = {23231:"Alexandre Dupont", 27881:"Sylvie Durant", 28121:"Isabelle Lebon"}
```
**Attn** : une même *'valeur'* peut être répétée au sein d'un dictionnaire; mais **les clés doivent être uniques**.

**Tip** : on accède à une valeur en utilisant sa clé (et non plus par son index, comme pour les séquences)
```python
mon_dictionnaire = {"a":1,"b":2,"c":3,"a":4}
mon_dictionnaire["a"]    # 4
```
