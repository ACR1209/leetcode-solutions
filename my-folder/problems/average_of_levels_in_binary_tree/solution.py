# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        
        if root is None:
            return result
        
        queue = [root]
        
        while queue:
            size = len(queue)
            level = []
            
            for i in range(size):
                current = queue.pop()
                level.append(current.val)
            
                if current.left:
                    queue.insert(0, current.left)
                if current.right:
                    queue.insert(0,current.right)
                    
            result.append(sum(level) / len(level))
        
        return result
            
            
        