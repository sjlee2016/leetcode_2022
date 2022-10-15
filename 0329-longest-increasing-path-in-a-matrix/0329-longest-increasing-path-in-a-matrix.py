class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [ [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        def dfs(r,c) : 
            nonlocal dp
            if dp[r][c] != 0:
                return dp[r][c]
            for d in [[1,0],[-1,0],[0,1],[0,-1]] :
                newR = r+d[0]
                newC = c+d[1]
                if newR >= 0 and newC >= 0 and newR < len(matrix) and newC < len(matrix[0]) and matrix[newR][newC] > matrix[r][c] :
                    if dp[newR][newC] != 0 :
                        m = dp[newR][newC]
                    else :
                        m = dfs(newR,newC)
                    dp[r][c] = max(dp[r][c], m) 
            dp[r][c]+= 1     
            return dp[r][c]
        
        ans = 0
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if dp[i][j] == 0 :
                    ans = max(ans,dfs(i,j))
        return ans
        
        
        
        