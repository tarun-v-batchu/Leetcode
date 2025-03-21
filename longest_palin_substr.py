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
            

# Attempt 2: 

# Longest Palindromic Substring

# Given a string s, return the longest substring of s that is a palindrome.
# A palindrome is a string that reads the same forward and backward.
# If there are multiple palindromic substrings that have the same length, return any one of them.

# Example 1:
# Input: s = "ababd"
# Output: "bab"
# Explanation: Both "aba" and "bab" are valid answers.

# Example 2:
# Input: s = "abbc"
# Output: "bb"

# Constraints:
#   - 1 <= s.length <= 1000
#   - s contains only digits and English letters.



class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        for k in range(len(s)) :
            
            i = k
            j = k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            max_str = max(s[i + 1:j], max_str, key=lambda x: len(x))
            
            i = k
            j = k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            max_str = max(s[i + 1:j], max_str, key=lambda x: len(x))
        
        return max_str

