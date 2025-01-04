# Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
#   - 1 <= s.length <= 1000
#   - s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[0] * len(s) for _ in range(len(s))]
        i = 0
        while i < len(s) :
            dp[i][i] = 1
            i += 1

        i_max = 0
        j_max = 0
        
        # print(dp)
        for i in range(len(s)-1,-1,-1) :
            for j in range(i + 1, len(s)) :
                # print(s[i:j+1], s[i], ",", s[j], ":", (dp[i + 1][j - 1] + 2) if (s[i] == s[j] and dp[i+1][j-1] != 0) else 0, "smaller:", dp[i + 1][j - 1], s[i+1:j])
                if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1] != 0):
                    
                    dp[i][j] = j - i + 1

                    if j_max - i_max +1 < j - i + 1 :
                        i_max, j_max = i, j
                # dp[i][j] = (dp[i + 1][j - 1] + 2) if (s[i] == s[j] and (dp[i+1][j-1] != 0 or i + 1 == j -1)) else 0

        # print(dp)

        return s[i_max:j_max+1]

