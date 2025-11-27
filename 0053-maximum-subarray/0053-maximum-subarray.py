class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = float('-inf'), float('-inf')

        for i in nums:
            if cur_sum > 0:
                cur_sum += i
            else:
                cur_sum = i
            
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum