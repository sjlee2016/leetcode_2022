class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        ans = []
        
        def backtrack(index,path) :
            if index > len(nums) :
                return
            m = list(sorted(path))
            if m not in ans :
                ans.append(m)
            
            for i in range(index+1, len(nums)) :
                path.append(nums[i])
                backtrack(i,path)
                path.pop()
        
        backtrack(-1,[])
        return ans
            