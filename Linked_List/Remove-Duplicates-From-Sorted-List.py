# 83

# Given the head of a sorted linked list, delete all duplicates such that each 
# element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head  

        itr1 = head
        itr2 = head.next

        while itr2 != None:
            if itr2.val != itr1.val:
                itr1 = itr2 
                itr2 = itr2.next
            else:
                itr2 = itr2.next
                itr1.next = itr2

        return head  