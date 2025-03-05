# Reorganize String
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""

# Constraints:
#   - 1 <= s.length <= 500
#   - s consists of lowercase English letters.

class Solution:
    def reorganizeString(self, s: str) -> str:

        if len(s) == 0 :
            return ""
        
        freq = defaultdict(int)
        for i in s :
            freq[i] += 1

        pq = [ ]
        ret_s = "" 
        arr = [(0 - freq[i], i) for i in freq]
        heapq.heapify(arr)


        # print(arr[0])
        while arr[0][0] < 0 :
            fr, val = heapq.heappop(arr)
            if len(ret_s) > 0 and val == ret_s[-1] :
                if len(arr) == 0 or arr[0][0] == 0 :
                    return ""
                fr2, val2 = heapq.heappop(arr)
                ret_s += val2
                heapq.heappush(arr, (fr2 + 1, val2))
                heapq.heappush(arr, (fr, val))
            else :
                ret_s += val
                heapq.heappush(arr, (fr + 1, val))

        #     print("After", arr)
        # print("At the end", arr)
        
        return ret_s

