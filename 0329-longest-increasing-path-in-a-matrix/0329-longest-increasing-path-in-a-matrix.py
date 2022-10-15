class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = {}
        def dfs(r,c) : 
            nonlocal dp
            if (r,c) in dp :
                return dp[(r,c)]
            
            for d in [[1,0],[-1,0],[0,1],[0,-1]] :
                newR = r+d[0]
                newC = c+d[1]
                if newR >= 0 and newC >= 0 and newR < len(matrix) and newC < len(matrix[0]) and matrix[newR][newC] > matrix[r][c] :
                    if (r,c) in dp :
                        dp[(r,c)] = max(dp[(r,c)], dfs(newR,newC)+1) 
                    else :
                        dp[(r,c)] = dfs(newR,newC)+1
            if (r,c) not in dp :
                dp[(r,c)] = 1 
            return dp[(r,c)]
        
        ans = 1
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                ans = max(ans,dfs(i,j))
        return ans
        
        
        
        