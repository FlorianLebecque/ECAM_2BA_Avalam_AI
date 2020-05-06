# Avalam AI

Intéligence artificielle créée dans le cadre dy cours d'informatique à l'écam en Bac2

## Stratégie
L'IA recois le tableau, on joue dans un ordre bien précis :
- On prend toutes les tours adverse qui ont une taille de 4
- On déplace toutes nos tours qui ont une tailles de 4 si elles sont menacées
- Ensuite on joue déplace nos tours restante sur celles de l'énemie
- Maintenant qu'on ne peut plus lui prendre de tour on déplace les siennes sur les siennes
- Les seuls mouvements possibles qu'ils restent sont nos tours sur nos tours

On recherche le coups qui va nous avantager le plus, pour cela on test chaque possibilité par stratégie et on attribue un nombre de point à l'état du jeux.

Le score est attribué de cette facons : NTI²-NEI
(NTI = nombre de tours allier, NEI = nombre de tour isoler)

## Démarrer l'IA
L'IA est un serveur web basé sur ce repos [AIGameRunner](https://github.com/ECAM-Brussels/AIGameRunner)

- Il faut avoir la librairie Cherrypy
- Lancer RunAI.py avec en argument le port

> ex : RunAI.py 8080