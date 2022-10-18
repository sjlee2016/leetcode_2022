class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        
        def backtrack(index,graph,path) :
            if index == len(graph)-1 :
                paths.append(list(path))
                return
            
            for adj in graph[index] :
                if adj not in path :
                    path.append(adj)
                    backtrack(adj,graph,path)
                    path.pop()
        backtrack(0,graph,[0])
        return paths