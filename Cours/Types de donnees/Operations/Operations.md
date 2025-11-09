#description Le présent chapitre détaillera les opérations à mesure que nous les verrons au cours.

# Quelques définitions

## 'opération' vs 'opérateur' 
On fera la distinction entre :
- #def **opération** : processus consistant à manipuler une donnée, et produisant un résultat.
- #def **opérateur** : le symbole qui représente cette opération.

Exemple :
- L'addition : est l'*opération* consistant à additionner deux nombres, pour en obtenir la somme.  On la représente à l'aide de l'*opérateur* `+` 
## 'opérande'
#def L'**opérande** est la donnée manipulée par l'opérateur
## opérateur 'unaire', 'binaire'
#def Un opérateur **unaire** est un opérateur qui ne prendra qu'un seul opérande.

Exemple :
- L'opérateur `-` , quand il représente l'opération de négation qui consiste à inverser le signe de l'opérande qui est placé à sa droite;  ne prend qu'un seul opérande; il s'agira donc d'un opérateur *unaire*.  (eg. `-7`).
- L'opérateur logique `not`, qui consiste à inverser la valeur de vérité de l'expression placée à sa droite; ne prend lui aussi qu'un seul opérande; et est donc également qualifié d'opérateur *unaire*. (eg. `not True`)

#def Un opérateur **binaire** est un opérateur qui prendra deux opérandes.

Exemple : 
- L'opérateur `*`  réalise l'opération de multiplication qui consiste à multiplier l'opérande situé à gauche, avec l'opérande situé à droite de l'opérateur.  Cet opérateur prend 2 opérandes; il s'agit donc bien d'un opérateur *binaire*.  (eg. `5 * 4`)
- L'opérateur de conjonction logique `and` réalise l'opération qui consiste retourner la valeur `True` si les opérandes situées à gauche et à droite de l'opérateur ont toutes deux `True` comme valeur; et `False` sinon.  Cet opérateur prend 2 opérandes; il s'agit donc bien ici également, d'une opérateur *binaire*. (eg. `True and False)

**Rem** : selon l'*opération* qu'il représente; un même *opérateur* peut jouer les deux rôles : *unaire* ou *binaire* (mais pas les deux en même temps).

Exemple : 
- Nous avons vu ci-dessus que l'opérateur `-` pouvait être utilisé pour représenter l'opération de négation de la valeur de l'opérande situé à sa droite; et était dans ce cas un opérateur *unaire*.
- Mais il peut également, dans le contexte d'une opération de 'différence', ou de 'soustraction' entre deux nombres, être qualifié d'opérateur *binaire*. (eg. `17 - 4`).
## expression
#def une **expression** est une combinaison de valeurs, d'opérateurs, et d'appels de fonction qui, une fois **évaluée** produit une valeur... (et cette valeur possède un *type*)

# Opérations et types de données
Les *opérations* et les *types de données* sont intimement liés; en ce sens que :
- Les *opérations* ne peuvent être réalisées que sur certains *types de données*.
  C'est à dire que le *type* des *opérandes* auquels s'applique un *opérateur* dépend du type d'*opération*.  Concrètement :
	-  toutes les opérations ne sont pas possibles sur tous les types de données.
- Le *type de données* d'une expression détermine les opérations qui peuvent lui être appliquées.

Les *opérations* produisent un résultat, lequel possède un *type* (c'est à dire qu'il fait partie d'un *type de données*).

## Priorité des opérateurs
Comme en mathématiques, il existe une priorité entre les opérateurs; c'est à dire que l'ordre dans lequel les composants d'une expression sont évalués va déterminer le résultat !

```python
3+2*5    # 13 (et non 25, si on lit juste de gauche à droite)
(3+2)*5  # 25
```

Principe :
- Les opérations sont réalisées selon l'ordre de priorité des opérateurs :
  Les opérations de plus grande priorité sont réalisées avant celles de moindre priorité.
- Quand des opérations de même priorité se situent au même niveau; elles sont évaluées de gauche à droite
- **Tip** : en cas d'ambiguïté, utiliser les parenthèses !
  Approche : procéder en étant systématique... 
	- parenthéser une opération à la fois (si l'on veut être prudent)
	- parenthéser les opérations par priorité descendante (commencer par les priorités élevées)
- **Tip** : quand une expression devient trop complexe; on peut la diviser en plusieurs sous-expressions 

### Tableau de priorité des opérateurs :
Les opérateurs sont listés par ordre de priorité décroissante !

| Opérateurs                                                       | Signification                                      |
| ---------------------------------------------------------------- | -------------------------------------------------- |
| `( )`                                                            | Parenthèses                                        |
| **                                                               | Exposant                                           |
| `+X`, `-X`,                                                      | Opérateurs unaires                                 |
| `*`,`/`,`//`,`%`                                                 | Multiplication, division, division entière, modulo |
| `+`, `-`                                                         | Addition, soustraction                             |
| `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparaison, identité, appartenance                |
| `not`                                                            | 'not' (négation) logique                           |
| `and`                                                            | 'et' logique                                       |
| `or`                                                             | 'ou' logique                                       |

# Opérateurs 'logiques'
- **Opérateurs** : `and`, `or`, `not`
- **Type des opérandes** : expression booléenne.
- **Type du résultat** : booléen.

Le résultat des opérations logique peut être calculé au départ de leur *table de vérité*

### Le 'et' logique : **and**
Le résultat de l'évaluation de l'expression est :
- `True` : si  les deux opérandes sont des expressions booléennes qui s'évaluent à `True`
- `False` : sinon

| expr1 | and   | expr2 |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | False |
| False | False | True  |
| False | False | False |

### Le 'ou' logique : **or**
Le résultat de l'évaluation de l'expression est :
- `False` : si les deux opérandes sont des expressions booléennes qui s'évaluent à `False`
- `True` : sinon

| expr1 | or    | expr2 |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | True  | False |
| False | True  | True  |
| False | False | False |
### La 'négation' logique : **not**
Le résultat de l'évaluation de l'expression est :
- `True` : si l'évaluation de l'opérande est `False`
- `False` : si l'évaluation de l'opérande est `True`

| not   | expr  |
| ----- | ----- |
| False | True  |
| Not   | False |

# Opérateurs 'arithmétiques'
 **Opérateurs** : `+`, `-`, `*`, `**`, `/`, `//`, `%`
 **Type des opérandes** : expression numérique
 **Type du résultat** : valeur numérique
 
| Opérateur | Nom              | Explication                               | Exemple    |
| --------- | ---------------- | ----------------------------------------- | ---------- |
| `+`       | Addition         |                                           | a +b       |
| `-`       | Soustraction     |                                           | a - b      |
| `*`       | Multiplication   |                                           | a * 2      |
| `**`      | Puissance        | élève la valeur de `a` à la puissance `b` | a ** b     |
| `/`       | Division         |                                           | a / 2      |
| `//`      | Division entière | Quotient de la division entière           | 17 // 3 =5 |
| `%`       | Modulo           | Reste de la division entière              | 17 % 3 = 2 |
|           |                  |                                           |            |
## La division euclidienne 
#def #bonus La 'division euclidienne' : est l'opération mathématique qui permet décomposer un entier (le dividende), en un quotient et un reste en utilisant un autre entier non nul (le diviseur), selon la relation : *a = b \* q +r,  avec 0 <= r < b*

![[4TT/Programmation/attachments/DivisionEuclidienne.jpg]]
### Explication sur la division entière :  **//**
Le résultat de la division entière correspond au **quotient** de la division euclidienne.
Exemple : le <span style="color:red; font-weight:bold">9</span> dans l'exemple ci-dessus.
### Explication sur le modulo : **%**
Le résultat du 'modulo' correspond au **reste** de la division euclidienne.
Exemple : le <span style="color:green; font-weight:bold">2</span> dans l'exemple ci-dessus.

# Opérateurs 'relationnels'
**Opérateurs** : `<`, `<=`, `>`, `>=`
**Type des opérandes** : 
- Numérique (int, float) : c'est l'ordre sur les valeurs numériques qui s'applique.
- Séquence (list, str, tuple) : les deux opérandes doivent être de même type.
	- Les éléments sont comparés un à un, en suivant l'ordre des indices.
	- Rem : pour le type *chaîne de caractère* (str); on compare un à un les caractères des deux chaînes.  C'est la valeur numérique (du *code point* en Unicode) correspondant au caractère qui sera utilisée pour la comparaison.
- Si les opérandes sont de types incompatibles entre eux, alors un `TypeError` est levé.
**Type du résultat** : booléen

| Opérateur | Signification     | Exemple  |
| --------- | ----------------- | -------- |
| `<`       | inférieur         | `a < b`  |
| `<=`      | inférieur ou égal | `a <= b` |
| `>`       | supérieur         | `a > b`  |
| `>=`      | supérieur ou égal | `a >= b` |
## Exemples 
```python
7 < 2        # False (on compare 2 'int')
2 < 7.15     # True (on compare 'int' avec un 'float')
"abc" > "bcd"     # False, car 'a' < 'b'
"abcde" > "abccf" # True, car 'd' < 'c'... 
15 >= "a"    # TypeError
[1,2,3] <= [1,2,4] # True, car 3 < 4
[1,2,3] <= [1,2,2,7,8,9] # False, car 2 < 3... peu importe la taille de la liste.
[1,2,3] <= (1,2,4) # TypeError, car on compare une 'liste' avec un 'tuple'
["ab","ce","ef"] > ["ab","cd","ef","gh"] # True, car "ce" > "cd"
["ab",7,"zz"] < ["ab",8,"yz"] # True, car 7 < 8
```










