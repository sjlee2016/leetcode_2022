from sortedcontainers import SortedSet

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        self.set = SortedSet()

    def addScore(self, playerId: int, score: int) -> None:
        self.set.discard((self.scores[playerId], playerId))
        self.scores[playerId] += score
        self.set.add((self.scores[playerId], playerId))

    def top(self, K: int) -> int:
        return sum( score for score, _ in islice(reversed(self.set), 0, K) )

    def reset(self, playerId: int) -> None:
        self.set.remove((self.scores[playerId], playerId))
        del self.scores[playerId]