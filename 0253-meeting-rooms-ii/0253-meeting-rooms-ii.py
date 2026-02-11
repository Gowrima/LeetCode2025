class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
            
        heap = []
        intervals.sort()
        #print (intervals)
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i][1])
    
        return len(heap)
                    