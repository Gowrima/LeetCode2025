from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        
        for i in range(len(nums)):
            to_find = target-nums[i]

            if to_find in d:
                return [d[to_find], i]
            
            d[nums[i]] = i