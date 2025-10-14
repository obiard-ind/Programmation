#description Cette fiche traitera du type de données 'Range' (intervalle, en français).
# Le type 'Range' : range

Le type `range` permet de générer une **séquence d'entiers**.
**Attn** : cette séquence se présentera sous la forme d'un intervalle d'entiers `[start, stop[`; dont la borne supérieure, ici représentée par la variable `stop` est toujours exclue !
**Tip** :  Il sera souvent utilisé dans les boucles `for` afin de répéter un certain nombre de fois un bloc d'instructions.
## Comment générer une séquence d'entiers
Pour générer une séquence d'entiers; on utilisera la fonction `range()`

Celle-ci peut prendre plusieurs arguments.
#def les arguments sont les valeurs que l'on passe à une fonction.  S'il y en a plusieurs; ceux-ci seront séparés par des virgules.

**Rem**: `range()` prend des arguments de type `int` (entier).

Dans la suite de cette présentation; `start`, `stop`, et `step` désigneront respectivement ces arguments.

### range(stop)
Génère une séquence d'entiers allant de `0` à `stop-1`.
De ce fait, `range(stop)` génère `stop` nombres entiers (puisque l'on commence à `0`)

```python
range(10)    # 0,1,2,3,4,5,6,7,8,9
```

```python
nombre = 5
range(nombre)    # 0,1,2,3,4
```

### range(start, stop)
Génère une séquence d'entiers allant de `start` à `stop-1

```python
range(7,15)   # 7,8,9,10,11,12,13,14
```

```python
debut = 10
fin = 12
range(debut, fin)     # 10,11
```

### range(start, stop, step)
Génère une séquence d'entiers allant de `start` à `stop-1`, par '_pas_' de `step`
```python
range(-12,10,3)    # -12,-9,-6,-3,0,3,6,9
range(5,20,7)      #  5,12,19
```

## Utilisation de `range` dans une boucle `for`
Une 'boucle for', parcourt une séquence d'éléments.
Or, comme on l'a vu; la fonction `range()` produit une séquence d'éléments.
Elle sera donc souvent utilisée sous l'un ou l'autre des formes vues ci-dessus.

```python
# Affiche, chaque fois sur une nouvelle ligne, les nombres allant de 0 à 9
for i in range(10):
    print(i)        
```

```python
# Affiche, chaque fois sur une nouvelleligne, les nombres allant de 1 à 10
for i in range(1,11):
    print(i)       
```

```python
# Affiche, chaque fois sur une nouvelle ligne, les nombres suivants : 
# 20,-15,-10,-5,0,5,10,15
for i in range(-20,20,5):
    print(i)       
```
**Rem** : l'on notera que le nombre `20` n'est pas affiché; car la borne supérieure de l'intervalle est toujours exclue ! `

Dans les exemples repris ci-dessus, on affiche la valeur de la variable `i` en guise d'illustration des valeurs que cette variable prendra tour à tour à chaque _itération_; mais ceci n'est pas obligatoire.
Ce qui est important; c'est de savoir quelle valeur la variable `i` prendra à chaque itération; et le nombre de fois que le bloc d'instruction va être exécuté !
