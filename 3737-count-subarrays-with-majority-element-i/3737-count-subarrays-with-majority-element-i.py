class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for start_idx in range(len(nums)):
            non_targets_found = 0
            targets_found = 0
            for end_idx in range(start_idx, len(nums)):
                if nums[end_idx] == target:
                    targets_found += 1
                else:
                    non_targets_found += 1

                if targets_found > non_targets_found:
                    ans += 1

        return ans


"""
1,2,2,3
  |
      |
  |   |
ans=3 ?

[1,2]


nums=[1,2,2,3,3]
[1] - no
[1,2] - no
[1,2,2] - yes
[1,2,2,3] - no
[2] - yes
[2,2] - yes
[2,2,3] - yes
[2] - yes
[2,3] - no
[3] - no

3+2+1=6 checks
4+3+2+1=10 (checks)
5+4+3+2+1=15 (checks)
6+5+4+3=2+1=21 checks
O(n^2)




1,1,1,1
|
| |
|   |
|     |
  |
  | |
  |   |
  
4+3+2+1 = 10

"""
