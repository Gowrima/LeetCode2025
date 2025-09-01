from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Construct the hash map between nums and their indices
        map = defaultdict()

        for i in range(len(nums)):
            if (not nums[i] in map):
                map[nums[i]] = [i]
            else:
                map[nums[i]].append(i)

        # Go through the elements of nums, and find its corresponding index pair

        for i in range(len(nums)):
            if (target - nums[i] in map):
                if (len(map[target - nums[i]]) > 1 and target == nums[i]*2):
                    return map[nums[i]][:2]
                elif (len(map[target - nums[i]]) == 1 and target == nums[i]*2):
                    continue
                else:
                    return [i, map[target - nums[i]][0]]