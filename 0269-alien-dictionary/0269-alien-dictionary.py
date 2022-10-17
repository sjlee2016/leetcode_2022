class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        res = []
        indegree = defaultdict(int)
        adjacent = defaultdict(list)
        dic = set()
        for word in words :
            for c in word :
                indegree[c] = 0
                adjacent[c] = []
        for i in range(1,len(words)) :
            word = words[i]
            prevWord = words[i-1]
            idx = 0
            idx2= 0
            
            while idx < len(word) and idx2 < len(prevWord) and word[idx] == prevWord[idx2] :
                    idx+=1
                    idx2+=1
                    
            if idx == len(word) and idx2 < len(prevWord) :
                return ""
            if idx < len(word) and idx2 < len(prevWord) :
                dic.add((prevWord[idx2], word[idx]))
            
        for edge in dic :
            node1 = edge[0]
            node2 = edge[1]
            indegree[node1] += 1
            adjacent[node2].append(node1)
        
        stack = [] 
        for node,degree in indegree.items() :
            if degree == 0 :
                stack.append(node)
        
        
        while len(stack) > 0 :
            node = stack.pop()
            res.append(node)
            for adj in adjacent[node] :
                indegree[adj]-=1
                if indegree[adj] == 0 :
                    stack.append(adj)
            
        if len(res) < len(indegree) :
            return ""
        return "".join(reversed(res))
            
            
            