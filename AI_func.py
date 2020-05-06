#Function that return a dictionary, It take :
#   The game board
#   the minimum size of the origin tower
#   the minimum size of the surrounding tower
#   the owner of the origin tower
#   the owner of the surrounding tower
def dico_FindXTowerX(List2D_board,int_gotAtLeast,int_SurroundBySize,int_playerTower,int_playerPieces):
    dico_Tower = {"towers":[]}
    for i in range(9):
        for j in range(9):
            #check that the tower is from the player
            if int_getPieces(List2D_board,i,j) == int_playerTower:
                #check that it is a tower of 4
                if len(List2D_board[i][j]) >= int_gotAtLeast:
                    dico_temp = {
                        "from":(i,j),   #position of the tower
                        "to":tuple_getAdjPieces(List2D_board,i,j,int_playerPieces,int_SurroundBySize) #position of the other player next to it
                    }
                    if len(dico_temp["to"]) > 0:    #only add if it is possible to take it
                        dico_Tower["towers"].append(dico_temp)
    
    return dico_Tower

#function that return the owner of a tower (int_i,int_j) on the field
def int_getPieces(List2D_board,int_i,int_j):
    if len(List2D_board[int_i][int_j]) > 0:
        return List2D_board[int_i][int_j][len(List2D_board[int_i][int_j])-1]
    return -1 

#Return the surrounding tower near the tower in (i,j), we also need the minimum size of those tower
def tuple_getAdjPieces(List2D_board,i,j,int_playerNbr,int_minSize):
    BOARDSIZE = 9
    MAXPIECES = 5

    pos_move = []
    pos = [(i,j-1),(i,j+1),(i-1,j),(i+1,j),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]     #UP,DOWN,LEFT,RIGHT, Diag UP LEFT, diag UP RIGHT, diag DOWN LEFT, diag DOWN RIGHT

    if len(List2D_board[i][j]) > 0:
        for p in pos:
            #check if in the board
            if p[0]>=0 and p[0] < BOARDSIZE and p[1] >= 0 and p[1] < BOARDSIZE:
                #check nbr of pieces per piles
                if  len(List2D_board[i][j]) + len(List2D_board[p[0]][p[1]]) <= MAXPIECES and len(List2D_board[p[0]][p[1]])>= int_minSize:
                    if int_getPieces(List2D_board,p[0],p[1]) == int_playerNbr:
                        pos_move.append(p)

    return pos_move

#copy the board by data
def List2D_CopyBoard(List2D_board):
    List2D_CopyBoard = []
    for i in range(9):
        List_temp = []
        for j in range(9):
            List_temp.append(List2D_board[i][j])
        List2D_CopyBoard.append(List_temp)
    return List2D_CopyBoard


#count the number of isolated tower
def int_CountIsolated(List2D_board,int_playerNbr,int_opposantNbr):
    int_MyTower = countTower(List2D_board,int_playerNbr) #number of tower
    int_Tower = 0

    List_PosICanGet = dico_FindXTowerX(List2D_board,1,1,int_playerNbr,int_playerNbr)    #Dictionary with all of my tower i can get
    List_PosHeCanGet = dico_FindXTowerX(List2D_board,1,1,int_opposantNbr,int_playerNbr) #Dictionary with all of my tower the enemy can get

    #Add all of the tower in a list
    List_TowerThatCanMove = []
    for t in List_PosICanGet["towers"]:
        List_TowerThatCanMove.append(t["from"])
    
    #Add all the tower in a list except if it is already in
    for t in List_PosHeCanGet["towers"]:
        for k in t["to"]:
            if not k in List_TowerThatCanMove:
                List_TowerThatCanMove.append(k)
    
    #the number of isolated tower is the total number of tower minus all the tower that can move
    int_Tower = int_MyTower - len(List_TowerThatCanMove)

    return int_Tower

#give a score to a board base on witch player we are looking for
def int_getScore(List2D_board,int_playerNbr,int_opposantNbr):
    int_MyIsolatedTower = int_CountIsolated(List2D_board,int_playerNbr,int_opposantNbr)
    int_HisIsolatedTower = int_CountIsolated(List2D_board,int_opposantNbr,int_playerNbr)

    return (int_MyIsolatedTower**2)-int_HisIsolatedTower

#Count the number of tower of a player
def countTower(List2D_board,int_playerNbr):
    int_total = 0
    for i in range(9):
        for j in range(9):
            if int_getPieces(List2D_board,i,j) == int_playerNbr:
                int_total += 1
    return int_total

#Apply a move on a board
def applyMove(List2D_board,frm,to):
    orgi_pile = List2D_board[frm[0]][frm[1]]
    dest_pile = []
    for i in range(len(orgi_pile)):
        dest_pile.append(orgi_pile[i])
    orgi_pile = []

    List2D_board[to[0]][to[1]] = dest_pile
    List2D_board[frm[0]][frm[1]] = []

    return List2D_board