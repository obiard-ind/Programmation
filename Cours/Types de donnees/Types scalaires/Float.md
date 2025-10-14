#description Cette fiche traitera du type de données 'Float'.

# Le type 'Float' : float

Le type Float représente les nombres avec une partie décimale.
L'on parlera aussi de nombres en *virgule flottante* (d'où le nom 'float')
## Ensemble des valeurs :
L'ensemble des nombres qui comportent une partie décimale.
Exemples : -1877.1234, -7.8 , 0.0 , 1.21, 3.14, 7.0, 15.234,...

**Rem** : la partie décimale est séparée de la partie entière à l'aide d'un 'point' (`.`)   ; et non d'une virgule (`,`) comme il est souvent d'usage dans nos notations mathématiques.

#bonus Les origines de cette notation sont
- historiques : c'est la notation anglo-saxonne qui a été adoptée.
- pratiques : la virgule (`,`) étant utilisée pour séparer les éléments dans les listes, les tuples, etc... mais aussi les arguments dans les fonctions; il est ainsi possible d'utiliser des nombres en virgule flottante dans ces cas, sans risquer de confondre entre la 'virgule' comme séparateur d'élément; et le symbole qui indique l'exisence d'une partie décimale d'un nombre.

**Rem** : dès qu'un nombre possède un point décimal dans sa notation; il s'agit d'un type *float* !
```python
2      # est de type 'int'
2.0    # est de type 'float'
```

## Opérations définies sur ces valeurs :
### ~~Les opérations 'logiques'~~
Opérateurs logiques : `and`, `or`, `not`

**Rem** : les opérations logiques fonctionnent également sur les nombres en virgule flottante; mais sont fort peu utilisées dans la pratique.  Elles sont mentionnées dans ce cours, par soucis de complétude; et ne sont pas à connaître pour les types autres que 'booléens'.
### Les opérations 'arithmétiques'
Opérateurs arithmétiques : `+`, `-`, `*`, `/`, `//`, `%`

### Les opérations 'relationnelles'
Opérateurs relationnels : `<`,`<=`, `>`, `>=`












