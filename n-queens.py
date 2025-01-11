# N-Queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]
 
# Constraints:
#   - 1 <= n <= 9


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(row_num, cols, front_diags, back_diags, n, ret, ret_all) :

            if n == 0 :
                ret_all += [["".join(i) for i in ret]]
                return ret_all

            if row_num >= len(cols) :
                return ret_all
            
            for i,b in enumerate(cols) :
                front_var = row_num - i + (len(cols)-1)
                back_var = row_num + i
                
                if not b and not front_diags[front_var] and not back_diags[back_var]:
                    
                    back_diags[back_var] = True
                    front_diags[front_var] = True
                    cols[i] = True
                    ret[row_num][i] = "Q"

                    ret_all = dfs(row_num + 1, cols, front_diags, back_diags, n-1, ret, ret_all)

                    back_diags[back_var] = False
                    front_diags[front_var] = False
                    cols[i] = False
                    ret[row_num][i] = '.'
            
            return ret_all

        rows = [False] * n
        cols = [False] * n
        front_diags = [False] * (2*n - 1)
        back_diags = [False] * (2*n - 1)
        ret = [["." for _ in range(n)] for _ in range(n)]
        ret_all = []

        for i in range(n) :
            ret_all = dfs(i, cols, front_diags, back_diags, n, ret, ret_all)
        
        return ret_all
