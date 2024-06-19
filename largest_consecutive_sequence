# Given an array of integers nums, return the length of the longest consecutive sequence of elements.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].
# 
# Example 2:
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7
#
# Constraints:
#   - 0 <= nums.length <= 1000
#   - -10^9 <= nums[i] <= 10^9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 :
            return 0

        mini = min(nums)
        maxi = max(nums)

        arr = [0] * (maxi - mini + 1)
        for i in nums :
            arr[i-mini]+=1
        
        print(arr)
        
        max_seq = -1
        curr_seq = 0
        for i in arr :
            # print(max_seq)
            if i == 0 :
                if max_seq < curr_seq :
                    max_seq = curr_seq
                curr_seq = 0
            else :
                # print(i, curr_seq)
                curr_seq += 1

        return max_seq if max_seq > curr_seq else curr_seq
