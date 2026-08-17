class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1,max(piles)
        finalk = low

        while low<=high:
            k = (low + high) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            
            if totalTime<=h:
                finalk = k
                high = k-1
            else:
                low = k+1
        return finalk

