# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode
# 
# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]
# 
# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]
# 
# Constraints:
# - 0 <= strs.length < 100
# - 0 <= strs[i].length < 200
# - strs[i] contains only UTF-8 characters.


class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += (i + "\n")
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        suh = ""
        arr = []
        while i < len(s) :
            if s[i] == "\n" :
                arr.append(suh)
                suh = ""
            else:
                suh += s[i]
            i+=1
        return arr
