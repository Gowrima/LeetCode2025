from typing import List
from itertools import count

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        for i in count(1):
            x = k * i
            if x not in seen:
                return x
