# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        visited = defaultdict(list)
        queue = [(root,0,0)]
        left = float('inf')
        right = float('-inf')
        while queue :
            node,row,col = queue.pop(0)
            if node :
                visited[col].append((node.val,row,col))
                left = min(left,col)
                right= max(right,col)
                queue.append((node.left, row+1,col-1))
                queue.append((node.right,row+1,col+1))
        res = []
        for i in range(left,right+1) :
            
            res.append([x[0] for x in sorted(visited[i], key=lambda x : x[1])])
        return res