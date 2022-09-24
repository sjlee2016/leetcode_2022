class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1 : return 0
        distinct = 0
        left = 0
        product = 1
        ans = 0
        for right in range(len(nums)) :
            product *= nums[right]
            while product >= k :
                product /= nums[left]
                left+=1
            ans += right-left+1

        return ans


