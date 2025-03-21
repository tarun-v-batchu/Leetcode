# Palindromic Substrings

# Given a string s, return the number of substrings within s that are palindromes.
# A palindrome is a string that reads the same forward and backward.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

# Constraints:
#   - 1 <= s.length <= 1000
#   - s consists of lowercase English letters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)) :

            k = i
            j = i
            while k >= 0 and j < len(s) and s[k] == s[j] :
                count += 1
                k -= 1
                j += 1

            k = i
            j = i + 1
            while k >= 0 and j < len(s) and s[k] == s[j] :
                count += 1
                k -= 1
                j += 1

        
        return count
             
