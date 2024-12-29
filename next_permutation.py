# Next Permutation

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], 
# [2, 3, 1], [3,1,2], [3,2,1]. The next permutation of an array of integers is the next lexicographically greater 
# permutation of its integer. More formally, if all the permutations of the array are sorted in one container 
# according to their lexicographical order, then the next permutation of that array is the permutation that follows 
# it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest 
# possible order (i.e., sorted in ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger 
# rearrangement. Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
#
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
#
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
#
# Constraints:
#   - 1 <= nums.length <= 100
#   - 0 <= nums[i] <= 100


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def selection_sort_in_place(arr, start, end): 
            for i in range(start, end): 
                min_index = i 
                for j in range(i + 1, end): 
                    if arr[j] < arr[min_index]: 
                        min_index = j # Swap the found minimum element with the first element 
                arr[i], arr[min_index] = arr[min_index], arr[i]
        
        if len(nums) <= 1 :
            return nums
        
        j = len(nums) - 1
        
        while j > 0 and nums[j-1] >= nums[j] :
            j -= 1
        if j == len(nums) - 1 :
            temp = nums[-1]
            nums[-1] = nums[-2]
            nums[-2] = temp
        else :
            # max_under_j = -1
            # for i in nums[j+1:] :
            #     if i > max_under_j

            # If j == 0 then just sort nums and thats it
            if j == 0 :
                nums.sort()
                return
            # Find next highest in nums[j:]
            next_highest_i = j
            i = j
            while i < len(nums) :
                # print(nums[i], nums[j-1], nums[next_highest_i])
                if nums[i] > nums[j-1] and nums[i] < nums[next_highest_i] :
                    next_highest_i = i
                i += 1
            # print(next_highest_i)

            # Sort nums[j:] excluding the next highest value
            # print([nums[next_highest_i]] + sorted(nums[j-1:next_highest_i] + nums[next_highest_i + 1:]))
            temp = nums[j-1]
            nums[j-1] = nums[next_highest_i]
            nums[next_highest_i] = temp
            # print(nums, j , len(nums))

            selection_sort_in_place(nums, j, len(nums))
            




        
