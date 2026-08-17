class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for a in range(len(nums)-2):
            for b in range(a+1,len(nums)-1):
                for c in range(b+1,len(nums)):
                    if nums[a]+nums[b]+nums[c] == 0:
                        val = sorted([nums[a],nums[b],nums[c]])
                        if val in result:
                            continue
                        result.append(val)           
        return result
                    
            

        