## Objectif
Les petits exercices suivants ont pour but de vous entraîner à la manipulation de listes; à l'utilisation de boucles, de structures conditionnelles et d'expressions boolénnes.
## Exercices
#### Ex1 : Liste de fruits
Créez un petit programme qui demande à l'utilisateur d'entrer 10 noms de fruits dans une liste.
Affichez ensuite cette liste.

```python
fruits = []
i = 0
while ( i <10 ):
    fruit = input("Entrez le nom du fruit à ajouter à la liste : ")
    fruits += [fruit]
    i += 1

print()
print("Voici la liste des fruits que vous avez ajoutés à votre panier : ")
for fruit in fruits:
    print(fruit)
```

#### Ex2 : Encodage de notes d'élèves
En vous aidant de 2 listes; créez un petit programme qui va enregistrer les notes des élèves. 
Vous utiliserez une boucle `while` qui continuera de demander à l'utilisateur le prénom et la note de l'élève.  La boucle sera répétée tant que l'utilisateur indiquera son intention de continuer en tapant validant son choix par 'o' ou 'O' (signifiant : 'oui').
Affichez ensuite la liste des élèves et leur note (un élève et sa note sur une ligne.)
```python
# Initialisation des variables
eleves = []
notes = []
continuer = "o"
# Encodage des élèves et des notes 
while (continuer.lower() == "o"):
    eleve = input("Entrez le prénom de l'élève : ")
    note = int(input("Entrez la note de l'élève : "))
    eleves.append(eleve)
    notes.append(note)
    continuer = input("Avez-vous encore un élève et sa note à ajouter ? [O/N] : ")
    
# Affichage des élèves et de la note associée 
print("Liste des élèves et de leurs points")
for i in range(len(eleves)):
    print(f"L'élève : {eleves[i]} a obtenu la note de {notes[i]}")
```
##### Ex2.1 : moyenne des notes
Reprenez votre exercice précédent; et calculez à présent la moyenne des notes des élèves.
Affichez cette moyenne après la liste des notes par élève.
```python
# Ajoutez ce code à la suite de celui de l'exercice précédent.
# Calcul de la moyenne des notes.
somme = 0    # Variable contenant la somme des notes
i = 0        # Compteur du nombre de notes
for note in notes:
    somme += note
    i+=1
print("La moyenne des notes vaut : ", "{:.2f}".format(somme / i))
```

#### Ex3 : Menu de manipulation de chaînes de caractères
Demandez à l'utilisateur d'introduire une chaîne de caractères.
Proposez-lui ensuite un menu pour réaliser quelques manipulations sur les chaînes, comme nous les avons vues à l'aide de l'opérateur de tranchage (slicing), à l'aide des doubles crochets : `[]`.
Ce menu se composera des opérations suivantes :
```
1. Renvoyer le caractère à une position donnée
2. Renvoyer une sous-chaine comprise entre 2 indices
3. Renvoyer la chaîne inversée 
```
Quand l'utilisateur entrera le chiffre correspondant à un entrée du menu; celle-ci sera exécutée.
##### Solution : 

```python
"""
Demandez à l'utilisateur d'introduire une chaîne de caractères.
Proposez-lui ensuite un menu pour réaliser quelques manipulations sur les chaînes,
comme nous les avons vues à l'aide de l'opérateur de tranchage (slicing), à l'aide des doubles crochets : `[]`.
Ce menu se composera des opérations suivantes :

1. Renvoyer le caractère à une position donnée
2. Renvoyer une sous-chaine comprise entre 2 indices
3. Renvoyer la chaîne inversée 
"""
# Initialise la variable menu à l'aide des entrées souhaitées.
menu = ["1. Renvoyer le caractère à une position donnée",
        "2. Renvoyer une sous-chaîne comprise entre deux indices",
        "3. Renvoyer la chaîne inversée"]
# Demande à l'utilisateur d'introduire la chaîne de caractères à manipuler.
chaine = input("Veuillez introduire une chaîne de caractères : \n")

# Affiche le menu 
print("===== Menu de manipulation de chaînes de caractères =====")
for entree in menu:
    print(entree)

# Demande à l'utilisateur de sélectionner son choix à l'aide du numéro de menu
choix = int(input("Veuillez faire votre choix parmi les options de menu [1,2,3] :"))

# Teste le choix de l'utilisateur et réalise l'option demandée.
if choix == 1:
    start = int(input(f"Veuillez introduire l'indice du caractère à renvoyer; entre 0 et {len(chaine)} : "))
    if 0 <= start <= len(chaine):
        print(chaine[start])
    else:
        print(f"Erreur : l'indice doit être compris entre 0 et {len(chaine)} ")
elif choix == 2:
    start = int(input(f"Veuillez introduire la position de départ; entre 0 et {len(chaine)} : "))
    end = int(input(f"Veuillez introduire la position de fin; entre {start+1} et {len(chaine)} : "))
    if 0 <= start < end <= len(chaine):
        print(chaine[start:end])
    else:
        print(f"Erreur dans le choix des bornes (start = {start}, end = {end})")
elif choix == 3:
    print(chaine[::-1])
else:
    print(f"Votre choix de menu : {choix} est incorrect ! Doit être 1 ou 2 ou 3.")
```

##### Ex3.1 : Idem, mais dans une boucle
Reprenez l'exercice précédent; et ajoutez une nouvelle entrée dans le menu
`0. Quittez cette application`
Désormais, le menu devra être proposé à l'utilisateur tant que l'utilisateur n'aura pas tapé `0`.
Rem : la chaîne de caractère n'est demandée qu'une fois; et le menu s'applique toujours à cette même chaîne.
##### Solution : 

```python
"""
Reprenez l'exercice précédent; et ajoutez une nouvelle entrée dans le menu
`0. Quittez cette application`
Désormais, le menu devra être proposé à l'utilisateur tant que l'utilisateur n'aura pas tapé `0`.
Rem : la chaîne de caractère n'est demandée qu'une fois; et le menu s'applique toujours à cette même chaîne.
"""
# Initialise la variable menu à l'aide des entrées souhaitées.
menu = ["0. Quittez cette application",
        "1. Renvoyer le caractère à une position donnée",
        "2. Renvoyer une sous-chaîne comprise entre deux indices",
        "3. Renvoyer la chaîne inversée"]
# Initialise la variable indiquant si l'on exécute la boucle ou non.
continuer = True
# Demande à l'utilisateur d'introduire la chaîne de caractères à manipuler.
chaine = input("Veuillez introduire une chaîne de caractères : \n")

while (continuer == True):
    # Affiche le menu 
    print("===== Menu de manipulation de chaînes de caractères =====")
    for entree in menu:
        print(entree)

    # Demande à l'utilisateur de sélectionner son choix à l'aide du numéro de menu
    choix = int(input("Veuillez faire votre choix parmi les options de menu [0,1,2,3] : "))

    # Teste le choix de l'utilisateur et réalise l'option demandée.
    if choix == 0:
        continuer = False
    elif choix == 1:
        start = int(input(f"Veuillez introduire l'indice du caractère à renvoyer; entre 0 et {len(chaine)} : "))
        if 0 <= start <= len(chaine)-1:
            print(chaine[start])
        else:
            print(f"Erreur : l'indice doit être compris entre 0 et {len(chaine)} ")
    elif choix == 2:
        start = int(input(f"Veuillez introduire la position de départ; entre 0 et {len(chaine)} : "))
        end = int(input(f"Veuillez introduire la position de fin; entre {start+1} et {len(chaine)} : "))
        if 0 <= start < end <= len(chaine):
            print(chaine[start:end])
        else:
            print(f"Erreur dans le choix des bornes (start = {start}, end = {end})")
    elif choix == 3:
        print(chaine[::-1])
    else:
        print(f"Votre choix de menu : {choix} est incorrect ! Doit être 0, 1, 2 ou 3.")
```

##### Ex3.2 : Idem, mais avec une nouvelle chaîne
Reprenez l'exercice précédent; mais cette fois ajoutez une nouvelle entrée de menu proposant de changer la chaîne de caractère à tester.
`4. Changer de chaîne de caractères`

##### Solution :

```
Même principe qu'à l'exercice précédent; dans lequel :
- A l'extérieur de la boucle : on initialisera la variable 'chaine' à "" (chaîne vide).
- on ajoutera la nouvelle entrée dans la liste 'menu'
- on testera la condition `4`; et si elle est vérifiée : on demandera à l'utilisateur d'affecter une nouvelle chaine de caractères à la variable chaîne définie précédemment.
```










