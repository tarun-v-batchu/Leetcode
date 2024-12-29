# Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:
#   - 1 <= nums.length <= 2 * 104
#   - -1000 <= nums[i] <= 1000
#   - -107 <= k <= 107


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        psum = 0
        mapa = defaultdict(int)
        mapa[0] = 1

        for i in nums :
            psum += i
            if psum - k in mapa :
                count += mapa[psum - k]
            if psum in mapa.keys() :
                mapa[psum] += 1
            else :
                mapa[psum] = 1
                        
        return count
