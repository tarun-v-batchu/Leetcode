# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
#   - 2 <= nums.length <= 105
#   - -30 <= nums[i] <= 30
#   - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        back = []
        for_product = 1
        back_product = 1
        for i in nums:
            for_product *= i
            forward.append(for_product)
        i = len(nums) - 1
        while i >= 0 :
            back_product *= nums[i]
            back.insert(0, back_product)
            i-=1        
        ret_arr = []
        ret_arr.append(back[1])
        i = 1
        while i < len(forward) - 1 :
            ret_arr.append(forward[i-1]*back[i+1])
            i+=1
        ret_arr.append(forward[-2])
        return ret_arr
