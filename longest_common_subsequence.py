# Longest Common Subsequence

# Given two strings text1 and text2, return the length of the longest common subsequence between 
# the two strings if one exists, otherwise return 0.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements 
# without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# A common subsequence of two strings is a subsequence that exists in both strings.

# Example 1:
# Input: text1 = "cat", text2 = "crabt" 
# Output: 3 
# Explanation: The longest common subsequence is "cat" which has a length of 3.

# Example 2:
# Input: text1 = "abcd", text2 = "abcd"
# Output: 4

# Example 3:
# Input: text1 = "abcd", text2 = "efgh"
# Output: 0

# Constraints:
#   - 1 <= text1.length, text2.length <= 1000
#   - text1 and text2 consist of only lowercase English characters.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        maximum = 0
        # print(dp)

        for i in range(len(text1)) :
            
            for j in range(len(text2)) :
                # print(i, j, len(text2), len(dp[i]))
                if text1[i] == text2[j] :
                    dp[i + 1][j + 1] = 1 + dp[i][j]   
                else :
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]



