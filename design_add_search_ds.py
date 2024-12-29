# Design Add and Search Words Data Structure

# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
#   - WordDictionary() Initializes the object.
#   - void addWord(word) Adds word to the data structure, it can be matched later.
#   - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
# Example:
# Input:
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output:
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 
# Constraints:
#   - 1 <= word.length <= 25
#   - word in addWord consists of lowercase English letters.
#   - word in search consist of '.' or lowercase English letters.
#   - There will be at most 2 dots in word for search queries.
#   - At most 104 calls will be made to addWord and search.


class Node :
        def __init__(self, key) :
            self.key = key
            self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = Node('.')

    def addWord(self, word: str) -> None:
        node = self.root
        i = 0
        word += '.'
        while i < len(word) :
            if word[i] not in node.children : # the children of the node doesnt contain the letter, add it to the children
                # print("Adding", word[i], "to", node.key)
                node.children[word[i]] = Node(word[i])
            # Set node to the child Node with key of word[i]
            node = node.children[word[i]]
            i += 1
        

    def search(self, word: str) -> bool:

        def recurse(node, index, word) :
            # print("Hi")
            # print(node.key)
            if index >= len(word) :
                if '.' in node.children :
                    return True
                return False
            if word[index] == '.' :
                for child in node.children :
                    boo = recurse(node.children[child], index + 1, word)
                    if boo :
                        return True
            if word[index] not in node.children :
                return False
            return recurse(node.children[word[index]], index + 1, word)
        # print("Word to find", word)
        return recurse(self.root, 0, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
