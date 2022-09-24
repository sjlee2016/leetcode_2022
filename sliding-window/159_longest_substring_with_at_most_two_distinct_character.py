from collections import Counter
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = maxLength = 0
        counter = Counter()
        numDistinct = 0
        while right < len(s) :
            if counter[s[right]] == 0 :
                numDistinct+=1
            counter[s[right]]+=1

            while numDistinct > 2 :
                counter[s[left]]-=1
                if counter[s[left]]==0 :
                    numDistinct-=1
                left+=1
            maxLength = max(maxLength,right-left+1)
            right+=1
        return maxLength

