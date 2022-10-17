from heapq import *
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals :
            return 0
        
        intervals = sorted(intervals, key = lambda x : x[0])
        free_rooms = []
        
        heapq.heappush(free_rooms,intervals[0][1])
        
        for i in range(1,len(intervals)) :
            currentStartTime = intervals[i][0]
            currentEndTime = intervals[i][1]
            
            if free_rooms[0] <= currentStartTime :
                heapq.heappop(free_rooms) ## time to free
            heapq.heappush(free_rooms, currentEndTime)
        
        return len(free_rooms)
            
        