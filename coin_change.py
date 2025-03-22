# Coin Change
# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of 
# money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Constraints:
#   - 1 <= coins.length <= 12
#   - 1 <= coins[i] <= 231 - 1
#   - 0 <= amount <= 104


class Solution:
    def coinChange(self, coins, amount) -> int :
        dp = [0]
        i = 1
        while i <= amount :
            val = -1
            for coin in coins :
                if i - coin < 0 or dp[i - coin] == -1 :
                    continue
                if val == -1 :
                    val = dp[i - coin] + 1
                else :
                    val = min(dp[i - coin] + 1, val)
            dp += [val]
            i += 1
        return dp[-1]
