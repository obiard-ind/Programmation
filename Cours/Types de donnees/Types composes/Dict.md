#description Cette fiche traitera du type de données 'Dictionnaire'.

# Le type 'dictionnaire' (dict)
#def un **dictionnaire** est une collection de paires de la forme `clé:valeur`

**Rem** : contrairement aux séquences (string, list, tuple, range) dont on accède aux éléments par leur indice (leur position dans la séquence); on accède aux valeurs d'un dictionnaire par leurs *clés* respectives.  Les *dictionnaires* en Python ne sont donc pas considérés comme des séquences d'éléments.  On parlera plutôt de *mapping* ; car il font correspondre une clé à une valeur.

## Propriétés des dictionnaires en Python
- **Les clés doivent être uniques** : les clés servent à accéder à la valeur associée.  Il ne peut donc y avoir deux clés identiques dans un dictionnaire.
  **Attention** : les clés sont *case-sensitive* (sensibles à la 'casse') ! Il faudra veiller à ce que le nom lors de l'utilisation corresponde à celui utilisé lors de la déclaration. 
- **Types autorisés**
	- **pour les clés** : il soit s'agir d'un type *immutable* ! On utilisera en général un type `string` ou `int`.
	- **pour les valeurs** : n'importe quel type est autorisé (booléen, entier, string, liste, dictionnaire, objet,...) 
- **Mutable** : on peut ajouter, modifier, et supprimer les éléments d'un dictionnaire.

## Déclaration / Comment créer un dictionnaire :
- un dictionnaire sera délimité par des accolades '{ }', dont les paires `clé:valeur` seront séparées par des **virgules**.
- Exemple :
```python
resultats = {'Alexandre':18,'Sylvie':17,'Frédéric':12,'Stéphane':14}
utilisateur1 = {
    'nom': "Duchemin",
    'prenom': "Jacques",
    'age':25
    'ville' : "Bruxelles"
    }
utilisateur2 = {
    'nom':"Dubois",
    'prenom': "Sylvain",
    'age':17,
    'ville' : "Charleroi"
    }
print(resultats)
print(utilisateur1['prenom'])
print(utilisateur2['age'])
```

**Tip** : Lorsque la déclaration du dictionnaire dépasse la longueur de la ligne; il est recommandé, pour la lisibilité, de placer chaque élément (paire `clé:valeur`) sur sa propre ligne.

### Comment ajouter une nouvelle entrée dans un dictionnaire ?
Pour ajouter une nouvelle paire `clé:valeur` dans un dictonnaire; il suffira de préciser la clé que l'on souhaite utiliser et la valeur à lui affecter.

```python
resultats = {'Alexandre':18,'Sylvie':17,'Frédéric':12,'Stéphane':14}
# Pour ajouter une nouvelle note d'élève dans le dictionnaire des résultats
resultats['Bruno'] = 11
resultats['Sylvie'] = 14
print(resultats) 
# {'Alexandre':18,'Sylvie':17,'Frédéric':12,'Stéphane':14, 'Bruno':11}
print(resultats['Sylvie'])   # 14
```

**Attn** : si la clé existe déjà dans le dictionnaire; la nouvelle valeur écrasera l'ancienne !

On testera alors si la clé existe; et on en informera l'utilisateur le cas échéant !
```python
resultats = {'Alexandre':18,'Sylvie':17,'Frédéric':12,'Stéphane':14}
prenom_eleve = input("Introduisez le prénom de l'élève : ")
points_eleve = input("Introduisez ses points /20 : ")
if prenom_eleve in resultats:
    print(f"{prenom_eleve} existe déjà dans le dictionnaire")
else:
    resultats[prenom_eleve] = points_eleve

print(resultats)
```


## Comment accéder à une valeur dans un dictionnaire ?
Comme les dictionnaires établissent un *mapping* (une correspondance) entre une **clé** (unique) et une **valeur**; on accèdera à la valeur en utilisant sa **clé**.
### Soit : à l'aide des crochets : `[]`
Ceci s'effectue grâce aux crochets : `[]`; de la même façon qu'on l'aurait fait pour une type de séquence.  Sauf qu'ici, on remplacera l'indice de l'élément par la valeur de la clé.

```Python
resultats = {'alexandre':18,'sylvie':17,'frédéric':12,'Stéphane':14}
voiture_luxe = {
    'marque': "Rolls-Royce"
    'modèle': "Black Badge",
    'moteur': "V12 bi-turbo",
    'puissance': "600 ch"
    'poids' : "2.4 tonnes"
}
pays_capitale = {
    'Belgique': "Bruxelles",
    'France': "Paris",
    'Espagne': "Madrid",
    'Thaïlande': "Bangkok"
}

pays_capitale['Thaïlande']    # "Bangkok"
voiture_luxe['moteur']        # "V12 bi-turbo"
resultats['Stéphane']         # 14

# Et si la clé que l'on utilise n'existe pas ?
pays_capitale['Brésil']       # KeyError : 'Brésil'
```

**Rem** : avec les crochets; si la clé que l'on veut utiliser n'existe pas dans le dictionnaire; une **erreur** de type `KeyError` sera levée et l'exécution du programme s'arrêtera !
### Soit : à l'aide de la méthode `.get()`
On pourra également utiliser la méthode `.get()`, en passant en argument la valeur de la clé correspondant à la valeur que l'on veut récupérer.

*En se basant sur les dictionnaires de l'exemple précédent* 
```python
pays_capitale.get('Thaïlande')  # "Bangkok"  
voiture_luxe.get('moteur')      # "V12 bi-turbo"
resultats.get('Stéphane')       # 14

# Et si la clé que l'on utilise n'existe pas ?
pays_capitale.get('Brésil')     # None
```

**Rem** : avec la méthode `.get()`; si la clé que l'on veut utiliser n'existe pas dans le dictionnaire; la valeur `None` sera renvoyée et le programme continuera son exécution !

### Alors : les crochets `[]` ou la méthode `.get()` ?
Cela dépend ! 
- S'il est important que le programme ne permette pas d'accéder à une clé qui n'existe pas; alors la méthode utilisant les crochets semble préférable.
- S'il est plus important que le programme continuer de fonctionner; alors on préférera la méthode `.get()`
Dans les deux cas, il est important de **notifier le problème à l'utilisateur** !
Ceci peut se faire :
- Dans le cas où une erreur est levée : en <u>capturant l'exception</u> !
  On verra comment faire cela plus tard #todo 
- Dans le cas où une valeur None est renvoyée : en <u>testant la valeur de retour de la méthode</u> !

*Exemple : test de la valeur de retour de la méthode*
```python
pays_capitale = {
    'Belgique': "Bruxelles",
    'France': "Paris",
    'Espagne': "Madrid",
    'Thaïlande': "Bangkok"
}

pays = input("De quel pays voulez-vous connaître la capitale ? ")
if (pays_capitale.get(pays) is None):
    print("Il n'existe aucune entrée pour ce pays dans notre dictionnaire !")
else:
    print("La capitale de ",pays," est ",pays_capitale[pays])
```

## Comment mettre à jour la valeur associée à une clé ?
Il suffira d'affecter cette valeur à l'élément du dictionnaire identifié par la clé !

```python
utilisateur1 = {
    'nom': "Duchemin",
    'prenom': "Jacques",
    'age':25
    'ville' : "Bruxelles"
}
# Mise à jour de la ville
utilisateur1['ville']= "Namur"
```

## Comment supprimer une clé (et sa valeur associée) ?
Supprimer une clé, supprimera également de facto la valeur qui y est associée.

### Soit : à l'aide du mot clé `del`
**Syntaxe** : `del nom_dictionnaire[nom_clé]`

Résultat de l'exécution :
- En cas de réussite (çad : si la clé existe) : ne renvoie rien, se contente juste de supprimer l'entrée correspondante.
- En cas d'échec (çad : si la clé n'existe pas) : lève une exception de type `KeyError` et provoque l'arrêt du programme.

*Reprenons l'exemple des résultats d'élèves
```python
resultats = {
    'Alexandre':18,
    'Sylvie':17,
    'Frédéric':12,
    'Stéphane':14
}
# Supprimons l'entrée associée à Frédéric
del resultats['Frédéric']
del resultats['Annette']    # Lève une Exception... KeyError : 'Annette'
# Affichons à présent le dictionnaire
print(resultats) # {'Alexandre':18,'Sylvie':17,'Stéphane':14}
```

### Soit : à l'aide de la méthode `.pop()`
**Syntaxe 1** : `nom_dictionnaire.pop(nom_clé)`

Résultat de l'exécution :
- En cas de réussite (çad : si la clé existe) : supprime l'entrée **et** renvoie la valeur associée à la clé.
- En cas d'échec (çad : si la clé n'existe pas) : lève une exception de type `KeyError`, comme avec l'utilisation du mot clé `del`.

*Toujours avec l'exemple des résultats d'élèves... que nous ne rédéfinirons pas ici*
```python
# Si la clé existe; supprimera l'entrée ET retournera la valeur associée.
resultat_execution = resultats.pop('Frédéric')
print(resultat_execution)  # 12
# Si la clé n'existe pas, lèvera une erreur de type KeyError 
resultats.pop('Annette')   # KeyError : 'Annette' 
```

**Syntaxe 2** : `nom_dictionnaire.pop(nom_clé, valeur_de_retour)`
Nous pouvons également utiliser la méthode `.pop()` avec un second argument; qui précisera la valeur que nous voulons voir retourner par la méthode en cas d'échec.
**Rem** : cette valeur de retour est un type quelconque : il peut s'agir d'une chaîne de caractère, de la valeur `None`, etc...

Résultat de l'exécution :
- En cas de réussite (çad : si la clé existe) : supprime l'entrée **et** renvoie la valeur associée à la clé.
- En cas d'échec (çad : si la clé n'exsite pas) : renverra la valeur indiquée dans le second argument.

```python
# Si la clé existe; supprimera l'entrée ET retournera la valeur associée.
resultat_execution = resultats.pop('Frédéric',"La clé n'existe pas")
print(resultat_execution)  # 12
# Si la clé n'existe pas, renverra la valeur du deuxième argument.
resultat_execution = resultats.pop('Annette', "La clé n'existe pas")
print(resultat_execution)  # "La clé n'existe pas" 
```

## Les méthodes `.keys()`, `.values() et .items()`
**Syntaxe** : `nom_dictionnaire.keys()`
Renvoie une *vue* des **clés** du dictionnaire
**Syntaxe** : `nom_dictionnaire.values()`
Renvoie une *vue* des **valeurs** du dictionnaire
**Syntaxe** : `nom_dictionnaire.items()`
Renvoie une *vue* sur les paires **clé,valeur** du dictionnaire.

**Attn** : la *vue* dont il est question ici  est un objet spécial qui est présenté sous forme de liste; mais qui n'en est pas une ! Cet objet possède des caractéristiques propres sur lesquelles nous ne nous étendrons pas.  Il est en revanche **itérable**; ce qui signifie que nous pouvons le parcourir à l'aide d'une boucle.

*Soit le dictionnaire suivant : 
```python
pays_capitale = {
    'Belgique': "Bruxelles",
    'France': "Paris",
    'Espagne': "Madrid",
    'Thaïlande': "Bangkok"
}
```

*Parcours des clés du dictionnaire 'pays_capitale'*
```python
for pays in pays_capitale.keys():
    print(pays)
```

*Parcours des valeurs du dictionnaire 'pays_capitale'*
```python
for capitale in pays_capitale.keys():
    print(capitale)
```

*Parcours des paires 'clés:valeur' du dictionnaire 'pays_capitale'*
```python
for pays, capitale in pays_capitale.items():
    print(f"{pays} a pour capitale {capitale}")
```
