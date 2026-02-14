class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        
        result = [intervals[0]]  # [1,8]
        j = 1

        # [1,8],[2,6],[7,10]
        #
        # 1      8
        # |------|      Result[i]
        #      |-----|  Interval[j]
        #      ?     X
        while j < len(intervals):
            # comapre result with intervals[j]
            # [1,6], [8,10]
            if intervals[j][0] <= result[-1][1]:
                new_interval = [
                    min(intervals[j][0], result[-1][0]),
                    max(intervals[j][1], result[-1][1]),
                ]
                # [1,8]
                result.pop()
                result.append(new_interval)  # [1,10]
            else:
                result.append(intervals[j])

            j += 1  # 2,

        return result
