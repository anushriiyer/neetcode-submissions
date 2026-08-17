class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        i = 0
        j = len(heights)-1
        while i<j:
            new_vol = (j-i)*min(heights[i],heights[j])
            vol = max(vol,new_vol)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
            
        return vol
            


        