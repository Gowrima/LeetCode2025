# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        res = dummy
        
        c1, c2 = l1, l2
        carry = 0

        while c1 and c2:
            sum_ = c1.val + c2.val + carry

            carry = sum_//10 # 1
            sum_ = sum_%10 # 0

            newnode = ListNode(sum_)

            if not res:
                res = newnode
            else:
                res.next = newnode
                res = newnode
            
            c1 = c1.next
            c2 = c2.next

        
        while c1:
            sum_ = c1.val + carry
            carry = sum_//10
            sum_ = sum_%10

            newnode = ListNode(sum_)
            
            res.next = newnode
            res = newnode

            c1 = c1.next
        
        while c2:
            sum_ = c2.val + carry
            carry = sum_//10
            sum_ = sum_%10

            newnode = ListNode(sum_)
            
            res.next = newnode
            res = newnode

            c2 = c2.next

        if carry:
            res.next = ListNode(carry)
        
        return dummy.next
            
        
        