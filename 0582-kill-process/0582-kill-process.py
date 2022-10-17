class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for i in range(len(pid)) :
            currentId = pid[i]
            parentId = ppid[i]
            graph[parentId].append(currentId)
            
        
        queue = [kill]
        res = []
        while queue :
            i = queue.pop()
            res.append(i)
            
            for child in graph[i] :
                queue.append(child)
        
        
        return res
        