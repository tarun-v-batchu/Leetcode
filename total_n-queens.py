# Total N-Queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

# Example 2:
# Input: n = 1
# Output: 1
 
# Constraints:
#   - 1 <= n <= 9

class Solution:
    def totalNQueens(self, n: int) -> int:
        

        def dfs(row_num, cols, front_diags, back_diags, n, ret) :

            if n == 0 :
                return 1

            if row_num >= len(cols) :
                return 0
            
            count = 0
            for i,b in enumerate(cols) :
                front_var = row_num - i + (len(cols)-1)
                back_var = row_num + i
                
                if not b and not front_diags[front_var] and not back_diags[back_var]:
                    
                    back_diags[back_var] = True
                    front_diags[front_var] = True
                    cols[i] = True
                    ret[row_num][i] = "Q"

                    count += dfs(row_num + 1, cols, front_diags, back_diags, n-1, ret)

                    back_diags[back_var] = False
                    front_diags[front_var] = False
                    cols[i] = False
                    ret[row_num][i] = '.'
            
            return count

        rows = [False] * n
        cols = [False] * n
        front_diags = [False] * (2*n - 1)
        back_diags = [False] * (2*n - 1)
        ret = [["." for _ in range(n)] for _ in range(n)]
        ret_all = []
        count = 0
        for i in range(n) :
            count += dfs(i, cols, front_diags, back_diags, n, ret)
        
        return count
