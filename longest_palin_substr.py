# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

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
        
        maxj = 0
        maxk = 0

        i = 0
        while i < len(s) :

            j, k = i, i
            while j >= 0 and k < len(s) and s[j] == s[k] :
                # print(i, ":", s[j], s[k], s[j:k])
                j -= 1
                k += 1
            
            if maxk - (maxj + 1) < k - (j + 1) :
                maxk = k
                maxj = j
            
            j, k = i, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k] :
                # print(i, ":", s[j], s[k], s[j:k])
                j -= 1
                k += 1
            
            if maxk - (maxj + 1) < k - (j + 1) :
                maxk = k
                maxj = j
            
            i += 1
        
        return s[maxj + 1:maxk]
            


