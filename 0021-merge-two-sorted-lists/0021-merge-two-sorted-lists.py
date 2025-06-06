# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, last = None, None
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val < l2.val:
                if head == None:
                    head = l1
                    last = head
                else:
                    last.next = l1
                    last = l1
                l1 = l1.next
            else:
                if head == None:
                    head = l2
                    last = head
                else:
                    last.next = l2
                    last = l2
                l2 = l2.next
        
        if l1 and not l2:
            if last:
                last.next = l1
            else:
                head = l1
        elif l2 and not l1:
            if last:
                last.next = l2
            else:
                head = l2
        
        return head
                