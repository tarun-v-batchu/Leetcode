# Merge Intervals
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# Constraints:
#   - 1 <= intervals.length <= 104
#   - intervals[i].length == 2
#   - 0 <= starti <= endi <= 104


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        arr = sorted(intervals, key = lambda x: x[0])
        i = 0
        while i < len(arr) - 1 :
            if arr[i][1] >= arr[i+1][0] :
                arr[i][1] = max(arr[i][1], arr[i+1][1])
                arr.pop(i+1)
            else :
                i += 1
        return arr
