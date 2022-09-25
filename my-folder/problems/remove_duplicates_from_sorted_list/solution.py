# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        
        def inspect(node):
            if not node or not node.next:
                return

            if node.next.val != node.val:
                inspect(node.next)
            else:
                node.next = node.next.next
                inspect(node)
        
        inspect(head)
        
        return head
                
            