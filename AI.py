import AI_func as af

class player:
    int_playerNbr = 0
    int_opposentNbr = 1
    List2D_board = []

    def __init__(self,body_json):
        #extract player information
        strList_players = body_json["players"]
        str_selfPlayer = body_json["you"]
        
        #find witch player we are, so we are sure to play at least correctly
        if strList_players[0] == str_selfPlayer:
            self.int_playerNbr = 0
            self.int_opposentNbr = 1
        else:
            self.int_playerNbr = 1
            self.int_opposentNbr = 0
        
        print("-------------------------------------------------------------------------")
        print("   | I am player :",self.int_playerNbr)

        self.List2D_board = body_json["game"]

        #function whitch optimise the best option possible, int_FirstIs represent if the "From" key is ennemy or our (0 = our | 1 = ennemy)
    def _opti_move(self,dico_TowerList,int_FirstIs):
         #let optimise the number of isolated tower
            int_NbrIso = -100

            int2D_To = []     
            int2D_From = []

            for dico_tower in dico_TowerList["towers"]: #for every final position               |dico (From = (i,j) , to: [(a,b),(c,d),(e,f),(g,h)])
                for tuple_org in dico_tower["to"]:      #for every origine position for attack  |tuple (a,b)
                    
                    List2D_boardTemp = af.List2D_CopyBoard(self.List2D_board)                       #we copy the board
                    List2D_boardTemp = af.applyMove(List2D_boardTemp,tuple_org,dico_tower["from"])  #we apply the move

                    int_isoScore = af.int_getScore(List2D_boardTemp,self.int_playerNbr,self.int_opposentNbr)   #we give a score to the board
                    
                    #we keep track of witch move give a higher score
                    if(int_NbrIso < int_isoScore):
                        int_NbrIso = int_isoScore
                        #we need to be sure to move the tower in the correct order
                        if int_FirstIs == 0:    #here the enemy tower is in the "To" key
                            int2D_From = dico_tower["from"]
                            int2D_To = tuple_org
                        else:                   #here the enemy tower is in the "from" key
                            int2D_From = tuple_org
                            int2D_To = dico_tower["from"]

            return (int2D_From,int2D_To)

    def _msg(self,tuple_move):
        print("   |",tuple_move,af.int_getPieces(self.List2D_board,tuple_move[0][0],tuple_move[0][1]),af.int_getPieces(self.List2D_board,tuple_move[1][0],tuple_move[1][1]))
        
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
        print("   | Nbr of tower : ",int_nbrTower," nbr of not move : ",int_notMove)

        #array with all the strategie : (Min origin tower,min surrounding tower, inverted position 0 or 1) Origin tower, surrounded by tower, message to send
        #we set to inverted when the opposent tower is the origin tower so we move from the surronding to the origin and not the opposite
        table_strat = [
            [(4,1,1),self.int_opposentNbr,self.int_playerNbr,"Haha je t'ai pris une tour de 4 ;)"],                         #Enemy tower of 4 surrond by my tower of 1
            [(4,1,0),self.int_playerNbr,self.int_opposentNbr,"J'ai fait une tour de 5 :p"],                                 #my tower of 4 surrond by his tower of 1
            #[(3,2,1),self.int_opposentNbr,self.int_playerNbr,"Haha je t'ai pris une tour de 3 pour en faire une de 5 ;)"],  #same with 3 and 2
            #[(3,2,0),self.int_playerNbr,self.int_opposentNbr,"J'ai sécuriser une tour de 5 :O"],                            #same but mine
            #[(2,3,1),self.int_opposentNbr,self.int_playerNbr,"Haha je t'ai pris une tour de 2 saperlipopette 5 ;)"],        #with 2 and 3
            #[(2,3,0),self.int_playerNbr,self.int_opposentNbr,"J'ai refait une tour de 5 O_o"],                              #and again but mine
            [(1,1,1),self.int_opposentNbr,self.int_playerNbr,"Je t'ai pris une tour :3"],                                   #his tower surround by mine
            [(1,1,1),self.int_opposentNbr,self.int_opposentNbr,"J'ai combiné tes tours :D"],                                #his tower surrond by his tower
            [(1,1,0),self.int_playerNbr,self.int_playerNbr,"J'ai du combiner une tour :/"]                                  #my tower surrond by mine
        ]

        #Here we do all the strategies in the list, we prioritize the first one
        for List_strategie in table_strat:
            
            tuple_crit = List_strategie[0]
            dico_TowerList = af.dico_FindXTowerX(self.List2D_board,tuple_crit[0],tuple_crit[1],List_strategie[1],List_strategie[2]) #get the data base on the strategie criteria

            if len(dico_TowerList["towers"]) > 0:
                print("   |",List_strategie)

                tuple_move = self._opti_move(dico_TowerList,tuple_crit[2])   #optimise the move taking in account if we need to invert the position

                #We create the move json
                dico_move["move"]["from"] = tuple_move[0]
                dico_move["move"]["to"] = tuple_move[1]
                dico_move["message"] = List_strategie[3]

                self._msg(tuple_move)
                print("-------------------------------------------------------------------------")

                #And here we go
                return dico_move