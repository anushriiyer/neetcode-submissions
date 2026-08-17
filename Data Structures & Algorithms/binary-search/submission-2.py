class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        middle = (len(nums)//2)
        
        if target==nums[middle]:
            return middle
        
        elif target<nums[middle]:
            new_list = nums[:middle]
            result = self.search(new_list,target)
            return result if result == -1 else result

        else:
            new_list = nums[middle+1:]
            result = self.search(new_list,target)
            return result if result == -1 else middle + 1 + result
