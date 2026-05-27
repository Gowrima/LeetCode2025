class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # expected_value = 0
        # for idx, num in enumerate(arr):
        #     if num == expected_value:
        #         return idx
        #     expected_value += 1
        # return -1

        left = 0
        right = len(arr) - 1

        ans = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            if mid == arr[mid]:
                ans = min(ans, mid)
                right = mid - 1

            # condition 1: search left
            elif mid < arr[mid]:
                right = mid - 1

            # condition 2: search right
            # else: mid < arr[mid]:
            else:
                left = mid + 1

        if ans == float("inf"):
            return -1
        return ans


"""
  0   1  2  3  4
-10, -5, 0, 3, 7


  0   1  2  3  4
-10,  1, 3, 3, 7

  0   1  2  3  4
-10, -5, 3, 3, 7


0 1 2 3 4
0 1 2 3 4
"""
