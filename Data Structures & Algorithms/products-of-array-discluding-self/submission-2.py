class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        result = [0]*len(nums)
        for i in range(len(nums)):
            product = 1
            j = i
            while j!=0:
                product*=nums[j]
                j-=1
            product *=nums[0]
            prefix[i]=product
        
        for i in range(len(nums)-1,-1,-1):
            product = 1
            j = i
            while j!=len(nums)-1:
                product*=nums[j]
                j+=1
            product *=nums[len(nums)-1]
            suffix[i]=product


        for i in range(len(nums)):
            preval = prefix[i-1] if i>0 else 1
            sufval = suffix[i+1] if i+1<len(nums) else 1
            result[i]=preval*sufval
        return result
            
