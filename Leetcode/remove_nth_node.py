# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_end_node = dummy_head = ListNode(next=head)
        cur_node = head
        i = 1
        while i < n:
            cur_node = cur_node.next
            i += 1
        
        while cur_node.next:
            cur_node = cur_node.next
            prev_end_node = prev_end_node.next
        
        prev_end_node.next = prev_end_node.next.next
        
        return dummy_head.next