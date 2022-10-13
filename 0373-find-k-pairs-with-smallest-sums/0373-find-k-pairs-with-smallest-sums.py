from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i = j = 0
        heap = [(nums1[0] + nums2[0], (0, 0))]
        result = []
        count = 0
        while count < k and heap:
            value, (i, j) = heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j+1], (i, j+1)) )   
            if j == 0 and i + 1 < len(nums1):
                heappush(heap, (nums1[i+1] + nums2[j], (i+1, j)) )   
            count += 1
        return result