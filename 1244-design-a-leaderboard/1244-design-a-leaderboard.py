from heapq import *
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores :
            self.scores[playerId] = 0
        self.scores[playerId] += score 

    def top(self, K: int) -> int:
        heap = []
        for x in self.scores.values() :
            heapq.heappush(heap, x) 
            
            if len(heap) > K :
                heapq.heappop(heap)
        s = 0
        while heap :
            s += heapq.heappop(heap)
        return s 

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)