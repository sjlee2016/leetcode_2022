class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h :
            return max(piles)
        left = 1 
        right = max(piles)
        ans = float('inf')
        while left <= right :
            mid = (left + right)//2
            hr = 0
            for i in range(len(piles)) :
                if mid > piles[i] :
                    hr += 1
                else :
                    hr += piles[i]//mid
                    if piles[i] % mid > 0 :
                        hr+=1 
            if hr <= h :
                ans = min(ans,mid)
                right = mid-1
            else :
                left = mid+1
        
        return ans