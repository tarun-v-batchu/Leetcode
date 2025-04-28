# Trapping Rain Water
#
# You are given an array non-negative integers heights which represent an elevation map. Each value heights[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.
#
# Example 1:
# Input: height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9
# 
# Constraints:
#   - 1 <= height.length <= 1000
#   - 0 <= height[i] <= 1000

class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        area = 0
        stack = []
        while i < len(height) and height[i] == 0:
            i+=1
        if i >= len(height) :
            return 0
        
        while i < len(height) :
            j = i + 1
            index = -1
            maxi = -1
            while j < len(height) :
                if height[i] <= height[j] :
                    maxi = height[j]
                    index = j
                    break
                if height[j] > maxi :
                    index = j
                    maxi = height[j]
                j+=1
            # Two borders and water is between i and index
            if index == -1 :
                break

            total_box = min(height[i], height[index]) * (index - i - 1)
            j = i + 1
            while j < index :
                total_box -= height[j]
                j += 1
            area += total_box
            i = index

        return area

# Trapping Rain Water
# Given n non-negative integers representing an elevation 
# map where the width of each bar is 1, compute how much 
# water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
#   - n == height.length
#   - 1 <= n <= 2 * 104
#   - 0 <= height[i] <= 105


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        total, max_left, max_right = 0, 0, 0
        while left < right :
            if height[left] < height[right] :
                max_left = max(max_left, height[left])
                total += (max_left - height[left])
                left += 1
            else :
                max_right = max(max_right, height[right])
                total += (max_right - height[right])
                right -= 1
        return total




