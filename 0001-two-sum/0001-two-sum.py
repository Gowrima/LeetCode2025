from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_ = defaultdict(int)

        for i in range(len(nums)):
            if target-nums[i] in dict_:
                return i, dict_[target-nums[i]]
            else:
                dict_[nums[i]] = i

        return -1, -1        
            