class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        cur_sum, max_sum = float('-inf'), float('-inf')

        for i in range(len(nums)):
            if cur_sum > 0:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum
            
        return max_sum
