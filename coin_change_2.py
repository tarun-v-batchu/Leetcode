# Coin Change 2

# You are given an integer array coins representing coins of different denominations 
# (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the number of distinct combinations that total up to amount. If it's impossible to 
# make up the amount, return 0. You may assume that you have an unlimited number of each coin 
# and that each value in coins is unique.

# Example 1:
# Input: amount = 4, coins = [1,2,3]
# Output: 4
# Explanation:
# 1+1+1+1 = 4
# 1+1+2 = 4
# 2+2 = 4
# 1+3 = 4

# Example 2:
# Input: amount = 7, coins = [2,4]
# Output: 0

# Constraints:
#   - 1 <= coins.length <= 100
#   - 1 <= coins[i] <= 1000
#   - 0 <= amount <= 1000


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[1]+[0 for _ in range(amount)] for _ in range(len(coins) + 1)]

        for i in range(1, len(coins) + 1) :
            for j in range(1, amount + 1) :
                # print(i, j, dp[i][j - coins[i - 1]])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j] + dp[i][j - coins[i - 1]] if j - coins[i-1] >= 0 else 0)
        
        print(dp)
        return dp[-1][-1]
