# Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]
 
# Constraints:
#   - 1 <= s.length <= 500
#   - s consists of lowercase English letters.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {}
        for i, c in enumerate(s) :
            d[c] = i
        
        front = 0
        end = 0
        arr = []

        for i, c in enumerate(s) :

            if d[c] > end :
                end = d[c]
            elif i == end :
                arr += [i - front + 1]
                end += 1
                front = end
            
        if end != front :
            arr += [end - front + 1]
        return arr
