# Minimum Array Length after Pair Removals

# Given an integer array num sorted in non-decreasing order.
# You can perform the following operation any number of times:

# Choose two indices, i and j, where nums[i] < nums[j].
# Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
# Return the minimum length of nums after applying the operation zero or more times.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 2:
# Input: nums = [1,1,2,2,3,3]
# Output: 0

# Example 3:
# Input: nums = [1000000000,1000000000]
# Output: 2
# Explanation:
# Since both numbers are equal, they cannot be removed.

# Example 4:
# Input: nums = [2,3,4,4,4]
# Output: 1


# Constraints:
#   - 1 <= nums.length <= 105
#   - 1 <= nums[i] <= 109
#   - nums is sorted in non-decreasing order.


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        for i in nums :
            freq[i] += 1
        
        m = max(freq.values())

        if m * 2 > len(nums) :
            return 2 * m - len(nums)
        
        return len(nums) % 2
