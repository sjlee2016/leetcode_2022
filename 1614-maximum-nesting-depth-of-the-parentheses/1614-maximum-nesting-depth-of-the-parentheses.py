class Solution:
    def maxDepth(self, s: str) -> int:
        left = 0
        ans = 0
        for i in range(len(s)) :
            if s[i] == "(" :
                left += 1 
                ans = max(ans,left)
            elif s[i] == ")" :
                left-=1
        return ans