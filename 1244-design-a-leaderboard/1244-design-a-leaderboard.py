class Leaderboard(object):

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.scores[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        heap = []
        
        for key in self.scores :
            value = self.scores[key]
            heapq.heappush(heap,(value,key))
            if len(heap) > K :
                heapq.heappop(heap)
                
        return sum(x[0] for x in heap)

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)