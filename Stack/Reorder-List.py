# 143

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = 0
        stack = []
        itr = head
        while itr:
            l += 1
            stack.append(itr.val)
            itr = itr.next
        
        itr = head
        y = 1
        while itr:
            if y == l-int((l-1)/2):
                itr.next = None
                break
            itr = itr.next
            y += 1    

        itr = head
        for i in range(int((l-1)/2)):
            x = ListNode(stack.pop(-1))
            x.next = itr.next
            itr.next = x
            itr = x.next