class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            return
        
        i = 0
        
        for j in range(len(nums)):
            if nums[j] != val:
                # copy only if it's not equal to val because
                # nums[j] == val has to be removed
                nums[i] = nums[j]
                i = i+1
                
        return i
                
        