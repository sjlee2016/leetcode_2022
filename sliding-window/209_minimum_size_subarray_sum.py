class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = right = 0
        total = 0
        length = sys.maxint

        for right in range(len(nums)) :
            total += nums[right]
            while total >= target :
                length = min(length,right-left+1)
                total -= nums[left]
                left+=1


