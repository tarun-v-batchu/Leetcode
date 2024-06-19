# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# 
# Input: nums = [1, 2, 3, 3]
# Output: true
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not len(nums) :
            return False
         
        mini = min(nums)
        maxi = max(nums)

        arr = [False] * (maxi - mini + 1)

        for i in nums :
            if arr[i - mini] :
                return True
            arr[i - mini] = True

        return False
        
