#description Cette fiche traitera du type de données "Chaîne de caractères" ('String', en anglais).

# Le type 'String' : str

Le type String représente l'ensemble des chaînes de caractères.
#def Une chaîne de caractères est définie comme une **séquence caractères**; c'est à dire, une collection finie d'éléments (ici, de caractères) qui se suivent dans un ordre donné.
#def Un caractère en Python, est une chaîne de caractère de longeur 1 !
## Ensemble des valeurs :
L'ensemble des chaînes de caractères !

Exemples : 
```python
""                     # La chaîne vide
" "                    # La chaîne qui contient le caractère d'espacement
"C'est la rentrée : je suis super content ! 😀 "
```

**Rem** : l'on notera dans les exemples ci-dessus, que les chaînes de caractères ne se composent pas uniquement de caractères alphabétiques; mais peuvent également contenir des symboles mathématiques, des émojis, etc...

## Comment construire une chaîne de caractères ?
### Délimiteurs de chaîne
Pour indiquer le début et la fin d'une chaîne de caractères; on pourra utiliser :
- des guillemets simples : `' '`
- des guillemets doubles : `" "`
- ou triples doubles guillemets : `"""  """`

**Rem** : le principe des délimiteurs est que le langage reconnaisse comme étant une chaîne de caractères, tout ce qui suit un délimiteur; et s'arrête dès qu'il voit le même délimiteur apparaître à nouveau.

**Attn** : le problème se pose lorsque, au sein de la chaîne, on doit insérer un caractère identique à celui qui sert de délimiteur (cf. exemples ci-dessous).  
Il faut alors l'*échapper* (*escape*, en anglais).  Ceci se fait en faisant précéder le caractère par le symbole `\` (backslash).   
#### Les guillemets simple : `' '`

```python
''                       # La chaîne vide
'Un montre alien : 👾' 
'C\'est la rentrée : je suis super content ! 😀 '
'Une citation : "cogito ergo sum"'
```
#### Les guillemets doubles : `" "`

```python
""                     # La chaîne vide
"C'est la rentrée : je suis super content ! 😀 "
"Une citation : \"cogito ergo sum\""
"Une citation : 'cogito ergo sum'"
```

#### Les guillemets triples : `"""  """`

```python
"""L'intérêt des guillemets triples, est de n'avoir pas
à 'échapper' les guillemets simple : '', ni doubles : "" 
quand ils apparaissent dans une chaîne de caractères.
Mais également de pouvoir entrer un texte de plusieurs lignes
sans devoir utiliser le caractère d'échappement \\n 
à la fin de chaque ligne pour notifier que l'on commence 
une nouvelle ligne !"""
```

### Echappement de caractères
L'échappement de caractères est la technique qui consiste à changer la signification que peut avoir un caractère dans une chaîne.  Deux cas de figure peuvent se présenter :
- Soit le caractère doit être interprété comme un caractère (mais il est interprété comme une commande). 
	- C'est notamment le cas lorsque des guillemets du même type que les délimiteurs de la chaîne sont utilisés au sein de la chaîne.  Python risque alors d'interpréter ceux-ci comme un marqueur de fin de chaîne; alors que l'on voudrait simplement les considérer comme des guillemets.
	- On placera dans ce cas, le symbole `\` (backslash) devant le guillemet pour indiquer que celui-ci doit être interprété comme caractère et non comme marqueur de fin de chaîne.
- Soit le caractère doit être interprété comme une commande (mais il est interprété comme un caractère).
	- `\n` : indique un retour à la ligne 
	- `\t` : indique une tabulation

## Opérations définies sur ces valeurs :
### ~~Les opérations 'logiques'~~
Opérateurs logiques : `and`, `or`, `not`

**Rem** : les opérations logiques fonctionnent également sur le type 'string'; mais sont fort peu utilisées dans la pratique.  Elles sont mentionnées dans ce cours, par soucis de complétude; et ne sont pas à connaître pour les types autres que 'booléens'.
### ~~Les opérations 'arithmétiques'~~
Les opérations arithmétiques ne s'appliquent pas aux chaînes de caractère.
### Les opérations 'relationnelles'
Opérateurs relationnels : `<`,`<=`, `>`, `>=`

Les chaînes de caractère (str) étant un type de séquence; les opérateurs relationnels fonctionnent ici sur le même principe que pour toutes les séquences; à savoir :
- On compare les éléments de la chaîne (ici, les caractères) :
	- un à un
	- dans l'ordre (de leur position dans la chaîne : leur indice)
- **Rem** : la valeur utilisée pour déterminer si un caractère est plus petit qu'un autre; est celle de son 'code point' Unicode (un code numérique unique associé à chaque caractère). 

| Operateur | Description       | Exemple        | Résultat |
| --------- | ----------------- | -------------- | -------- |
| `>`       | Inférieur (ordre) | 'abc' < 'def'  | True     |
| `<`       | Supérieur (ordre) | 'xyz' > 'abc'  | True     |
| `<=`      | Inférieur ou égal | 'abc' <= 'abc' | True     |
| `>=`      | Supérieur ou égal | 'abc' <= 'abb' | False    |

### Les opérations d'inclusion
Opérateurs d'inclusion : `in`, `not in`

Les opérateurs d'inclusions vérifient si un élément est présent ou non dans une séquence.
Or, les chaînes de caractères sont des séquences de caractères.

Les opérateurs d'inclusion pour les chaînes, vérifient donc si un élément est présent ou absent dans une chaîne de caractères.
**Rem** : cet élément est lui-même une chaîne de caractères de taille quelconque ! 

| Opérateur | Opération               | Résultat                                                      |
| --------- | ----------------------- | ------------------------------------------------------------- |
| `in`      | element `in` chaine     | `True` si l'element est dans la chaîne<br>`False` sinon       |
| `not in`  | element `not in` chaine | `True` si l'élement n'est pas dans la chaîne<br>`False` sinon |
```python
'b' in 'bonjour'        # True
'b' not in 'bonjour'    # False 
'pluie' in "il fait gris, et il y a de la pluie aujourd'hui"  # True 
'vent' in "il fait gris, et il y a de la pluie aujourd'hui"   # False
```

### Les opérations de tranchage (slicing)

| Syntax         | Description                                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s[start:end]` | Retourne une sous-séquence comprise entre l'indice `start` et l'indice `end-1`<br>Note : on ne retourne donc pas l'élément situé à l'indice `end` |
Comme les *chaînes de caractères* sont des séquences; les opérations de tranchage s'appliquent donc à celles-ci.

**Rappel** : l'indice du premier élément dans une séquence est égal à `0`

```python
origine_python = "Python a été créé par Guido Van Rossum"
origine_python[22:27]    # 'Guido'  
```
**Rappel** : on retourne la sous-séquence jusqu'à l'indice `end` **non compris** !

**Rem** : on peut omettre les valeurs d'indices pour `start` et/ou `end`
- Si l'on omet `start` : Python utilisera par défaut le premier indice.
- Si l'on omet `end` : Python utilisera par défaut le dernier indice

```python
alphabet = "abcdefghijklomnopqrstuvwxyz"
alphabet[7:] # 'hijklomnopqrstuvwxyz' (end = len(alphabet))
alphabet[:7] # 'abcdefg' (start = 0).
```

| Syntax              | Description                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `s[start:end:step]` | Retourne une sous-séquence comprise entre l'indice `start` et l'indice `end-1`; en prenant les éléments tous les `step` pas. |
**Attn** : si l'on utilise des `steps` (pas) négatifs; comme l'on parcourt la chaîne à l'envers; s'assurer que l'indice correspondant à `start` soit **strictement plus grand (>)**  que l'indice correspondant à `end`

```python
abcd = "abcd, efgh, ijkl, mnop, qrst, uvwx, yz"
abcd[::3]      # 'adehilmpqtuxy'
abcd[6:25:-2]  # vide... car on parcours à l'envers => start doit être > end !
abcd[25:6:-2]  # 'r pn lj hf'  
```

### Quelques fonctions sur les chaînes
`.lower()` : convertit une chaîne en minuscules
`.upper()` : convertit une chaîne en majuscules





