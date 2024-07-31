# Longest Subarray of 1's after Deleting One Element
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
#
# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
#
# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
# Constraints:
#   - 1 <= nums.length <= 105
#   - nums[i] is either 0 or 1.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        
        while j < len(nums) and nums[j] != 0:
            j += 1
        
        if j >= len(nums) :
            return len(nums) - 1
        # print(i, j)
        maxi = j - i
        j += 1 # i->j contains 1110x
        while j < len(nums):
            while j < len(nums) and nums[j] != 0:
                j += 1
            if j - i - 1 > maxi :
                # print(i, j)
                maxi = j - i - 1
            while i < len(nums) and nums[i] != 0:
                i+=1
            j += 1
            i += 1 # Now i->j contains 111...10
        
        return maxi

