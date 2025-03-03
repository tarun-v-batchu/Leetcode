# Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 
# Constraints:
#   - m == grid.length
#   - n == grid[i].length
#   - 1 <= m, n <= 300
#   - grid[i][j] is '0' or '1'.


class Solution:

    def numIslands(self, grid):
        
        def dfs(grid, i, j, visited) :
            # print(i, j, visited[i][j], grid[i][j] != 1)
            if visited[i][j] or grid[i][j] != "1":
                return visited
            # print("dfs")
            
            visited[i][j] = True
            if i > 0 and not visited[i - 1][j]:
                visited = dfs(grid, i - 1, j, visited)
            if i < len(visited) - 1 and not visited[i + 1][j]:
                visited = dfs(grid, i + 1, j, visited)
            if j < len(visited[i]) - 1 and not visited[i][j + 1]:
                visited = dfs(grid, i, j + 1, visited)
            if j > 0 and not visited[i][j - 1]:
                visited = dfs(grid, i, j - 1, visited)
            return visited

        visited = [[False for _ in grid[0]] for _ in grid]
        num_islands = 0
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                # print(grid[i][j], visited[i][j])
                if grid[i][j] == '1' and not visited[i][j] :
                    # print("looking")
                    visited = dfs(grid, i, j, visited)
                    num_islands += 1
                    # print(visited)
        return num_islands
                


