class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = {}
        for num in nums:
            number[num]=number.get(num,0)+1
        
        for key, val in number.items():
            if val>1:
                return True
        
        return False

         