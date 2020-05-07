# Avalam AI

18024 : Lebecque Florian

Intéligence artificielle créée dans le cadre du cours d'informatique à l'ecam en bac2

## stratégie

L'IA reçoit le tableau, on joue dans un ordre bien précis :

- On prend tous les tours adverses qui ont une taille de 4
- On déplace tous nos tours qui ont une taille de 4 si elles sont menacées
- On déplace ensuite nos tours de 2 sur celle de 3 du joueur adverse
- Après on déplace nos tours de 3 sur celle de 2 du joueur énemie
- On continue cette stratégie avec les tours de 2
- Ensuite on joue déplace nos tours restantes sur celles de l'énemie
- Maintenant qu'on ne peut plus lui prendre de tour on déplace les siennes sur les siennes
- Les seuls mouvements possibles qu'ils restent sont nos tours sur nos tours

On recherche le coup qui va nous avantager le plus, pour cela on test chaque possibilité par stratégie et on attribue un nombre de points à l'état du jeu.

### Calcule

Le score est attribué de cette façon : NTI²-NEI 
(NTI = nombre de tours alliées, NEI = nombre de tours énemie isolées) 

### Modulaire

Les stratégies possible sont modifiable à souhait. Elles sont stockées dans une list et executé dans l'ordre de la list
* Le premier élément est un Tuple, il contient les informations sur la recherche
  * (4,1,1) : cela indique qu'on veut des tours de 4 entourés de tours de 1. Le dernier 1 indique qu'on inverse le mouvement de la tours "To" vers la tour "From"
  * (1,1,0) : cela indique qu'on veut des tours de 1 entourés de tours de 1. Ici on inverse pas le mouvement
* Le deuxième paramètre indique les tours d'origine
* Le troisème paramètre indique les tours qui sont adjacentes à la tour d'origine
* Le quatrième est just un message

```python
table_strat = [
            [(4,1,1),self.int_opposentNbr,self.int_playerNbr,"Haha je t'ai pris une tour de 4 ;)"],                         #Enemy tower of 4 surrond by my tower of 1
            [(4,1,0),self.int_playerNbr,self.int_opposentNbr,"J'ai fait une tour de 5 :p"],                                 #my tower of 4 surrond by his tower of 1
            [(3,2,1),self.int_opposentNbr,self.int_playerNbr,"Haha je t'ai pris une tour de 3 pour en faire une de 5 ;)"],  #same with 3 and 2
            [(3,2,0),self.int_playerNbr,self.int_opposentNbr,"J'ai sécuriser une tour de 5 :O"],                            #same but mine
            [(2,3,0),self.int_playerNbr,self.int_opposentNbr,"J'ai refait une tour de 5 O_o"],                              #and again but mine
            [(2,3,1),self.int_opposentNbr,self.int_playerNbr,"Haha je t'ai pris une tour de 2 saperlipopette 5 ;)"],        #with 2 and 3
            [(1,1,1),self.int_opposentNbr,self.int_playerNbr,"Je t'ai pris une tour :3"],                                   #his tower surround by mine
            [(1,1,1),self.int_opposentNbr,self.int_opposentNbr,"J'ai combiné tes tours :D"],                                #his tower surrond by his tower
            [(1,1,0),self.int_playerNbr,self.int_playerNbr,"J'ai du combiner une tour :/"]                                  #my tower surrond by mine
        ]
```


## Démarrer

L'IA est un serveur web basé sur ce repos [AIGameRunner](https://github.com/ECAM-Brussels/AIGameRunner)

- Il faut avoir la librairie Cherrypy
- Lancer RunAI.py avec en argument le port 

Le fichier RunAI.py gère aussi l'inscription aux serveur de jeux

``` 
py RunAI.Py 8080
```
