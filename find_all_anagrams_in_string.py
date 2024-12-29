# Find all Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
#   - The substring with start index = 0 is "cba", which is an anagram of "abc".
#   - The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
#   - The substring with start index = 0 is "ab", which is an anagram of "ab".
#   - The substring with start index = 1 is "ba", which is an anagram of "ab".
#   - The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:
#   - 1 <= s.length, p.length <= 3 * 104
#   - s and p consist of lowercase English letters.


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p) :
            return []
        m = defaultdict(int)
        for i in p :
            m[i] += 1
        
        i = 0
        d = defaultdict(int)
        while i < len(p) - 1 :
            d[s[i]] += 1
            i += 1
        
        arr = []
        while i < len(s) :
            # print(d)
            d[s[i]] += 1
            boo = True
            for k in d :
                if d[k] != m[k] :
                    boo = False
                    continue
            if boo :
                arr += [i + 1 - len(p)]
            i += 1
            d[s[i - len(p)]] -= 1
        
        return arr
