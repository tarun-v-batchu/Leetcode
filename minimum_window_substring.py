# Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) 
# is included in the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Constraints:
#   - m == s.length
#   - n == t.length
#   - 1 <= m, n <= 105
#   - s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t) :
            return ""
        
        dic = defaultdict(int)

        for i in t :
            dic[i] += 1
        remaining_chars = len(t)
        r = (0, float('inf'))
        i,j = 0, 0
        while i < len(s) :
            # print(remaining_chars)
            if j >= len(s) and remaining_chars > 0 :
                break
            if remaining_chars > 0 :
                if dic[s[j]] > 0 :
                    remaining_chars -= 1
                dic[s[j]] -= 1
                j += 1 
            elif remaining_chars == 0 :
                r = r if r[1] - r[0] + 1 < j - i + 1 else (i, j)
                dic[s[i]] += 1
                if dic[s[i]] > 0 :
                    remaining_chars += 1
                i += 1
            
        # print(r)
        return "" if r == (0, float('inf')) else s[r[0]:r[1]]
