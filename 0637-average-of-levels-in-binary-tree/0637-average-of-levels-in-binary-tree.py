# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)

        result = []

        while queue:
            level_sum = 0  
            
            # for tmp in queue:  [1,2,3,4,5]
            # for i in range(5)
            size = len(queue)
            
            for i in range(size):
                tmp = queue.popleft() #3 
                level_sum += tmp.val # 3

                if tmp.left:
                    queue.append(tmp.left) # 9

                if tmp.right:
                    queue.append(tmp.right) # 9, 20
            
            level_avg = level_sum/size
            result.append(level_avg) # 3

        return result
        

