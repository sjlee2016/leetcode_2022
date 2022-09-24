from collections import Counter
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = 0
        counter = Counter()
        maxLength = 0
        left = 0
        right = 0
        numDistinct = 0


        while right < len(s) :
            if counter[s[right]] == 0 : // first seen
                numDistinct += 1  // increment
            counter[s[right]]+=1  // count letter
            while numDistinct > k : // while num distinct is larger
                counter[s[left]]-=1 // move left pointer, decrement count
                if counter[s[left]] == 0 : // now the letter is not counted
                    numDistinct-=1 // decrement numDistinct
                left+=1
            maxLength = max(maxLength, right-left+1)
            right+=1
        return maxLength

