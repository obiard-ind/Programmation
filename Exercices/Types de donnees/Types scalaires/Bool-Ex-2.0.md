#description Exercices sur les expressions boolénnes (utilisant des valeurs booléennes; mais aussi des expressions relationnelles sur les types 'int' et 'float')

## Combinaisons

```python
(3 > 2) and (4 < 5)
(10 == 10) or (2 > 5)
not (7 <= 7)
```

## Mini problèmes

- Écrire une expression booléenne qui vérifie si un nombre `x` est **pair**.
- Écrire une expression qui vérifie si un nombre `n` est **compris entre 0 et 100 inclus**.
- Écrire une expression qui teste si deux flottants `a` et `b` sont **égaux à 0.1 près** (utile pour comparer des `float`).
- Écrire une expression qui est `True` si une personne a **entre 18 et 65 ans inclus** (variable `age`).
- Écrire une expression qui est `False` seulement si deux conditions `c1` et `c2` sont toutes les deux vraies.
- Écrire une expression qui est `True` si la somme de deux nombres `x` et `y` est **supérieure à 100**.
- Écrire une expression qui est `True` si `x` est un **multiple de 7**.


























# Evaluation simple :
Sans vous aider de l'ordinateur; évaluez les expressions booléennes suivantes :
```python
True or False
False and True
False and not True
not True or not False
not (True or not False)
False or True and False
```

# Parenthésage
Le parenthésage est l'opération qui consiste à placer des parenthèses.

L'exercice suivant consiste à parenthéser les expressions afin de les rendre plus lisibles; sans en changer le résultat.
```python
True or False and True or False
True or not True or not False
False and not False or True
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
"Il fait beau, ou je prends mon parapluie et je ne vais pas promer mon chien"
"Je ne prends pas mon parapluie et je ne vais pas promener mon chien"
```

# Trouvez une expression équivalente
Soit `a` et `b`, des expressions booléennes quelconques.
Trouvez pour chacune des expressions suivantes, une expression équivalente.
**Note** : par *expression équivalente*, on entend une expression dont l'évaluation produit la même valeur de vérité que l'expression initiale.
```python
not (not a)
a and True
a or False
a and a
```
**Tip** : Lois de De Morgan
```python
not (a and b)
not (a or b)
```
**Tip** : Distributivité
```python
(a and b) or a
(a or b) and a
(a or b) and (a or not b)
```

