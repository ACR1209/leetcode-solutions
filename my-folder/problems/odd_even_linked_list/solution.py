# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count: int = 0
        left_tail: ListNode = None
        left_head: ListNode = None
        right_tail: ListNode = None
        right_head: ListNode = None
        current: ListNode = head

        while current:
            if count % 2 == 0:
                if not left_tail or not left_head:
                    left_head = ListNode(current.val)
                    left_tail = left_head
                else:
                    left_tail.next = ListNode(current.val)
                    left_tail = left_tail.next
            else:
                if not right_tail or not right_head:
                    right_head = ListNode(current.val)
                    right_tail = right_head
                else:
                    right_tail.next = ListNode(current.val)
                    right_tail = right_tail.next
            count += 1
            current = current.next

        if left_tail and right_head:
            left_tail.next = right_head

        return left_head

