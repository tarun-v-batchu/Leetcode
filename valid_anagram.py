Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
#
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
# Constraints:
#   - s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            print("hi")
            return False
        
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)


        for i in s :
            s_dic[i] += 1
        
        for j in t :
            t_dic[j] += 1
            
        for i in s :
            if t_dic[i] != s_dic[i] :
                return False
        return True
