class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = [ [ 0  for _ in range(COL)] for _ in range(ROW)] 
        
        def backtrack(i,j,index, visited) :
            nonlocal word, board
            if index == len(word)-1 :
                return True 
            
            for d in [ [-1,0], [1,0], [0,1], [0,-1]] :
                newRow = i + d[0]
                newCol = j + d[1]
                if newRow >= 0 and newCol >= 0 and newRow < ROW and newCol < COL and visited[newRow][newCol] == 0 and board[newRow][newCol] == word[index+1] :
                    visited[newRow][newCol] = 1
                    if backtrack(newRow, newCol, index+1, visited) == True :
                        return True
                    visited[newRow][newCol] = 0
            
            return False
        
        for i in range(ROW) :
            for j in range(COL) :
                if board[i][j] == word[0] :
                    visited[i][j] = 1
                    if backtrack(i,j,0,visited) == True :
                        return True
                    visited[i][j] = 0
        return False