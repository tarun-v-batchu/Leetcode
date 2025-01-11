# Palindrome Paritioning

# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
# You may return the solution in any order.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Constraints:
#   - 1 <= s.length <= 20
#   - s contains only lowercase English letters.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s) :
            i,j = 0, len(s) - 1

            while i < j :
                if s[i] != s[j] :
                    return False
                i += 1
                j -= 1
            return True

        
        def recurse(s, i, arr, all_arr) :

            if i >= len(s) :
                return all_arr + [arr]
            
            for j in range(i, len(s)) :
                if is_palindrome(s[i:j+1]) :
                    temp = arr.copy() + [s[i:j+1]]
                    all_arr = recurse(s, j + 1, temp, all_arr)
            
            return all_arr

        return recurse(s, 0, [], [])
