#description Cette fiche traitera du type de données "Liste" ('List', en anglais).

# Le type 'Liste' : list

#def Une liste est définie comme une **séquence d'éléments**; c'est à dire, une collection finie d'éléments qui se suivent dans un ordre donné.
Les éléments sont les valeurs individuelles qui constituent la liste.  Ils peuvent être de différents types; et sont séparés entre eux par des virgules '**`,`**'.

## Propriétés des listes en Python
- **Doublons autorisés** : ne liste peut contenir un même élément plusieurs fois.
- **Types différents autorisés** : les listes en python peuvent contenir des éléments de types différents (Rem : ce n'est pas le cas dans tous les langages). 
- **Mutable** : on peut ajouter, modifier, et supprimer les éléments d'une liste.

## Comment créer une liste ?
Pour créer une liste, on utilisera les délimiteurs 'crochets' : **`[]`**
Les éléments de la liste seront séparés par des virgules : **`,`**

```python
# Une liste vide; çàd, sans éléments !
liste = []  
# Une liste de prénoms... on notera que les doublons sont bien autorisés !
prenoms = ["Jean", "Jacques", "Albert", "Martine", "Jean"]
# Une liste de températures
temperatures = [12.7,5.0,18.1,7.2,15.6,-2.3,0.0]
# Une liste mixant des éléments de types différents.
liste_mixe = ["François", 18, True]
```

## Comment accéder à un élément à une liste ?
Comme les listes sont des **séquences**, le plus simple pour accéder à un élément de la liste; et de le faire en utilisant sa position au sein de celle-ci; à savoir son **index**.
**Rappel** : les éléments sont indexés à partir de `0`
```python
mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
# le neuvième mois de l'année est...
mois[8]    # septembre... car l'indexation commence à 0 !
```

## Comment retrouver l'index d'un élément ?
### En recherchant dans toute la liste
Inversément, on peut vouloir retrouver la valeur de l'index d'un élément dans une liste.
La _'méthode'_ `index()` :
- Si la valeur est dans la liste : renverra la valeur de l'index du premier élément correspondant à la valeur recherchée (celle-ci étant passée en argument)
- Si la valeur n'est pas dans la liste : renverra une erreur de type `ValueError`
**Syntaxe** : `list.index(element)`
```python
prenoms = ["Jean", "Jacques", "Albert", "Martine", "Jean","Frédéric","Sylvain"]
# Quel est l'index de l'élément "Jean" ?
prenoms.index("Jean")   # Retourne : 0
prenom.index("Sylvie")  # Renvoie une erreur : ValueError
```

### En limitant la recherche entre certains indices
L'on peut également limiter la recherche à une certaine plage d'indices.
On passera alors deux arguments supplémentaires à la méthode `index()`
- Le premier argument : la valeur à rechercher
- Le second argument : la borne inférieure
- Le troisième argument : la borne supérieure
**Syntaxe** : `list.index(element,index_start,index_stop)`
```python
nombres = [7,15,17,19,5,1,6,8,41,2,3,8,6,9,5,4,6,2,9,10]
prenoms = ["Jean", "Jacques", "Albert", "Martine", "Jean","Frédéric","Sylvain"]
# Existe-t'il un entier égal à 1 entre les indices 3 et 9 ?
nombres.index(41,3,9)   # Retourne : 8
# Existe-t'il un autre "Jean" ailleurs dans la liste, qu'à l'indice 0 ?
prenoms.index("Jean",1,len(prenoms)-1)   # Retourne : 4
```

## Comment connaître la longueur d'une liste ?
La longeur d'une liste est le nombre de ses éléments.
La longeur d'une **séquence** (chaîne de caractères, liste,...) s'obtient à l'aide de la _fonction_ `len()`
La fonction `len()` prendra en argument la liste dont on veut connaître la longueur.
**Syntaxe** : `len(type de sequence)`
**Attn** : comme l'indexation des éléments commence à `0` :
- la longueur d'une liste est toujours égale à la valeur de l'index du dernier élément + 1
- et réciproquement; la valeur de l'index du dernier élément est toujours égale à la longeur -1
**Tip** : cette propriété est souvent utilisée pour connaître la valeur du dernier élément de la liste; et ainsi éviter d'accéder par son index à un élément qui n'existerait pas... ce qui renverrait une erreur !

```python
prenoms = ["Jean", "Jacques", "Albert", "Martine", "Jean","Frédéric","Sylvain"]
# La valeur de l'index du dernier élément de la liste 'prénoms'
prenoms_longeur = len(prenoms)          # vaut 7
prenoms_dernier_index = len(prenoms)-1  # vaut 6
# Existe-t'il un autre "Jean" ailleurs dans la liste, qu'à l'indice 0 ?
prenoms.index("Jean",1,len(prenoms)-1)   # Retourne : 4
```
## Comment modifier un élément d'une liste ?
### Modifier l'élement à l'indice '_i_' 
Si l'on connaît l'indice de l'élement, il suffit juste de lui affecter la nouvelle valeur
```python
prenoms = ["Jean", "Jacques", "Albert", "Martine", "Jean","Frédéric","Sylvain"]
# On remplace le second 'Jean', par le prénom 'Christophe'
prenoms[4] = "Christophe"
```

## Comment ajouter un élément à une liste ?
### Ajouter un élement à la fin d'une liste
On pourra utiliser l'opérateur de concaténation de listes : `+` 
**Attn** : s'assurer que l'élement que l'on ajoute est bien également une liste... 

Exemple : ajout incorrect
```python
# On veut ajouter "ananas", mais on omet de le présenter comme une liste !
fruits = ["pomme","poire","abricot"]
fruits += "ananas" 
print(fruits) # ['pomme','poire','abricot','a,'n','a','n','a','s']
```
Exemple : ajout correct
```python
# S'assurer que ce que l'on ajoute est bien une liste !
fruits = ["pomme","poire","abricot"]
fruits += ["ananas"]
print(fruits) # ["pomme","poire","abricot","ananas"]
```

**Rem** : on peut concaténer des listes de plusieurs éléments
```python
fruits_locaux = ["pomme","poire","prunes","cerise"]
fruits_exotiques = ["banane","ananas","mangue"]
fruits = fruits_locaux + fruits_exotiques
print(fruits) # ["pomme","poire","prunes","cerise","banane","ananas","mangue"]
```

On pourra également utiliser la méthode `append()`
**Syntaxe** : `list.append(element)`
```python
fruits = []
fruits_locaux = ["pomme","poire","prunes","cerise"]
fruits_exotiques = ["banane","ananas","mangue"]
fruits.append(fruits_locaux)
fruits.append(fruits_exotiques)
print(fruits) # ["pomme","poire","prunes","cerise","banane","ananas","mangue"]
```

### Ajouter un élément n'importe où dans une liste
Pour ajouter un élément à une position déterminée dans une liste; on aura besoin :
- de l'indice où l'on veut ajouter l'élément
- de l'élément à ajouter à cet indice
On utilisera pour cela la méthode `insert()`
**Syntaxe** : `list.insert(index,element)`
```python
capitales = ["Rome","Bruxelles","Berlin","Madrid"]
# Ajouter 'Paris' entre Bruxelles et Berlin... çàd, à l'indice 2
capitales.insert(2,"Paris")
print(capitales)
```

## Supprimer un élément dans une liste
Pour supprimer un élément dans une liste, on utilisera la méthode `remove()`
**Syntaxe** : `list.remove(element)`
La méthode `remove()` :
- Si l'élément existe : supprimera la première occurrence de l'élément passé en argument
- Si l'élément n'existe pas : renvoie une erreur de type `ValueError`
```python
capitales_europeennes = ["Rome","Berlin","Madrid","Lisbonne","Londres","Dublin"]
# ... oups, le Royaume Uni ne fait plus partie de l'Union Européenne
capitales_europeennes.remove("Londres")
print(capitales_europeennes)
```

## Trier les éléments d'une liste
### Si l'on accepte que la liste soit modifiée en place : sort()
Pour trier les éléments d'une liste, on peut utiliser la méthode `sort()`.
**Attn** : la liste est alors modifiée; et l'ordre initial des éléments est alors perdu !
**Rem** : de plus, la méthode renvoie la valeur `None`... et non la liste triée ! 
**Syntaxe** : `list.sort()`
- Tri ascendant : c'est le comportement par défaut.
- Tri descendant : on passera alors l'argument `reverse = True` à la méthode.

```python
prenoms = ["Zoé", "Isidore", "Blaise", "Thomas"]
# Trie la liste par ordre 'ascendant'
prenoms.sort()  # Trie la liste, et renvoie `None`
print(prenoms.sort()) # Affiche 'None'
print(prenoms)        # Affiche ["Blaise", "Isidore", "Thomas", "Zoé"]
# Trie la liste par ordre 'descendant'
prenoms.sort(reverse = True) # Trie la liste, et renvoie 'None'
print(prenoms.sort(reverse = True)) # Affiche 'None'
print(prenoms)        # Affiche ["Zoé", "Thomas", "Isidore", "Blaise"]
```

### Si l'on n'accepte pas que la liste soit modifiée : sorted()
Pour trier les éléments d'une liste, on peut également utiliser la fonction `sorted()`
**Rem** : 
- `sort()`, est une <u>méthode</u> qui s'applique à la liste; et modifie celle-ci.
- `sorted()`, est une <u>fonction</u> qui prendre la liste en argument et renvoie celle-ci triée; sans modifier cette dernière !
**Syntaxe** : `sorted(list)`

```python
prenoms = ["Zoé", "Isidore", "Blaise", "Thomas"]
sorted(prenoms) # Renvoie la liste triée : ["Blaise", "Isidore", "Thomas", "Zoé"]
print(sorted(prenoms)) # Affiche : ["Blaise", "Isidore", "Thomas", "Zoé"]
print(prenoms) # Affiche la liste initale (non triée); celle-ci n'ayant pas été modifiée.
sorted(prenoms, reverse = True) # Renvoie la liste triée en ordre inverse
print(sorted(prenoms, reverse = True)) # ["Zoé", "Thomas", "Isidore", "Blaise"]
print(prenoms) # la liste initiale n'a pas été modifiée.
```
