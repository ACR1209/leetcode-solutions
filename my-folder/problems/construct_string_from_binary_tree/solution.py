# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def to_str(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val)
            if not root.right:
                return str(root.val) + "(" + to_str(root.left) + ")"

            return str(root.val) + "("+to_str(root.left) +")" + "("+to_str(root.right) +")"
        return to_str(root)