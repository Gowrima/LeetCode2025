class Solution:
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        
        while lo<=hi:
            mid = lo + (hi-lo)//2

            #print ("mid = ", mid, "low = ", lo, "high = ", hi)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1

        return lo
        



        
            
        
            
        