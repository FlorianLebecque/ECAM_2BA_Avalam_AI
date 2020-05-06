import AI_func as af

class player:
    int_playerNbr = 0
    int_opposentNbr = 1
    List2D_board = []

    def __init__(self,body_json):
        #extract player information
        strList_players = body_json["players"]
        str_selfPlayer = body_json["you"]
        
        if strList_players[0] == str_selfPlayer:
            self.int_playerNbr = 0
            self.int_opposentNbr = 1
        else:
            self.int_playerNbr = 1
            self.int_opposentNbr = 0
        
        self.List2D_board = body_json["game"]

    def play(self):
        dico_move = {
            "move" :{
                "from":[0,0],
                "to":[0,0]  
            },
            "message":""
        }

        int_nbrTower = af.countTower(self.List2D_board,self.int_playerNbr)
        int_notMove = af.int_CountIsolated(self.List2D_board,self.int_playerNbr,self.int_opposentNbr)
        print("nbr of tower : ",int_nbrTower," nbr of not move : ",int_notMove)

        #First try to steal a tower of four of the adverair
        dico_towerOfFourOP = af.dico_FindTowerFour(self.List2D_board,self.int_opposentNbr,self.int_playerNbr) #every tower of four of the opposant
        if len(dico_towerOfFourOP["towers"])>0:
            #let optimise the number of isolated tower
            int_NbrIso = -100

            int2D_To = dico_towerOfFourOP["towers"][0]["from"]        #enemy tower
            int2D_From = dico_towerOfFourOP["towers"][0]["to"][0]     #our tower

            for dico_tower in dico_towerOfFourOP["towers"]:   #for every final position               |dico (From = (i,j) , to: [(a,b),(c,d),(e,f),(g,h)])
                for tuple_org in dico_tower["to"]:           #for every origine position for attack  |tuple (a,b)
                    
                    List2D_boardTemp = af.List2D_CopyBoard(self.List2D_board)
                    List2D_boardTemp = af.applyMove(List2D_boardTemp,tuple_org,dico_tower["from"])

                    int_isoScore = af.int_CountIsolated(List2D_boardTemp,self.int_playerNbr,self.int_opposentNbr)
                    
                    if(int_NbrIso < int_isoScore):
                        int_NbrIso = int_isoScore
                        int2D_From = tuple_org
                        int2D_To = dico_tower["from"]

            dico_move["move"]["from"] = int2D_From
            dico_move["move"]["to"] = int2D_To
            dico_move["message"] = "Haha je t'ai pris une tour de 4 ;) "

            print(int2D_From,af.int_getPieces(self.List2D_board,int2D_From[0],int2D_From[1]),int2D_To,af.int_getPieces(self.List2D_board,int2D_To[0],int2D_To[1]))

            return dico_move

        #then let's try to save our tower of four
        dico_towerOfFourPL = af.dico_FindTowerFour(self.List2D_board,self.int_playerNbr,self.int_opposentNbr) #every tower of four with our tower next to it
        if len(dico_towerOfFourPL["towers"])>0:
            int_NbrIso = -100

            int2D_From = dico_towerOfFourPL["towers"][0]["from"]
            int2D_To = dico_towerOfFourPL["towers"][0]["to"][0]

            for dico_tower in dico_towerOfFourPL["towers"]:   #for every final position               |dico (From = (i,j) , to: [(a,b),(c,d),(e,f),(g,h)])
                for tuple_org in dico_tower["to"]:           #for every origine position for attack  |tuple (a,b)
                    
                    List2D_boardTemp = af.List2D_CopyBoard(self.List2D_board)
                    List2D_boardTemp = af.applyMove(List2D_boardTemp,tuple_org,dico_tower["from"])

                    int_isoScore = af.int_CountIsolated(List2D_boardTemp,self.int_playerNbr,self.int_opposentNbr)
                    
                    if(int_NbrIso < int_isoScore):
                        int_NbrIso = int_isoScore
                        int2D_From = dico_tower["from"]
                        int2D_To = tuple_org

            dico_move["move"]["from"] = int2D_From
            dico_move["move"]["to"] = int2D_To

            dico_move["message"] = "J'ai fait une tour de 5 :p "

            print(int2D_From,af.int_getPieces(self.List2D_board,int2D_From[0],int2D_From[1]),int2D_To,af.int_getPieces(self.List2D_board,int2D_To[0],int2D_To[1]))

            return dico_move
        
        #now let's juste make more tower
        #we first need to find all enemy tower that we can take
        #We also need to isolate our tower.
        dico_EnnemyTower = af.dico_FindTower(self.List2D_board,self.int_opposentNbr,self.int_playerNbr) #every tower of our enemy with tower of ours next to it
        if len(dico_EnnemyTower["towers"])>0:
            
            #let optimise the number of isolated tower of our
            int_NbrIso = -100

            int2D_To = dico_EnnemyTower["towers"][0]["from"]        #enemy tower
            int2D_From = dico_EnnemyTower["towers"][0]["to"][0]     #our tower

            for dico_tower in dico_EnnemyTower["towers"]:   #for every final position               |dico (From = (i,j) , to: [(a,b),(c,d),(e,f),(g,h)])
                for tuple_org in dico_tower["to"]:           #for every origine position for attack  |tuple (a,b)
                    
                    List2D_boardTemp = af.List2D_CopyBoard(self.List2D_board)
                    List2D_boardTemp = af.applyMove(List2D_boardTemp,tuple_org,dico_tower["from"])

                    int_isoScore = af.int_CountIsolated(List2D_boardTemp,self.int_playerNbr,self.int_opposentNbr)
                    
                    if(int_NbrIso < int_isoScore):
                        int_NbrIso = int_isoScore
                        int2D_From = tuple_org
                        int2D_To = dico_tower["from"]

            print(int_NbrIso)
            dico_move["move"]["from"] = int2D_From
            dico_move["move"]["to"] = int2D_To
            dico_move["message"] = "Je t'ai pris une tour :3 "

            print(int2D_From,af.int_getPieces(self.List2D_board,int2D_From[0],int2D_From[1]),int2D_To,af.int_getPieces(self.List2D_board,int2D_To[0],int2D_To[1]))

            return dico_move

        #We may have the possibilities to take opposant tower with his tower
        dico_myTower = af.dico_FindTower(self.List2D_board,self.int_opposentNbr,self.int_opposentNbr) #every tower of our enemy with tower of ours next to it
        if len(dico_myTower["towers"])>0:

            #let optimise the number of isolated tower of our
            int_NbrIso = 100

            int2D_To = dico_myTower["towers"][0]["from"]        #enemy tower
            int2D_From = dico_myTower["towers"][0]["to"][0]     #our tower

            for dico_tower in dico_myTower["towers"]:   #for every final position               |dico (From = (i,j) , to: [(a,b),(c,d),(e,f),(g,h)])
                for tuple_org in dico_tower["to"]:           #for every origine position for attack  |tuple (a,b)
                    
                    List2D_boardTemp = af.List2D_CopyBoard(self.List2D_board)
                    List2D_boardTemp = af.applyMove(List2D_boardTemp,tuple_org,dico_tower["from"])

                    int_isoScore = af.int_CountIsolated(List2D_boardTemp,self.int_opposentNbr,self.int_playerNbr)
                    
                    if(int_NbrIso > int_isoScore):
                        int_NbrIso = int_isoScore
                        int2D_From = tuple_org
                        int2D_To = dico_tower["from"]

            print(int_NbrIso)
            dico_move["move"]["from"] = int2D_From
            dico_move["move"]["to"] = int2D_To
            
            dico_move["message"] = "J'ai combiné tes tours :D "

            print(int2D_From,af.int_getPieces(self.List2D_board,int2D_From[0],int2D_From[1]),int2D_To,af.int_getPieces(self.List2D_board,int2D_To[0],int2D_To[1]))

            return dico_move

        #now we juste have to take our own tower
        dico_myTower = af.dico_FindTower(self.List2D_board,self.int_playerNbr,self.int_playerNbr) #Our towers with our towers next to it
        if len(dico_myTower["towers"])>0:
            #let optimise the number of isolated tower of our
            int_NbrIso = -100

            int2D_To = dico_myTower["towers"][0]["from"]        #enemy tower
            int2D_From = dico_myTower["towers"][0]["to"][0]     #our tower

            for dico_tower in dico_myTower["towers"]:   #for every final position               |dico (From = (i,j) , to: [(a,b),(c,d),(e,f),(g,h)])
                for tuple_org in dico_tower["to"]:           #for every origine position for attack  |tuple (a,b)
                    
                    List2D_boardTemp = af.List2D_CopyBoard(self.List2D_board)
                    List2D_boardTemp = af.applyMove(List2D_boardTemp,tuple_org,dico_tower["from"])

                    int_isoScore = af.int_CountIsolated(List2D_boardTemp,self.int_playerNbr,self.int_opposentNbr)
                    
                    if(int_NbrIso < int_isoScore):
                        int_NbrIso = int_isoScore
                        int2D_From = tuple_org
                        int2D_To = dico_tower["from"]

            dico_move["move"]["from"] = int2D_From
            dico_move["move"]["to"] = int2D_To
            dico_move["message"] = "J'ai du combiner une tour :/ "

            print(int2D_From,af.int_getPieces(self.List2D_board,int2D_From[0],int2D_From[1]),int2D_To,af.int_getPieces(self.List2D_board,int2D_To[0],int2D_To[1]))

            return dico_move