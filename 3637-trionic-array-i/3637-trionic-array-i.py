class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        """
        p, q = -1, -1

        # 0..p incr
        # p..q decr
        # q..n incr

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False

            if p < 0 and nums[i] > nums[i+1]:
                p = i
                continue

            if p > 0 and nums[i] < nums[i+1]:
                q = i
                break

        if p < 0 and q < 0:
            return False

        i = 0

        while i<p-1:
            if nums[i] > nums[i+1]:
                return False
            i += 1

        i = p

        while i<q-1:
            if nums[i] < nums[i+1]:
                return False
            i += 1

        i = q

        while i<len(nums)-1:
            if nums[i] > nums[i+1]:
                return False
            i += 1

        return True
        """
        if nums[1] <= nums[0]:
            return False
        if nums[-1] <= nums[-2]:
            return False

        section = 1
        # 1 = must be increasing
        # 2 = must be decreasing
        # 3 = must be increasing
        # ...

        # [1,3,5,4,2,6]
        for ii in range(len(nums) - 1):
            if nums[ii] == nums[ii + 1]:
                return False

            elif nums[ii] < nums[ii + 1]:
                if section % 2 == 1:
                    continue
                else:
                    section += 1

            else:  # nums[ii] > nums[ii+1]:
                if section % 2 == 1:
                    section += 1
                else:
                    continue

        return section == 3
