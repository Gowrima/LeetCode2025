# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        ll_nodes = set(nums)
        
        cur = head # 1
        prev = None

        while cur:
            if cur.val in ll_nodes:
                if prev is None:
                    head = cur.next #2
                    del cur 
                    cur = head # 2,1,2,1,2 
                elif cur.next is None:
                    prev.next = None
                    del cur
                    cur = prev
                else:
                    prev.next = cur.next
                    del cur 
                    cur = prev.next
            else:
                prev = cur
                cur = cur.next
    
        return head