# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        ll_nodes = set(nums)
        
        cur = head
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head

        while cur:
            if cur.val in ll_nodes:
                prev.next = cur.next
                del cur 
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
    
        return dummy.next