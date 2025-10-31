# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.parent_x, self.parent_y = None, None
        self.depth_x, self.depth_y = 0, 0

        def dfs(node, parent, depth):
            if not node:
                return None
            
            if node.val == x:
                self.parent_x = parent
                self.depth_x = depth
            
            if node.val == y:
                self.parent_y = parent
                self.depth_y = depth
            
            if self.parent_x and self.parent_y:
                return
            
            dfs(node.left, node, depth+1)
            dfs(node.right, node, depth+1)
        
        dfs(root, None, 0)

        return self.parent_x != self.parent_y and self.depth_x == self.depth_y
            
