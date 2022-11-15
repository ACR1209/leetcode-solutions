# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, node: Optional[TreeNode], count: int = 0) -> int:
        if not node:
            return count
            
        count += 1 + self.countNodes(node.left) + self.countNodes(node.right)
        return count
       