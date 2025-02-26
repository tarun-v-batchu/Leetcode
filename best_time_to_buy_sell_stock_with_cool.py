# Best Time to Buy and Sell Stock with Cooldown

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may buy and sell one NeetCoin multiple times with the following restrictions:
#   - After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is 
#   a cooldown period of one day).
#   - You may only own at most one NeetCoin at a time.
# You may complete as many transactions as you like.

# Return the maximum profit you can achieve.

# Example 1:
# Input: prices = [1,3,4,0,4]
# Output: 6
# Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

# Example 2:
# Input: prices = [1]
# Output: 0
# Constraints:
#   - 1 <= prices.length <= 5000
#   - 0 <= prices[i] <= 1000

# 1.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[0 for i in range(len(prices) + 1)] for i in range(len(prices) + 1)]

        for i in range(1, len(prices) + 1) :
            for j in range(i, len(prices) + 1) :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], prices[j - 1] - prices[i - 1])
                if i >= 2 :
                    # print(i, j, ":", prices[i-1], prices[j-1], " - ", dp[i][j], dp[i-2][i-2], prices[j - 1] - prices[i - 1])
                    dp[i][j] = max(dp[i][j], dp[i-2][i-2] + prices[j - 1] - prices[i - 1])
        # print(dp)
        return dp[-1][-1]
