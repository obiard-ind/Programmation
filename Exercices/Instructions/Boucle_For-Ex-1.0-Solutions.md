**Consigne** : tous exercices ci-dessous sont à réaliser en utilisant une boucle `for`

# Exercices simples : 
- Affichez les nombres de 1 à 10
```python
for i in range(1,11):
    print(i)
```
- Idem, mais affichez les sur une même ligne, à l'aide de tabulations
```python
for i in range(1,11):
    print(i,end="\t")
```
- Affichez les multiples de 2 compris dans l'intervalle \[-20, 20\]
```python
for i in range(-20,21):
    if i%2 == 0:
        print(i)
```
- Soit la chaîne `"L'imagination est plus forte que la science."` (A. Einstein).
  Affichez, sur une même ligne, un caractère sur 2 !
```python
phrase = "L'imagination est plus forte que la science."
index = 0

for lettre in phrase:
    if index % 2 == 0:
        print(lettre,end="")
    index+=1
```
- Demandez à l'utilisateur d'introduire un nombre entier; et et calculez la somme des nombres allant de `0` au nombre introduit.
  Exemple : pour le nombre `8`, on fera la somme de 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
```python
nombre = int(input("Veuillez introduire un nombre entier : "))
somme = 0

for i in range(nombre+1):
    somme += i
print(f"La somme des nombre allant de 0 à {nombre} vaut {somme}")
```

# Exercices plus complets 

## Comptage du nombre de mot d'une phrase
- Comptez le nombre de mots que contient la phrase suivante :
  `"Le contraire de la liberté, c'est d'être prisonnier des préjugés du sens commun, des croyances de son temps et de son pays, et de l'habitude" (Bertrand Russel)`
- Complétez la solution en affichant chaque mot reconnu sur une ligne séparée.
#### Solution :
```python
phrase = "Le contraire de la liberté, c'est d'être prisonnier des préjugés du sens commun, des croyances de son temps et de son pays, et de l'habitude."
alphabet_min = "abcdefghijklmnopqrstuvwxyz"
alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_diacritiques = "éèêïàç"
alphabet_total = alphabet_min + alphabet_maj + caracteres_diacritiques
nb_word = 0
new_word = False
mot = ''

for lettre in phrase:
    if lettre not in (alphabet_total):
        if new_word == True:   # Pour ne pas répéter l'affichage du mot si plusieurs symboles n'appartenant pas à l'alphabet, se suivent.
            print(mot)
            new_word = False
        continue
    if new_word == False:
        new_word = True
        mot = ''
        nb_word += 1
    mot = mot + lettre

print(f"La phrase : {phrase} \n.  Cette phrase contient {nb_word} mots !")
```

## Création d'une table de multiplication

- Créez une grille de `m x n` cases
- A l'intérieur de chacune de ces cases, affichez le nombre correspondant à la multiplication du numéro de la ligne par celui de la colonne. 
  Remarque :
	- On commencera la numérotation des lignes à la valeur `1`
	- La taille des colonnes sera  fixée à 5 caractères
  Exemple de résultat attendu : 
  ![[TableMultiplication-Ex.png]]

#### Solution :
```python
COL_SIZE = 5

nb_ligne = int(input("Veuillez entrer le nombre de lignes : "))
nb_col = int(input("Veuillez entrer le nombre de colonnes : "))
ligne_sep = ("-" * COL_SIZE * nb_col) + ("-" * (nb_col + 1))  
  
for i in range(1, nb_ligne + 1):
    print(ligne_sep)
    ligne = "|"
    for j in range(1, nb_col + 1):
        ligne += f"{i * j:^{COL_SIZE}}|"
    print(ligne)

print(ligne_sep)
```

