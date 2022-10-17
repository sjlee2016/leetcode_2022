class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [ False ] * (len(s) + 1)
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(len(s)+1) :
            for j in range(i) :
                currentString = s[j:i]
                if dp[j] == True and currentString in wordSet :
                    dp[i]  = True
                    break
                    
        return dp[len(s)]