# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        levels: List[TreeNode] = [root]

        while levels:
            next_level: List[TreeNode] = []
            for node in levels:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            if not next_level:
                return levels[0].val
            
            levels = next_level
        


            
