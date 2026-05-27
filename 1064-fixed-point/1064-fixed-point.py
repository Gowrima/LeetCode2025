class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        result = -1
        left, right = 0, len(arr)-1

        while left<=right:
            mid = (right+left)//2

            if arr[mid] == mid:
                result = mid
                right = mid-1
            elif arr[mid] < mid:
                left = mid+1
            else:
                right = mid-1
        
        return result
        