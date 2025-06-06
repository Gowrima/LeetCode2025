# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None
      
        n1, n2 = l1, l2
        carry = 0

        while n1 and n2:
            #print ("n1 = ", n1.val, "n2 = ", n2.val)

            sum_ = n1.val + n2.val + carry

            #print (sum_)
            su = sum_%10
            carry = sum_//10

            #print (sum_, carry)
            
            newnode = ListNode(su)

            if head == None:
                newnode.next = head
                head = newnode
                tail = head
            else:
                tail.next = newnode
                tail = newnode
            
            n1 = n1.next
            n2 = n2.next
        
        while n1 or n2:
            if n1:
                sum_ = n1.val + carry

                su = sum_%10
                carry = sum_//10

                newnode = ListNode(su)
                n1 = n1.next
            
            if n2:
                sum_ = n2.val + carry

                su = sum_%10
                carry = sum_//10

                newnode = ListNode(su)
                n2 = n2.next

            if head != None:
                tail.next = newnode
                tail = newnode
            else:
                newnode.next = head
                head = newnode
                tail = newnode

        if carry > 0 and n1 == None and n2 == None:
            newnode = ListNode(carry)
            tail.next = newnode
            tail = newnode

        return head

    
            
            