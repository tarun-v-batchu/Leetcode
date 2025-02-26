# Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 
# Constraints:
#   - m == board.length
#   - n = board[i].length
#   - 1 <= m, n <= 6
#   - 1 <= word.length <= 15
#   - board and word consists of only lowercase and uppercase English letters.
 
# Follow up: Could you use search pruning to make your solution faster with a larger board?


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(board, x, y, word, index) :
            found = False

            if index == len(word) :
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]) :
                return False
            if board[x][y] != word[index] or (x, y) in path:
                return False
            
            path.add((x, y))
            ret = (dfs(board, x + 1, y, word, index+1) or dfs(board, x - 1, y, word, index+1) or dfs(board, x, y + 1, word, index+1) or dfs(board, x, y-1, word, index+1))
            path.remove((x, y))
            return ret

        # print(len(board), len(board[0]))
        for i in range(len(board)) :
            for j in range(len(board[i])) :
                if dfs(board, i, j, word, 0) :
                    return True
        
        return False
            

