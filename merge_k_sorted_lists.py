# Merge k Sorted Lists
# You are given an array of k linked lists lists, where each list is sorted in ascending order.
# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:
# Input: lists = [[1,2,4],[1,3,5],[3,6]]
# Output: [1,1,2,3,3,4,5,6]

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Constraints:
#   - 0 <= lists.length <= 1000
#   - 0 <= lists[i].length <= 100
#   - -1000 <= lists[i][j] <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(a, b) :
            if a == None :
                return b
            if b == None :
                return a
            head = None
            if a.val < b.val :
                head = a
                a = a.next
            else :
                head = b
                b = b.next
            node = head
            
            while a != None and b != None :
                if a.val < b.val :
                    node.next = a
                    a, node = a.next, node.next
                else :
                    node.next = b
                    b, node = b.next, node.next
            
            while a != None :
                node.next = a
                a, node = a.next, node.next
            while b != None :
                node.next = b
                b, node = b.next, node.next
            
            return head

        def recurse(lis) :
            if len(lis) == 0 :
                return None
            if len(lis) == 1 :
                return lis[0]
            a = recurse(lis[:len(lis)//2])
            b = recurse(lis[len(lis)//2:])

            merged = merge(a, b)
            return merged

        return recurse(lists)
