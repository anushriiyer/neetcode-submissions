class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        res = 0
        imax, jmax = height[i],height[j]
        while i<j:
            if height[i]<height[j]:
                i+=1
                imax = max(imax,height[i])
                res += imax - height[i]
            else:
                j-=1
                jmax = max(jmax,height[j])
                res+=jmax - height[j]
        return res

        