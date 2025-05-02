# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 
# Constraints:
#   - -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        if not x :
            return 0
        operation, x = x/abs(x), abs(x)
        new_num = 0
        while x :
            # print(x, new_num)
            new_num = (new_num * 10) + (x % 10)
            x //= 10
        # print(x, new_num, int(new_num * operation))
        return int(new_num * operation) if - 2 ** 31 < int(new_num * operation) < 2 ** 31 - 1 else 0
