from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ = defaultdict()
        res = tuple()

        for i in range(len(nums)):
            to_find = target - nums[i]       
            
            if to_find in hash_:
                res = (hash_[to_find], i)
            else:
                hash_[nums[i]] = i

        return res
