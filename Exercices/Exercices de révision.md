Objectif : révisions intégrant les **séquences**, **boucles**, **structures conditionnelles** sur les nombres (int et float) et les chaînes de caractère (string)
# Exercices sur les nombres
## Ex1 : Calculer la somme et la moyenne
Ecrivez un programme qui utilisera une boucle pour demander à l'utilisateur d'introduire un nombre à chaque itération.

La boucle continuera de s'exécuter tant que l'utilisateur n'aura pas exprimé son intention d'en sortir.  Pour ce faire, le programme devra lui poser la question suivante : "Voulez-vous quitter le programme ? (oui / non) : ".

Si l'utilisateur répond 'oui'; alors le programme affichera le message suivant : `Merci d'avoir utilisé notre programme.`
Si l'utilisateur répond 'non'; alors le programme affichera : `C'est reparti pour un tour !`
Si l'utilisateur répond n'importe quoi d'autre que 'oui' ou 'non'; alors la question doit lui être reposée.
Rem : toutes les variation de *casse* (majuscules / minuscules) doivent être prises en compte.  Ainsi : 'OUI', 'oui', 'Oui'... sont équivalentes.  Idem, pour 'Non', 'non', 'Non', 'nOn',...

A la sortie du programme, vous afficherez la **somme** des nombres introduits par l'utilisateur; et leur **moyenne** !

## Ex2 : plus petit... plus grand !
#### Prérequis
Le module `random` contient des fonctions permettant de générer des nombres pseudo-aléatoires.
Pour l'utiliser, il suffira d'importer le module en début de programme.
Nous utiliserons la fonction `randint(start,stop)` du module `random` pour générer un nombre compris entre la valeur de `start` et la valeur de `stop`. 

```python
import random

x = random.randint(0,10)   # générera un nombre aléatoire : 0 <= x <=10
```

#### Exercice
Demandez à l'utilisateur d'introduire 2 nombres entiers.
Générez un nombre pseudo-aléatoire compris entre ces deux nombres.

A présent, votre programme va vous demander de tenter de deviner de quel nombre il s'agit !
Pour ce faire; le programme vous demandera d'introduire un nombre entre les deux bornes que vous avez indiquées.
Si le nombre est plus petit que le nombre à deviner; il affichera : "plus grand !"
Si le nombre est plus grand que le nombre à deviner; il affichera : "plus petit !"
Si le nombre est trouvé, il affichera : "Bravo, vous avez trouvé !"
Tant que vous n'avez pas trouvé le nombre; il vous demandera de choisir un nouveau nombre à tester.

Lors de la sortie de la boucle; il vous indiquera combien de fois vous avez dû vous y prendre pour trouver la solution !




