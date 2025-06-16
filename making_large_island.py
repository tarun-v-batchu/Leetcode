# Making a Large Island

# FAILED FROM TLE, BUT PASSED 64/75, prolly can be optimized, but looks like Python is just slow for this question

# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# Example 2:
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

# Example 3:
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 
# Constraints:
#   - n == grid.length
#   - n == grid[i].length
#   - 1 <= n <= 500
#   - grid[i][j] is either 0 or 1.


class UnionSet :
    def __init__(self, size) :
        self.parents = [i for i in range(size)]
        self.size = [1] * size
    
    def find_root(self, n) :
        if self.parents[n] == n :
            return n
        self.parents[n] = self.find_root(self.parents[n])
        return self.parents[n]

    def union_find(self, a, b) :
        a, b = self.find_root(a), self.find_root(b)
        if a == b :
            return a
        if self.size[a] >= self.size[b] :
            self.parents[b] = a
            self.size[a] += self.size[b]
        else :
            self.parents[a] = b
            self.size[b] += self.size[a]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        n = len(grid)
        m = len(grid[0])
        uf = UnionSet(n * m)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(x, y) :
            
            queue = deque()
            queue.append((x, y))

            while queue :
                x, y = queue.popleft()
                
                node = x * m + y
                visited.add((x, y))

                for dx, dy in dirs :
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or (nx, ny) in visited or grid[nx][ny] == 0 :
                        continue
                    # Atp we know (nx, ny) is also 1 so we can union-find
                    neighbor = nx * m + ny
                    uf.union_find(node, neighbor)
                    
                    queue += [(nx, ny)]
    
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 1 and (i, j) not in visited :
                    bfs(i, j)
        
        max_size = max(uf.size)
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 0 :
                    roots = set()
                    for dx, dy in dirs :
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]:
                            roots.add(uf.find_root(nx * m + ny))
                    total = 1 + sum([uf.size[x] for x in roots])
                    # print(i, j, total)
                    max_size = max(max_size, total)

        
        return max_size
