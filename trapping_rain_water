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

