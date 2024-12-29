# Minimum Remove to Make Valid Parenthesis

# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
#   - It is the empty string, contains only lowercase characters, or
#   - It can be written as AB (A concatenated with B), where A and B are valid strings, or
#   - It can be written as (A), where A is a valid string.

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.


# Constraints:
#   - 1 <= s.length <= 105
#   - s[i] is either '(' , ')', or lowercase English letter.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        i = 0

        while i < len(s) :
            if s[i] == '(' :
                stack += [i]

            if s[i] == ')' :
                if len(stack) == 0 :
                    s = s[:i] + s[i + 1:]
                    i -= 1
                else :
                    stack.pop(len(stack) - 1)
            i += 1
        
        while len(stack) != 0 :
            index = stack.pop(len(stack) - 1)
            s = s[:index] + s[index + 1:]
        
        return s
                    


