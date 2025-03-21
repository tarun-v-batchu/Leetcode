# House Robber 2

# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this 
# place are arranged in a circle. That means the first house is the 
# neighbor of the last one. Meanwhile, adjacent houses have a security 
# system connected, and it will automatically contact the police if two 
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each 
# house, return the maximum amount of money you can rob tonight without 
# alerting the police.

 

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 
# (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3


class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums) :
            if len(nums) == 0 :
                return 0
            if len(nums) == 1 :
                return nums[0]
            list = [0] * (len(nums))
            list[0] = nums[0]
            list[1] = max(nums[0], nums[1])
            i = 2
            while i < len(nums):
                list[i] = max(list[i - 1], list[i - 2] + nums[i])
                i += 1
            return list[-1]
        if len(nums) == 0 :
            return 0
        if len(nums) == 1 :
            return nums[0]
        max_one = house_robber(nums[:len(nums) - 1])
        max_two = house_robber(nums[1:])
        
        return max(max_one, max_two)
