# Meeting Rooms 2
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return 
# the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1
 
# Constraints:
#   - 1 <= intervals.length <= 104
#   - 0 <= starti < endi <= 106


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda x:x[0])
        num_conf = 0
        heap = []
        
        for inter in intervals :
            while heap and inter[0] >= heap[0] :
                heapq.heappop(heap)
            heapq.heappush(heap, inter[1])
            num_conf = max(num_conf, len(heap))
        
        return num_conf

