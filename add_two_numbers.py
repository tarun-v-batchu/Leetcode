# Add Two Numbers

# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Return the sum of the two numbers as a linked list.

# Example 1:
# Input: l1 = [1,2,3], l2 = [4,5,6]
# Output: [5,7,9]
# Explanation: 321 + 654 = 975.

# Example 2:
# Input: l1 = [9], l2 = [9]
# Output: [8,1]

# Constraints:
#   - 1 <= l1.length, l2.length <= 100.
#   - 0 <= Node.val <= 9


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)) % 10)
        ret = head
        carry = ((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)) // 10
        
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None

        while l1 != None or l2 != None :
            val = ((l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)) + carry
            dig = val % 10
            carry = val // 10
            head.next = ListNode(dig)
            l1, l2, head = l1.next if l1 != None else None, l2.next if l2 != None else None, head.next
    
        if carry > 0 :
            head.next = ListNode(carry)
        
        return ret

