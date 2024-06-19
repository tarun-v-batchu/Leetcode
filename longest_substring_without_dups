# Longest Substring Without Duplicates
# 
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
# Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.
#
# Example 2:
# Input: s = "xxxx"
# Output: 1
#
# Constraints:
#   - 0 <= s.length <= 1000
#   - s may consist of printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        arr = []
        
        max_string = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            while j < len(s) and s[j] not in arr :
                arr.append(s[j])
                j+=1
            if j - i > max_string :
                print(i, j, j - i)
                max_string = j - i
            if j >= len(s) :
                return max_string
            while i < len(s) and s[j] in arr :
                arr.remove(s[i])
                i+=1
            arr.append(s[j])
            j+=1
        return max_string
