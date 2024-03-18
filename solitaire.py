#Giannis Fillis A.M.:5380

board1=[" ","A","B","C","D","E","F","G"]
board2=[1," "," ",1,1,1," "," "] 
board3=[2," "," ",1,1,1," "," "] 
board4=[3,1,1,1,1,1,1,1] 
board5=[4,1,1,1,0,1,1,1] 
board6=[5,1,1,1,1,1,1,1] 
board7=[6," "," ",1,1,1," "," "] 
board8=[7," "," ",1,1,1," "," "] 
lst=[] #edo vazo ta 1(diladi tis mpales) gia na metraei poses apomenoun
directions= ["L","R","U","D"] #Oi kateuthinseis pou mporoume na dosoume
wrongplaces= ["A1","A2","A6","A7","B1","B2","B6","B7","F1","F2","F6","F7","G1",
              "G2","G6","G7"] #theseis me kena
places={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7} #To kathe gramma se poia stili antistoixei
board = [board1,board2,board3,board4,board5,board6,board7,board8]
numbers=["1","2","3","4","5","6","7"] #pithanoi arithmoi pou mporei na dosei
counter= 32 #posa 1 yparxoun arxika(diladi poses mpales)
notindexR=["C6","D6","E6","C7","D7","E7"] #theseis apo tis opoies an kinithei ena mpalaki mporei na pesei ektos pinaka
notindexL=["C1","D1","E1","C2","D2","E2"] #theseis apo tis opoies an kinithei ena mpalaki mporei na pesei ektos pinaka
notindexU=["A3","A4","A5","B3","B4","B5"] #theseis apo tis opoies an kinithei ena mpalaki mporei na pesei ektos pinaka
notindexD=["G3","G4","G5","F3","F4","F5"] #theseis apo tis opoies an kinithei ena mpalaki mporei na pesei ektos pinaka


        
        
def movements(move1):  #h synartisi twn kinisewn
    
        if move1[2]=="D" :  
            if board[int(move1[1])][places[move1[0]]+2]==0 and board[int(move1[1])][places[move1[0]]+1]==1 and board[int(move1[1])][places[move1[0]]]==1:
                board[int(move1[1])][places[move1[0]]+2]=1
                board[int(move1[1])][places[move1[0]]+1]=0
                board[int(move1[1])][places[move1[0]]]=0 
                
            
        elif move1[2]=="U":
            if board[int(move1[1])][places[move1[0]]-2]==0 and board[int(move1[1])][places[move1[0]]-1]==1 and board[int(move1[1])][places[move1[0]]]==1:
                board[int(move1[1])][places[move1[0]]-2]=1
                board[int(move1[1])][places[move1[0]]-1]=0
                board[int(move1[1])][places[move1[0]]]=0
                
            
        elif move1[2]=="L":
            if board[int(move1[1])-2][places[move1[0]]]==0 and board[int(move1[1])-1][places[move1[0]]]==1 and board[int(move1[1])][places[move1[0]]]==1:
                board[int(move1[1])-2][places[move1[0]]]=1
                board[int(move1[1])-1][places[move1[0]]]=0
                board[int(move1[1])][places[move1[0]]]=0
                
            
        elif move1[2]=="R":
            if board[int(move1[1])+2][places[move1[0]]]==0 and board[int(move1[1])+1][places[move1[0]]]==1 and board[int(move1[1])][places[move1[0]]]==1:
                board[int(move1[1])+2][places[move1[0]]]=1
                board[int(move1[1])+1][places[move1[0]]]=0
                board[int(move1[1])][places[move1[0]]]=0
                



def errors(move1): #h synartisi gia pithana lathoi pou mporei na ginoun apo ton user

        if len(move1)!=3:
                print("Something wrong with your input")

        elif move1[0] not in places:
                print("Something wrong with your input")

        elif move1[1] not in numbers:
                print("Something wrong with your input")

        elif move1[2] not in directions:
                print("Direction is not L or R or U or D!")

        elif move1[:2] in wrongplaces:
                print("Given peg position is out of board!")

        elif board[int(move1[1])][places[move1[0]]]==0:
                print("Given peg position does not have a peg!")

        elif move1[2]=="R" and move1[:2] in notindexR:
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="L" and move1[:2] in notindexL:
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="U" and move1[:2] in notindexU:
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="D" and move1[:2] in notindexD:
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="D" and board[int(move1[1])][places[move1[0]]+2]==" ":
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="U" and board[int(move1[1])][places[move1[0]]-2]==" ":
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="L" and board[int(move1[1])-2][places[move1[0]]]==" ":
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="R" and board[int(move1[1])+2][places[move1[0]]]==" ":
                print("Moving peg will fall out of bounds!")

        elif move1[2]=="D" and board[int(move1[1])][places[move1[0]]+1]==0: 
                print("No peg at next position to jump over!")

        elif move1[2]=="U" and board[int(move1[1])][places[move1[0]]-1]==0:
                print("No peg at next position to jump over!")
        

        elif move1[2]=="L" and board[int(move1[1])-1][places[move1[0]]]==0:
                print("No peg at next position to jump over!")

        elif move1[2]=="R" and board[int(move1[1])+1][places[move1[0]]]==0:
                print("No peg at next position to jump over!")

        elif move1[2]=="D" and board[int(move1[1])][places[move1[0]]+2]==1:
                print("Landing position is occupied!")

        elif move1[2]=="U" and board[int(move1[1])][places[move1[0]]-2]==1:
                print("Landing position is occupied!")

        elif move1[2]=="L" and board[int(move1[1])-2][places[move1[0]]]==1:
                print("Landing position is occupied!")

        elif move1[2]=="R" and board[int(move1[1])+2][places[move1[0]]]==1:
                print("Landing position is occupied!")
               
        else:
                movements(move1)

def keep_game_alive(): #synartisi gia na elegxei an yparxoun alles kiniseis
        for i in range(1,len(board)): #tropos metrisis twn 1(diladi twn mpalwn)
                for x in board:
                    if x[i]==1:
                        lst.append(x[i])

        else:
                for i in range(3,len(board)-2):#afora tous arithmous sthn mesh tou pinaka
                        for x in range(3,len(board)-2):
                                if board[x][i]==1: 
                                        if board[x+1][i]==1 or board[x-1][i]==1 or board[x][i+1]==1 or board[x][i-1]==1:
                                            if board[x+2][i]==0 or board[x-2][i]==0 or board[x][i+2]==0 or board[x][i-2]==0:                                    
                                                return True
        
                for i in range(3,len(board)-2):#afora tous arithmous sta aristera tou pinaka
                        for x in range(1,len(board)-5):
                                if board[x][i]==1:
                                        if board[x+1][i]==1 or board[x][i-1]==1 or board[x][i+1]==1:
                                                if board[x+2][i]==0 or board[x][i-2]==0 or board[x][i-2]==0:
                                                        return True

                for i in range(3,len(board)-2): #afora tous arithmous sta dexia tou pinaka
                        for x in range(len(board)-2,len(board)):
                                if board[x][i]==1:
                                        if board[x-1][i]==1 or board[x][i-1]==1 or board[x][i+1]==1:
                                                if board[x-2][i]==0 or board[x][i-2]==0 or board[x][i-2]==0:
                                                        return True
                          
                for i in range(1,len(board)-5): #afora tous arithmous sto pano meros tou pinaka
                        for x in range(3,len(board)-2):
                                if board[x][i]==1:
                                        if board[x][i+1]==1 or board[x-1][i]==1 or board[x+1][i]==1:
                                                if board[x][i+2]==0 or board[x-2][i]==0 or board[x+2][i]==0:
                                                        return True
        
                for i in range(len(board)-2,len(board)): #afora tous arithmous sto kato meros tou pinaka
                        for x in range(3,len(board)-2):
                                if board[x][i]==1:
                                        if board[x][i-1]==1 or board[x+1][i]==1 or board[x-1][i]==1:
                                                if board[x][i-2]==0 or board[x+2][i]==0 or board[x-2][i]==0:
                                                        return True
        
                return False
 
            
while keep_game_alive() == True: #loop gia na trexei 
        for i in range(len(board)): #print tou pinaka
                for x in board:
                        print(x[i],end=" ") 
                print()
        move= input("Enter peg position followed by move (L, R, U, or D):")
        move1 = move.upper()
        errors(move1)           
        lst.clear()
else:
        if len(lst)==1:
                for i in range(len(board)): #print tou pinaka
                        for x in board:
                                print(x[i],end=" ") 
                        print()
                print("No more moves.Congratulations",len(lst),"pegs left")
        else:
                for i in range(len(board)): #print tou pinaka
                        for x in board:
                                print(x[i],end=" ")
                        print()
                print("No more moves.",len(lst),"pegs left")
