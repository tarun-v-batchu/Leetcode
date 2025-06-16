# Similar String Groups

# Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent 
# by swapping at most two letters (in distinct positions) within the string X.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are 
# similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice 
# that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is 
# such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in 
# strs. How many groups are there?

 

# Example 1:
# Input: strs = ["tars","rats","arts","star"]
# Output: 2

# Example 2:
# Input: strs = ["omv","ovm"]
# Output: 1
 

# Constraints:
#   - 1 <= strs.length <= 300
#   - 1 <= strs[i].length <= 300
#   - strs[i] consists of lowercase letters only.
#   - All words in strs have the same length and are anagrams of each other.


class UnionFind :
    def __init__(self, size) :
        self.parent = [i for i in range(size)]
    
    def find_root(self, n) :
        if self.parent[n] == n :
            return n
        self.parent[n] = self.find_root(self.parent[n]) 
        return self.parent[n]
    
    def union_set(self, x, y) :
        x, y = self.find_root(x), self.find_root(y)
        if x != y :
            self.parent[y] = x

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind(len(strs))
        def similar(a, b) :
            diff = 0
            for x, y in zip(a, b) :
                if x != y :
                    diff += 1
            return diff == 0 or diff == 2
        for i in range(len(strs)) :
            for j in range(i + 1, len(strs)) :
                if similar(strs[i], strs[j]) :
                    uf.union_set(i, j)
        # print([(word, parent) for word, parent in zip(strs, uf.parent)])
        return sum([1 for i in range(len(uf.parent)) if i == uf.parent[i]])




