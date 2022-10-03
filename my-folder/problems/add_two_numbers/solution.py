# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes_sum = 0
        current = ListNode()
        res = current
        
        while l1 or l2:
            if l1:
                nodes_sum += l1.val
                l1 = l1.next
            
            if l2:
                nodes_sum += l2.val
                l2 = l2.next
            
            current.next = ListNode(nodes_sum % 10)
            current = current.next
            
            nodes_sum = 0 if nodes_sum <= 9 else 1
        
        if nodes_sum:
            current.next = ListNode(nodes_sum)
        
        return res.next