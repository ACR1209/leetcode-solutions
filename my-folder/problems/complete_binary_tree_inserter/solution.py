# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        que = deque([root])
        while que:
            node = que.popleft()
            if not node.left or not node.right:
                self.q.append(node)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

    def insert(self, val: int) -> int:
        node = self.q[0]
        self.q.append(TreeNode(val))
        if not node.left:
            node.left = self.q[-1]
        else:
            node.right = self.q[-1]
            self.q.popleft()
        return node.val    
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()