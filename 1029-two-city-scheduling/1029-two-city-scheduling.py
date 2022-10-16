class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        """
        Greedy approach
        maximize the profits u make if u choose to place the person to city A than city B (bcost_i - acost_i)
        """
        
        
        costs.sort(key = lambda x : x[1]-x[0])
        
        total = 0
        n = len(costs)
        for i in range(n//2) :
            total += costs[i][1]
        
        for i in range(n//2,n) :
            total += costs[i][0]
        return total