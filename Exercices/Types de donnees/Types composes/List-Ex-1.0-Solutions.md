
# Exercices pour commencer :
- Créez une liste constituée des prénoms des élèves de la classe.  Appelez celle-ci `prenoms` !
`prenoms = ["Sylvie", "Antoine", "Nicolas", "Thomas", "Robert", "Hubert", "Jonas"]
- Affichez celle-ci, à raison d'un prénom par ligne
  Tip : utilisez pour ce faire une boucle `for`
```python
for prenom in prenoms:
    print prenom
```
- Accédez au 5ème prénom de la liste.
`prenoms[4]`
- Ajoutez aux positions indiquées, les prénoms suivants  :
	- en début de liste : `Zoé`
`prenoms.insert(0,"Zoé")`
	- à la 4ème position : `Ignace`
`prenoms.insert(3,"Ignace")`
	- à la 7ème position : `Isidore`
`prenoms.insert(6, "Isidore")`
	- à la dernière position : `Alexandre`
`prenoms.append("Alexandre")`
- Créez une nouvelle liste, appelée `prenoms_grecs` , et composée des prénoms suivants : "Miltiade", "Thémistocle", "Périclès", "Thucydide"
```python
prenoms_grecs = 
```
- Ajoutez cette liste à la précédente (celle qui contient les prénoms des élèves de la classe)
- Dans la liste `prenoms` ainsi augmentée, récupérez l'index de la position occupée par "Thémistocle".
- Quelle est la taille de cette nouvelle liste ?
- Supprimez "Miltiade" de la liste.
- Supprimez "Ignace"
- Créez une nouvelle liste de prénoms, appelée `prenoms1` , qui contiendra les prénoms de la liste `prenoms` compris entre les indices 3 et 7.
- Créez une nouvelle liste de prénoms, appelée `prenoms2`, qui contiendra les prénoms de la liste `prenoms` à partir du deuxième prénom, jusqu'à la fin de la liste.
- Supprimez de la liste `prenoms` tous les prénoms qui contiennent la lettre `i` (en majuscule ou minuscule)
  Tip : pour ce faire, vous pouvez utiliser la méthode `lower()` ou `upper()` sur les chaînes de caractères.
- Créez une liste `capitales_ue`, des noms des capitales des pays de l'Union Européenne. 
- Affichez cette liste, par nom croissant, mais sans en modifier le contenu.
- Triez cette liste (en en réorganisant le contenu), par nom croissant, puis affichez le résultat.  
- Créez une liste `capitales_ue_mediterranée`, des capitales des pays de l'UE qui bordent la mer Méditerranée.
- Supprimez de la liste des capitales des pays de l'UE, ceux de la liste des pays qui bordent la Méditerranée.

# Exercices pour s'entraîner
## Création d'un 'menu utilisateur'
**Description de la tâche** : L'exercice suivant consistera à créer, afficher, ajouter et supprimer des éléments à un menu à l'aide d'une liste.

Au départ, le menu contiendra uniquement les entrées suivantes : 
```
0. Quitter ce menu
1. Ajouter une nouvelle entrée
2. Supprimez une entrée 
```

- Lorsque l'utilisateur appuiera sur le chiffre `1` :  le menu sera affiché sous la forme suivante 
  (se référer à l'exemple ci-dessus pour une illustration)
```
=============== Menu de l'utilisateur ===============
<numéro entrée>. <Description de l'entrée>
```

- Lorsque l'utilisateur appuiera sur le chiffre `1` : il lui sera demandé d'ajouter une nouvelle entrée au menu.  Celle-ci sera ajouté à la suite des options de menus existantes.
- Lorsque l'utilisateur appuiera sur le chiffre `2` : il lui sera demandé quelle entrée de menu il souhaite supprimer, en indiquant le numéro de l'entrée à supprimer.
  **Rem** : il ne doit pas pouvoir être autorisé à supprimer les entrées initiales (numérotation de 0 à 2); uniquement celles qu'il aura ajoutées lui-même !
- Lorsque l'utilisateur appuiera sur un chiffre correspondant à une entrée qu'il aura lui-même créée, le message suivant sera affiché :
  `Vous êtes dans le menu <numéro entrée> : <Description de l'entrée>`

## Gestion d'un dictionnaire
**Description de la tâche** : L'objectif de cet exercice est la création et la gestion d'un dictionnaire de mots et de définitions à l'aide de listes.

**Tip** : utilisation de deux listes synchronisées (au travers de la gestion de leurs indices).

On utilisera le menu réalisé précédemment pour afficher les tâches suivantes :
```
0. Quitter ce menu
1. Affichez la liste de tous les mots
2. Affichez la liste des mots commençant par une lettre donnée 
3. Affichez la définition d'un mot
4. Ajoutez un nouveau mot et sa définition dans la liste
5. Modifiez la définition d'un mot
6. Supprimez un mot de la liste
```

Pour chaque entrée, on implémentera l'action correspondante.
# Exercices pour se dépasser
## Gestion d'une liste de tâches
**Description de la tâche** : créer et gérer une liste de tâches.

**Tip** : on utilisera des listes imbriquées; à savoir : 
- une liste principale qui contient les tâches
- chaque tâche étant décrite par une liste

Toujours en utilisant le menu réalisé précédemment; on utilisera celui-ci pour afficher les entrées suivantes :
```
0. Quitter le menu
1. Créer une nouvelle tâche
2. Afficher la liste des tâches
3. Afficher les tâches actives
4. Afficher les tâches terminées
5. Afficher les tâches comprises entre deux dates au format (yyyy-mm-dd)
6. Modifiez une tâche existante
7. Supprimez une tâche de la liste
```

Pour l'entrée `6. Modifiez une tâche existante`, on affichera le sous-menu suivant :
```
0. Quitter le sous-menu
1. Modifier la date
2. Modifier l'heure
3. Modifier le statut (actif / terminé )
4. Modifier le nom de la tâche
5. Modifier la description de la tâche
```

