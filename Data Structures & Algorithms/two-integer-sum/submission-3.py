class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num]=i
        
        for value, key in enumerate(nums):
            diff = target-key
            if diff in hashmap and hashmap[diff]!=value:
                return [value, hashmap.get(diff)]
