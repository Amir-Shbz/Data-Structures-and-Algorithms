# 203

# Given the head of a linked list and an integer val, remove all the nodes of the linked list 
# that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        x = ListNode(-1)
        x.next = head
        itr = x

        while itr.next:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next

        return x.next 