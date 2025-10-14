#description Cette fiche traitera du type de données 'Dictionnaire'.

# Le type 'dictionnaire' (dict)
#def un **dictionnaire** est une collection de paires de la forme `clé:valeur`

## Déclaration :
- un dictionnaire sera délimité par des accolades '{ }', dont les paires `clé:valeur` seront séparées par des **virgules**.
- à l'instar des autres types en Python, on pourra avoir au sein d'un même dictionnaire :
	- des clés de type différent
	- des valeurs de type différent
	Rem : attention toutefois à rester cohérent de façon à maintenir un code compréhensible ! 
- Exemple :
```python
resultats = {"alexandre":18, "sylvie":17, "frédéric":12, "stéphane":14}
utilisateur1 = {"nom":"Duchemin", "prenom": "Jacques", "age":25}
utilisateur2 = {"nom":"Dubois", "prenom": "Sylvain", "age":17}
n_importe_quoi = {"nom":33, 17:"age"}  # syntaxiquement valide, mais                                                        sémantiquement peu compréhensible !!!
print(resultats)
print(utilisateur1["prenom"])
print(n_importe_quoi[17])
```

