# Add Binary
#
# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
#   - 1 <= a.length, b.length <= 104
#   - a and b consist only of '0' or '1' characters.
#   - Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        s = ""

        while i >= 0 and j >= 0 :
            p = (int(a[i]) + int(b[j]) + carry)
            x, carry = p % 2, p // 2
            s = str(x) + s
            i -= 1
            j -= 1
        
        while i >= 0 :
            p = (int(a[i]) + carry)
            x, carry = p % 2, p // 2
            s = str(x) + s
            i -= 1

        while j >= 0 :
            p = (int(b[j]) + carry)
            x, carry = p % 2, p // 2
            s = str(x) + s
            j -= 1

        return ("1" if carry == 1 else "") + s
         
