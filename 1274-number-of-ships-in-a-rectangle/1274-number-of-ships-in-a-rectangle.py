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
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y :
            return 0 
        if sea.hasShips(topRight,bottomLeft) == False :
            return 0
        if bottomLeft.x == topRight.x and topRight.x == bottomLeft.x :
            return 1 
        
        bx = bottomLeft.x 
        by = bottomLeft.y 
        tx = topRight.x 
        ty = topRight.y 
        midX = (bx+tx)//2
        midY = (by+ty)//2 
        
        return self.countShips(sea,Point(midX,midY), bottomLeft) + self.countShips(sea,Point(midX,ty), Point(bx,midY+1)) + self.countShips(sea,Point(tx,midY), Point(midX+1,by)) + self.countShips(sea, topRight, Point(midX+1, midY+1))