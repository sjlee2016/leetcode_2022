class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ## check columns
        complete = False
        while not complete :
            complete = True
            for i in range(len(board)) :
                for j in range(len(board[0])-2) :
                    if board[i][j] == 0 :
                        continue
                    c1 = board[i][j]
                    c2 = board[i][j+1]
                    c3 = board[i][j+2]
                    if abs(c1) == abs(c2) and abs(c2) == abs(c3) and c1 != 0 :
                        board[i][j] = - abs(c1)
                        board[i][j+1] = -abs(c2)
                        board[i][j+2] = -abs(c3)
                        complete = False
        ## check rows
            for i in range(len(board[0])) :
                for j in range(len(board)-2) :
                    if board[j][i] == 0 :
                        continue
                    c1 = board[j][i]
                    c2 = board[j+1][i]
                    c3 = board[j+2][i]
                    if abs(c1) == abs(c2) and abs(c2) == abs(c3) and c1 != 0 :
                        board[j][i] = -abs(c1)
                        board[j+1][i] = -abs(c2)
                        board[j+2][i] = -abs(c3)
                        complete = False
                        
        
        
        ## gravity
            for j in range(len(board[0])) :
                empty = 0
                for i in range(len(board)-1,-1,-1) :
                    if board[i][j] == 0 :
                        empty+=1
                    elif board[i][j] < 0 :
                        board[i][j] = 0
                        empty += 1
                    else :
                        if empty > 0 :
                            board[i+empty][j] = board[i][j]
                            board[i][j] = 0
        return board