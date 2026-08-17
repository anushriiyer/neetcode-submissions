class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        for num in nums:
            countmap[num]=countmap.get(num,0)+1
        
        sorted_nums = sorted(countmap.keys(), key=lambda x: countmap[x], reverse=True)
        
        return sorted_nums[:k]
            


        