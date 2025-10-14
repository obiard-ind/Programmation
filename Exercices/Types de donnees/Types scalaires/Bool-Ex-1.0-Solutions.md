#description Exercices sur les expressions boolénnes (impliquant uniquement des booléens)

# Evaluation simple :
Sans vous aider de l'ordinateur; évaluez les expressions booléennes suivantes :
```python
True or False              # True
False and True             # False
False and not True         # False
not True or not False      # True
not (True or not False)    # False
False or True and False    # False
```

# Parenthésage
Le parenthésage est l'opération qui consiste à placer des parenthèses.

L'exercice suivant consiste à parenthéser les expressions afin de les rendre plus lisibles; sans en changer le résultat... jusqu'à ce que toute l'expression soit parenthésée.
```python
True or False and True or False   # ((True or (False and True)) or False)
True or not True or not False     # ((True or (not True)) or (not False))
False and not False or True       # ((False and (not False) or True)
```

# Exprimer les conditions suivantes
Soit les assertions suivantes :
```python
a = "Il fait beau"
b = "Je prends mon parapluie"
c = "Je vais promner mon chien"
```
En utilisant les variables `a,b,c` ; exprimez chacune des phrases suivantes sous la forme d'une expression booléenne.
```python
"Il ne fait pas beau, et je vais promener mon chien"
# not a and c
"Il fait beau ou je prends mon parapluie et je ne vais pas promer mon chien"
# a or b and not c
# ...mais aussi : (a or b) and not c
# La phrase en français peut être exprimée de plusieurs façons en logique booléenne...  On dira qu'elle est ambiguë ! En programmation, l'ambiguïté est source de nombreux problèmes et doit être évitée.  
"Je ne prends pas mon parapluie et je ne vais pas promener mon chien"
# not b and not c
```

# Trouvez une expression équivalente
Soit `a` et `b`, des expressions booléennes quelconques.
Trouvez pour chacune des expressions suivantes, une expression équivalente.
**Note** : par *expression équivalente*, on entend une expression dont l'évaluation produit la même valeur de vérité que l'expression initiale.
```python
not (not a)    # a (double négation)
a and True     # a (True est neutre pour 'and'... comme 1 est neutre pour '*')
a or False     # a (False est neutre pour 'or'... comme 0 est neutre pour '+')
a and a        # a (Idempotence pour 'and')
a or a         # a (Idempotence pour 'or)
```
**Tip** : Lois de De Morgan
```python
not (a and b)   # (not a) or (not b) 
not (a or b)    # (not a) and (not b)
```
**Tip** : Distributivité et absorption
```python
(a and b) or a             # a (règle d'absorption : P or (P and Q) ≡ P     )
(a or b) and a             # a (règle d'absorption : P and (P or Q) ≡ P     )
(a or b) and (a or not b)  
    # (a and (a or not b)) or (b and (a or not b)))    (Distributivité)
    # a or (b and (a or not b))                        (Absorption)
    # a or ((b and a) or (b and not b)                 (Distributivité)
    # a or ((b and a) or False)
    # a or (b and a)
    # a                                                (Absorption)
```

