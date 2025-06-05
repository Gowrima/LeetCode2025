from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ = defaultdict()
        result = tuple()

        for i in range(len(nums)):
            to_find = target-nums[i]

            if to_find in hash_:
                result = (i, hash_[to_find])
                break
            
            hash_[nums[i]] = i
        
        return result
        