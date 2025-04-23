# Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output:
# true

# Example 2:
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output:
# false

# Note:
#   - You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Constraints:
#   - 1 <= n <= 100
#   - 0 <= edges.length <= n * (n - 1) / 2


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        pres = defaultdict(list)

        for to, fro in edges :
            pres[to] += [fro]
            pres[fro] += [to]

        visited = set()
        seen = set()
        def recurse(s, prev) :
            if s in visited :
                print(s, "found", visited)
                return False

            visited.add(s)

            for i in pres[s] :
                if i == prev :
                    continue
                if not recurse(i, s) :
                    print("error found at", s, "pointing at", i)
                    return False
            
            return True
        

        return recurse(0, -1) and len(visited) == n
        
