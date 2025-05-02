# Binary Tree Level Order Traversal

# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 
# Constraints:
#   - The number of nodes in the tree is in the range [0, 2000].
#   - -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []

        queue = [root]        
        level_order = []

        while len(queue) :
            new_queue = []
            curr_level = []
            while len(queue) :
                node = queue.pop(0)
                curr_level += [node.val]
                if node.left :
                    new_queue += [node.left]
                if node.right :
                    new_queue += [node.right]

            level_order += [curr_level]
            queue = new_queue
            
        return level_order

