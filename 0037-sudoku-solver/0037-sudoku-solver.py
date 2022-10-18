class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
        
    def backtrack(self,board) :
        row, col = self.findNextZero(board)
        if row == None and col == None :
            return True
        
        for i in range(1,10) :
            if self.checkValid(board,row,col,str(i)) == True :
                board[row][col] = str(i)
                if self.backtrack(board) == True :
                    return True
                board[row][col] = "."
        return False 
    
    def findNextZero(self,board) :
        for i in range(9) :
            for j in range(9) :
                if board[i][j] == "." :
                    return i,j
        return None, None
    
    def checkValid(self,board,row,col,value) :
        for i in range(9) :
            if board[row][i] == value :
                return False
            if board[i][col] == value :
                return False
        
        R = (row//3)*3
        C = (col//3)*3
        
        
        for i in range(3) :
            for j in range(3) :
                if board[i+R][j+C] == value :
                    return False
        return True