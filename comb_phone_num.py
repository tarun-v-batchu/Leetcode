# Letter Combinations of a Phone Number

# You are given a string digits made up of digits from 2 through 9 inclusive.
# Each digit (not including 1) is mapped to a set of characters as shown below:
# A digit could represent any one of the characters it maps to.
# Return all possible letter combinations that digits could represent. You may return the answer in any order.

# Example 1:
# Input: digits = "34"
# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

# Example 2:
# Input: digits = ""
# Output: []

# Constraints:
#   - 0 <= digits.length <= 4
#   - 2 <= digits[i] <= 9


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        s = dic[digits[0]]
        for i in digits[1:] :
            temp = []
            for number in s :
                temp += [number + str(j) for j in dic[i]]
            # print(temp)
            s = temp
        return s
