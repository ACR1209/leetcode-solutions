# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current: ListNode = head
        count: int = 0
        while current: 
            count += 1
            current = current.next
        
        current = head
        for _ in range(count // 2):
            current = current.next
        return current
