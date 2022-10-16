class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(s)) :
            if len(stack) == 0 or stack[-1][0] != s[i] :
                stack.append([s[i],1])
            else :
                stack[-1][1]+=1
                if stack[-1][1] == k :
                    stack.pop()
        
        return "".join(c*x for c,x in stack)