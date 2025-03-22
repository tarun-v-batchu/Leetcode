# Word Break

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
# a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
#
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
#
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 

# Constraints:

#   - 1 <= s.length <= 300
#   - 1 <= wordDict.length <= 1000
#   - 1 <= wordDict[i].length <= 20
#   - s and wordDict[i] consist of only lowercase English letters.
#   - All the strings of wordDict are unique.


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        position_made = [False] * (len(s) + 1)
        position_made[0] = True
        i = 0
        while i < len(s) :
            if position_made[i] :
                for word in wordDict :
                    # print(s[i : i + len(word)], word)
                    if i + len(word) < len(s) + 1 and s[i : i + len(word)] == word :
                        position_made[i + len(word)] = True
            # print(position_made)
            i += 1

        return position_made[-1] 

# Attempt 2

# Word Break

# Given a string s and a dictionary of strings wordDict, return true if 
# s can be segmented into a space-separated sequence of one or more 
# dictionary words.

# Note that the same word in the dictionary may be reused multiple 
# times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet 
# code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as 
# "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 
# Constraints:
#   - 1 <= s.length <= 300
#   - 1 <= wordDict.length <= 1000
#   - 1 <= wordDict[i].length <= 20
#   - s and wordDict[i] consist of only lowercase English letters.
#   - All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        i = 1
        while i < len(s) + 1 :
            if not dp[i - 1] :
                i += 1
                continue
            for word in wordDict :
                if i + len(word) - 1 < len(dp) and word == s[i - 1: i - 1 + len(word)] :
                    dp[i + len(word) - 1] = True
            i += 1
        return dp[-1]


