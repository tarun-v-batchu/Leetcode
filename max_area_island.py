# Max Area of Island

# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:
# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]
# Output: 6
# Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

# Constraints:
#   - 1 <= grid.length, grid[i].length <= 50


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, x, y, visited) :
            # print(x, y)
            if visited[x][y] or grid[x][y] == 0:
                return visited, 0
            
            visited[x][y] = True
            count = 0
            if x > 0:
                visited, num = dfs(grid, x - 1, y, visited)
                count += num
            if y > 0 :
                visited, num = dfs(grid, x, y - 1, visited)
                count += num
            if x < len(grid) - 1 :
                visited, num = dfs(grid, x + 1, y, visited)
                count += num
            if y < len(grid[0]) - 1 :
                visited, num = dfs(grid, x, y + 1, visited)
                count += num
            
            return visited, count + 1
        
        maximum = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                # print(i, j)
                visited, area = dfs(grid, i, j, visited)
                maximum = max(maximum, area)
        
        return maximum
