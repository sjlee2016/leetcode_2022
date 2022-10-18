class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftBracket = 0
        maxBracket = 0
        for i in range(len(s)) :
            if s[i] == "(" :
                leftBracket+=1
                maxBracket = max(maxBracket , leftBracket)
            elif s[i] == ")" :
                leftBracket-=1
                
        if maxBracket == float('-inf') :
            return 0
        return maxBracket