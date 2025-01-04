# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
#   - nums1.length == m
#   - nums2.length == n
#   - 0 <= m <= 1000
#   - 0 <= n <= 1000
#   - 1 <= m + n <= 2000
#   - -106 <= nums1[i], nums2[i] <= 106

import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = nums1 + nums2
        if len(arr) == 1 :
            return arr[0]
        
        max_heap = [-min(arr[0], arr[1])]    # First half of elements
        min_heap = [max(arr[0], arr[1])]   # Second half of elements

        i = 2
        
        print(arr)

        while i < len(arr) :

            if len(min_heap) > len(max_heap) :
                # Put into the min heap
                heapq.heappush(min_heap, arr[i])
                rem_elem = heapq.heappop(min_heap)
                heapq.heappush(max_heap, 0 - rem_elem)

            else :
                heapq.heappush(max_heap, 0 - arr[i])
                rem_elem = heapq.heappop(max_heap)
                # print("Pushing rem_elem into max_heap:", arr[i])
                heapq.heappush(min_heap, 0 - rem_elem)
            # print("After")
            # print(min_heap)
            # print(max_heap)
            
            i += 1
        # print("max_heap:", max_heap)
        # print("min_heap: ", min_heap)
        if len(max_heap) == len(min_heap) :
            return ((0 - max_heap[0]) + min_heap[0])/2
        elif len(max_heap) > len(min_heap) :
            return max_heap[0]
        else :
            return min_heap[0]
                



