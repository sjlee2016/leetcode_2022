class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def add(idx,path) :
            ans.append(list(path))
            if idx == len(nums)-1 :
                return 
            
            for i in range(idx+1,len(nums)) :
                path.append(nums[i])
                add(i,path)
                path.pop()
        
        add(-1,[])
        return ans