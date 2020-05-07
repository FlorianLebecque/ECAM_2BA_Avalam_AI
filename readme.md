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

Le score est attribué de cette façon : NTI²-NEI 
(NTI = nombre de tours alliées, NEI = nombre de tours énemie isolées) 

## Démarrer

l'IAL'IA est un serveur web basé sur ce repos [AIGameRunner](https://github.com/ECAM-Brussels/AIGameRunner)

- Il faut avoir la librairie Cherrypy
- Lancer Run Ai.py avec en argument le port 

> ex : Run Ai.Py 8080