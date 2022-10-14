# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        i = 0
        count_node = search_node = head
        while count_node:
            i += 1
            count_node = count_node.next
        
       
        mid = i // 2
        
        for _i in range(mid - 1):
            search_node = search_node.next
        
        search_node.next = search_node.next.next
        return head
        
            

            
                            
                    
        
        
        
        
         
        