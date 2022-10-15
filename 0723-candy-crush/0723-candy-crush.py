class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
         ***
         *
         *
        
        2 3 4  5
       -1 2 3 -8
       -1 6 7 -8
       -1 3 4 -8
       -1 -1 -1 -1      
        
       0 0 0  0
       0 3 4  0
       0 2 3  0
       0 6 7  0
       2 3 4  5      
        
        
        """
        
        ROW = len(board)
        COL = len(board[0])
        complete = False
        ## mark the candies that need to be crushed in each row
        while not complete :
            complete = True
            for i in range(ROW) :
                for j in range(COL-2) :
                    c1 = board[i][j]
                    c2 = board[i][j+1]
                    c3 = board[i][j+2]
                    if c1 == 0 :
                        continue
                
                    if abs(c1) == abs(c2) and abs(c3) == abs(c2) :
                        board[i][j] = - abs(c1)
                        board[i][j+1] = - abs(c2)
                        board[i][j+2] = - abs(c3)
                        complete = False 
        
        
        ## mark the candies that need to be crushed in each column
            for j in range(COL) :
                for i in range(ROW-2) :
                    c1 = board[i][j]
                    c2 = board[i+1][j]
                    c3 = board[i+2][j]
                    if c1 == 0 :
                        continue
                
                    if abs(c1) == abs(c2) and abs(c3) == abs(c2) :
                        board[i][j] = - abs(c1)
                        board[i+1][j] = - abs(c2)
                        board[i+2][j] = - abs(c3)
                        complete = False 
            
        ## gravity         
            for j in range(COL) :
                emptyBox = 0
                for i in range(ROW-1,-1,-1) :
                    if board[i][j] == 0 :
                        emptyBox += 1 
                    elif board[i][j] < 0 :
                        board[i][j] = 0
                        emptyBox += 1 
                    else :
                        if emptyBox > 0 :
                            board[i+emptyBox][j] = board[i][j]
                            board[i][j] = 0 
        return board