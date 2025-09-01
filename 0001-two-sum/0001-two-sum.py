class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict()
        result = tuple()

        for i in range(len(nums)):
            to_find = target - nums[i]

            if to_find in map:
                result = (map[to_find], i)
            else:
                map[nums[i]] = i
        
        return result
