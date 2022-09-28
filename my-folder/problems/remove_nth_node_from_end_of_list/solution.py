# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        
        # Move the fast pointer foward such as there is n spaces between slow and fast
        # Ex:
        # 1, 2, 3, 4, 5    n=2
        # s     f
        for i in range(n):
            # If it's the end and the current element is the target then erase it
            if not fast.next and i == n - 1:
                head = head.next
                return head
            
            fast = fast.next
        
        # Find the end of the list and erase the next element from the slow pointer
        # because that is the target element
        # Ex:
        # 1, 2, 3, 4, 5    n=2
        #       s     f
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        
        
        
        