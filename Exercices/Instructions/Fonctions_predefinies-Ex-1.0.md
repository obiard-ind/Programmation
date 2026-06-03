# Fonctions sur les chaînes de caractères

## Fonctions de base :

Demandez à l'utilisateur d'introduire une phrase.
- Affichez ensuite la longueur de cette phrase
- Affichez la phrase uniquement avec des majuscules.
- Idem, mais uniquement avec des minuscules.
- Remplacez tous les *espaces* par des *underscores* `_`

## Traitement d'un texte
Soit le texte suivant :
```
Que j’aime à faire apprendre un nombre utile aux sages !  
Glorieux Archimède, artiste ingénieux,  
Toi de qui Syracuse aime encore la gloire,  
Soit ton nom conservé par de savants grimoires !  
Jadis, mystérieux, un problème bloquait  
Tout l’admirable procédé, l’œuvre grandiose  
Que Pythagore découvrit aux anciens Grecs.  
O, quadrature ! Vieux tourment du philosophe !  
Insoluble rondeur, trop longtemps vous avez  
Défié Pythagore et ses imitateurs.  
Comment intégrer l’espace bien circulaire ?  
Former un triangle auquel il équivaudra ?  
Nouvelle invention : Archimède inscrira  
Dedans un hexagone, appréciera son aire,  
Fonction du rayon. Pas trop ne s’y tiendra  
Dédoublera chaque élément antérieur ;  
Toujours de l’orbe calculée approchera ;  
Définira limite ; enfin, l’arc, le limiteur  
De cet inquiétant cercle, ennemi trop rebelle !  
Professeur, enseignez son problème avec zèle !
```

- importez le module `re`
- Celui-ci contient une fonction nommée `split()` dont la *signature* est la suivante :
  ```python
  re.split(pattern, string, maxsplit=0, flags=0)
  ```
Vous passerez à cette dernière les arguments suivants :
	- pour *pattern* : `r"'!?;,.:s+"`
	- pour *string* : une chaine de caractères qui contient notre texte

La fonction retournera une <u>liste constituée des mots</u> individuels qui constituent le texte.
**Rem** :  par <u>mot</u>, on entend ici, toute suite consécutive de caractères qui ne contient aucun des symboles décrits dans *pattern* : `!`, `?`, `;`, `,`,`.`,`:`,`un ou plusieurs caractères d'espacement`.
Autrement formulé : un mot, est toute chaine consécutive de caractères délimitée par l'un des symboles listé dans *pattern*.

- vous allez ensuite concaténer la longueur de chaque mot dans une chaine qui, une fois que vous aurez parcouru tous les 'mots' de la liste renvoyée par `re.split()`, contiendra, dans l'ordre la longueur de chacun de ceux-ci.
	- utilisez pour cela une boucle pour parcourir la liste retournée par la fonction `re.split()`
	- A l'intérieur du corps de cette boucle; vous calculerez la longueur de chaque mot à l'aide de le fonction `len()`
	- Comme len() renvoie une valeur numérique; vous convertirez celle-ci en chaîne de caractères à l'aide de la fonction `str()`
	- Et vous concaténerez celle-ci à la chaine qui contient la longueur des mots déjà lus.
- Vous allez enfin affichez le résultat, en insérant une virgule `,` après le premier caractère.
	- Pour cela, vous utiliserez les opérateurs de slicing pour obtenir le premier caractère de la chaine... ainsi que le reste de la chaine à partir du deuxième caractère; et vous insérerez la virgule entre ces deux sous-chaines.

... Qu'avez-vous obtenu comme résultat ? 






