# Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' 
# values. (i.e., from left to right, then right to left for the next level and alternate 
# between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 
# Constraints:
#   - The number of nodes in the tree is in the range [0, 2000].
#   - -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root :
            return []
        stack = []
        new_stack = [root]
        arr = []
        goRight = True

        while len(new_stack) > 0 :
            stack = new_stack
            new_stack = []
            new_arr = []
            while len(stack) > 0 :
                elem = stack.pop()
                new_arr += [elem.val]
                if goRight :
                    if elem.left :
                        new_stack += [elem.left]
                    if elem.right :
                        new_stack += [elem.right]
                else :
                    if elem.right :
                        new_stack += [elem.right]
                    if elem.left :
                        new_stack += [elem.left]
            goRight = not goRight
            arr.append(new_arr)
        
        return arr
        


        
