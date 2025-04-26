# Remove Invalid Parenthesis
# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()","()()()"]

# Example 2:
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]

# Example 3:
# Input: s = ")("
# Output: [""]
 
# Constraints:
#   - 1 <= s.length <= 25
#   - s consists of lowercase English letters and parentheses '(' and ')'.
#   - There will be at most 20 parentheses in s.

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        
        def dfs(s, index, total, curr_string) :

            if index >= len(s) :
                # num chars skipped, curr_string
                if total == 0 :
                    return len(s) - len(curr_string), set([curr_string])
                return 25, set()
            if total < 0 :
                return 25, set()
            min_removals, arr = 25, set()

            if s[index] not in ['(', ')'] :
                return dfs(s, index + 1, total, curr_string + s[index])
            
            if s[index] == '(':
                removals, temp = dfs(s, index + 1, total + 1, curr_string + s[index])
                if removals < min_removals :
                    arr = temp
                    min_removals = removals
                elif removals == min_removals:
                    arr.update(temp)
            if s[index] == ')':
                removals, temp = dfs(s, index + 1, total - 1, curr_string + s[index])
                if removals < min_removals :
                    min_removals = removals
                    arr = temp
                elif removals == min_removals:
                    arr.update(temp)

            removals, temp = dfs(s, index + 1, total, curr_string)
            if removals < min_removals :
                min_removals = removals
                arr = temp
            elif removals == min_removals:
                arr.update(temp)
        
            return min_removals, arr
            
        return list(dfs(s, 0, 0, "")[1])

        


