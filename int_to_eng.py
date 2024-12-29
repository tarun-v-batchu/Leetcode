# Integer to English Words

# Convert a non-negative integer num to its English words representation.

# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 
# Constraints:
#   - 0 <= num <= 231 - 1

class Solution:

    def numberToWords(self, num: int) -> str:
        under_ten = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        bases = ["", "Thousand", "Million", "Billion"]
        
        def convert_ten(i, j) :
            if i * 10 + j < 20 :
                return under_ten[i * 10 + j]
            elif j == 0 :
                return tens[i - 2]
            else :
                return tens[i - 2] + " " + under_ten[j]

        def convert_hundred(i: int, j: int, k: int) :
            if j == 0 and k == 0 :
                return under_ten[i] + " Hundred"
            elif i == 0 :
                return convert_ten(j, k)
            return under_ten[i] + " Hundred " + convert_ten(j, k)
        
        s = ""
        base_index = 0
        while num >= 0 :
            word = ""
            if num < 10 :
                a = num % 10
                num //= 10
                word = under_ten[a] + (" " + bases[base_index] if base_index != 0 else "")
                s = word + " " + s
            elif num < 100:
                # print("Come here", num)
                a = num % 10
                num //= 10
                b = num % 10
                num //= 10
                word = convert_ten(b, a) + (" " + bases[base_index] if base_index != 0 else "")
                s = word + " " + s
                # print("Should be 0", num)
            else :
                a = num % 10
                num //= 10
                b = num % 10
                num //= 10
                c = num%10
                num //= 10
                if a == 0 and b == 0 and c == 0 :
                    s = word + s
                else :
                    word = convert_hundred(c, b, a) + (" " + bases[base_index] if base_index != 0 else "")
                    s = word + " " + s


            base_index += 1
            
            if num == 0 :
                break

        return s[:-1]
        

