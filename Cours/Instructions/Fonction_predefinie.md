# Fonction vs méthode - définitions :
## Fonctions
#def une fonction est un bloc de code réutilisable
- qui possède un **nom** (à l'aide duquel elle pourra être appelée)
- qui peut avoir des **arguments** (à l'aide desquels on pourra lui *passer des **valeurs***)
- qui **renvoie** une valeur
	- à l'aide du mot-clé `return`
	  **Rem** : si aucune valeur n'est retournée; c'est la valeur `None` qui est renvoyée implicitement.

 #def un **argument** (on dira aussi, un paramètre) agit comme une déclaration de variable
		- Il possède un nom
		- Une valeur par défaut peut lui être affectée ( avec l'opérateur d'affectation :  `=`, comme pour une variable).
 #def une **valeur** correspond à la valeur réelle que l'on passera à un argument de la fonction quand on appelera celle-ci !  Cela revient à affecter une valeur à une variable.

Pour appeler une fonction : 
- il suffit de taper son nom, suivi de la liste des **valeurs** correspondant à ses **arguments** éventuels.
  `nom_fonction(valeur1, valeur2,...)`
- Rem : on dira que les *valeurs sont passées en arguments* (ou tout simpelment, que les *valeurs sont passées*) à la fonction.
- **Attn** : les valeurs passées à la fonction doivent correspondre **en nombre** et en **type** aux arguments de la fonction. 

Syntaxe d'un appel de fonction :
`nom_fonction(valeur1, valeur2,...)`

```python
prenoms = ["Linda", "Jean", "Hubert", "Matteo", "Sylvie", "Alfred"]
# len() est une fonction qui retourne la taille de la séquence passée en argument.
len(prenoms)
# sorted est une fonction qui retourne la liste triée, sans affecter la liste d'origine
sorted(prenoms)
# print() affiche de l'objet passé en argument... celui-ci étant converti en 'string' au préalable
print(prenoms)
print("Ma liste a une longueur de {} éléments : ".format(len(prenoms)))
# une fonction peut posséder une liste d'arguments; séparés par des 'virgules'
# ici, print() prend un second argument qui définit un délimiteur entre les élements à afficher... sans retour de ligne '\n' après l'affichage.
for prenom in prenoms:
    print(prenom, end=" ") 
```
## Méthodes
#def une méthode est une fonction liée à un objet.
- Dès lors, comme une fonction, elle possède un **nom**, peut avoir des **arguments** et **renvoie** une valeur.
- A la différence d'une fonction : elle est définie sur un **type** (mais pas d'inquiétude, on verra ce que sont les **types** et les **objets** plus tard); mais sachez que vous en avez déjà utilisé sans le savoir 😉.

Pour appeler une méthode :
- une méthode s'appelle comme une fonction; à savoir, en tapant son nom, suivi de la liste des **valeurs** correspondant à ses **arguments** éventuels.... à une petite différence près :
	- on ne peut pas l'appeler directement
	- on doit passer par le nom d'un **objet** du **type** sur lequel la méthode a été définie. 

Syntaxe d'un appel de méthode :
`nom_objet.nom_methode(valeur1, valeur2,...)`

```python
prenoms = ["Linda", "Jean", "Hubert", "Matteo", "Sylvie", "Alfred"]
# La méthode index est définie sur les 'types' de séquence; dont le type 'list'
# La méthode index est appelée un objet de type 'list'; ici, prenoms.
prenoms.index("Sylvie")   # Retourne l'indice de la première occurrence de                                   # 'Sylvie' dans la liste 'prenoms'
magique = "abracadabra"
magique.count('a')
```

# Fonctions

Celles-ci peuvent être catégorisées de différentes manières :
- En fonction de leur provenance
- En fonction du type de tâche (math, image, son, fichiers, OS, chaînes de caractère, IA, vidéo,...)

## Fonctions intégrées du langage (built-in)

#ref [Liste des fonctions intégrées au langage ](https://docs.python.org/3/library/functions.html)
- Il s'agit des fonctions intégrées ('built-in') au langage Python; et donc toujours accessibles.
- Ce sont les fonctions les plus 'fondamentales'; au nombre de +/-70 (Python v3.12)
- Il existe de nombreuses autres fonctions qui peuvent être importées depuis des modules.
- Nous pouvons également créer nos propres fonctions (on verra cela plus tard)
##### Quelques fonctions intégrées courantes

| Fonction | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| print()  | Affiche le contenu passé en argument                                          |
| input()  | Retourne le contenu entré par l'utilisateur sous forme de chaîne de caractère |
| id()     | Retourne l'identifiant de l'objet passé en argument                           |
| type()   | Retourne le type de  l'objet passé en argument                                |
| range()  | Retourne une séquence de nombres                                              |
| len()    | Retourne la longeur de la séquence passée en argument                         |
| min()    | Retourne la plus petite valeur de l'itérable passé en argument                |
| max()    | Retourne la plus grande valeur de l'itérable passé en argument                |
| ord()    | Retourne un entier représentant la valeur numérique d'un caractère Unicode    |
| etc...   |                                                                               |
## Fonctions de la librairie standard (stdlib)
La *librairie standard* en Python, est une vaste collection de modules installés avec Python.
Elle contient des milliers de fonctions assurant des tâches diverses (gestion des fichiers, fonctions mathématiques, appels à des routine de l'OS, traitement des chaînes de caractère, etc...)

## Fonctions de librairies tierces (third-party)
Il s'agit généralement de librairies spécialisées externes.
Elles doivent être installées :
- A l'aide de l'outil de gestion de paquets : `pip`
  **Rem** : il est généralement intégré; mais il peut arriver qu'il ne fasse pas partie de l'installation par défaut.  Dans ce cas, il faudra l'installer à l'aide du gestionnaire de paquets du système d'exploitation (OS) hôte.  Exemple sous Fedora Linux : `sudo dnf install python3-pip`
- Depuis un dépôt : https://pypi.org (par défaut)
##### Quelques commandes utiles de `pip`

| Commande                | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| `pip --version`         | Donne la version du `pip` installé ! Sinon, il faut installer 'pip' |
| `pip install <package>` | Installe le *package* (omettre les balises <> )                     |
| `pip freeze`            | Affiche la liste des modules et leur version                        |
**Ref** : [[Prof/Archive/D2TT/UAA2-Programmation/attachments/cheat_sheet_pip.pdf|Pip cheat sheet]]

**Tip** : pour exporter un projet sur une autre machine, et s'assurer de la comptabilité des packages (nom et version); l'on peut procéder comme suit :
- Sur la machine source : 
```python
# Enregistrer la liste des modules dans le fichier .txt indiqué
pip freeze > requirements.txt
```
- Sur la machine destination :
```python
# Installer la liste des modules référencés dans le fichier .txt
pip install -r requirements.txt
```

#### Quelques poins d'attention :
##### La compatiblité des modules :
Avant d'installer tout module sur une machine, s'assurer de la compatibilité de celui-ci avec :
- votre version de Python;
- mais également des autres modules déjà présents sur la machine.
Pour ce dernier cas, certains programmes Python installés sur la machine peuvent dépendre de certains modules dont ils utilisent les fonctions.
Parfois, la mise à jour d'un module entraîne la suppression ou la modification (de la signature) de certaines fonctions présentes.
En conséquence, les programmes qui en dépendent pourraient ne plus fonctionner !

Il existe des solutions :
- #todo Création d'environnements Python virtuels
- #todo Utilisation de conteneurs
- #todo Utilisation d'Anaconda

##### La fiabilité / la réputation du développeur
L'utilisation de modules repose sur la confiance que l'on a dans le travail d'autrui !
Il est impossible de vérifier toutes les lignes de code que l'on importe / utilise.

Les modules importés pourraient en effet :
- contenir des erreurs... avec des conséquences sur le fonctionnement de vos programmes.
- contenir du code 'malveillant'

Il n'y a pas de 'garantie' absolue; juste des règles de prudence à observer :
- La provenance du code : n'importer de modules que de sources 'sûres' ou 'officielles' (eg. https://pypi.org)
- La réputation de l'éditeur ou du développeur du code : 
	- Parfois sous forme de ranking (notation) par les pairs.
	- Vérification de l'identité
- Révision du code par les pairs
  #def les *pairs*, ce sont les autres personnes de même compétence (ou supérieure), dans le domaine concerné.
  **Rem** : cette révision par les *pairs* n'est possible que si le code a été publié en *open source*. 
##### La licence
La licence décrit les devoirs et responsabilités des différentes parties.
En particulier; de l'usage qui peut être fait ou non par l'utilisateur du code.
Cet usage peut dépendre du contexte d'utilisation :
- projet éducatifs / académiques
- usage personnel
- usage commercial
- etc...
**Attn** : enfreindre les règles de licence peut avoir des conséquences légales et financières importantes; surtout dans le cadre professionnel !
#todo rédiger une section plus complète sur le thème des licences.
##### Le niveau d'activité du développement
Celui-ci constitue un indicateur de l'intérêt que la communauté des développeurs porte au module.
Ceci peut avoir des conséquences sur :
- l'ajout de nouvelles fonctionnalités 
  Rem : mais aussi, la suppression / le remplacement de fonctionnalités existantes.
- la rapidité de correction des bugs / erreurs
- le niveau de support

Quelques indicateurs du niveau d'activité 
- Le nombre d'utilisateurs actifs dans la communauté de développement
- Le nombre de *forks* du projet
  #def un *fork* est un développement dérivé (et témoigne donc de l'intérêt porté au projet parent)
- L'historique d'activité (le nombre de modification par période, de révision, etc...)
  Exemple : [Matplotlib](https://pypi.org/project/matplotlib/#history)
## Fonctions définies par l'utilisateur (user-defined)
... mais ceci sera vu au cours de 5ème année : [[4-Fonctions personnalisees]]









