class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = right = length = 0
        zeros = 0
        while right < len(nums) :
            if nums[right] == 0 :
                zeros+=1

            while zeros > k :
                if nums[left] == 0 :
                    zeros-=1
                left+=1

            right+=1
            length = max(length, right-left)

        return length


