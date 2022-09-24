from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        start = 0
        end = 0
        count = Counter()
        while end < len(s) :
            count[s[end]]+=1
            while count[s[end]] > 1 :
                count[s[start]]-=1
                start+=1
            length = max(length, end-start+1)
            end+=1
        return length

