# Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head. You must solve 
# the problem without modifying the values in the list's nodes (i.e., only nodes 
# themselves may be changed.)


# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]


# Constraints:
#   - The number of nodes in the list is in the range [0, 100].
#   - 0 <= Node.val <= 100


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head :
            return None

        new_head = ListNode(-1, None)
        ret_head = new_head
        
        while head != None :
            curr_node = head
            second = curr_node.next
            if second == None :
                new_head.next = curr_node
                curr_node.next = None
                break
            temp = second.next
            new_head.next = second
            second.next = curr_node
            curr_node.next = None
            new_head = curr_node
            head = temp
        
        return ret_head.next
