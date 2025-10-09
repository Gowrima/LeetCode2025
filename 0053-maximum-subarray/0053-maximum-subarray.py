class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]

            if curSum > maxSum:
                maxSum = curSum
        
        return maxSum
                
