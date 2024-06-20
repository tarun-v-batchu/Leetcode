# Generate Parenthesis
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
#
# Example 1:
# Input: n = 1
# Output: ["()"]
#
# Example 2:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#
# You may return the answer in any order.
# Constraints:
#   - 1 <= n <= 7

# Solution 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = [["()"]]
        i = 2
        while i <= n :
            new_arr = ['(' + x + ')' for x in arr[-1]] # (A(x-1))
            x = 0
            while x < len(arr) :
                for j in arr[x] :
                    for j2 in arr[len(arr) - x - 1] :
                        if j+j2 not in new_arr :
                            new_arr.append(j + j2)
                x+=1
            arr.append(new_arr)
            i+=1
        return arr[-1]

        
        # 0: ()
        # 1: (()) ()()
        # 2: ((())) (()()) (())() ()()() ()(())
        # 3: (((()))) (()())
