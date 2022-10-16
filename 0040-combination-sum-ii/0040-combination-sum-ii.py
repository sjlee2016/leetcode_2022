class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        
        ans = []
        visited = {}
        
        def visit(s,start,comb,nums) :
           
            if s == target :
                ans.append(comb[:])
                return
            
            for idx in xrange(start,len(nums)) : 
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue

                if candidates[idx] + s > target :
                    return 
                
                m = nums[:idx]+nums[idx+1:]
                comb.append(nums[idx])
                visit(s+nums[idx],idx,comb,m)
                comb.pop()
                
        visit(0,0,[],candidates)
        return ans