class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count +=1
                continue
            product*=num
            if zero_count>1:
                break
        
        if zero_count>1:
            for i in range(len(nums)):
                nums[i] = 0
        
        elif zero_count ==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i] = product
                else: nums[i] = 0
        
        else:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
        return nums

        