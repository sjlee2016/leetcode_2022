# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        tx, ty = topRight.x, topRight.y
        bx, by = bottomLeft.x, bottomLeft.y
        
        if tx < bx or ty < by :
            return 0
        if sea.hasShips(topRight,bottomLeft) == False :
            return 0
        if tx == bx and ty == by :
            return 1 
        midx = (tx+bx)//2
        midy = (ty+by)//2
        ## else.. find by divide and conquer 
        W1 = self.countShips(sea,Point(midx,midy),bottomLeft) ## correct
        W2 = self.countShips(sea,Point(midx,ty), Point(bx,midy+1))
        W3 = self.countShips(sea,Point(tx,midy), Point(midx+1,by))
        W4 = self.countShips(sea,topRight, Point(midx+1,midy+1)) ## correct
        return W1+W2+W3+W4
    
        