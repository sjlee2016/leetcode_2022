"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    
    def flattenDFS(self,prev,curr) :
        if curr is None :
            return prev 
        curr.prev = prev 
        prev.next = curr 
        
        temp = curr.next 
        tail = self.flattenDFS(curr,curr.child)
        curr.child = None 
        return self.flattenDFS(tail,temp)
        
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None :
            return None
        pseudoHead = Node(None,None,head,None)
        self.flattenDFS(pseudoHead,head)
        
        pseudoHead.next.prev = None
        return pseudoHead.next 