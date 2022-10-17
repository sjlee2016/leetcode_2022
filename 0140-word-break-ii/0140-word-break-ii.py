class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []

        wordSet = set(wordDict)

        dp = [[]] * (len(s)+1)
        dp[0] = [[0]]

        for endIndex in range(1, len(s)+1):
            stops = []
            for startIndex in range(0, endIndex):
                word = s[startIndex:endIndex]
                if word in wordSet:
                    stops.append([startIndex, endIndex])
            dp[endIndex] = stops

        ret = []
        def wordDFS(sentence, dp_index):
            if dp_index == 0:
                ret.append(" ".join(sentence))
                return

            for start, end in dp[dp_index]:
                word = s[start:end]
                wordDFS([word] + sentence, start)

        wordDFS([], len(s))

        return ret