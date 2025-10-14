#description Exercices sur les chaînes de caractères.

# Ecriture d'une chaîne de caractères :
Ecrivez les chaines de caractères suivantes; en utilisant pour chacune : les guillemets simples `' '`et les guillemets doubles `" "`

- Chaîne 1 : Bonjour tout le monde
- Chaîne 2 : Qu'est ce qui se passe ? Quel est ce bruit ?
- Chaîne 3 : Il m'a dit : "Regarde !", et puis s'est tu.
# Retours à la ligne
Ecrives la chaine de caractères suivante; en respectant les retours à la ligne.  Utilisez les doubles guillemets `" "` et les triples doubles guillemets `"""   """` pour tester les deux solutions.

- Chaîne 1 :
```
Alan Turing, né le 23 juin 1912 à Londres
et mort le 7 juin 1954
est un mathématicien et cryptologue britannique,
auteur de travaux qui fondent scientifiquement l'informatique.
Il est aussi l'un des pionniers de l'Intelligence artificielle
```

# Acccès aux caractères
Soit une chaîne contenant, dans l'ordre, les 26 lettres de l'alphabet.
En utilisant les indices :
- retournez la dernière lettre de l'alphabet.  Quel est son indice ?
- retournez la première lettre de l'alphabet. Quel est son indice ?
- Quel est l'indice de la lettre 'k' ?
```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

# Opérations relationnelles
A l'aide des opérateurs relationnels : `<`, `<=`, `>`, `>=`
Comparez les chaînes suivantes, afin que le résultat corresponde au booléen indiqué :
- "abc" et "bca" : `True`
- "Zxv" et "Zxv" : `True`
- "dcc" et "cdbbb" : `False`
- "yza" et "zaay" : False
Ordonnez les chaînes suivantes entre elles :
- "ert", "xcv", "vivv", "vviv"
- "kdd", "avb", "abb", "akcj"

# Tests d'appartenance
A l'aide des opérateurs : `in` et `not in`, vérifiez l'inclusion d'une chaîne dans une autre.
Exprimez, dans la chaîne suivante : "John Presper Eckert, John William Mauchly"
- L'appartenance du mot 'Presper' à cette chaîne.
- Est-ce que 'Von Neumann' en fait partie ?
- Est-ce que l'on y retrouve la sous-chaîne 'ke' ?
- Cette chaîne comporte-t'elle une virgule `,` ?
```python
eniac_developpeurs = "John Presper Eckert, John William Mauchly."
```


# Extraire des sous-chaines (slicing)
A l'aide des opération de slicing, extrayez de la phrase suivante :
- Le mot 'Eniac'
- Le mot 'premier'
Toujours avec l'aide de ces opérations :
- Renvoyez la phrase dans son intégralité
- Affichez un caractère sur deux
- Renvoyez la phrase, mais inversée (le premier caractère devient le premier, et le premier devient le dernier)

```python
eniac = "L'Eniac est le premier ordinateur entièrement électronique"
```
