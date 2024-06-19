# Valid Parenthesis
#
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
# Input: s = "[]"
# Output: true
#
# Example 2:
# Input: s = "([{}])"
# Output: true
# 
# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.
# 
# Constraints:
#   - 1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s :
            if i == '(' or i == '{' or i == '[' :
                stack.append(i)
            elif i == ')':
                if len(stack) == 0 or stack[-1] != '(' :
                    return False
                stack.pop()
            elif i == '}':
                if len(stack) == 0 or stack[-1] != '{' :
                    return False
                stack.pop()
            elif i == ']':
                if len(stack) == 0 or stack[-1] != '[' :
                    return False
                stack.pop()
        
        if len(stack) == 0 :
            return True
        return False
