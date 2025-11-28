# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        sec_sm = float('inf')
        sm = root.val

        def dfs(root):
            nonlocal sec_sm
            
            if not root:
                return

            if sm < root.val < sec_sm:
                sec_sm = root.val
            elif root.val == sm:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root) 
        return sec_sm if sec_sm < float('inf') else -1