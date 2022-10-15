class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        target = len(graph)-1 
        
      
        def dfs(start,path) :
            if start == target :
                result.append(list(path))
                return 
            for adj in graph[start] :
                path.append(adj)
                dfs(adj,path)
                path.pop()
            
        dfs(0,[0])
        return result