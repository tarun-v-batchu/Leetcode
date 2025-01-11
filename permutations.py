# Permutations

# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]
 

# Constraints:
#   - 1 <= nums.length <= 6
#   - -10 <= nums[i] <= 10
#   - All the integers of nums are unique.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
            
        def recurse(nums, visited, curr_list, total_list) :
            all_visited = True
            for i in range(len(nums)) :
                # print(visited)
                if not visited[i] :
                    temp_list = curr_list + [nums[i]]
                    temp_visited = visited.copy()
                    temp_visited[i] = True
                    total_list = recurse(nums, temp_visited, temp_list, total_list)
                    all_visited = False
            
            if all_visited :
                total_list += [curr_list]
            
            return total_list

        return recurse(nums, [False] * len(nums), [], [])

            
