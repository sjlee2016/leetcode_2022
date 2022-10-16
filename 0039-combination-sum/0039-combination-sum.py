class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        
        output = []
        def check(index,path,s) :
            if s == target :
                m = sorted(list(path))
                if m not in output :
                    output.append(m)
                    return 
            if s > target :
                return 
            
            for i in range(len(candidates)) :
                path.append(candidates[i])
                check(i,path,s+candidates[i])
                path.pop()
        
        
        check(-1,[],0)
        
        return output