# Number of Closed Islands
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 
# 4-directionally connected group of 0s and a closed island is an island totally 
# (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

# Example 1:
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).

# Example 2:
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1

# Example 3:
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
 

# Constraints:
#   - 1 <= grid.length, grid[0].length <= 100
#   - 0 <= grid[i][j] <=1


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        def bfs(x, y) :
            queue = deque()
            queue.append((x, y))
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            is_closed = True
            while queue :
                x, y = queue.popleft()
                if (x, y) in visited or grid[x][y] == 1 :
                    continue
                visited.add((x, y))

                for dx, dy in dirs :
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) :
                        is_closed = False
                        continue
                    queue += [(nx, ny)]
            return is_closed
    

        islands = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 and (i, j) not in visited and bfs(i, j) :
                    islands += 1
        
        return islands
