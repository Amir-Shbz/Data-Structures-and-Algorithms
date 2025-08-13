# 21

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by 
# splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1   

        p1 = list1
        p2 = list2
        res = None
        itr = None
        while p1!=None or p2!= None:
            if p1 is None:
                itr.next = p2
                break
            if p2 is None:
                itr.next = p1
                break    
            x = ListNode(min(p1.val, p2.val),None)
            if res is None:
                res = x
                itr = res
            else:
                itr.next = x
                itr = itr.next

            if p1.val > p2.val:
                p2 = p2.next
            else:
                p1 = p1.next                            

        return res     