# Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:
#   - 0 representing an empty cell,
#   - 1 representing a fresh orange, or
#   - 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
# Constraints:
#   - m == grid.length
#   - n == grid[i].length
#   - 1 <= m, n <= 10
#   - grid[i][j] is 0, 1, or 2.



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_oranges = []
        num_oranges = 0
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if grid[i][j] == 2 :
                    rotten_oranges += [(i, j)]
                    num_oranges += 1
                elif grid[i][j] == 1 :
                    num_oranges += 1
        
        if num_oranges == 0 :
            return 0
        
        i = 0
        turn_length = len(rotten_oranges)
        num_turns = -1

        while i < len(rotten_oranges) :
            x, y = rotten_oranges[i]
            if x > 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                rotten_oranges += [(x-1, y)]
            if x < len(grid) - 1 and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                rotten_oranges += [(x+1, y)]
            if y > 0 and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                rotten_oranges += [(x, y-1)]
            if y < len(grid[0]) - 1 and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                rotten_oranges += [(x, y+1)]

            i += 1
            if i == turn_length :
                num_turns += 1
                turn_length = len(rotten_oranges)

        print(len(rotten_oranges), num_oranges)
            
        return num_turns if len(rotten_oranges) == num_oranges else -1

