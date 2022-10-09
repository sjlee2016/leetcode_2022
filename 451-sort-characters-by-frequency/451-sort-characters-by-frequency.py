from collections import Counter, OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        
        if len(s) <= 1 :
            return str
        s = sorted(s) 
        ans = []
        prev = s[0]
        c = 1
        for i in range(1,len(s)) :
            if s[i] == prev :
                c+=1
            else :
                ans.append(prev*c)
                prev = s[i]
                c=1
        ans.append(c*s[-1])
        
        ans = sorted(ans,reverse=True, key=len)
        res = ''
        for letter in ans :
            res += letter
        return res