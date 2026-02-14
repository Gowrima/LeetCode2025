# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        order = 0
        q = deque()
        q.append(root)
        result = []

        while q:
            tmp_result = []

            for i in range(len(q)):
                tmp = q.popleft()

                if tmp.left:
                    q.append(tmp.left)
                
                if tmp.right:
                    q.append(tmp.right)
   
                tmp_result.append(tmp.val)
            
            if not order:
                result.append(tmp_result)
                order = 1
            else:
                result.append(tmp_result[::-1])
                order = 0

        return result