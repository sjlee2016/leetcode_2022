import heapq
class Solution:
    def getDistance(self,worker,bike) :
        return abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
    
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        heap = []
        dist = {}
        visited = set()
        ans = [0 ]* len(workers) 
        for i in range(len(workers)) :
            dist_bikes = []
            for j in range(len(bikes)) :
                dist_bikes.append((self.getDistance(workers[i],bikes[j]),i,j))
            dist_bikes.sort(reverse=True)
            heap.append(dist_bikes.pop())
            dist[i] = dist_bikes
        heapq.heapify(heap)
        while heap :
            distance, worker, bike = heapq.heappop(heap)
            if bike in visited :
                heapq.heappush(heap,dist[worker].pop())
            else :
                ans[worker] = bike
                visited.add(bike)
        return ans
                