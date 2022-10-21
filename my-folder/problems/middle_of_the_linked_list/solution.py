# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        current = head
        
        while current:
            n += 1
            current = current.next

        mid = n // 2 if n % 2 != 0 else math.ceil(n / 2)
        
        current = head
        for i in range(mid):
            current = current.next
        
        return current
        
        
        